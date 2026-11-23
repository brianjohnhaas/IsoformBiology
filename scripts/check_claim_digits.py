#!/usr/bin/env python3
"""Report every number in a claim that is not on the lines the record cites.

Why this exists. `verify_claims.py` proves the stored audit quote is byte-exact
inside the cited lines. That says nothing about the rest of the claim. A claim
can carry a figure that is perfectly correct in the paper, and correct in the
record, and still sit on a line the record does not cite -- which means nobody
following the anchor can check it, and the number's denominator, cohort or arm
may belong to a different sentence entirely.

Reviewers on three chapters each found this independently: 28 claims in one
chapter 9 block, 7 in chapter 4's corrections, and clusters of the same in every
chapter 7 block. It is the commonest reachable defect in this project that no
other check looks for.

This is a LOCAL check, not a CI gate, for the same reason `verify_claims.py` is:
it reads the paperclip corpus, which CI does not have.

    python3 scripts/check_claim_digits.py                       # all areas
    python3 scripts/check_claim_digits.py research/09-catalogs.yml
    python3 scripts/check_claim_digits.py --ids CAT-279,CAT-280

What it does NOT do. It does not decide whether a number is right. A number the
claim derives (a percentage the book computes, a sum, a ratio) is expected to be
absent from the source, and so is a number written in words where the source
writes digits, or the other way round. Every hit is a question for a human:
either widen `lines:` to the line that carries the figure, or say in the claim
that the arithmetic is the book's own. Exit status is 0 on findings for that
reason; a non-zero status means the run itself failed.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from verify_claims import fetch, norm  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent

# A number worth checking. Bare 0 and 1 are skipped: they appear in almost any
# line and in prose words ("one of the two"), so they generate noise rather than
# findings. Years are kept, because a wrong year is a real defect.
TOKEN = re.compile(r"\d[\d,]*(?:\.\d+)?")
SKIP = {"0", "1", "2", "3", "4", "5"}


def variants(tok: str) -> set[str]:
    """The spellings of one number a source might use.

    A source writing 1,683,827 and a claim writing 1683827 are the same figure,
    as are 50 and 50.0, and 0.59 and .59. Matching only the claim's exact
    spelling reported all three as missing on the first draft of this check.
    """
    out = {tok, tok.replace(",", "")}
    bare = tok.replace(",", "")
    if "." in bare:
        out.add(bare.rstrip("0").rstrip("."))
        if bare.startswith("0."):
            out.add(bare[1:])
    else:
        out.add(bare + ".0")
        # 1683827 -> 1,683,827, for the claim-has-bare, source-has-commas case.
        if len(bare) > 3:
            grouped, rest = [], bare
            while len(rest) > 3:
                grouped.insert(0, rest[-3:])
                rest = rest[:-3]
            out.add(",".join([rest] + grouped))
    return {v for v in out if v}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--ids", help="comma-separated record ids to check")
    args = ap.parse_args()

    paths = [pathlib.Path(f) for f in args.files] or sorted(
        (ROOT / "research").glob("[0-9][0-9]-*.yml"))
    only = set((args.ids or "").split(",")) - {""}

    total = flagged = 0
    for path in paths:
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        findings = []
        for c in doc.get("claims") or []:
            if only and c["id"] not in only:
                continue
            src, ev = c.get("source") or {}, c.get("evidence") or {}
            doc_id, lines = src.get("doc_id"), ev.get("lines")
            if not doc_id or not lines:
                continue
            toks = {t for t in TOKEN.findall(c.get("claim") or "")
                    if t not in SKIP}
            if not toks:
                continue
            total += 1
            try:
                text = fetch(str(doc_id), str(lines))
            except Exception as exc:  # a corpus read failure is not a finding
                findings.append((c["id"], f"CANNOT READ {doc_id} {lines}: {exc}", []))
                continue
            hay = norm(text)
            missing = sorted(t for t in toks
                             if not any(v in hay for v in variants(t)))
            if missing:
                flagged += 1
                findings.append((c["id"], f"{doc_id} {lines}", missing))
        if findings:
            print(f"\n## {path.name}")
            for cid, where, missing in findings:
                if missing:
                    print(f"  [{cid}] {where}")
                    print(f"      not on the cited lines: {', '.join(missing)}")
                else:
                    print(f"  [{cid}] {where}")
    print(f"\n{total} claim(s) with a number checked; "
          f"{flagged} carrying a figure that is not on its cited lines.")
    print("Each is a question, not a verdict: widen `lines:` to the line that "
          "carries the figure, or say in the claim that the arithmetic is the "
          "book's own.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
