# Development Guide

This guide is for developers who want to contribute to the project or run the scripts locally outside of the container.

## Prerequisites

- Python 3.9 or higher
- Git

## Local Development Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd Jenkins2Tekton_converter
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv --prompt jenkins2tekton
```

### 3. Activate the virtual environment

```bash
# On Linux/macOS:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

**Note:** To exit the virtual environment when you're done, simply run:
```bash
deactivate
```

### 4. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Set up your API key

Export your Gemini API key as an environment variable:

```bash
export GEMINI_API_KEY="your-actual-api-key-here"
```

To make it persistent across sessions, add it to your `~/.bashrc` or `~/.zshrc`:

```bash
echo 'export GEMINI_API_KEY="your-actual-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

## Running Locally

Once your environment is set up, you can run the scripts directly:

### Build the Vector Index

The RAG index is included in the container image, so users don't need to build it themselves. As a developer, you **must** build this index locally before building the container:

```bash
# Build the ChromaDB index locally (this will be included in the container image)
python ingest_tekton_data.py
```

This creates the `chroma_db/` directory with the ChromaDB vector database. This directory is **excluded from git** (due to large file sizes) but **required for building the container image**.

**Important Notes:**
- The `chroma_db/` directory is in `.gitignore` and not committed to version control
- You must build the index locally before building the container image
- When you update Tekton documentation in `tekton_docs/`, rebuild the index before building a new container image
- Different developers may have slightly different index files due to timestamp/randomness in the embedding process, but they are functionally equivalent

### Generate Tekton Pipeline

```bash
python generate_tekton_pipeline.py <YOUR_JENKINSFILE_NAME>
```

## Project Structure

```
.
├── images/
│   └── Containerfile          # Container image definition
├── ingest_tekton_data.py      # Document ingestion script
├── generate_tekton_pipeline.py # Pipeline generation script
├── requirements.txt           # Python dependencies
├── tekton_docs/              # Tekton documentation for RAG (committed to git)
├── chroma_db/                # ChromaDB vector database (gitignored, built locally, included in container)
└── .venv/                    # Virtual environment (gitignored)
```

## Contributing

1. Create a new branch for your feature or bug fix
2. Make your changes
3. Test your changes locally
4. Submit a pull request

## Building and Publishing the Container Image

### Prerequisites

Before building the container, you **must** build the ChromaDB index locally. The Containerfile copies this directory into the image.

```bash
# Check if the index exists
ls -la chroma_db/

# If the directory doesn't exist or is empty, build it:
python ingest_tekton_data.py

# Verify the index was created
du -sh chroma_db/
```

### Build the Container

```bash
# Build the container image
podman build -f images/Containerfile -t quay.io/<your-image-repo>/jenkins2tekton:latest .

# Optional: Tag with a version
podman tag quay.io/<your-image-repo>/jenkins2tekton:latest quay.io/<your-image-repo>/jenkins2tekton:v1.0.0
```

**Note:** If the build fails with an error about `chroma_db/` not found, you forgot to build the index first (see Prerequisites above).

### Test the Container Locally

```bash
podman run -it --rm \
    -e GEMINI_API_KEY="${GEMINI_API_KEY}" \
    -p 8320:8320 \
    quay.io/<your-image-repo>/jenkins2tekton:latest

# Inside the container, test the generation:
python generate_tekton_pipeline.py <test-jenkinsfile>
```

### Push to Quay.io

Once tested, push the image to the registry:

```bash
# Login to Quay.io
podman login quay.io

# Push the latest tag
podman push quay.io/<your-image-repo>/jenkins2tekton:latest

# Push version tag (if created)
podman push quay.io/<your-image-repo>/jenkins2tekton:v1.0.0
```

### Update Workflow

When updating the Tekton documentation:

1. Update documentation files in `tekton_docs/`
2. Rebuild the ChromaDB index: `python ingest_tekton_data.py`
3. Commit the documentation changes: `git add tekton_docs/ && git commit -m "Update Tekton docs"`
4. Rebuild the container image (it will pick up the new index)
5. Test the new image locally
6. Push to Quay.io with a new version tag
7. Update the README if the image tag changed

