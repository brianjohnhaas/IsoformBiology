#!/usr/bin/env python3
"""Mechanical checks on chapter prose.

The book is written impersonally, and impersonal prose drifts toward dry by
default. These checks exist because that drift is gradual and invisible from
inside a single chapter: nobody notices the mean sentence creeping from 18 to 26
words, and by then the book reads like a review article.

What is checked:
  - mean sentence length (target < 19 words)
  - no sentence over 45 words
  - no first person (the book has no narrator)
  - banned AI-tell vocabulary and constructions
  - no em dashes
  - no run of 4+ sentences within 2 words of each other in length

What is NOT checked: whether a section ends on a claim rather than a summary.
That one is in STYLE.md and needs a human.

Usage:
    python3 scripts/check_style.py                      # all chapters
    python3 scripts/check_style.py chapters/02-animals.qmd
Exit 1 on any failure.
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

MEAN_MAX = 19.0
MIN_SENTENCES = 20   # below this a chapter is still a stub
SENTENCE_MAX = 45
RUN_LEN = 4

FIRST_PERSON = re.compile(
    r"(?<![\w-])(?:[Ww]e|[Oo]ur|[Oo]urs|us|I|my|mine)(?![\w-])")
BANNED_WORDS = re.compile(
    r"\b(delve|delving|leverage[ds]?|landscape|ecosystem|tapestry|nuanced|"
    r"crucially|importantly|notably|quietly|seamless(ly)?|paradigm|"
    r"revolutioni[sz]\w*|game.chang\w+|unlock\w*|harness\w*|myriad|plethora|"
    r"testament to|underscore[sd]?|showcase[sd]?)\b", re.I)
BANNED_PHRASES = re.compile(
    r"(it is worth noting|here's the thing|in this section|let's |"
    r"in conclusion|despite these challenges|that said,|needless to say|"
    r"at the end of the day|when it comes to)", re.I)
EDITORIALISING = re.compile(
    r",\s+(highlighting|underscoring|emphasi[sz]ing|showcasing|"
    r"demonstrating the (importance|need))\b", re.I)


def prose_only(text: str) -> str:
    """Strip everything that is not the chapter's own running prose."""
    text = re.sub(r"(?s)^---.*?---", " ", text)          # yaml front matter
    text = re.sub(r"(?s):::.*?:::", " ", text)           # callouts and asides
    text = re.sub(r"(?s)```.*?```", " ", text)           # code
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)[^\n]*", " ", text)  # figures+captions
    text = re.sub(r"^#.*$", " ", text, flags=re.M)       # headings
    text = re.sub(r"\[@[^\]]*\]", "", text)              # citations
    text = re.sub(r"\*+", "", text)                      # emphasis markers
    # A list item is its own unit, so terminate it before unwrapping.
    text = re.sub(r"^\s*[-*+]\s+(.*?)\s*$", r"\1. ", text, flags=re.M)
    # Source is hard-wrapped. Join lines inside a paragraph, keep blank lines,
    # or every wrapped line would count as a sentence.
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
    return text


# Periods that do not end a sentence. Without these, "C. elegans" and "et al."
# split a sentence in two, which deflates the mean and can hide an overlong
# sentence by cutting it into legal-looking halves.
ABBREV = re.compile(
    r"(?:\b(?:et al|e\.g|i\.e|cf|vs|ca|approx|no|Dr|Prof|St|Fig|Figs|Suppl"
    r"|Mr|Ms|Mrs|Jr|Sr|Inc|Ltd|ibid|viz|al)\.)"
    r"|(?:\b[A-Z]\.(?=\s*[a-z]))",          # C. elegans, A. thaliana
    re.X)
SENTINEL = "\u0001"


def sentences(text: str) -> list[str]:
    masked = ABBREV.sub(lambda m: m.group(0).replace(".", SENTINEL), text)
    parts = re.split(r"(?<=[.!?])\s+", masked)
    out = []
    for p in parts:
        p = p.replace(SENTINEL, ".").strip()
        if len(p.split()) >= 3:
            out.append(p)
    return out


def check(path: pathlib.Path) -> list[str]:
    raw = path.read_text(encoding="utf-8")
    text = prose_only(raw)
    sents = sentences(text)
    fails = []

    if not sents:
        return []  # stub chapter, nothing to check yet

    lens = [len(s.split()) for s in sents]
    mean = sum(lens) / len(lens)
    if len(sents) < MIN_SENTENCES:
        return []   # stub; nothing to judge yet
    if mean >= MEAN_MAX:
        fails.append(f"mean sentence {mean:.1f} words (target < {MEAN_MAX}) "
                     f"- the prose has gone stately; break sentences up")

    for s, n in zip(sents, lens):
        if n > SENTENCE_MAX:
            fails.append(f"{n}-word sentence: {s[:90]}...")

    if "—" in raw:
        fails.append(f"em dash present ({raw.count('—')}x); use a comma, "
                     "period or parentheses")

    for m in FIRST_PERSON.finditer(text):
        fails.append(f"first person {m.group(0)!r} - the book has no narrator")
        break
    for m in BANNED_WORDS.finditer(text):
        fails.append(f"banned vocabulary: {m.group(0)!r}")
    for m in BANNED_PHRASES.finditer(text):
        fails.append(f"filler phrase: {m.group(0)!r}")
    for m in EDITORIALISING.finditer(text):
        fails.append(f"participle editorialising: {m.group(0).strip()!r} "
                     "- state the specific implication or cut it")

    for i in range(len(lens) - RUN_LEN + 1):
        window = lens[i:i + RUN_LEN]
        if max(window) - min(window) <= 2:
            fails.append(f"{RUN_LEN} consecutive sentences of length "
                         f"{window} - metronomic; vary one")
            break

    return fails


def main() -> int:
    targets = ([pathlib.Path(a).resolve() for a in sys.argv[1:]]
               or [ROOT / "index.qmd"]
               + sorted((ROOT / "chapters").glob("*.qmd"))
               + sorted((ROOT / "walkthroughs").glob("*.qmd")))

    total = 0
    for path in targets:
        if not path.exists():
            continue
        fails = check(path)
        text = prose_only(path.read_text(encoding="utf-8"))
        sents = sentences(text)
        if not sents:
            continue
        lens = [len(s.split()) for s in sents]
        status = "FAIL" if fails else "ok"
        rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        print(f"{status:4s} {rel}  "
              f"({len(sents)} sentences, mean {sum(lens)/len(lens):.1f})")
        for f in fails:
            print(f"       - {f}")
        total += len(fails)

    print(f"\n{total} style issue(s).")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
