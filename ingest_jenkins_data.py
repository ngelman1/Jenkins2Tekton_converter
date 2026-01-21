import sys
import argparse
from termcolor import cprint
from typing import List

from llama_index.core import VectorStoreIndex, Document
from llama_index.core.storage.storage_context import StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

from rag_config import setup_rag_configuration, JENKINS_DB_PATH, JENKINS_COLLECTION_NAME
from jenkins_instance_info import (
    get_jenkins_client,
    get_installed_plugins,
    get_shared_libraries,
    get_all_jobs
)

def create_jenkins_documents() -> List[Document]:
    """
    Connect to Jenkins, fetch data, and convert it into LlamaIndex Documents.
    """
    cprint("Connecting to Jenkins...", "blue")
    server = get_jenkins_client()
    
    documents = []
    
    # Plugins
    plugins = get_installed_plugins(server)
    if plugins:
        content = "Jenkins Installed Plugins:\n"
        for p in plugins:
            status = "ACTIVE" if p['active'] else "INACTIVE"
            content += f"- {p['name']} (Version: {p['version']}, Status: {status})\n"
        
        doc = Document(
            text=content,
            metadata={"source": "jenkins_api", "type": "plugins_list"}
        )
        documents.append(doc)
   

    # 2. Shared Libraries
    libs = get_shared_libraries(server)
    if libs:
        content = "Jenkins Shared Libraries:\n"
        for lib in libs:
            name = lib.get('name', 'Unknown')
            url = lib.get('url', 'N/A')
            content += f"- Library: {name} | Repo: {url}\n"
            
        doc = Document(
            text=content,
            metadata={"source": "jenkins_api", "type": "shared_libraries"}
        )
        documents.append(doc)

    return documents


def ingest_jenkins_data(documents: List[Document]):

    if not documents:
        cprint("No documents to ingest.", "yellow")
        return

    cprint(f"Initializing ChromaDB at: {JENKINS_DB_PATH}", "blue")
    chroma_client = chromadb.PersistentClient(path=JENKINS_DB_PATH)

    chroma_collection = chroma_client.get_or_create_collection(
        name=JENKINS_COLLECTION_NAME,
        metadata={"description": "Personal data scraped from Jenkins instance"}
    )

    cprint(f"Using collection: '{JENKINS_COLLECTION_NAME}'", "blue")

    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    cprint(f"Ingesting {len(documents)} documents...", "blue")
    
    VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context
    )

    cprint(f"✓ Successfully ingested Jenkins data into collection '{JENKINS_COLLECTION_NAME}'", "green")

def main():
    parser = argparse.ArgumentParser(description="Scrape Jenkins instance data and ingest into ChromaDB")
    parser.parse_args()

    setup_rag_configuration() #from rag_config.py to set embedding model and api key
    
    documents = create_jenkins_documents()
    ingest_jenkins_data(documents)

if __name__ == "__main__":
    main()

