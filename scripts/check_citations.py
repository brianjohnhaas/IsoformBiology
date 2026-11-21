#!/usr/bin/env python3
"""Check that every cited number in the prose is in the claim it cites.

The other gates each guard a different seam. verify_claims.py proves a claim
record was read from the paper it names. check_overlap.py proves the prose does
not reuse source wording. Neither proves the thing that actually goes wrong when
a chapter is written quickly: a number recalled from memory, or carried over from
a neighbouring claim, sitting in a sentence that cites a real paper. The
citation is valid, the paper is real, and the figure attached to it is not in it.

So this checks the prose against the claim records directly:

  - every [@bibkey] in a chapter resolves to a key in references.bib
  - every bare number in a section appears either in a claim sentence for a
    bibkey cited in that same section, or as the publication year of one
  - a section carrying numbers and no citation at all is reported

Scope is the section, not the paragraph. A paragraph often introduces a figure
that the next paragraph cites, and paragraph scope reported every one of those.
Section scope still catches the failure that matters, which is a number that
appears in no claim belonging to any source the section rests on.

A number that is deliberately not from a paper, such as the year a website was
last updated, is exempted by putting a comment in the section:

    <!-- numbers-ok: dates refer to the resources themselves, not to claims -->

Numbers embedded in names are not counted. FGFR1, CD45 and N2BA contribute no
number; "exon 9" and "3,200 kDa" do.

Usage:
    python3 scripts/check_citations.py
    python3 scripts/check_citations.py chapters/02-animals.qmd
    python3 scripts/check_citations.py --verbose
Exit 1 on any failure.
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# A number is a digit run, optionally with thousands commas or a decimal tail,
# flanked by non-letters. The flanks are what keep FGFR1 and CD45 out.
NUMBER = re.compile(
    r"(?<![A-Za-z0-9.,])(?<![A-Za-z]-)"   # not CD45, not TDP-43, not 3.14
    r"(\d+(?:,\d{3})*(?:\.\d+)?)(?![A-Za-z0-9])")
# Quarto cross-references share the @ sigil with citations and are not keys.
XREF = "sec|fig|tbl|eq|lst|thm|lem|cor|prp|def|exm|exr"
CITE = re.compile(rf"@(?!(?:{XREF})-)([A-Za-z][A-Za-z0-9_:-]*)")

# Numbers that are structure, not fact: list ordinals and the like.
IGNORE_NUMBERS = {"1", "2", "3", "4"}


def norm(n: str) -> str:
    n = n.replace(",", "")
    if "." in n:
        n = n.rstrip("0").rstrip(".")
    return n


def claim_index() -> tuple[dict[str, set[str]], dict[str, str]]:
    """bibkey -> every number appearing in its claims; bibkey -> year."""
    import yaml

    numbers: dict[str, set[str]] = {}
    years: dict[str, str] = {}
    for path in sorted((ROOT / "research").glob("*.yml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for c in doc.get("claims") or []:
            s = c.get("source") or {}
            key = str(s.get("bibkey", "")).strip()
            if not key:
                continue
            if s.get("year"):
                years[key] = str(s["year"])
            text = " ".join([
                str(c.get("claim", "")),
                str(c.get("topic", "")),
                str(s.get("title", "")),
            ])
            bucket = numbers.setdefault(key, set())
            for m in NUMBER.finditer(text):
                bucket.add(norm(m.group(1)))
            # Spelled-out numbers in a claim still license the digit form.
            for word, digit in WORDS.items():
                if re.search(rf"\b{word}\b", text, re.I):
                    bucket.add(digit)
    return numbers, years


WORDS = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10",
    "eleven": "11", "twelve": "12", "twenty": "20", "thirty": "30",
    "forty": "40", "fifty": "50", "hundred": "100", "thousand": "1000",
}


def bib_keys() -> set[str]:
    bib = ROOT / "references.bib"
    if not bib.exists():
        return set()
    return set(re.findall(r"@\w+\{([^,]+),", bib.read_text(encoding="utf-8")))


def blank_out(text: str) -> str:
    """Remove a span's content but keep its newlines, so lines still count."""
    def sub(m):
        return "\n" * m.group(0).count("\n")
    text = re.sub(r"(?s)^---.*?---", sub, text)
    text = re.sub(r"(?s)^```.*?^```", sub, text, flags=re.M)
    return text


EXEMPT = re.compile(r"<!--\s*numbers-ok\b")


def sections(text: str) -> list[tuple[int, str]]:
    """(starting line, text) per heading-delimited section. Citations kept."""
    text = blank_out(text)
    out: list[tuple[int, str]] = []
    buf: list[str] = []
    start = 1
    for i, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if line.startswith("#") and not line.startswith("#|"):
            if buf:
                out.append((start, " ".join(buf)))
            buf, start = [], i
            continue
        if line.startswith(":::") or line.startswith("!["):
            continue
        if not buf:
            start = i
        buf.append(line)
    if buf:
        out.append((start, " ".join(buf)))
    return [(n, s) for n, s in out if s.strip()]


def strip_markup(p: str) -> str:
    # Inline code is a path, a key or an identifier, never a quantity, and
    # research/01-foundations.yml would otherwise contribute the number 1.
    p = re.sub(r"`[^`]*`", " ", p)
    p = re.sub(r"<!--.*?-->", " ", p)
    p = re.sub(r"\{[^}]*\}", " ", p)        # attrs: {#sec-x}, {width=100%}
    p = re.sub(r"\]\([^)]*\)", "] ", p)     # link targets
    p = re.sub(r"\*+", "", p)
    return p


def check(path: pathlib.Path, numbers, years, keys, verbose=False) -> list[str]:
    fails = []
    raw = path.read_text(encoding="utf-8")
    for line_no, sec in sections(raw):
        cited = set(CITE.findall(sec))
        for k in sorted(cited):
            if keys and k not in keys:
                fails.append(f"{path.name}:{line_no}: citation @{k} is not in "
                             "references.bib")
        if EXEMPT.search(sec):
            continue
        body = strip_markup(re.sub(r"\[@[^\]]*\]", " ", sec))
        found = {norm(m.group(1)) for m in NUMBER.finditer(body)}
        found -= IGNORE_NUMBERS
        if not found:
            continue
        if not cited:
            fails.append(f"{path.name}:{line_no}: section has numbers "
                         f"{sorted(found)} and no citation")
            continue
        allowed: set[str] = set()
        for k in cited:
            allowed |= numbers.get(k, set())
            if k in years:
                allowed.add(years[k])
        missing = sorted(found - allowed)
        if missing:
            fails.append(
                f"{path.name}:{line_no}: {missing} not in any claim for "
                f"{sorted(cited)}")
        elif verbose:
            print(f"     ok {path.name}:{line_no} {sorted(found)}")
    return fails


def main() -> int:
    verbose = "--verbose" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    targets = ([pathlib.Path(a).resolve() for a in args]
               or [ROOT / "index.qmd"]
               + sorted((ROOT / "chapters").glob("*.qmd"))
               + sorted((ROOT / "walkthroughs").glob("*.qmd")))

    numbers, years = claim_index()
    keys = bib_keys()

    total = 0
    for path in targets:
        if not path.exists():
            continue
        fails = check(path, numbers, years, keys, verbose)
        rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        print(f"{'FAIL' if fails else 'ok':4s} {rel}")
        for f in fails:
            print(f"       - {f}")
        total += len(fails)

    print(f"\n{total} citation issue(s).")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
