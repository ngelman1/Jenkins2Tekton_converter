General Explanation
The project uses Retrieval-Augmented Generation (RAG) to create robust Tekton YAMLs. When you run the generation script, the process follows these three steps:

Query RAG: The script sends a query (currently hard-coded) to the vector database (powered by LlamaStack).

Retrieve Context: The system retrieves relevant code snippets and documentation chunks from your indexed knowledge base (the documents you ingested).

Final Conversion: This retrieved context is sent to the Large Language Model (LLM) along with your conversion prompt, allowing the LLM to generate an accurate, context-aware Tekton PipelineRun YAML.




💻 Essential Usage Instructions
This project requires the LlamaStack server running in the background to handle the vector database and RAG functionality.

1. Start the LlamaStack Server (Mandatory)
The server runs on http://localhost:8321 and acts as the backend for the vector database and LLM endpoint.

Ensure your GEMINI_API_KEY is set in your environment before running:

Bash

export GEMINI_API_KEY=<your-api-key>

podman run -it --rm \
  -v ./config.yaml:/app/config.yaml:z \
  -v ${SQLITE_STORE_DIR:-~/.llama/distributions/gemini}:/data \
  -e GEMINI_API_KEY=$GEMINI_API_KEY \
  -e SQLITE_STORE_DIR=/data \
  -p 8321:8321 \
  docker.io/llamastack/distribution-starter \
  --config config.yaml
Goal: The server must be running and accessible at http://localhost:8321.

2. Run Document Ingestion (One-Time Setup)
This step processes your Tekton documentation and loads it into the vector database. Only run this when adding new documentation.

Bash

uv run --with llama-stack-client ingest_tekton_data.py
