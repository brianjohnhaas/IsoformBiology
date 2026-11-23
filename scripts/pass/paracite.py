#!/usr/bin/env python3
"""How many cited paragraphs cite exactly one source.

CONTRIBUTING names single-source paragraphs as the clearest sign that prose was
assembled from records rather than written by somebody who had read the field.
No gate measures it, so a deepening pass can triple a chapter's length and make
that defect worse. This counts it, before and after.

    scripts/pass/paracite.py chapters/*.qmd
"""
import re, sys, pathlib

CITE = re.compile(r"@([A-Za-z][\w:-]*)")
total_c = total_1 = 0
for arg in sys.argv[1:]:
    txt = pathlib.Path(arg).read_text(encoding="utf-8")
    txt = re.sub(r"^---\n.*?\n---\n", "", txt, flags=re.S)
    txt = re.sub(r"```.*?```", "", txt, flags=re.S)
    paras = [p for p in txt.split("\n\n") if p.strip()]
    cited = one = 0
    for p in paras:
        if p.lstrip().startswith(("#", ":::", "|", "![", ":")):
            continue
        keys = set(CITE.findall(p))
        if not keys:
            continue
        cited += 1
        if len(keys) == 1:
            one += 1
    total_c += cited
    total_1 += one
    if cited:
        print(f"{one:4d}/{cited:4d} single-source cited paragraphs  "
              f"({100*one/cited:4.0f}%)  {arg}")
if total_c:
    print(f"\n{total_1}/{total_c} book-wide ({100*total_1/total_c:.0f}%)")
