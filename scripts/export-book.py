#!/usr/bin/env python3
import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]

def read_yaml(path):
    if yaml is None:
        raise SystemExit("Pythonpaketet PyYAML saknas. Installera med: python3 -m pip install pyyaml")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def validate_markdown(path, text):
    errors = []
    if re.search(r"^####", text, flags=re.MULTILINE):
        errors.append(f"{path}: innehåller H4-rubrik eller djupare rubrik.")
    if text.count("```") % 2 != 0:
        errors.append(f"{path}: kodblock verkar sakna avslutande ```.")
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.match(r"^\|.*\|$", line):
            if i + 1 < len(lines) and not re.match(r"^\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?$", lines[i + 1]):
                if i == 0 or not re.match(r"^\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?$", lines[i]):
                    errors.append(f"{path}: möjlig tabell utan korrekt separatorrad nära rad {i+1}.")
                    break
    for match in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", text):
        img = match.group(1)
        if img.startswith("http://") or img.startswith("https://"):
            continue
        if not (path.parent / img).resolve().exists():
            errors.append(f"{path}: bildreferens saknas: {img}")
    return errors

def build_markdown(metadata):
    chapters = metadata.get("chapters", [])
    if not chapters:
        raise SystemExit("Metadata saknar kapitelordning.")
    build_dir = ROOT / "build"
    build_dir.mkdir(exist_ok=True)
    combined = build_dir / "book.md"
    errors = []
    parts = []
    for chapter in chapters:
        path = ROOT / chapter
        if not path.exists():
            errors.append(f"Saknat kapitel: {chapter}")
            continue
        text = path.read_text(encoding="utf-8")
        errors.extend(validate_markdown(path, text))
        parts.append(text.strip() + "\n")
    if errors:
        print("Valideringsfel:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)
    combined.write_text("\n\n".join(parts), encoding="utf-8")
    return combined

def run_pandoc(metadata, source, fmt):
    if shutil.which("pandoc") is None:
        raise SystemExit("Pandoc saknas. Installera Pandoc och kör scriptet igen.")
    exports = ROOT / "exports"
    exports.mkdir(exist_ok=True)
    title = metadata.get("title", "")
    author = metadata.get("author", "")
    lang = "sv-SE" if metadata.get("language") == "sv" else "en-US"
    slug = metadata.get("project_slug", "book")
    if not title or not author:
        raise SystemExit("Metadata måste innehålla title och author före export.")
    if fmt == "epub":
        out = exports / f"{slug}.epub"
        cmd = [
            "pandoc", str(source), "--from=gfm", "--to=epub3",
            "--metadata", f"title={title}",
            "--metadata", f"author={author}",
            "--metadata", f"lang={lang}",
            "--css", str(ROOT / "styles/epub.css"),
            "--output", str(out),
        ]
    elif fmt == "pdf":
        out = exports / f"{slug}.pdf"
        cmd = [
            "pandoc", str(source), "--from=gfm",
            "--pdf-engine=xelatex",
            "--toc", "--toc-depth=3",
            "--metadata", f"title={title}",
            "--metadata", f"author={author}",
            "--metadata", f"lang={lang}",
            "--output", str(out),
        ]
    elif fmt == "docx":
        out = exports / f"{slug}.docx"
        cmd = [
            "pandoc", str(source), "--from=gfm", "--to=docx",
            "--metadata", f"title={title}",
            "--metadata", f"author={author}",
            "--metadata", f"lang={lang}",
            "--output", str(out),
        ]
    elif fmt == "markdown":
        out = exports / f"{slug}.md"
        shutil.copyfile(source, out)
        print(f"Skapade {out}")
        return
    else:
        raise SystemExit(f"Okänt format: {fmt}")
    print("Kör:", " ".join(cmd))
    subprocess.run(cmd, check=True)
    print(f"Skapade {out}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=["epub", "pdf", "docx", "markdown", "all"], default="all")
    args = parser.parse_args()
    meta_path = ROOT / "docs/export-metadata.yaml"
    if not meta_path.exists():
        meta_path = ROOT / "book.yaml"
    metadata = read_yaml(meta_path)
    source = build_markdown(metadata)
    formats = ["epub", "pdf", "docx", "markdown"] if args.format == "all" else [args.format]
    for fmt in formats:
        run_pandoc(metadata, source, fmt)

if __name__ == "__main__":
    main()
