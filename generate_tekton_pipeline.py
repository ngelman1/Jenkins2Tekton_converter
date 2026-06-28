# generate_tekton_pipeline.py
"""Orchestrator: converts a Jenkinsfile into Tekton YAML via RAG + LLM."""
import sys
import argparse
from pathlib import Path
from typing import List

from termcolor import cprint
from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.schema import NodeWithScore
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

from rag_config import (
    setup_rag_configuration,
    TEKTON_DB_PATH, DEFAULT_COLLECTION_NAME,
)
from jenkins_shared_lib import build_shared_lib_section
from output_writer import save_output
from tekton_validator import validate_and_fix


# --- CONFIGURATION ---
TEKTON_TOP_K = 4
# ---------------------
LLM_PROMPT = """
You are a Tekton expert. Convert the following Jenkinsfile into valid Tekton v1 YAML.

Use the following Tekton reference material from the knowledge base to guide the conversion:

{tekton_rag_context}

{shared_lib_section}

Requirements:
1. Break down the pipeline into separate Tekton resources:
   - One Task per Jenkins STAGE (not per individual step/utility call).
     Group all steps within a single Jenkins stage into one Task with
     multiple steps. Only create a separate Task for truly independent
     pre-pipeline setup logic (e.g. fetching config, cloning source).
   - A Pipeline object that references those Tasks.
   - A PipelineRun object that executes the Pipeline.
2. Use only Tekton v1 syntax (apiVersion: tekton.dev/v1).
3. Scripts must be strings (not arrays).
4. Output MUST be multiple YAML documents separated by '---':
   first the Task(s), then the Pipeline, then the PipelineRun.
5. Output ONLY raw YAML — no markdown fences, no explanations, no comments outside YAML.
6. All YAML string values that contain single quotes, commas, colons, or
   special characters MUST be wrapped in double quotes. For example:
   description: "'true' if the build should be skipped, 'false' otherwise."
   NOT: description: 'true' if the build should be skipped, 'false' otherwise.
6. If a simple value or string is passed between steps, prefer using
   results instead of workspaces. Use workspaces only for files or larger data.
   Results have a 4096-byte limit per result.

Conversion patterns (MUST follow):

ExternalConfig handling:
- ExternalConfig objects in the Jenkinsfile fetch configuration files from a
  Bitbucket/Git repository at runtime. Convert each ExternalConfig into Pipeline
  parameters that preserve the project, repo, file path, and ref.
  Then create a fetch-config Task that clones the config repo and extracts
  values from the YAML file using yq, storing each value as a Task result.
  Downstream tasks receive these values via $(tasks.<name>.results.<key>).
- When writing yq queries, use the FULL nested path that matches the actual
  YAML structure. For example, if the YAML has pipeline.branches[].versionType,
  use yq '.pipeline.branches[] | select(.id == "release") | .versionType'
  — NOT yq '.versionType' at the root level.

When expressions:
- Tekton when expressions ONLY support operators "in" and "notin". Do NOT use
  "eq", "ne", "equals", or "notEquals". To skip a task when a result equals
  "true", use: operator: notin, values: ["true"].

Pipeline ordering and structure:
- All Pipeline tasks MUST declare runAfter to enforce correct execution order.
  Tasks without runAfter run in parallel — only do this when stages are
  explicitly independent.
- Use generateName (not name) in PipelineRun metadata. Note: PipelineRuns
  with generateName must be applied with "kubectl create", not "kubectl apply".
- Jenkins post {{ success/failure/unstable }} blocks map to the Pipeline's
  finally section. Use $(tasks.status) to get the pipeline status in finally
  tasks. Do NOT use $(context.pipeline.status) — it does not exist.
- Pipeline workspace declarations MUST only define name and description.
  Do NOT put volumeClaimTemplate or persistentVolumeClaim in the Pipeline spec.
  Volume bindings belong ONLY in the PipelineRun.

Workspace rules:
- A single Task MUST NOT bind more than one PVC-backed workspace. Use emptyDir
  for caches (Maven, NPM) and configMap for config files (e.g. settings.xml).
  Only the main source code workspace should use a volumeClaimTemplate.
- In the PipelineRun, use the key "configMap" (not "config") for ConfigMap
  workspace bindings. Example: configMap: {{ name: maven-settings }}
- NEVER use volumeMounts to access workspaces. Tekton mounts workspaces
  automatically. Access them via $(workspaces.<name>.path) in scripts and env
  vars. For example, use -Dmaven.repo.local=$(workspaces.maven-cache.path)
  instead of mounting a volume to /m2repo.
- Do not copy a file from one location in a workspace to another location in
  the SAME workspace if source and destination paths are identical.

Git cloning in steps:
- Do not use `git clone <url> <path>` in steps — the workspace directory
  already exists and git clone will fail. Instead use:
  git init && git remote add origin <url> && git fetch origin <ref> --depth=1
  && git checkout FETCH_HEAD

Container images:
- Use well-known public images with valid tags. For Maven, use
  maven:3.9-eclipse-temurin-17 (NOT maven:3.9.6-openjdk-17). For Node.js, use
  node:<version>-alpine. For git operations, use alpine/git. For yq, use
  mikefarah/yq:4. For general utilities, use alpine or
  registry.access.redhat.com/ubi8/ubi-minimal.
- NEVER reference internal OpenShift registry images
  (image-registry.openshift-image-registry.svc:5000/...) — these are
  customer-specific and will not exist on other clusters.

Defensive scripting:
- Before running npm ci or npm install, check if package.json exists first.
- Use set -eu in all scripts for fail-fast behavior.
- Use || true for commands that may legitimately fail (e.g. git commit when
  there are no changes, or cp when optional files don't exist).
- NEVER use shell heredocs (<<EOF ... EOF) inside script: | blocks. The
  unindented heredoc body breaks YAML literal block parsing. Instead, use
  printf or echo with escaped newlines to write multi-line content.

Jenkinsfile:
{jenkinsfile_content}
"""


