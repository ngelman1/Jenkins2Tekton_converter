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

INDEX_STORAGE_DIR = "./tekton_docs_index"
QUERY_TEXT = "How to convert a Jenkinsfile to a Tekton pipeline"
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

    Settings.embed_model = GoogleGenAIEmbedding(model_name="models/text-embedding-004" , api_key=api_key)
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


def read_jenkinsfile(filename: str) -> str:
    if not Path(filename).exists():
        cprint(f"File -'{filename}' does not exist in this directry" , "red")
        exit(1)
    with open(Path(filename) , 'r' , encoding='utf-8') as file:
        return file.read()
    


def run_conversion_query(index: VectorStoreIndex, jenkinsfile_content: str, query: str, top_k: int) -> tuple[str, str]:
    
    cprint(f"RAG retrieval query: {query}", "yellow")
    retriever = VectorIndexRetriever(index=index, similarity_top_k=top_k)
    retrieval_results: List[NodeWithScore] = retriever.retrieve(query)

    cprint("\n[Retrieval Assessment]", "yellow")
    context_texts = []
    
    for i, node_with_score in enumerate(retrieval_results, 1):
        score = node_with_score.score
        source = node_with_score.metadata.get('file_name', node_with_score.metadata.get('source', 'N/A'))
        context_texts.append(node_with_score.text)

        print(f"  [{i}] Source: {source} | SCORE: {score:.4f} ")
    
    combined_context = "\n\n---\n\n".join(context_texts)
    final_yaml_output = generate_final_conversion(combined_context, jenkinsfile_content)
    
    cprint("\n[Final Tekton Conversion]", "blue")
    print(final_yaml_output)

    return combined_context, final_yaml_output


def generate_final_conversion(RAG_response: str , jenkinsfile: str) -> str:
    prompt = LLM_prompt.format(
        RAG_result_placeholder = RAG_response , 
        jenkinsfile_content_placeholder = jenkinsfile
    )
    response = Settings.llm.complete(prompt)
    return response.text.strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('jenkinsfile_path', help='Path to the Jenkinsfile to convert.') 
    args = parser.parse_args()
    vector_index = load_index()
    jenkinsfile_content = read_jenkinsfile(args.jenkinsfile_path)
    run_conversion_query(vector_index, jenkinsfile_content, QUERY_TEXT, 4)

if __name__ == "__main__":
    main()