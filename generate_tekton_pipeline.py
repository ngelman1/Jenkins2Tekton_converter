import os
import sys
import argparse
from pathlib import Path
from termcolor import cprint
from typing import List
from dotenv import load_dotenv
import logging

from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.storage.storage_context import StorageContext
from llama_index.core.schema import NodeWithScore
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

# --- CONFIGURATION ---
CHROMA_PERSIST_DIR = "./chroma_db"
COLLECTION_NAME = "default_data"
EMBEDDING_DIMENSION = 768
TOP_K_CHUNKS = 4
# ---------------------

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    cprint("GEMINI_API_KEY not set", "red")
    sys.exit(1)
LLM_prompt = """
        You are a Tekton expert. Convert the following Jenkinsfile into valid Tekton v1 YAML.

        Use the following reference material from the knowledge base (RAG results) to guide the conversion:

        {RAG_result_placeholder}

        Requirements:
        1. Break down the pipeline into separate Tekton resources:
        - One or more Task objects (one per Jenkins stage/step).
        - A Pipeline object that references those Tasks.
        - A PipelineRun object that executes the Pipeline.
        2. Use only Tekton v1 syntax.
        3. Scripts must be strings (not arrays).
        4. Output MUST be multiple YAML documents separated by '---':
        first the Task(s), then the Pipeline, then the PipelineRun.
        5. Output ONLY raw YAML, no markdown formatting or explanations.
        6. **Important:** If a simple value or string is passed between steps, prefer using **results** instead of workspaces. Use workspaces only for files or larger data.

        Jenkinsfile:
        {jenkinsfile_content_placeholder}
        """


try:
    Settings.embed_model = GoogleGenAIEmbedding(model_name="models/text-embedding-004" , api_key=api_key)
    Settings.llm = GoogleGenAI(model="gemini-2.5-flash" , api_key=api_key)
    cprint("RAG configuration Loaded" , "green")
except Exception as e:
    cprint(f"RAG configuration failed: {e}", "red")
    sys.exit(1)


def read_jenkinsfile(filename: str) -> str:
    if not Path(filename).exists():
        cprint(f"File -'{filename}' does not exist in this directry" , "red")
        sys.exit(1)
    with open(Path(filename) , 'r' , encoding='utf-8') as file:
        return file.read()


def load_index_chromadb() -> VectorStoreIndex:
    """
    Load the default Tekton documentation index from ChromaDB.
    Uses the 'default_data' collection that ships with the container.
    Future: Support loading per-customer collections for multi-tenancy.
    """
    if not Path(CHROMA_PERSIST_DIR).exists():
        cprint(f"ChromaDB storage '{CHROMA_PERSIST_DIR}' does not exist.", "red")
        cprint(f"To create the index, run: python ingest_tekton_data.py", "yellow")
        sys.exit(1)

    try:
        cprint(f"Loading ChromaDB from: {CHROMA_PERSIST_DIR}", "blue")

        # Initialize ChromaDB client
        chroma_client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)

        # Get the default collection
        chroma_collection = chroma_client.get_collection(name=COLLECTION_NAME)

        cprint(f"✓ Collection loaded: '{COLLECTION_NAME}' ({chroma_collection.count()} vectors)", "green")

        # Create vector store from collection
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

        # Return index from vector store
        return VectorStoreIndex.from_vector_store(vector_store=vector_store)
    except Exception as e:
        cprint(f"Failed loading ChromaDB index: {e}", "red")
        sys.exit(1)


def generate_final_conversion(RAG_context: str, jenkinsfile_content: str) -> str:
    prompt = LLM_prompt.format(
        RAG_result_placeholder = RAG_context,
        jenkinsfile_content_placeholder = jenkinsfile_content
    )
    response = Settings.llm.complete(prompt)
    return response.text.strip()


def run_conversion_query(index: VectorStoreIndex, jenkinsfile_content: str, query: str, top_k: int):

    cprint(f"\n--- RAG Retrieval Query ---", "yellow")
    retriever = VectorIndexRetriever(index=index, similarity_top_k=top_k)
    retrieval_results: List[NodeWithScore] = retriever.retrieve(query)

    cprint("\n[Retrieval Assessment]", "yellow")
    context_texts = []

    for i, node_with_score in enumerate(retrieval_results, 1):
        score = node_with_score.score
        source = node_with_score.node.metadata.get('file_name', node_with_score.node.metadata.get('source', 'N/A'))
        context_texts.append(node_with_score.text)
        print(f"  [{i}] Source: {source} | SCORE: {score:.4f} ")

    combined_context = "\n\n---\n\n".join(context_texts)

    final_yaml_output = generate_final_conversion(combined_context, jenkinsfile_content)
    cprint("\n[Final Tekton Conversion]", "blue")
    print(final_yaml_output)


def main():
    parser = argparse.ArgumentParser(
        description="Generate Tekton pipeline from Jenkinsfile using ChromaDB-powered RAG"
    )
    parser.add_argument('jenkinsfile_path', help='Path to the Jenkinsfile to convert')
    args = parser.parse_args()

    # Load the default Tekton documentation index from ChromaDB
    index = load_index_chromadb()

    jenkinsfile_content = read_jenkinsfile(args.jenkinsfile_path)
    RETRIEVAL_QUERY = f"Convert this Jenkinsfile to Tekton YAML: {Path(args.jenkinsfile_path).name}"

    run_conversion_query(index, jenkinsfile_content, RETRIEVAL_QUERY, TOP_K_CHUNKS)


if __name__ == "__main__":
    main()
