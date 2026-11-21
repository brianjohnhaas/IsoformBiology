#!/usr/bin/env python3
"""Flag chapter prose that overlaps verbatim with recorded source quotes.

The audit quotes in research/*.yml are the only source text we ever store, so
this is the one place a close paraphrase can be caught mechanically. Any shared
span of N+ consecutive words between a chapter and a quote gets flagged.

This is a smoke alarm, not a plagiarism detector. It cannot see text we never
recorded. A clean run means "no overlap with what we stored", nothing stronger.

Usage:
    python3 scripts/check_overlap.py [--n 8] [--quiet]
Exit status 1 if anything is flagged, so CI can gate on it.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Shared technical phrasing that is not plagiarism -- names of things, standard
# terms of art. Overlap consisting only of these is noise.
STOPSPANS = re.compile(
    r"^(?:(?:the|of|and|in|a|an|to|for|with|by|from|that|is|are|was|were|"
    r"alternative|splicing|isoform|isoforms|transcript|transcripts|rna|mrna|"
    r"pre-mrna|gene|genes|exon|exons|intron|introns|sequencing|long-read|"
    r"single-cell|expression|human|mouse)\s*)+$",
    re.I,
)


# A number is one word. Splitting 203,672 into "203" and "672", or 2.7 into
# "2" and "7", let a short shared phrase reach the 8-word threshold on digits
# alone and reported overlap where there was none.
TOKEN = re.compile(r"\d+\.\d+|[A-Za-z0-9'\-]+")


def words(text: str) -> list[str]:
    text = re.sub(r"(?<=\d),(?=\d\d\d)", "", text.lower())
    return TOKEN.findall(text)


def shingles(ws: list[str], n: int) -> set[tuple[str, ...]]:
    return {tuple(ws[i : i + n]) for i in range(len(ws) - n + 1)}


def load_quotes() -> list[tuple[str, str, str]]:
    """Return (area_file, claim_id, quote). Hand-rolled so pyyaml isn't required."""
    out = []
    for path in sorted((ROOT / "research").glob("*.yml")):
        claim_id = "?"
        for raw in path.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\s*-?\s*id:\s*(\S+)", raw)
            if m:
                claim_id = m.group(1).strip("\"'")
            m = re.match(r"\s*quote:\s*(?:[>|][-+]?\s*)?(.*)", raw)
            if m:
                q = m.group(1).strip().strip("\"'")
                if q:
                    out.append((path.name, claim_id, q))
                else:
                    out.append((path.name, claim_id, "__BLOCK__"))
                continue
            # continuation lines of a block scalar
            if out and out[-1][2] == "__BLOCK__" and raw.startswith(" " * 8):
                out[-1] = (out[-1][0], out[-1][1], raw.strip())
    return [(a, c, q) for a, c, q in out if q != "__BLOCK__"]


def strip_markup(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)          # code blocks
    text = re.sub(r"^\s*(?:#|:::).*$", " ", text, flags=re.M)   # headings, callouts
    text = re.sub(r"\[[^\]]*\]\([^)]*\)", " ", text)            # links
    text = re.sub(r"\[@[^\]]*\]|@[a-z]+-[\w-]+", " ", text)     # citations, xrefs
    text = re.sub(r"\"[^\"]{0,400}\"", " ", text)               # explicit quotations
    return text


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=8, help="shared-word span to flag")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    quotes = load_quotes()
    if not quotes:
        print("No audit quotes found in research/*.yml -- nothing to check against.")
        return 0

    qshingles: dict[tuple[str, ...], tuple[str, str]] = {}
    for area, cid, q in quotes:
        for sh in shingles(words(q), args.n):
            qshingles.setdefault(sh, (area, cid))

    flagged = 0
    chapters = sorted((ROOT / "chapters").glob("*.qmd")) + [ROOT / "index.qmd"]
    for ch in chapters:
        if not ch.exists():
            continue
        ws = words(strip_markup(ch.read_text(encoding="utf-8")))
        hits = []
        for sh in shingles(ws, args.n):
            if sh in qshingles and not STOPSPANS.match(" ".join(sh)):
                hits.append((" ".join(sh), qshingles[sh]))
        if hits:
            flagged += len(hits)
            print(f"\n{ch.relative_to(ROOT)}: {len(hits)} overlapping span(s)")
            for span, (area, cid) in sorted(hits)[:10]:
                print(f'  "{span}"\n    <- {area} {cid}')

    if flagged:
        print(
            f"\n{flagged} span(s) of {args.n}+ words match recorded source text.\n"
            "Restate in your own words, or make it an explicit attributed quotation."
        )
        return 1
    if not args.quiet:
        print(
            f"OK: no {args.n}+ word overlap between "
            f"{len(chapters)} chapter(s) and {len(quotes)} recorded quote(s)."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
