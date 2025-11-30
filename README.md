
## Overview

This an AI-powered tool that helps you generate Tekton PipelineRuns. It uses a combination of vector database storage and large language models to understand Tekton documentation and generate valid PipelineRun configurations and leverages AI agent to validate the generated PipelineRun YAML.

## Features

- **Document Ingestion**: Automatically processes and indexes Tekton documentation for contextual understanding
- **PipelineRun Generation**: Creates Tekton PipelineRuns based on natural language requirements
- **Dual Backend**: Supports both local file system (FAISS) and external server (PostgreSQL) storage.

## How It Works

The project uses **Retrieval-Augmented Generation (RAG)** to create robust Tekton YAMLs. When you run the generation script, the process follows these three steps:

* **Query RAG**: Dynamically Loads Index from the chosen backend (Postgres or Local Disk) and queries it.
* **Retrieve Context**: The system retrieves relevant code snippets and documentation chunks (based on similarity scores) directly from your local disk storage.
* **Final Conversion**: This retrieved context is sent to the Large Language Model (LLM) (Gemini) along with your conversion prompt, allowing the LLM to generate an accurate, context-aware Tekton PipelineRun YAML.

---

## Prerequisites

- Podman (or Docker)
- A Gemini API key

## Usage

### 1. Set up your API key

Export your Gemini API key as an environment variable:

```bash
export GEMINI_API_KEY="your-actual-api-key-here"
```

### 2. Start the Jenkins2Tekton container

The container comes with a pre-built RAG index, so you can start using it immediately:

```bash
podman run -it --rm \
    -e GEMINI_API_KEY="${GEMINI_API_KEY}" \
    -p 8320:8320 \
    quay.io/ngelman/jenkins2tekton:latest
```

**Note:** The pre-built index is included in the container image. You don't need to mount volumes or build the index yourself.

### 3. Generate Tekton Pipeline

Inside the container, copy your Jenkinsfile to `/app` and run the generation script:

```bash
# Copy your Jenkinsfile into the container (from another terminal):
podman cp /path/to/your/Jenkinsfile <container-id>:/app/

# Inside the container, generate the pipeline:
python generate_tekton_pipeline.py Jenkinsfile --backend LLAMA_INDEX
```

Or mount your Jenkinsfile directory when starting the container:

```bash
podman run -it --rm \
    -e GEMINI_API_KEY="${GEMINI_API_KEY}" \
    -v $(pwd):/workspace:z \
    -p 8320:8320 \
    quay.io/ngelman/jenkins2tekton:latest

# Inside the container:
python generate_tekton_pipeline.py /workspace/Jenkinsfile --backend LLAMA_INDEX
```

---

## Development

For information on local development setup, testing, and contributing to the project, see [DEVELOPMENT.md](DEVELOPMENT.md).
