#!/usr/bin/env python3
"""Verify every row of the accounting tables against its OWN claim record.

check_citations.py accepts a number if it appears in a claim for *any* source
the section cites. The accounting chapter cites nine sources in one section, so
that gate would pass a row whose figure came from a different paper than the one
the row names. This check closes that hole: for each table row it takes the
bibkey in the row and requires the row's figures to appear in a claim recorded
against that bibkey.

Usage: python3 scripts/check_accounting.py
Exit 1 on any mismatch.
"""
from __future__ import annotations

import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
TARGET = ROOT / "chapters" / "13-accounting.qmd"
NUM = re.compile(r"\d+(?:[.,]\d+)*")


def claims_by_bibkey() -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for p in sorted((ROOT / "research").glob("*.yml")):
        doc = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        for c in doc.get("claims") or []:
            key = (c.get("source") or {}).get("bibkey")
            if not key:
                continue
            text = " ".join(
                str(c.get(f, "")) for f in ("claim", "topic")
            ) + " " + str((c.get("source") or {}).get("title", ""))
            out.setdefault(key, set()).update(
                n.replace(",", "") for n in NUM.findall(text))
    return out


def main() -> int:
    if not TARGET.exists():
        print(f"{TARGET.name} not present; nothing to check")
        return 0
    index = claims_by_bibkey()
    fails = []
    rows = 0
    for lineno, line in enumerate(TARGET.read_text(encoding="utf-8").splitlines(), 1):
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        keys = re.findall(r"@([A-Za-z][A-Za-z0-9]+)", cells[-1] if cells else "")
        if not keys:
            continue            # header or separator row
        rows += 1
        figures = {n.replace(",", "") for n in NUM.findall(cells[0])}
        for key in keys:
            if key not in index:
                fails.append(f"{TARGET.name}:{lineno}: no claim records for "
                             f"{key!r}")
                continue
            missing = sorted(figures - index[key])
            if missing:
                fails.append(
                    f"{TARGET.name}:{lineno}: {missing} not in any claim for "
                    f"{key!r} - row figure and row source disagree")
    for f in fails:
        print(f"  - {f}")
    print(f"\n{rows} table row(s) checked, {len(fails)} mismatch(es).")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
