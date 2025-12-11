import sys
import os
import argparse
from pathlib import Path
from termcolor import cprint
from typing import List, Dict, Any

from jenkins import Jenkins
from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.schema import NodeWithScore
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

from rag_config import setup_rag_configuration, CHROMA_PERSIST_DIR, COLLECTION_NAME
from jenkins_instance_info import get_shared_libraries, JENKINS_URL_ENV, JENKINS_USER_ENV, JENKINS_TOKEN_ENV

# --- CONFIGURATION ---
TOP_K_CHUNKS = 4
# ---------------------
LLM_PROMPT = """
You are a Tekton expert. Convert the following Jenkinsfile into valid Tekton v1 YAML.

    Use the following reference material from the knowledge base (RAG results) to guide the conversion:
    
    {RAG_result_placeholder}
    
    Context about available Jenkins Shared Libraries on the source instance:
    {shared_libs_placeholder}
    
    Requirements:
    1. Break down the pipeline into separate Tekton resources:
   - One or more Task objects (one per Jenkins stage/step).
   - A Pipeline object that references those Tasks.
   - A PipelineRun object that executes the Pipeline.
2. Use only Tekton v1 syntax.
3. Scripts must be strings (not arrays).
4. Output MUST be multiple YAML documents separated by '---':
   first the Task(s), then the Pipeline, then the PipelineRun.
5. Output ONLY raw YAML, no markdown formatting or explanations.
6. **Important:** If a simple value or string is passed between steps, prefer using **results** instead of workspaces. Use workspaces only for files or larger data.

Jenkinsfile:
{jenkinsfile_content_placeholder}
"""


def read_jenkinsfile(filename: str) -> str:
    """
    Read and return the contents of a Jenkinsfile.

    Args:
        filename: Path to the Jenkinsfile

    Returns:
        str: Contents of the Jenkinsfile

    Exits:
        If the file does not exist
    """
    if not Path(filename).exists():
        cprint(f"File '{filename}' does not exist in this directory", "red")
        sys.exit(1)
    with open(Path(filename), 'r', encoding='utf-8') as file:
        return file.read()


def load_index_chromadb() -> VectorStoreIndex:
    """
    Load the default Tekton documentation index from ChromaDB.
    Uses the 'default_data' collection that ships with the container.
    Future: Support loading per-customer collections for multi-tenancy.
    """
    if not Path(CHROMA_PERSIST_DIR).exists():
        cprint(f"ChromaDB storage '{CHROMA_PERSIST_DIR}' does not exist.", "red")
        cprint(f"To create the index, run: python ingest_tekton_data.py", "yellow")
        sys.exit(1)

    try:
        cprint(f"Loading ChromaDB from: {CHROMA_PERSIST_DIR}", "blue")

        # Initialize ChromaDB client
        chroma_client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)

        # Get the default collection
        chroma_collection = chroma_client.get_collection(name=COLLECTION_NAME)

        cprint(f"✓ Collection loaded: '{COLLECTION_NAME}' ({chroma_collection.count()} vectors)", "green")

        # Create vector store from collection
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

        # Return index from vector store
        return VectorStoreIndex.from_vector_store(vector_store=vector_store)
    except Exception as e:
        cprint(f"Failed loading ChromaDB index: {e}", "red")
        sys.exit(1)



def generate_final_conversion(rag_context: str, jenkinsfile_content: str, shared_libs_context: str) -> str:
    """
    Generate the final Tekton YAML conversion using the LLM.

    Args:
        rag_context: Retrieved context from the RAG system
        jenkinsfile_content: Original Jenkinsfile content to convert
        shared_libs_context: String summary of available shared libraries

    Returns:
        str: Generated Tekton YAML
    """
    prompt = LLM_PROMPT.format(
        RAG_result_placeholder=rag_context,
        jenkinsfile_content_placeholder=jenkinsfile_content,
        shared_libs_placeholder=shared_libs_context
    )
    response = Settings.llm.complete(prompt)
    return response.text.strip()


def run_conversion_query(index: VectorStoreIndex, jenkinsfile_content: str, query: str, top_k: int, shared_libs_context: str = "N/A"):
    """
    Run the RAG retrieval and generate Tekton conversion.

    Args:
        index: VectorStoreIndex to query for relevant context
        jenkinsfile_content: Original Jenkinsfile content
        query: Query string for RAG retrieval
        top_k: Number of top results to retrieve
        shared_libs_context: Summary of shared libraries
    """
    cprint("\n--- RAG Retrieval Query ---", "yellow")
    retriever = VectorIndexRetriever(index=index, similarity_top_k=top_k)
    retrieval_results: List[NodeWithScore] = retriever.retrieve(query)

    cprint("\n[Retrieval Assessment]", "yellow")
    context_texts = []

    for i, node_with_score in enumerate(retrieval_results, 1):
        score = node_with_score.score
        source = node_with_score.node.metadata.get('file_name', node_with_score.node.metadata.get('source', 'N/A'))
        context_texts.append(node_with_score.text)
        print(f"  [{i}] Source: {source} | SCORE: {score:.4f}")

    combined_context = "\n\n---\n\n".join(context_texts)

    final_yaml_output = generate_final_conversion(combined_context, jenkinsfile_content, shared_libs_context)
    cprint("\n[Final Tekton Conversion]", "blue")
    print(final_yaml_output)


def fetch_jenkins_shared_libs() -> str:
    """Connect to Jenkins and retrieve shared library info formatted as a string."""
    jenkins_url = os.getenv(JENKINS_URL_ENV)
    username = os.getenv(JENKINS_USER_ENV)
    token = os.getenv(JENKINS_TOKEN_ENV)
    
    if not jenkins_url or not username or not token:
        cprint("Warning: JENKINS credentials not set. Skipping shared library fetch.", "yellow")
        return "No shared library context available (Missing credentials)."

    try:
        server = Jenkins(jenkins_url, username=username, password=token)
        libs = get_shared_libraries(server)
        if not libs:
            return "No shared libraries found on instance."
            
        summary = []
        for lib in libs:
            name = lib.get('name', 'Unknown')
            url = lib.get('url', 'N/A')
            implicit = lib.get('implicit', False)
            summary.append(f"- Library: {name} (Implicit: {implicit}) | Repo: {url}")
        return "\n".join(summary)
    except Exception as e:
        cprint(f"Warning: Failed to fetch shared libraries: {e}", "yellow")
        return f"Error fetching shared libraries: {e}"


def main():
    """Main entry point for the Tekton pipeline generation script."""
    parser = argparse.ArgumentParser(
        description="Generate Tekton pipeline from Jenkinsfile using ChromaDB-powered RAG"
    )
    parser.add_argument('jenkinsfile_path', help='Path to the Jenkinsfile to convert')
    args = parser.parse_args()

    # Setup RAG configuration
    setup_rag_configuration()

    # Load the default Tekton documentation index from ChromaDB
    index = load_index_chromadb()

    # Fetch Shared Library Context
    cprint("Fetching shared library info from Jenkins...", "blue")
    shared_libs_context = fetch_jenkins_shared_libs()

    # Read Jenkinsfile and run conversion
    jenkinsfile_content = read_jenkinsfile(args.jenkinsfile_path)
    query = f"Convert this Jenkinsfile to Tekton YAML: {Path(args.jenkinsfile_path).name}"

    run_conversion_query(index, jenkinsfile_content, query, TOP_K_CHUNKS, shared_libs_context)


if __name__ == "__main__":
    main()
