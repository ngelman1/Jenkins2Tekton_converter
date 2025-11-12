import os
import sys
from pathlib import Path
from termcolor import cprint
from dotenv import load_dotenv

from llama_index.core import VectorStoreIndex, Settings
from llama_index.core import SimpleDirectoryReader
from llama_index.core.storage.storage_context import StorageContext
from llama_index.core.schema import Document
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.vector_stores.postgres import PGVectorStore


DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "raguser"
DB_PASS = "ragpassword"
DB_NAME = "tekton_vector_db"
VECTOR_TABLE_NAME_DOCS = "conversion_docs_chunks"
VECTOR_TABLE_NAME_PLUGINS = "plugins_info_chunks"
EMBEDDING_DIMENSION = 768
DOCS_DIR = Path("./tekton_docs")
CATALOG_BASE_URL = "https://artifacthub.io/packages/tekton-task/tekton-catalog-tasks/"
GITHUB_RAW_URL = "https://raw.githubusercontent.com/tektoncd/catalog/main/task/"
TEKTON_CATALOG_URL = "https://artifacthub.io/packages/search?repo=tekton-catalog-tasks"

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


#---------------------------------DOCS_VECTOR------------------------------------------------------------------


def ingest_data_to_postgres():

    try:
        documents = SimpleDirectoryReader(input_dir=DOCS_DIR).load_data()
        if not documents:
            cprint(f"No documents found in {DOCS_DIR}.", "yellow")
            return
    except Exception as e:
        cprint(f"Error reading documents: {e}", "red")
        sys.exit(1)

    cprint(f"Connecting to PostgreSQL database: {DB_NAME} for DOCS", "blue")
    docs_vector_store = PGVectorStore.from_params(
        database=DB_NAME,
        host=DB_HOST,
        password=DB_PASS,
        port=DB_PORT,
        user=DB_USER,
        table_name=VECTOR_TABLE_NAME_DOCS,
        embed_dim=EMBEDDING_DIMENSION,
    )


    cprint("Building Index for DOCS and sending vectors to PostgreSQL...", "blue")
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=StorageContext.from_defaults(vector_store= docs_vector_store)
    )

    cprint(f"Ingestion complete. {len(documents)} documents vectorized and stored in '{VECTOR_TABLE_NAME_DOCS}'.", "green")


#---------------------------------PLUGINS_VECTOR------------------------------------------------------------------


    plugins_vector_store = PGVectorStore.from_params(
        database=DB_NAME,
        host=DB_HOST,
        password=DB_PASS,
        port=DB_PORT,
        user=DB_USER,
        table_name=VECTOR_TABLE_NAME_PLUGINS,
        embed_dim=EMBEDDING_DIMENSION,
    )



if __name__ == "__main__":
    ingest_data_to_postgres()