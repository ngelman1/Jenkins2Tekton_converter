# Development Guide

This guide is for developers who want to contribute to the project or run the scripts locally outside of the container.

## Prerequisites

- Python 3.9 or higher
- Git
- A [Gemini API key](https://aistudio.google.com/apikey)

## Local Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/ngelman1/Jenkins2Tekton_converter.git
cd Jenkins2Tekton_converter
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv --prompt jenkins2tekton
source .venv/bin/activate
```

To deactivate when you're done:

```bash
deactivate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Set up your API key

```bash
export GEMINI_API_KEY="your-actual-api-key-here"
```


## Running Locally

### Build the Tekton RAG Index

The Tekton documentation index must be built before running conversions. This indexes `tekton_docs/` into ChromaDB:

```bash
python ingest_tekton_data.py
```

This creates the `chroma_db/tekton/` directory. It is **gitignored** (large binary files) but **required for the container image build**.

### (Optional) Ingest Jenkins Shared Library

If your Jenkinsfiles use a shared library, ingest it for better conversion accuracy:

```bash
python ingest_jenkins_data.py /path/to/your/jenkins-shared-library
```

This creates the `chroma_db/jenkins/` directory with vectors for `vars/`, `src/`, resources, Jenkinsfiles, and config YAMLs.

### Generate a Tekton Pipeline

```bash
# Without shared library context:
python generate_tekton_pipeline.py path/to/Jenkinsfile

# With shared library context (recommended):
python generate_tekton_pipeline.py path/to/Jenkinsfile --jenkins-dir /path/to/shared-library
```

Output is saved to `output-dir/<Jenkinsfile-name>/` with one file per resource.

## Project Structure

```
.
├── generate_tekton_pipeline.py  # Main entry point — orchestrates RAG, prompt, and conversion
├── ingest_tekton_data.py        # Indexes Tekton docs into ChromaDB
├── ingest_jenkins_data.py       # Indexes a local Jenkins shared library into ChromaDB
├── jenkins_shared_lib.py        # Parses shared library calls and resolves imports
├── output_writer.py             # Splits YAML into individual resource files
├── tekton_validator.py          # Validates generated YAML, auto-fixes via LLM retry
├── rag_config.py                # Shared LLM/embedding/ChromaDB configuration
├── requirements.txt             # Python dependencies
├── config.yaml                  # Additional configuration
├── tekton_docs/                 # Tekton reference docs (committed, indexed into RAG)
├── chroma_db/                   # ChromaDB vector databases (gitignored, built locally)
│   ├── tekton/                  # Tekton documentation vectors
│   └── jenkins/                 # Jenkins shared library vectors
├── tools/                       # Optional tooling (gitignored)
│   ├── tekton-genie/            # Validator source (separate repo)
│   └── tekton-validate          # Compiled validator binary
├── images/
│   └── Containerfile            # Container image definition
└── .venv/                       # Virtual environment (gitignored)
```

## Building and Publishing the Container Image

### Prerequisites

Before building the container, you **must** build the ChromaDB Tekton index locally. The Containerfile copies this directory into the image.

```bash
# Build the Tekton index if it doesn't exist:
python ingest_tekton_data.py

# Verify it was created:
ls -la chroma_db/tekton/
```

### Build the Container

```bash
podman build -f images/Containerfile -t quay.io/<your-repo>/jenkins2tekton:latest .
```

### Test Locally

```bash
podman run -it --rm \
    -e GEMINI_API_KEY="${GEMINI_API_KEY}" \
    -v $(pwd):/workspace:z \
    quay.io/<your-repo>/jenkins2tekton:latest

# Inside the container:
python generate_tekton_pipeline.py /workspace/Jenkinsfile
```

### Push to Registry

```bash
podman login quay.io
podman push quay.io/<your-repo>/jenkins2tekton:latest
```

### Update Workflow

When updating the Tekton documentation:

1. Update files in `tekton_docs/`
2. Rebuild the index: `python ingest_tekton_data.py`
3. Commit the doc changes
4. Rebuild and test the container image
5. Push to registry

## Contributing

1. Create a new branch for your feature or bug fix
2. Make your changes
3. Test your changes locally
4. Submit a pull request
