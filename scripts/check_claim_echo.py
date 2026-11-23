#!/usr/bin/env python3
"""No claim record may reuse 8 consecutive words from its own audit quote.

This is the upstream half of `check_overlap.py`, and it exists because that gate
alone is not enough.

A record's `claim:` is meant to be the researcher's own sentence. The `quote:`
beside it is a byte-exact fragment of the source, kept only so a later reader can
audit the claim, and never published. The writing pass works from a digest that
withholds the quotes, so the writer cannot copy a source sentence directly. What
the writer can do is copy a claim, and if that claim carries the source's wording
then the source's wording reaches the book through a field nobody was watching.

That is not hypothetical. When this check was first run across the whole book it
found 75 such records in nine of the twelve research files. The three files it
found nothing in are the three whose passes had already run it by hand.

A numeral and the noun it counts are exempt in practice rather than in code: a
list of probe counts cannot be said another way, and the few records that trip
the check for that reason carry a note saying so. Prefer restating the claim.

Usage:
    scripts/check_claim_echo.py                 # every research/*.yml
    scripts/check_claim_echo.py research/06-cancer.yml
"""
from __future__ import annotations

import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
N = 8
WORD = re.compile(r"[a-z0-9']+")

# Records whose shared span is a run of numerals and the nouns they count, where
# restating would mean altering a figure. Each must carry a note saying so.
EXEMPT = {
    "TECH-004",   # two mRNA sizes in kilobases
    "TECH-017",   # three probe and gene counts in one list
}


def words(text: str) -> list[str]:
    return WORD.findall(text.lower())


def main() -> int:
    paths = [pathlib.Path(a) for a in sys.argv[1:]] or sorted(
        (ROOT / "research").glob("*.yml"))
    bad = 0
    checked = 0
    for path in paths:
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for claim in doc.get("claims") or []:
            cid = str(claim.get("id", "?"))
            if cid in EXEMPT:
                continue
            checked += 1
            cw = words(claim.get("claim", "") or "")
            qw = words((claim.get("evidence") or {}).get("quote", "") or "")
            grams = {tuple(qw[i:i + N]) for i in range(len(qw) - N + 1)}
            hits = [" ".join(cw[i:i + N]) for i in range(len(cw) - N + 1)
                    if tuple(cw[i:i + N]) in grams]
            if hits:
                bad += 1
                print(f"[{path.name} {cid}] claim reuses {len(hits)} "
                      f"{N}-word span(s) from its own quote:")
                for hit in dict.fromkeys(hits):
                    print(f"    {hit}")
    print(f"\n{checked} claims checked, {bad} reusing their own quote at "
          f"{N} words ({len(EXEMPT)} exempt).")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
