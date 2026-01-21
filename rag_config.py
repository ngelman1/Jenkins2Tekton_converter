"""
Shared RAG configuration utilities for Jenkins2Tekton converter.

This module provides common configuration setup for RAG operations
used across multiple scripts in the project.
"""
import os
import sys
from termcolor import cprint
from llama_index.core import Settings
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.llms.google_genai import GoogleGenAI


# Model Configuration
EMBEDDING_MODEL = "models/text-embedding-004"
LLM_MODEL = "gemini-2.5-flash"
EMBEDDING_DIMENSION = 768

# ChromaDB Configuration
# Separate paths for static shared data(Tekton) and dynamic personal data(Jenkins)
TEKTON_DB_PATH = "./chroma_db/tekton"
JENKINS_DB_PATH = "./chroma_db/jenkins"

DEFAULT_COLLECTION_NAME = "default_data"
JENKINS_COLLECTION_NAME = "jenkins_data"


def setup_rag_configuration() -> str:
    api_key = os.getenv('GEMINI_API_KEY')

    if not api_key:
        cprint("FATAL: GEMINI_API_KEY environment variable is not set.", "red")
        cprint("Please set it using: export GEMINI_API_KEY='your-api-key'", "yellow")
        sys.exit(1)

    try:
        Settings.embed_model = GoogleGenAIEmbedding(model_name=EMBEDDING_MODEL, api_key=api_key)
        Settings.llm = GoogleGenAI(model=LLM_MODEL, api_key=api_key)
        cprint("✓ RAG Configuration Loaded.", "green")
        return api_key

    except Exception as e:
        cprint(f"FATAL: RAG Configuration error: {e}", "red")
        sys.exit(1)

