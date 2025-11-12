import os
import sys
import argparse

from pathlib import Path
from termcolor import cprint
from typing import List
from dotenv import load_dotenv


from llama_index.core import VectorStoreIndex, Settings , load_index_from_storage
from llama_index.core.storage.storage_context import StorageContext
from llama_index.core.schema import NodeWithScore
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.response.pprint_utils import pprint_response
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core.response_synthesizers import ResponseMode
from llama_index.vector_stores.postgres import PGVectorStore

DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "raguser"
DB_PASS = "ragpassword"
DB_NAME = "tekton_vector_db"
VECTOR_TABLE_NAME_DOCS = "conversion_docs_chunks"
VECTOR_TABLE_NAME_PLUGINS = "plugins_info_chunks"
EMBEDDING_DIMENSION = 768
TOP_K_CHUNKS = 4

# INDEX_STORAGE_DIR = "./tekton_docs_index"


load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
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
    if not api_key:
        cprint("GEMINI_API_KEY not set")
        exit(1)

    Settings.embed_model = GoogleGenAIEmbedding(model_name="models/text-embedding-004" , api_key=api_key) #consider 001 instead
    Settings.llm = GoogleGenAI(model="gemini-2.5-flash" , api_key=api_key)
    cprint("RAG configuration Loaded" , "green")

except Exception as e:
    cprint("RAG configuration failed" , "red")
    exit(1)




def load_indexs() ->tuple[VectorStoreIndex, VectorStoreIndex]:
    try:
        docs_vector_store = PGVectorStore.from_params(
            database=DB_NAME,
            host=DB_HOST,
            password=DB_PASS,
            port=DB_PORT,
            user=DB_USER,
            embed_dim=EMBEDDING_DIMENSION,
            table_name=VECTOR_TABLE_NAME_DOCS
        )
        docs_index = VectorStoreIndex.from_vector_store(vector_store= docs_vector_store)
        cprint(f"Index loaded: {VECTOR_TABLE_NAME_DOCS}", "green")

        plugins_vector_store = PGVectorStore.from_params(
            database=DB_NAME,
            host=DB_HOST,
            password=DB_PASS,
            port=DB_PORT,
            user=DB_USER,
            embed_dim=EMBEDDING_DIMENSION,
            table_name=VECTOR_TABLE_NAME_PLUGINS
        )
        plugins_index = VectorStoreIndex.from_vector_store(vector_store=plugins_vector_store)
        cprint(f"Index loaded: {VECTOR_TABLE_NAME_PLUGINS}", "green")

        return docs_index ,plugins_index

    except Exception as e:
        cprint(f"Failed loading indexes from POSTGRES. Check the server is running. Error: {e}" , "Red")



def read_jenkinsfile(filename: str) -> str:
    if not Path(filename).exists():
        cprint(f"File -'{filename}' does not exist in this directry" , "red")
        exit(1)
    with open(Path(filename) , 'r' , encoding='utf-8') as file:
        return file.read()



def generate_final_conversion(RAG_context: str, jenkinsfile_content: str) -> str:
    prompt = LLM_prompt.format(
        RAG_result_placeholder = RAG_context,
        jenkinsfile_content_placeholder = jenkinsfile_content
    )
    response = Settings.llm.complete(prompt)
    return response.text.strip()



def run_conversion_query(index: VectorStoreIndex, jenkinsfile_content: str, query: str, top_k: int):

    cprint(f"\n--- RAG Retrieval Query ---", "yellow")
    cprint(f"Query: {query}", "yellow")


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
    parser = argparse.ArgumentParser()
    parser.add_argument('jenkinsfile_path', help='Path to the Jenkinsfile to convert.')
    args = parser.parse_args()
    docs_index, plugins_index = load_indexs()
    jenkinsfile_content = read_jenkinsfile(args.jenkinsfile_path)
    RETRIEVAL_QUERY = f"Convert this Jenkinsfile to Tekton YAML: {Path(args.jenkinsfile_path).name}"
    run_conversion_query(docs_index, jenkinsfile_content, RETRIEVAL_QUERY, TOP_K_CHUNKS)

if __name__ == "__main__":
    main()