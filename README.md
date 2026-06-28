# Jenkins2Tekton Converter

An AI-powered tool that converts Jenkins pipelines (including shared library code) into valid Tekton v1 YAML resources. It uses Retrieval-Augmented Generation (RAG) with ChromaDB and Google Gemini to produce context-aware, production-ready Tekton Pipelines, Tasks, and PipelineRuns.

## How It Works

```
Jenkinsfile + Shared Library (local dir)
            │
            ▼
┌───────────────────────┐
│  Ingest Jenkins Data  │──▶ ChromaDB (jenkins vector store)
└───────────────────────┘
                                    │
┌───────────────────────┐           │
│  Ingest Tekton Docs   │──▶ ChromaDB (tekton vector store)
└───────────────────────┘           │
                                    ▼
┌──────────────────────────────────────────────┐
│          generate_tekton_pipeline.py          │
│                                              │
│  1. Query both RAG indexes for context       │
│  2. Parse shared library calls + imports     │
│  3. Build LLM prompt with all context        │
│  4. Gemini generates Tekton YAML             │
│  5. Split into individual resource files     │
│  6. Validate & auto-fix with LLM retry loop  │
└──────────────────────────────────────────────┘
            │
            ▼
    output-dir/<Jenkinsfile>/
        00-task-*.yaml
        01-task-*.yaml
        00-pipeline-*.yaml
        00-pipelinerun-*.yaml
```

The converter takes a **local directory** containing your Jenkins shared library (Jenkinsfiles, `vars/`, `src/`, config YAMLs) and uses that context alongside Tekton documentation to generate accurate conversions.

## Prerequisites

- **Python 3.9+**
- **A Gemini API key** — get one at [Google AI Studio](https://aistudio.google.com/apikey)
- **Podman or Docker** (optional, for running via container)

## Quick Start (Local)

### 1. Clone and set up the environment

```bash
git clone https://github.com/ngelman1/Jenkins2Tekton_converter.git
cd Jenkins2Tekton_converter

python3 -m venv .venv --prompt jenkins2tekton
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Set your API key

```bash
export GEMINI_API_KEY="your-api-key-here"
```

### 3. Build the Tekton RAG index

This indexes the Tekton documentation shipped in `tekton_docs/` into ChromaDB:

```bash
python ingest_tekton_data.py
```

### 4. (Optional) Ingest your Jenkins shared library

If your Jenkinsfile uses a shared library, ingest the library directory to give the LLM full context on what each function actually does:

```bash
python ingest_jenkins_data.py /path/to/your/jenkins-shared-library
```

The directory should follow the standard Jenkins shared library layout:

```
your-shared-library/
├── vars/              # Pipeline entry points (*.groovy)
├── src/               # Supporting Groovy classes
├── resources/         # Resource files (pod YAMLs, templates)
├── Jenkinsfile*       # Pipeline definitions
└── pipeline*.yml      # Pipeline configuration
```

### 5. Generate Tekton pipeline

```bash
# Basic conversion (no shared library context):
python generate_tekton_pipeline.py path/to/Jenkinsfile

# With shared library context (recommended):
python generate_tekton_pipeline.py path/to/Jenkinsfile --jenkins-dir /path/to/your/jenkins-shared-library
```

Output is written to `output-dir/<Jenkinsfile-name>/` with one file per Tekton resource (configurable via `OUTPUT_DIR` in `output_writer.py`).

## Quick Start (Container) — Optional

The container is **not required** to use this tool. The local setup above is the primary workflow. The container is provided as a convenience — it comes with a pre-built Tekton RAG index so you can skip the ingestion step:

```bash
podman run -it --rm \
    -e GEMINI_API_KEY="${GEMINI_API_KEY}" \
    -v $(pwd):/workspace:z \
    quay.io/ngelman/jenkins2tekton:latest

# Inside the container:
python generate_tekton_pipeline.py /workspace/Jenkinsfile \
    --jenkins-dir /workspace/your-shared-library
```

## Project Structure

```
.
├── generate_tekton_pipeline.py  # Main entry point — orchestrates RAG query, prompt building, and conversion
├── ingest_tekton_data.py        # Indexes Tekton docs into ChromaDB (tekton vector store)
├── ingest_jenkins_data.py       # Indexes a local Jenkins shared library into ChromaDB (jenkins vector store)
├── jenkins_shared_lib.py        # Parses shared library calls, resolves imports, extracts relevant source code
├── output_writer.py             # Splits multi-document YAML into individual resource files
├── tekton_validator.py          # Validates generated YAML and retries fixes via LLM
├── rag_config.py                # Shared RAG/LLM configuration (model names, ChromaDB paths)
├── requirements.txt             # Python dependencies
├── tekton_docs/                 # Tekton reference documentation (indexed into RAG)
├── images/
│   └── Containerfile            # Container image definition
├── DEVELOPMENT.md               # Developer setup and contribution guide
└── config.yaml                  # Additional configuration
```

## Development

For information on local development setup, building the container image, and contributing, see [DEVELOPMENT.md](DEVELOPMENT.md).
