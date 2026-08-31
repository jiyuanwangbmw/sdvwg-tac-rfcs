#!/usr/bin/env python3

"""
Generate the mdBook source tree from the RFC repository layout.

RFCs live under text/, while src/ is generated just before building the book.
"""

import os
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RFC_DIR = ROOT / "text"
SOURCE_DIR = ROOT / "src"
SUPPORTING_DOCUMENTS = (
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "COPYRIGHT",
    "LICENSE-APACHE",
    "LICENSE-MIT",
    "LICENSE-documentation",
)


def main():
    if SOURCE_DIR.exists():
        shutil.rmtree(SOURCE_DIR)
    SOURCE_DIR.mkdir()

    for path in RFC_DIR.iterdir():
        if not path.name.startswith("."):
            symlink(path, SOURCE_DIR / path.name)
    symlink(ROOT / "README.md", SOURCE_DIR / "introduction.md")
    for name in SUPPORTING_DOCUMENTS:
        symlink(ROOT / name, SOURCE_DIR / name)

    with (SOURCE_DIR / "SUMMARY.md").open("w", encoding="utf-8") as summary:
        summary.write("[Introduction](introduction.md)\n\n")
        collect(summary, RFC_DIR, 0)
        summary.write("\n- [Contributing](CONTRIBUTING.md)\n")
        summary.write("- [Code of Conduct](CODE_OF_CONDUCT.md)\n")

    subprocess.run(["mdbook", "build"], cwd=ROOT, check=True)


def collect(summary, path, depth):
    entries = [entry for entry in os.scandir(path) if entry.name.endswith(".md")]
    entries.sort(key=lambda entry: entry.name)
    for entry in entries:
        indent = "    " * depth
        entry_path = Path(entry.path)
        name = entry_path.stem
        link_path = entry_path.relative_to(RFC_DIR).as_posix()
        summary.write(f"{indent}- [{name}]({link_path})\n")
        maybe_subdir = entry_path.with_suffix("")
        if maybe_subdir.is_dir():
            collect(summary, maybe_subdir, depth + 1)


def symlink(src, dst):
    target = os.path.relpath(src, dst.parent)
    dst.symlink_to(target, target_is_directory=src.is_dir())


if __name__ == "__main__":
    main()
