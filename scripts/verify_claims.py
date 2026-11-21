#!/usr/bin/env python3
"""Verify that every audit quote in research/*.yml really appears in its source.

For each claim: re-reads the cited line range from the paperclip corpus and
asserts the stored quote is a byte-exact substring (whitespace collapsed only --
NO Unicode folding, so a typed ' where the source has U+2032 fails, as it should).
Also checks quote length, anchor/doc_id agreement, and ID uniqueness.

This is the gate that makes a claim citable. A claim that fails here is either
mis-anchored or was written from memory; both are disqualifying.

Usage:
    python3 scripts/verify_claims.py                  # all areas
    python3 scripts/verify_claims.py research/09-catalogs.yml
Exit status 1 if any claim fails.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MAX_QUOTE_WORDS = 25


def norm(s: str) -> str:
    """Collapse whitespace only. Deliberately no Unicode normalization."""
    return re.sub(r"\s+", " ", s).strip()


def fetch(doc_id: str, lines: str) -> str:
    """Return the text of the cited lines. `lines` is 'L12-L18' or 'L12,L14'."""
    nums: list[int] = []
    for part in lines.replace("L", "").split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-", 1)
            nums.extend(range(int(a), int(b) + 1))
        else:
            nums.append(int(part))
    if not nums:
        return ""
    chunks = []
    for n in sorted(set(nums)):
        # A single --lines N returns a section index on some documents, so always
        # request a range, even a degenerate one.
        res = subprocess.run(
            ["paperclip", "cat", f"/papers/{doc_id}/content.lines",
             "--lines", f"{n}-{n}"],
            capture_output=True, text=True, timeout=120,
        )
        chunks.append(res.stdout)
    return norm(" ".join(chunks))


def main() -> int:
    try:
        import yaml
    except ImportError:
        print("Needs pyyaml:  pip install --user pyyaml", file=sys.stderr)
        return 2

    targets = (
        [pathlib.Path(a) for a in sys.argv[1:]]
        if len(sys.argv) > 1
        else sorted((ROOT / "research").glob("*.yml"))
    )

    total = problems = 0
    seen_ids: dict[str, str] = {}

    for path in targets:
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        claims = doc.get("claims") or []
        print(f"\n=== {path.name}: {len(claims)} claims ===")
        for c in claims:
            total += 1
            cid = c.get("id", "<no id>")
            fails = []

            if cid in seen_ids:
                fails.append(f"duplicate id (also in {seen_ids[cid]})")
            seen_ids[cid] = path.name

            ev = c.get("evidence") or {}
            src = c.get("source") or {}
            quote = norm(str(ev.get("quote", "")))
            lines = str(ev.get("lines", ""))
            doc_id = str(src.get("doc_id", ""))

            if not quote:
                fails.append("no audit quote")
            if len(quote.split()) > MAX_QUOTE_WORDS:
                fails.append(f"quote is {len(quote.split())} words (max {MAX_QUOTE_WORDS})")
            if not src.get("doi"):
                fails.append("no DOI")
            if not src.get("bibkey"):
                fails.append("no bibkey")
            if ev.get("text_access") not in ("full_text", "abstract_only"):
                fails.append(f"bad text_access: {ev.get('text_access')!r}")
            anchor = str(ev.get("anchor", ""))
            if doc_id and anchor and doc_id not in anchor:
                fails.append("anchor does not reference doc_id")

            if quote and lines and doc_id and len(quote.split()) <= MAX_QUOTE_WORDS:
                try:
                    body = fetch(doc_id, lines)
                    if quote not in body:
                        fails.append("QUOTE NOT FOUND in cited lines")
                except Exception as exc:  # noqa: BLE001
                    fails.append(f"could not read source: {exc}")

            if fails:
                problems += 1
                print(f"  [X] {cid}")
                for f in fails:
                    print(f"        {f}")

    print(f"\n{total} claims checked, {problems} with problems.")
    if problems:
        print("Fix or drop every flagged claim. A claim that fails here is not citable.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
