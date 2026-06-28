# ingest_jenkins_data.py
import sys
import argparse
from pathlib import Path
from termcolor import cprint
from typing import List

from llama_index.core import VectorStoreIndex, Document
from llama_index.core.storage.storage_context import StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

from rag_config import setup_rag_configuration, JENKINS_DB_PATH, JENKINS_COLLECTION_NAME

GROOVY_EXTENSIONS = {".groovy"}
JENKINSFILE_PREFIXES = ("Jenkinsfile",)
CONFIG_EXTENSIONS = {".yml", ".yaml"}
CONFIG_PATTERNS = ["pipeline*.yml", "*deployment*.yml", "uft*.yml"]


def scan_local_directory(directory: Path) -> List[Document]:
    """
    Scan a local Jenkins shared library directory and convert files
    into LlamaIndex Documents for ingestion.

    Expected directory layout (standard Jenkins shared library):
      vars/          - Pipeline entry points (e.g. standardMavenPipeline.groovy)
      src/           - Supporting Groovy classes
      resources/     - Resource files (templates, pod YAMLs)
      Jenkinsfile*   - Pipeline definitions
      *.yml          - Pipeline/deployment configuration
    """
    if not directory.is_dir():
        cprint(f"FATAL: Directory '{directory}' does not exist.", "red")
        sys.exit(1)

    documents = []
    counts = {"shared_library_var": 0, "shared_library_src": 0,
              "jenkinsfile": 0, "pipeline_config": 0, "resource": 0}

    # --- vars/ directory: pipeline entry points ---
    vars_dir = directory / "vars"
    if vars_dir.is_dir():
        for f in sorted(vars_dir.rglob("*")):
            if f.is_file() and f.suffix in GROOVY_EXTENSIONS:
                doc = _file_to_document(f, directory, "shared_library_var")
                documents.append(doc)
                counts["shared_library_var"] += 1

    # --- src/ directory: supporting classes ---
    src_dir = directory / "src"
    if src_dir.is_dir():
        for f in sorted(src_dir.rglob("*")):
            if f.is_file() and f.suffix in GROOVY_EXTENSIONS:
                doc = _file_to_document(f, directory, "shared_library_src")
                documents.append(doc)
                counts["shared_library_src"] += 1

    # --- resources/ directory ---
    resources_dir = directory / "resources"
    if resources_dir.is_dir():
        for f in sorted(resources_dir.rglob("*")):
            if f.is_file() and f.suffix in (".yml", ".yaml", ".json"):
                doc = _file_to_document(f, directory, "resource")
                documents.append(doc)
                counts["resource"] += 1

    # --- Root-level Jenkinsfiles ---
    for f in sorted(directory.iterdir()):
        if f.is_file() and f.name.startswith(JENKINSFILE_PREFIXES):
            doc = _file_to_document(f, directory, "jenkinsfile")
            documents.append(doc)
            counts["jenkinsfile"] += 1

    # --- Root-level config YAMLs ---
    for pattern in CONFIG_PATTERNS:
        for f in sorted(directory.glob(pattern)):
            if f.is_file():
                doc = _file_to_document(f, directory, "pipeline_config")
                documents.append(doc)
                counts["pipeline_config"] += 1

    cprint(f"\nScan summary for '{directory}':", "blue")
    for doc_type, count in counts.items():
        if count > 0:
            cprint(f"  {doc_type}: {count} files", "cyan")
    cprint(f"  Total: {len(documents)} documents", "blue")

    return documents


def _file_to_document(filepath: Path, base_dir: Path, doc_type: str) -> Document:
    """Read a file and wrap it as a LlamaIndex Document with metadata."""
    relative_path = str(filepath.relative_to(base_dir))
    content = filepath.read_text(encoding="utf-8", errors="replace")

    header = f"File: {relative_path}\nType: {doc_type}\n---\n"

    return Document(
        text=header + content,
        metadata={
            "source": "local_directory",
            "type": doc_type,
            "file_name": filepath.name,
            "file_path": relative_path,
        }
    )


def ingest_jenkins_data(documents: List[Document]):
    if not documents:
        cprint("No documents to ingest.", "yellow")
        return

    cprint(f"\nInitializing ChromaDB at: {JENKINS_DB_PATH}", "blue")
    chroma_client = chromadb.PersistentClient(path=JENKINS_DB_PATH)

    try:
        chroma_client.delete_collection(name=JENKINS_COLLECTION_NAME)
        cprint(f"Cleared existing collection '{JENKINS_COLLECTION_NAME}'.", "yellow")
    except Exception:
        pass

    chroma_collection = chroma_client.get_or_create_collection(
        name=JENKINS_COLLECTION_NAME,
        metadata={"description": "Jenkins shared library and pipeline data from local directory"}
    )

    cprint(f"Using collection: '{JENKINS_COLLECTION_NAME}'", "blue")

    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    cprint(f"Ingesting {len(documents)} documents...", "blue")

    VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context
    )

    cprint(f"✓ Successfully ingested {len(documents)} documents into '{JENKINS_COLLECTION_NAME}'", "green")


def main():
    parser = argparse.ArgumentParser(
        description="Ingest Jenkins shared library files from a local directory into ChromaDB"
    )
    parser.add_argument(
        "directory",
        help="Path to the local directory containing Jenkins shared library files "
             "(expected layout: vars/, src/, Jenkinsfile*, *.yml)"
    )
    args = parser.parse_args()

    setup_rag_configuration()

    directory = Path(args.directory).resolve()
    documents = scan_local_directory(directory)
    ingest_jenkins_data(documents)


if __name__ == "__main__":
    main()

