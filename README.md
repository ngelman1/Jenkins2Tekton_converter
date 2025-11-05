
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

* **Query RAG**: The script constructs a complex query (including the Jenkinsfile content) and sends it to the local vector index.
* **Retrieve Context**: The system retrieves relevant code snippets and documentation chunks (based on similarity scores) directly from your local disk storage.
* **Final Conversion**: This retrieved context is sent to the Large Language Model (LLM) (Gemini) along with your conversion prompt, allowing the LLM to generate an accurate, context-aware Tekton PipelineRun YAML.

---

## 💻 Essential Usage Instructions

This workflow runs your LlamaIndex application directly inside a custom Podman container, leveraging your local files for persistent storage.

### 1. Start the RAG container

Ensure your `GEMINI_API_KEY` is set in your environment before running:
Add it to your .env file, or run: 

```bash
export GEMINI_API_KEY=<your-api-key>
```

```bash
podman run -it --rm \
    -v $(pwd)/tekton_docs:/app/tekton_docs:z \
    -v $(pwd)/tekton_docs_index:/app/tekton_docs_index:z \
    -p 8320:8320 \
    quay.io/ngelman/jenkins2tekton:latest

```
### How to run
To build the vector index needed for RAG (run this inside the container):
``` bash
python ingest_tekton_data.py
```

To run the pipeline generation, make sure your jenkinsfile is in the same directory as the generating script

``` bash
python generate_tekton_pipeline.py <YOUT JENKINSFILE NAME>
```