#!/usr/bin/env python3
"""Write a Markdown outline and page count for a PDF using pypdf."""

from __future__ import annotations

import sys
from pathlib import Path

from pypdf import PdfReader


def flatten_outline(reader: PdfReader, items, depth=0):
    rows = []
    for item in items:
        if isinstance(item, list):
            rows.extend(flatten_outline(reader, item, depth + 1))
            continue
        title = getattr(item, "title", str(item)).strip()
        try:
            page = reader.get_destination_page_number(item) + 1
        except Exception:
            page = None
        rows.append((depth, title, page))
    return rows


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: pdf_outline.py input.pdf output.md", file=sys.stderr)
        return 2
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    reader = PdfReader(str(src))
    rows = flatten_outline(reader, reader.outline)

    lines = [
        f"# {src.name}",
        "",
        f"- Pages: {len(reader.pages)}",
        f"- Outline entries: {len(rows)}",
        "",
        "## Outline",
        "",
    ]
    for depth, title, page in rows:
        indent = "  " * depth
        page_text = f" p. {page}" if page else ""
        lines.append(f"{indent}- {title}{page_text}")
    dst.write_text("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
