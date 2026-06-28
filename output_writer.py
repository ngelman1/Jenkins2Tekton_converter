# output_writer.py
"""YAML output splitting and file writing for Tekton conversion results."""
import re
from pathlib import Path
from typing import Dict, List

import yaml
from termcolor import cprint

OUTPUT_DIR = Path("./output-dir")
MARKDOWN_FENCE_RE = re.compile(r"^\s*```\w*\s*\n?", re.MULTILINE)


def strip_markdown_fences(text: str) -> str:
    """Remove markdown code fences (```yaml ... ```) the LLM sometimes adds."""
    return MARKDOWN_FENCE_RE.sub("", text).strip()


def _extract_kind_and_name(raw_doc: str) -> tuple:
    """Best-effort extraction of kind and name from a raw YAML string."""
    kind = "unknown"
    name = "unnamed"
    for line in raw_doc.splitlines():
        stripped = line.strip()
        if stripped.startswith("kind:"):
            kind = stripped.split(":", 1)[1].strip().strip('"').strip("'").lower()
        if stripped.startswith("name:") and name == "unnamed":
            name = stripped.split(":", 1)[1].strip().strip('"').strip("'")
        if stripped.startswith("generateName:") and name == "unnamed":
            name = stripped.split(":", 1)[1].strip().strip('"').strip("'").rstrip("-")
    return kind, name


def _save_parsed_docs(docs: list, out_dir: Path) -> List[Path]:
    """Save cleanly parsed YAML documents."""
    written: List[Path] = []
    task_counter: Dict[str, int] = {}

    for doc in docs:
        if doc is None:
            continue

        kind = doc.get("kind", "unknown").lower()
        name = doc.get("metadata", {}).get("name") or doc.get("metadata", {}).get("generateName", "unnamed")
        name = name.rstrip("-")
        if name.startswith(f"{kind}-"):
            name = name[len(kind) + 1:]

        if kind in task_counter:
            task_counter[kind] += 1
        else:
            task_counter[kind] = 0

        filename = f"{task_counter[kind]:02d}-{kind}-{name}.yaml"
        filepath = out_dir / filename

        filepath.write_text(
            yaml.dump(doc, default_flow_style=False, sort_keys=False),
            encoding="utf-8",
        )
        written.append(filepath)

    return written


def _save_raw_docs(yaml_content: str, out_dir: Path) -> List[Path]:
    """Fallback: split on '---' and save raw text with best-effort naming."""
    raw_docs = re.split(r"\n---\s*\n", yaml_content)
    written: List[Path] = []
    task_counter: Dict[str, int] = {}

    for raw_doc in raw_docs:
        raw_doc = raw_doc.strip()
        if not raw_doc:
            continue

        kind, name = _extract_kind_and_name(raw_doc)
        if name.startswith(f"{kind}-"):
            name = name[len(kind) + 1:]

        if kind in task_counter:
            task_counter[kind] += 1
        else:
            task_counter[kind] = 0

        filename = f"{task_counter[kind]:02d}-{kind}-{name}.yaml"
        filepath = out_dir / filename

        filepath.write_text(raw_doc + "\n", encoding="utf-8")
        written.append(filepath)

    return written


def save_output(yaml_content: str, jenkinsfile_name: str) -> List[Path]:
    """Split YAML into individual resources and save each to a separate file.

    Tries yaml.safe_load_all first for clean output; falls back to raw
    '---' splitting if the LLM produced malformed YAML.
    """
    yaml_content = strip_markdown_fences(yaml_content)

    safe_name = jenkinsfile_name.replace("/", "_").replace("\\", "_")
    out_dir = OUTPUT_DIR / safe_name
    if out_dir.exists():
        for old_file in out_dir.glob("*.yaml"):
            old_file.unlink()
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        docs = list(yaml.safe_load_all(yaml_content))
        use_parsed = True
    except yaml.YAMLError as e:
        cprint(f"  Warning: LLM produced invalid YAML, falling back to raw split: {e}", "yellow")
        docs = None
        use_parsed = False

    if use_parsed and docs:
        return _save_parsed_docs(docs, out_dir)
    return _save_raw_docs(yaml_content, out_dir)
