# jenkins_shared_lib.py
"""Jenkins shared library parsing and context building.

Detects shared library calls in Jenkinsfiles, loads the vars/ entry point,
resolves imported src/ classes, and builds a context section for the LLM prompt.
"""
import re
from pathlib import Path
from typing import Dict, Optional

from termcolor import cprint

GROOVY_IMPORT_RE = re.compile(r"^import\s+([\w.]+)\s*$", re.MULTILINE)

METHOD_TRIM_THRESHOLD = 2000


def detect_shared_lib_call(jenkinsfile_content: str, jenkins_dir: Optional[Path] = None) -> Optional[str]:
    """Detect the shared library entry-point function called by a Jenkinsfile.

    Scans the vars/ folder for available function names, then checks which
    ones appear in the Jenkinsfile. Returns the first match.
    """
    if jenkins_dir is None:
        return None

    vars_dir = jenkins_dir / "vars"
    if not vars_dir.is_dir():
        return None

    available = {f.stem for f in vars_dir.glob("*.groovy")}

    for name in available:
        if re.search(rf"\b{name}\s*[\({{]", jenkinsfile_content):
            return name

    return None


def load_shared_lib_source(jenkins_dir: Path, func_name: str) -> Optional[str]:
    """Read the shared library source file for a given function name.

    In a Jenkins shared library, vars/<funcName>.groovy is the entry point.
    """
    lib_file = jenkins_dir / "vars" / f"{func_name}.groovy"
    if not lib_file.exists():
        cprint(f"  Shared library file not found: {lib_file}", "yellow")
        return None

    content = lib_file.read_text(encoding="utf-8")
    cprint(f"  Loaded shared library: {lib_file.name} ({len(content):,} chars)", "green")
    return content


def _class_name(import_path: str) -> str:
    """Extract the simple class name from a fully qualified import path."""
    return import_path.rsplit(".", 1)[-1]


def _strip_imports_and_comments(source: str) -> str:
    """Return the groovy body without import lines and block comments."""
    lines = source.splitlines()
    body_lines = []
    in_block_comment = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("/*"):
            in_block_comment = True
        if in_block_comment:
            if "*/" in stripped:
                in_block_comment = False
            continue
        if stripped.startswith("import "):
            continue
        body_lines.append(line)
    return "\n".join(body_lines)


def _find_called_methods(class_name: str, body: str) -> set:
    """Find method names called on a class in the groovy body (ClassName.method)."""
    return set(re.findall(rf"\b{class_name}\.(\w+)", body))


def _extract_methods(class_source: str, method_names: set) -> str:
    """Extract class header and only the specified methods from Groovy source.

    Uses brace-depth tracking to find method boundaries.
    """
    lines = class_source.splitlines()
    header_lines = []
    body_start = 0

    for i, line in enumerate(lines):
        stripped = line.strip()
        header_lines.append(line)
        if re.match(r"^(class|abstract\s+class|final\s+class)\s+", stripped):
            body_start = i + 1
            break

    result_lines = list(header_lines)
    in_method = False
    brace_depth = 0
    seen_open_brace = False

    for line in lines[body_start:]:
        stripped = line.strip()

        if not in_method:
            for m in method_names:
                if re.search(rf"\b{m}\s*\(", stripped):
                    in_method = True
                    brace_depth = 0
                    seen_open_brace = False
                    result_lines.append("")
                    break

        if in_method:
            result_lines.append(line)
            brace_depth += line.count("{") - line.count("}")
            if "{" in line:
                seen_open_brace = True
            if seen_open_brace and brace_depth <= 0:
                in_method = False

    result_lines.append("}")
    return "\n".join(result_lines)


def resolve_imported_sources(jenkins_dir: Path, groovy_source: str) -> Dict[str, str]:
    """Parse import statements from a Groovy file and load relevant sources.

    Only includes classes that have direct static method calls (ClassName.method)
    in the groovy body. Skips classes that are only instantiated with 'new' or
    referenced in commented-out code. Large files are trimmed to only include
    the methods actually called.
    """
    imports = GROOVY_IMPORT_RE.findall(groovy_source)
    body = _strip_imports_and_comments(groovy_source)

    active_imports = []
    for imp in imports:
        cls = _class_name(imp)
        if re.search(rf"\b{cls}\.\w+", body):
            active_imports.append(imp)

    sources: Dict[str, str] = {}
    for imp in active_imports:
        rel_path = imp.replace(".", "/") + ".groovy"
        src_file = jenkins_dir / "src" / rel_path
        if not src_file.exists():
            continue

        content = src_file.read_text(encoding="utf-8")
        cls = _class_name(imp)

        if len(content) > METHOD_TRIM_THRESHOLD:
            called = _find_called_methods(cls, body)
            sources[imp] = _extract_methods(content, called)
        else:
            sources[imp] = content

    return sources


def build_shared_lib_section(jenkins_dir: Optional[Path], jenkinsfile_content: str) -> str:
    """Build the shared library context section for the LLM prompt.

    If a jenkins-dir is provided and the Jenkinsfile calls a shared library,
    load the vars/ source and all imported src/ classes.
    """
    if jenkins_dir is None:
        return ""

    func_name = detect_shared_lib_call(jenkinsfile_content, jenkins_dir)
    if not func_name:
        cprint("  No shared library call detected in Jenkinsfile.", "cyan")
        return ""

    cprint(f"  Detected shared library call: {func_name}()", "cyan")
    source = load_shared_lib_source(jenkins_dir, func_name)
    if not source:
        return ""

    sections = [
        f"The Jenkinsfile calls the shared library function `{func_name}()`. "
        f"Below is the FULL source code of `vars/{func_name}.groovy` — "
        f"this IS the pipeline implementation. Convert every stage and step "
        f"from this file into Tekton resources:\n\n{source}",
    ]

    imported = resolve_imported_sources(jenkins_dir, source)
    if imported:
        cprint(f"  Resolved {len(imported)} imported source classes", "green")

        sections.append(
            "\nBelow are the source files for the utility classes imported by "
            "the shared library. Use these to understand what each function "
            "actually does — do NOT generate placeholder/simulated steps:\n"
        )
        for imp, content in imported.items():
            sections.append(f"# --- {imp} ---\n{content}")

    return "\n\n".join(sections)
