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
from llama_index.core.query_engine import RetrieverQueryEngine 
from llama_index.core.response.pprint_utils import pprint_response
from llama_index.core.retrievers import VectorIndexRetriever
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
    Settings.llm = GoogleGenAI(model="gemini-2.5-flash" , api_key=api_key)
    cprint("RAG configuration Loaded" , "green")

except Exception as e:
    cprint("RAG configuration failed" , "red")
    exit(1)

    

def load_index() ->VectorStoreIndex:
    if not Path(INDEX_STORAGE_DIR).exists():
        cprint(f"{INDEX_STORAGE_DIR} does not exists in the current directory" , "red")
        cprint("To create index, run documents ingestion" , "red")
        exit(1)

    try:
        index_context = StorageContext.from_defaults(persist_dir=INDEX_STORAGE_DIR) #this bundels all refernces of the data store files created while ingestion
        index = load_index_from_storage(index_context) #initiation of the index object
        return index
    except Exception as e:
        cprint(f"Failed loading index: {e}" , "red")



def run_simple_query(index: VectorStoreIndex , query:str , top_k: int):
    cprint(f"RAG query for hard-coded question:{QUERY_TEXT}" , "yellow")
    retriever = VectorIndexRetriever(index = index , similarity_top_k = top_k)
    query_engine = RetrieverQueryEngine(retriever=retriever)
    response = query_engine.query(QUERY_TEXT)

    cprint("\n[LLM Answer (Synthesis)]", "blue")
    pprint_response(response)
    

    cprint("\n[Retrieval Assessment]", "yellow")
    for i, node_with_score in enumerate(response.source_nodes, 1):
        score = node_with_score.score
        source = node_with_score.metadata.get('file_name', node_with_score.metadata.get('source', 'N/A'))
        print(f"  [{i}] Source: {source} | SCORE: {score:.4f} ")



def main():
    vector_index = load_index()
    run_simple_query(vector_index , QUERY_TEXT , 4)

if __name__ == "__main__":
    main()