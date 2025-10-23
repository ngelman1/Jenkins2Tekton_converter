import os
import time
from pathlib import Path
from typing import List, Dict
from termcolor import cprint
import uuid



from llama_index.core import VectorStoreIndex , SimpleDirectoryReader
from llama_index.core.schema import Document
from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from dotenv import load_dotenv 

load_dotenv()
api_key= os.getenv("GEMINI_API_KEY")
INDEX_STORAGE_DIR = "./tekton_docs_index"



try:
    Settings.embed_model = GoogleGenAIEmbedding(model_mane="models/text-embedding-004" , api_key=api_key)
    Settings.llm=GoogleGenAI(model="gemini-2.5-flash" , api_key=api_key)
except ValueError as e:
    cprint(f"GEMINI CONFIGURATION ERROR: {e}", "red")
    exit(1)


documents = SimpleDirectoryReader("tekton_docs/").load_data()
print(f"Total documents loaded: {len(documents)}")
# if documents:
#     for doc in documents:
#         print(f"Document ID: {doc.doc_id}")
#         print(f"Source: {doc.metadata.get('file_name', 'N/A')}")
# print("---------------------------\n")

index = VectorStoreIndex.from_documents(documents)
index.storage_context.persist(persist_dir=INDEX_STORAGE_DIR)

query_engine = index.as_query_engine()


