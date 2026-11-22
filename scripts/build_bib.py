#!/usr/bin/env python3
"""Generate references.bib from the claim records.

The bibliography is derived, never hand-edited. Every entry traces to a source
in research/*.yml whose metadata was resolved against Crossref, so the book
cannot cite anything that no claim rests on, and an entry cannot drift from the
record it came from.

Usage:
    python3 scripts/build_bib.py            # write references.bib
    python3 scripts/build_bib.py --check    # fail if it would change (for CI)
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Minimal TeX escaping. Titles come from Crossref and can carry & % _ # $.
ESC = {"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_"}


def tex(s: str) -> str:
    s = str(s or "").strip()
    out = []
    for ch in s:
        out.append(ESC.get(ch, ch))
    s = "".join(out)
    # Protect capitalised gene/acronym runs from BibTeX lowercasing.
    return re.sub(r"\b([A-Z]{2,}[0-9]*|[A-Z][a-z]*[0-9]+)\b", r"{\1}", s)


PERSONAL_NAME = re.compile(r"^[^,]+,\s*(?:[A-Z]\.|[A-Z]$)")
# A corporate author is recognised positively, so that a personal name written
# in the wrong order is not silently braced into an institution. That happened:
# a research pass recorded "Yu Hu; Li Fang" instead of "Hu, Y.; Fang, L.", and
# an earlier version of this heuristic emitted {Yu Hu} and {Li Fang}, which
# renders every author as though it were an organisation.
CORPORATE = re.compile(
    r"Consortium|Administration|Collaborat|Initiative|Network|Project|Group\b"
    r"|Center|Centre|Institute|Program(me)?\b|Committee|Society|Working Party"
    r"|\bInc\b|\bLtd\b|\bLLC\b|on behalf of|Amgen|Genentech", re.I)


def author_format_problems(sources: dict) -> list[str]:
    """Author strings that do not follow SCHEMA.md's 'Lastname, A. B.' form.

    Checked here because the bibliography is where a wrong format becomes
    visible to a reader, and because nothing else looks at this field.
    """
    out = []
    for key in sorted(sources):
        for part in str(sources[key].get("authors", "") or "").split(";"):
            part = part.strip()
            if not part or CORPORATE.search(part) or PERSONAL_NAME.match(part):
                continue
            out.append(f"{key}: author {part!r} is neither "
                       "'Lastname, A. B.' nor a recognisable organisation")
    return out


def one_work_one_key_problems(key_dois: dict) -> list[str]:
    """Two bibkeys for one DOI, or two DOIs under one bibkey.

    Both put a second entry for the same work into the bibliography, and
    neither is visible in a single research file: the chapter 2 pass produced
    one of each, and they were found only by grouping every record in the book
    by DOI. A preprint read under the journal version's DOI is the legitimate
    case of one work with two documents, and it shares the one bibkey, so it
    does not trip this.
    """
    out = []
    by_doi: dict[str, set[str]] = {}
    for key, dois in key_dois.items():
        if len(dois) > 1:
            out.append(f"bibkey {key} carries {len(dois)} DOIs: "
                       + ", ".join(sorted(dois)))
        for doi in dois:
            by_doi.setdefault(doi, set()).add(key)
    for doi, keys in sorted(by_doi.items()):
        if len(keys) > 1:
            out.append(f"DOI {doi} is cited under {len(keys)} bibkeys: "
                       + ", ".join(sorted(keys)))
    return out


def authors_to_bibtex(s: str) -> str:
    """'Lastname, A. B.; Other, C.' -> 'Lastname, A. B. and Other, C.'

    A corporate author is wrapped in an extra pair of braces so that BibTeX
    treats it as one literal name. Without that, "US Food and Drug
    Administration, Center for Drug Evaluation and Research" is parsed as three
    people with the comma splitting surname from initials, and renders as
    "Food, U., Drug Administration, C. for D. E. & Research".
    """
    parts = [p.strip() for p in str(s or "").split(";") if p.strip()]
    out = []
    for part in parts:
        corporate = CORPORATE.search(part) or " and " in part
        out.append("{" + part + "}" if corporate else part)
    return " and ".join(out)


def entry_type(journal: str, doc_id: str = "") -> str:
    """BibTeX type for a source.

    A regulatory document or a trial registry record is a report, not a journal
    article. Typed as @article it renders in the reference list as though it had
    been peer reviewed, which an approval package has not been.
    """
    j = (journal or "").lower()
    if doc_id.startswith("fda_") or doc_id.startswith("NCT"):
        return "techreport"
    if any(k in j for k in ("biorxiv", "medrxiv", "arxiv", "research square")):
        return "misc"
    return "article"


def research_files() -> list[pathlib.Path]:
    """Research files the repository actually tracks.

    An in-progress file sitting in the working tree but ignored by git would
    otherwise put sources into references.bib that CI, which only sees
    committed files, cannot account for.
    """
    import subprocess

    found = sorted((ROOT / "research").glob("*.yml"))
    try:
        r = subprocess.run(
            ["git", "check-ignore", "--stdin"],
            input="\n".join(str(p) for p in found),
            capture_output=True, text=True, cwd=ROOT, timeout=30,
        )
        ignored = {line.strip() for line in r.stdout.splitlines() if line.strip()}
    except Exception:
        ignored = set()
    kept = [p for p in found if str(p) not in ignored]
    for p in found:
        if str(p) in ignored:
            print(f"skipping (git-ignored): {p.name}")
    return kept


def main() -> int:
    try:
        import yaml
    except ImportError:
        print("Needs pyyaml:  pip install --user pyyaml", file=sys.stderr)
        return 2

    check = "--check" in sys.argv
    sources: dict[str, dict] = {}
    used_by: dict[str, set[str]] = {}
    key_dois: dict[str, set[str]] = {}

    for path in sorted(research_files()):
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for c in doc.get("claims") or []:
            s = c.get("source") or {}
            key = str(s.get("bibkey", "")).strip()
            if not key:
                continue
            sources.setdefault(key, s)
            used_by.setdefault(key, set()).add(path.stem)
            doi = str(s.get("doi", "") or "").strip().lower()
            if doi:
                key_dois.setdefault(key, set()).add(doi)

    lines = [
        "% Generated by scripts/build_bib.py -- do not edit by hand.",
        "% Every entry backs at least one claim in research/*.yml.",
        f"% {len(sources)} sources.",
        "",
    ]
    for key in sorted(sources):
        s = sources[key]
        journal = str(s.get("journal", "") or "")
        kind = entry_type(journal, str(s.get("doc_id", "")))
        areas = ", ".join(sorted(used_by[key]))
        lines.append(f"% cited in: {areas}")
        lines.append(f"@{kind}{{{key},")
        lines.append(f"  author  = {{{authors_to_bibtex(s.get('authors'))}}},")
        lines.append(f"  title   = {{{tex(s.get('title'))}}},")
        if kind == "article":
            lines.append(f"  journal = {{{tex(journal)}}},")
        elif kind == "techreport":
            # The issuing body is the author here, so institution would repeat
            # it; the series string carries the BLA, PMA or NCT identifier that
            # a reader needs to find the document.
            lines.append(f"  type    = {{{tex(journal)}}},")
        else:
            lines.append(f"  howpublished = {{{tex(journal) or 'Preprint'}}},")
        if s.get("year"):
            lines.append(f"  year    = {{{s['year']}}},")
        if s.get("doi"):
            lines.append(f"  doi     = {{{s['doi']}}},")
        if s.get("url"):
            lines.append(f"  url     = {{{s['url']}}},")
        lines.append("}")
        lines.append("")

    text = "\n".join(lines)
    out = ROOT / "references.bib"

    problems = author_format_problems(sources)
    problems += one_work_one_key_problems(key_dois)
    if problems:
        print(f"{len(problems)} bibliography problem(s):")
        for p in problems[:20]:
            print(f"  - {p}")
        if len(problems) > 20:
            print(f"  ... and {len(problems) - 20} more")
        return 1

    if check:
        current = out.read_text(encoding="utf-8") if out.exists() else ""
        if current != text:
            print("references.bib is stale. Run: python3 scripts/build_bib.py")
            return 1
        print(f"references.bib up to date ({len(sources)} entries).")
        return 0

    out.write_text(text, encoding="utf-8")
    print(f"wrote references.bib: {len(sources)} entries from "
          f"{len(list((ROOT / 'research').glob('*.yml')))} research files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
