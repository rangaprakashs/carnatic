#!/usr/bin/env python3
"""Search local Cubase KB PDFs and print page-level snippets."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from pypdf import PdfReader


KB_RAW = Path("/Users/rangaprakash/.gemini/antigravity/knowledge/cubase-carnatic/raw")


def compact(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: search_cubase_pdfs.py query [max_results]", file=sys.stderr)
        return 2
    query = sys.argv[1]
    max_results = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    terms = [t.lower() for t in re.findall(r"\w+", query) if len(t) > 1]
    if not terms:
        return 0

    results = []
    for pdf in sorted(KB_RAW.glob("*.pdf")):
        reader = PdfReader(str(pdf))
        for i, page in enumerate(reader.pages):
            text = compact(page.extract_text() or "")
            low = text.lower()
            score = sum(low.count(term) for term in terms)
            if score:
                pos = min([low.find(term) for term in terms if low.find(term) >= 0] or [0])
                start = max(0, pos - 160)
                end = min(len(text), pos + 520)
                results.append((score, pdf.name, i + 1, text[start:end]))

    for score, name, page, snippet in sorted(results, reverse=True)[:max_results]:
        print(f"## {name} p. {page} score={score}")
        print(snippet)
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
