import os
import time
from pathlib import Path
from typing import List, Dict
from termcolor import cprint
import uuid
from llama_stack_client import LlamaStackClient

# --- Init client and config ---
client = LlamaStackClient(base_url="http://localhost:8321")

VECTOR_DB_ID = "tekton_docs_vector_db"
DOCS_DIR = Path("./tekton_docs")
SUPPORTED_FORMATS = {'.md', '.txt', '.pdf', '.html', '.docx', '.pptx', '.csv', '.json', '.yaml', '.yml'}

# --- Load documents from directory ---
def load_documents_for_rag(doc_dir: Path) -> List[Dict]:
    docs = []
    for file in doc_dir.iterdir():
        if file.suffix.lower() not in SUPPORTED_FORMATS:
            continue
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
            docs.append({
                "id": str(uuid.uuid4()),
                "text": content,
                "metadata": {
                    "source": str(file),
                    "uploaded_at": int(time.time())
                }
            })
        except Exception as e:
            print(f"Error reading {file.name}: {e}")
    return docs

# --- Ingest documents using rag_tool ---
def ingest_documents_into_rag(client: LlamaStackClient, documents: List[Dict], vector_db_id: str):
    try:
        cprint(f"Starting ingestion of {len(documents)} documents into vector DB", "blue")
        
        provider_id = os.environ.get('VECTOR_STORE', 'faiss')

        # Register vector DB if it doesn't exist
        try:
            client.vector_dbs.register(
                vector_db_id=vector_db_id,
                embedding_model="text-embedding-004",
                embedding_dimension=384,
                provider_id=provider_id
            )
        except Exception as e:
            if "already exists" not in str(e).lower():
                raise

        # Insert documents
        for doc in documents:
            try:
                # Split large content into smaller chunks if needed
                content = doc["text"]
                max_chunk_size = 10000  # characters per chunk
                
                if len(content) > max_chunk_size:
                    cprint(f"Splitting large document: {doc['metadata']['source']} ({len(content)} chars)", "yellow")
                    chunks = [content[i:i+max_chunk_size] for i in range(0, len(content), max_chunk_size)]
                    
                    for i, chunk in enumerate(chunks):
                        chunk_id = f"{doc['id']}_chunk_{i}"
                        chunk_metadata = doc["metadata"].copy()
                        chunk_metadata["chunk_index"] = i
                        chunk_metadata["total_chunks"] = len(chunks)
                        
                        client.tool_runtime.rag_tool.insert(
                            documents=[{
                                "document_id": chunk_id,
                                "content": chunk,
                                "metadata": chunk_metadata
                            }],
                            vector_db_id=vector_db_id,
                            chunk_size_in_tokens=512,
                        )
                    cprint(f"Ingested {len(chunks)} chunks for: {doc['metadata']['source']}", "green")
                else:
                    client.tool_runtime.rag_tool.insert(
                        documents=[{
                            "document_id": doc["id"],
                            "content": content,
                            "metadata": doc["metadata"]
                        }],
                        vector_db_id=vector_db_id,
                        chunk_size_in_tokens=512,
                    )
                    cprint(f"Ingested document: {doc['metadata']['source']}", "green")
            except Exception as e:
                cprint(f"Error ingesting document {doc['metadata']['source']}: {e}", "red")

        cprint(f"Completed ingestion into '{provider_id}' vector DB.", "green")
    except Exception as e:
        cprint(f"Error during ingestion process: {e}", "red")
        raise

# --- Main ---
if __name__ == "__main__":
    print("📄 Loading Tekton YAML documents...")
    docs = load_documents_for_rag(DOCS_DIR)

    if not docs:
        print("No valid documents found to ingest.")
    else:
        ingest_documents_into_rag(client, docs, VECTOR_DB_ID)
