#!/usr/bin/env python3
"""Find source wording that a corrections pass copied out of a reviewer's report.

The gap this closes. A records reviewer reads the paper and reports each defect
as a pair: "claim says: <the record's words>" and "source says: <what the lines
actually support>", the second often quoting the paper verbatim. Whoever then
writes the corrected claim is reading that report, not the paper, so the
research/writing separation holds in form. It does not hold in substance: a
corrected claim drafted close to the reviewer's quotation carries the paper's
own wording into the record, and from the record into the book.

No other check in this project can see it:

  check_claim_echo.py compares a claim against the quotes stored in its own file.
  check_overlap.py   compares the chapters against those same stored quotes.

Neither knows the reviewer reports exist, and the reviewer's quotation is not a
stored quote. Four passages in the chapter 7 corrections shared eight or more
words with text a reviewer had marked as the source's, and all four were found
by this check and restated.

    python3 scripts/check_review_leak.py REVIEWDIR research/07-neuro-mendelian.yml

Only text the reviewer introduced with "source says:" and wrapped in quotation
marks is treated as the source's. A blunter version compared whole reports and
was useless, because a report quotes the record under review verbatim and so
almost every record matched itself.

Expect false positives of two kinds, and read every hit rather than trusting the
count: this project's own tier strings, which reviewers quote back, and spans
that were already in the record before the review. Both are fine. What is not
fine is a span that entered the record in the corrections pass.
"""
from __future__ import annotations

import pathlib
import re
import sys

import yaml

N = 8
# Strings that are the project's own vocabulary, not any source's.
HOUSE = ("isoform specific biochemical", "correlation of isoform ratio",
         "isoform specific perturbation with phenotype",
         "none of the three tiers applies", "cohort measurement of assay performance")


def words(text: str | None) -> list[str]:
    return re.findall(r"[a-z0-9]+", (text or "").lower())


def main() -> int:
    revdir, target = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    blob = " ".join(p.read_text(encoding="utf-8", errors="replace")
                    for p in sorted(revdir.rglob("*.md")))

    quoted: list[str] = []
    for m in re.finditer(r"source says:(.{0,900}?)"
                         r"(?=\n\s*(?:lines read|also|Also|claim says|note says|\Z))",
                         blob, re.S):
        quoted += re.findall(r'"([^"]{15,700})"', m.group(1))
        quoted += re.findall(r"“([^”]{15,700})”", m.group(1))

    spans: dict[str, str] = {}
    for q in quoted:
        w = words(q)
        for i in range(len(w) - N + 1):
            spans.setdefault(" ".join(w[i:i + N]), q[:110])

    doc = yaml.safe_load(target.read_text(encoding="utf-8"))
    hits = 0
    for c in doc["claims"]:
        for field in ("claim", "note"):
            w = words(c.get(field))
            found = [(" ".join(w[i:i + N]), spans[" ".join(w[i:i + N])])
                     for i in range(len(w) - N + 1)
                     if " ".join(w[i:i + N]) in spans]
            found = [(s, q) for s, q in found if not any(h in s for h in HOUSE)]
            if found:
                hits += 1
                print(f"[{c['id']}.{field}] {len(found)} span(s)")
                print(f"    RECORD: {found[0][0]}")
                print(f"    SOURCE: {found[0][1]}")
    print(f"\n{len(spans)} source span(s) from {len(quoted)} quotation(s) in "
          f"{revdir}; {hits} field(s) in {target.name} share one.")
    print("Read each. A span already in the record before the review is fine; "
          "one the corrections pass introduced is not.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
