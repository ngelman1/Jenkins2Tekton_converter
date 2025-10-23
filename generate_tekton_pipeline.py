import os
import sys
import argparse
from pathlib import Path
from termcolor import cprint
from typing import List
from dotenv import load_dotenv 

from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.storage.storage_context import StorageContext
from llama_index.core import load_index_from_storage
from llama_index.core.schema import NodeWithScore 
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.llms.google_genai import GoogleGenAI

INDEX_STORAGE_DIR = "./tekton_docs_index"
QUERY_TEXT = "How to convert a Jenkinsfile to a Tekton pipeline"
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

try:
    if not api_key:
        cprint("GEMINI_API_KEY not set")
        exit(1)

    Settings.embed_model = GoogleGenAIEmbedding(model_mane="models/text-embedding-004" , api_key=api_key)
    Settings.llm=GoogleGenAI(model="gemini-2.5-flash" , api_key=api_key)
    cprint("RAG configuration Loaded" , "green")

except Exception as e:
    cprint("RAG configuration failed" , "red")
    exit(1)

    