def read_jenkinsfile(filename: str) -> str:
    """Read and return the contents of a Jenkinsfile."""
    path = Path(filename)
    if not path.exists():
        cprint(f"File '{filename}' does not exist.", "red")
        sys.exit(1)
    return path.read_text(encoding="utf-8")


def load_chromadb_index(db_path: str, collection_name: str) -> VectorStoreIndex:
    """Load a VectorStoreIndex from a ChromaDB collection."""
    if not Path(db_path).exists():
        cprint(f"ChromaDB storage '{db_path}' does not exist.", "red")
        if collection_name == DEFAULT_COLLECTION_NAME:
            cprint("To create it, run: python ingest_tekton_data.py", "yellow")
        else:
            cprint("To create it, run: python ingest_jenkins_data.py <directory>", "yellow")
        sys.exit(1)

    try:
        chroma_client = chromadb.PersistentClient(path=db_path)
        chroma_collection = chroma_client.get_collection(name=collection_name)
        cprint(f"  Collection '{collection_name}': {chroma_collection.count()} vectors", "green")

        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        return VectorStoreIndex.from_vector_store(vector_store=vector_store)
    except Exception as e:
        cprint(f"Failed loading ChromaDB collection '{collection_name}': {e}", "red")
        sys.exit(1)


def retrieve_context(index: VectorStoreIndex, query: str, top_k: int, label: str) -> str:
    """Run RAG retrieval against an index and return combined context text."""
    retriever = VectorIndexRetriever(index=index, similarity_top_k=top_k)
    results: List[NodeWithScore] = retriever.retrieve(query)

    cprint(f"\n[{label} - {len(results)} results]", "yellow")
    context_texts = []
    for i, node_with_score in enumerate(results, 1):
        score = node_with_score.score
        source = node_with_score.node.metadata.get(
            "file_name", node_with_score.node.metadata.get("source", "N/A"))
        context_texts.append(node_with_score.text)
        print(f"  [{i}] Source: {source} | SCORE: {score:.4f}")

    return "\n\n---\n\n".join(context_texts) if context_texts else "No context available."


GENERATION_MAX_TOKENS = 32768


def generate_final_conversion(tekton_context: str, shared_lib_section: str, jenkinsfile_content: str) -> str:
    """Build the LLM prompt and generate the Tekton YAML conversion."""
    prompt = LLM_PROMPT.format(
        tekton_rag_context=tekton_context,
        shared_lib_section=shared_lib_section,
        jenkinsfile_content=jenkinsfile_content,
    )
    response = Settings.llm.complete(prompt, max_tokens=GENERATION_MAX_TOKENS)
    return response.text.strip()


def main():
    parser = argparse.ArgumentParser(
        description="Generate Tekton pipeline from Jenkinsfile using ChromaDB-powered RAG"
    )
    parser.add_argument("jenkinsfile_path", help="Path to the Jenkinsfile to convert")
    parser.add_argument(
        "--jenkins-dir",
        help="Path to the Jenkins shared library directory (contains vars/, src/, etc.)",
        default=None,
    )
    args = parser.parse_args()

    setup_rag_configuration()

    cprint("Loading Tekton RAG index...", "blue")
    tekton_index = load_chromadb_index(TEKTON_DB_PATH, DEFAULT_COLLECTION_NAME)

    jenkinsfile_content = read_jenkinsfile(args.jenkinsfile_path)
    jenkinsfile_name = Path(args.jenkinsfile_path).name

    tekton_query = f"Convert Jenkins pipeline to Tekton: {jenkinsfile_name}"
    tekton_context = retrieve_context(
        tekton_index, tekton_query, TEKTON_TOP_K, "Tekton RAG")

    jenkins_dir = Path(args.jenkins_dir).resolve() if args.jenkins_dir else None
    if jenkins_dir and not jenkins_dir.is_dir():
        cprint(f"Jenkins directory not found: {jenkins_dir}", "red")
        sys.exit(1)

    cprint("\nResolving shared library context...", "blue")
    shared_lib_section = build_shared_lib_section(jenkins_dir, jenkinsfile_content)

    cprint("\n--- Generating Tekton Conversion ---", "blue")
    final_yaml = generate_final_conversion(tekton_context, shared_lib_section, jenkinsfile_content)

    written_files = save_output(final_yaml, jenkinsfile_name)
    cprint(f"\n✓ Conversion saved {len(written_files)} resources:", "green")
    for f in written_files:
        cprint(f"  {f.name}  ({f.stat().st_size:,} bytes)", "cyan")

    all_valid = validate_and_fix(written_files)
    if not all_valid:
        cprint("\n⚠ Some resources still invalid after fix attempts. Review the errors above.", "yellow")
        sys.exit(2)
    else:
        cprint("\n✓ All Tekton resources passed validation.", "green")


if __name__ == "__main__":
    main()
