from pathlib import Path

LLAMA_STACK_HOST = "http://localhost:8322"
DEFAULT_MODEL = "gemini"
VECTOR_DB_ID = "tekton_docs_vector_db"
JENKINSFILE_PATH = Path("Jenkinsfile")

SUPPORTED_MODELS = {
    "gemini": "gemini-2.5-pro",
    "granite": "granite-8b"
}

# RAG query configuration parameters. comment out to use default
DEFAULT_QUERY_CONFIG = {
    "chunk_template": "Result {index}\nContent: {chunk.content}\nMetadata: {metadata}\n",
    "max_chunks": 10,
    "max_tokens_in_context": 1000,
    "mode": "vector"
}

