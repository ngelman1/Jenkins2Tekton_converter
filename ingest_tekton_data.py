import sys
import argparse
from pathlib import Path
from termcolor import cprint
from typing import List

from llama_index.core import VectorStoreIndex
from llama_index.core import SimpleDirectoryReader
from llama_index.core.storage.storage_context import StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

from rag_config import setup_rag_configuration, TEKTON_DB_PATH, DEFAULT_COLLECTION_NAME

# Documentation directory
DOCS_DIR = Path("./tekton_docs")


def load_documents(docs_dir: Path) -> List:

    if not docs_dir.exists():
        cprint(f"FATAL: Documentation directory '{docs_dir}' does not exist.", "red")
        sys.exit(1)

    cprint(f"Loading documents from: {docs_dir}", "blue")
    documents = SimpleDirectoryReader(input_dir=docs_dir).load_data()
    cprint(f"✓ Loaded {len(documents)} documents", "green")

    return documents



def ingest_data_to_chromadb(documents: List):

    cprint(f"Initializing ChromaDB at: {TEKTON_DB_PATH}", "blue")

    chroma_client = chromadb.PersistentClient(path=TEKTON_DB_PATH)

    # Drop the old collection so we don't accumulate duplicate vectors.
    try:
        chroma_client.delete_collection(name=DEFAULT_COLLECTION_NAME)
        cprint(f"  Dropped existing collection '{DEFAULT_COLLECTION_NAME}'", "yellow")
    except ValueError:
        pass

    chroma_collection = chroma_client.create_collection(
        name=DEFAULT_COLLECTION_NAME,
        metadata={"description": "Default Tekton documentation shipped with container"}
    )

    cprint(f"Using collection: '{DEFAULT_COLLECTION_NAME}'", "blue")

    # Create ChromaDB vector store using the llama_index wrapper
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

    # Create storage context
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    cprint(f"Building index and ingesting {len(documents)} documents to ChromaDB...", "blue")

    # Create index from documents
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context
    )

    cprint(f"✓ Ingestion complete. {len(documents)} documents vectorized and stored in collection '{DEFAULT_COLLECTION_NAME}'.", "green")
    cprint(f"✓ ChromaDB persisted to: {TEKTON_DB_PATH}", "green")


def main():
    """Main entry point for the ingestion script."""
    parser = argparse.ArgumentParser(
        description="Ingest Tekton documentation into ChromaDB vector database"
    )
    args = parser.parse_args()

    # Setup RAG configuration
    setup_rag_configuration()

    # Load documents
    documents = load_documents(DOCS_DIR)

    # Ingest to ChromaDB
    ingest_data_to_chromadb(documents)


if __name__ == "__main__":
    main()
