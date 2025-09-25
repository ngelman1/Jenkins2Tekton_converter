
## Overview

This an AI-powered tool that helps you generate Tekton PipelineRuns. It uses a combination of vector database storage and large language models to understand Tekton documentation and generate valid PipelineRun configurations and leverages AI agent to validate the generated PipelineRun YAML.

## Features

- 📚 **Document Ingestion**: Automatically processes and indexes Tekton documentation for contextual understanding
- 🔧 **PipelineRun Generation**: Creates Tekton PipelineRuns based on natural language requirements

## Components

### 1. Document Ingestion (`ingest_tekton_data.py`)

This component handles the ingestion of Tekton documentation into a vector database:

- Supports multiple document formats (.md, .txt, .pdf, .html, .docx, .pptx, .csv, .json, .yaml, .yml)
- Processes documents into chunks for efficient retrieval
- Stores documents with metadata in a vector database (FAISS by default)

### 2. PipelineRun Generation (`generate_tekton_pipeline.py`)

The main PipelineRun generation tool that:

- Searches the knowledge base for relevant examples and context
- Generates valid Tekton PipelineRun configurations


## 💡 General Explanation

The project uses **Retrieval-Augmented Generation (RAG)** to create robust Tekton YAMLs. When you run the generation script, the process follows these three steps:

* **Query RAG**: The script sends a query (currently hard-coded) to the vector database (powered by LlamaStack).
* **Retrieve Context**: The system retrieves relevant code snippets and documentation chunks from your indexed knowledge base (the documents you ingested).
* **Final Conversion**: This retrieved context is sent to the Large Language Model (LLM) along with your conversion prompt, allowing the LLM to generate an accurate, context-aware Tekton PipelineRun YAML.

---

## 💻 Essential Usage Instructions

This project requires the LlamaStack server running in the background to handle the vector database and RAG functionality.

### 1. Start the LlamaStack Server (Mandatory)

The server runs on `http://localhost:8321` and acts as the backend for the vector database and LLM endpoint.

Ensure your `GEMINI_API_KEY` is set in your environment before running:

```bash
export GEMINI_API_KEY=<your-api-key>

podman run -it --rm \
  -v ./config.yaml:/app/config.yaml:z \
  -v ${SQLITE_STORE_DIR:-~/.llama/distributions/gemini}:/data \
  -e GEMINI_API_KEY=$GEMINI_API_KEY \
  -e SQLITE_STORE_DIR=/data \
  -p 8321:8321 \
  docker.io/llamastack/distribution-starter \
  --config config.yaml
