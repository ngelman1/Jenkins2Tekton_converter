import os
import sys
import argparse
from pathlib import Path
from termcolor import cprint
from dotenv import load_dotenv
from typing import List

from llama_index.core import VectorStoreIndex, Settings
from llama_index.core import SimpleDirectoryReader
from llama_index.core.storage.storage_context import StorageContext
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

# ChromaDB Configuration
CHROMA_PERSIST_DIR = "./chroma_db"
COLLECTION_NAME = "default_data"
EMBEDDING_DIMENSION = 768
DOCS_DIR = Path("./tekton_docs")

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')


try:
    if not api_key:
        cprint("FATAL: GEMINI_API_KEY not set in .env file.", "red")
        sys.exit(1)
    Settings.embed_model = GoogleGenAIEmbedding(model_name="models/text-embedding-004", api_key=api_key)
    Settings.llm = GoogleGenAI(model="gemini-2.5-flash", api_key=api_key)
    cprint("RAG Configuration Loaded.", "green")
except Exception as e:
    cprint(f"API_KEY Configuration error: {e}", "red")
    sys.exit(1)


documents = SimpleDirectoryReader(input_dir=DOCS_DIR).load_data()
print(f"Total documents loaded: {len(documents)}")


def ingest_data_to_chromadb(documents: List):
    """
    Ingest Tekton documentation into ChromaDB.
    Creates the 'default_data' collection that ships with the container image.
    Future: Support per-customer collections for multi-tenancy.
    """
    cprint(f"Initializing ChromaDB at: {CHROMA_PERSIST_DIR}", "blue")

    # Initialize ChromaDB client with persistent storage
    chroma_client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)

    # Get or create the default collection
    # Note: ChromaDB will create the collection if it doesn't exist
    chroma_collection = chroma_client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"description": "Default Tekton documentation shipped with container"}
    )

    cprint(f"Using collection: '{COLLECTION_NAME}'", "blue")

    # Create ChromaDB vector store
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

    # Create storage context
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    cprint(f"Building index and ingesting {len(documents)} documents to ChromaDB...", "blue")

    # Create index from documents
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context
    )

    cprint(f"✓ Ingestion complete. {len(documents)} documents vectorized and stored in collection '{COLLECTION_NAME}'.", "green")
    cprint(f"✓ ChromaDB persisted to: {CHROMA_PERSIST_DIR}", "green")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Ingest Tekton documentation into ChromaDB vector database"
    )
    args = parser.parse_args()

    ingest_data_to_chromadb(documents)
