#!/usr/bin/env python3
"""Count prose words in a chapter, the same way every time.

The book's word targets kept drifting because each count was made by hand with a
slightly different idea of what counts. This is the definition, and it is the
only one the project uses:

prose is the running text a reader reads. It excludes YAML front matter, fenced
code, the fence lines of callout and figure divs, table rows, figure and table
captions, block attributes, HTML comments, and the citation keys themselves.
Headings count, because a heading is read.

Usage:  scripts/wordcount.py chapters/*.qmd
        scripts/wordcount.py --total chapters/*.qmd
"""
import re
import sys

FENCE = re.compile(r"^\s*(```|~~~)")
DIVFENCE = re.compile(r"^\s*:::")
TABLEROW = re.compile(r"^\s*\|")
ATTRS = re.compile(r"^\s*\{[#.]")
CAPTION = re.compile(r"^\s*!\[")
CITE = re.compile(r"\[@[^\]]*\]|@[A-Za-z][\w:-]*")
INLINE = re.compile(r"`[^`]*`")
PUNCT = re.compile(r"^[^\w]+$")


def prose_words(text: str) -> int:
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        end = next((i for i, ln in enumerate(lines[1:], 1) if ln.strip() == "---"), 0)
        lines = lines[end + 1:]
    out, in_code, in_caption = [], False, False
    for ln in lines:
        if FENCE.match(ln):
            in_code = not in_code
            continue
        if in_code:
            continue
        if in_caption:
            if ")" in ln:
                in_caption = False
            continue
        if CAPTION.match(ln):
            if ln.count("(") > ln.count(")"):
                in_caption = True
            continue
        if DIVFENCE.match(ln) or TABLEROW.match(ln) or ATTRS.match(ln):
            continue
        out.append(ln)
    body = "\n".join(out)
    body = re.sub(r"<!--.*?-->", " ", body, flags=re.S)
    body = INLINE.sub(" ", body)
    body = CITE.sub(" ", body)
    body = body.replace("#", " ")
    return sum(1 for w in body.split() if not PUNCT.match(w))


def main(argv: list[str]) -> int:
    total_only = "--total" in argv
    paths = [a for a in argv if not a.startswith("--")]
    total = 0
    for p in paths:
        with open(p, encoding="utf-8") as fh:
            n = prose_words(fh.read())
        total += n
        if not total_only:
            print(f"{n:>7}  {p}")
    print(f"{total:>7}  TOTAL ({len(paths)} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
