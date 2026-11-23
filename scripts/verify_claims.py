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


def corpus_root(doc_id: str) -> str:
    """Which paperclip directory holds this document.

    The corpus is not only papers. It holds FDA regulatory documents under
    /fda, clinical trial records under /trials, and protein entries under
    /proteins, and a claim may legitimately cite any of them. This function
    existed implicitly as the hardcoded string "/papers", which meant every
    quote taken from an approval letter, a review memo or a trial record was
    reported as QUOTE NOT FOUND. Eight such claims were flagged on one chapter,
    all eight byte-exact, and the risk was that someone would resolve the
    failure by deleting the best primary sources in the chapter.

    The `tri_` prefix was missing for the same reason, and it cost more than a
    false alarm. Trial records from the registries other than ClinicalTrials.gov
    carry that prefix: the European CTIS, ISRCTN, jRCT and the WHO platform. A
    research agent found that the only quantified endpoint wording for one trial
    sat in its CTIS record, read it, confirmed it byte-exact, and then could not
    record the claim because this function sent the verifier to /papers. The
    record went into a leads block instead, with the diagnosis attached.
    """
    if doc_id.startswith("fda_"):
        return "/fda"
    if doc_id.startswith("NCT") or doc_id.startswith("tri_"):
        return "/trials"
    if re.fullmatch(r"[OPQ][0-9][A-Z0-9]{3}[0-9](-\d+)?", doc_id):
        return "/proteins"
    return "/papers"


_FIRST_LABEL: dict[str, int] = {}


def first_label(doc_id: str) -> int:
    """The line label the document starts at, which is not always 1.

    `cat --lines N-N` addresses lines by POSITION while `lines:` in a claim
    record, the anchor URL and `grep -n` all use the document's own LABEL.
    Most documents label the first line L1 and the two agree. Some FDA
    documents start at L0, so every label is one ahead of its position and a
    position-based read silently returns the wrong line. That reported five
    byte-exact quotes as QUOTE NOT FOUND.
    """
    if doc_id not in _FIRST_LABEL:
        res = subprocess.run(
            ["paperclip", "cat",
             f"{corpus_root(doc_id)}/{doc_id}/content.lines", "--lines", "1-1"],
            capture_output=True, text=True, timeout=120,
        )
        m = re.match(r"\s*L(\d+):", res.stdout or "")
        _FIRST_LABEL[doc_id] = int(m.group(1)) if m else 1
    return _FIRST_LABEL[doc_id]


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
    # Labels to positions. Read one line either side too, because a quote can
    # be split across a line boundary by the extractor.
    off = first_label(doc_id) - 1
    nums = sorted({n for x in nums for n in (x - 1, x, x + 1)})
    chunks = []
    for n in [x - off for x in nums if x - off >= 1]:
        # A single --lines N returns a section index on some documents, so always
        # request a range, even a degenerate one.
        res = subprocess.run(
            ["paperclip", "cat",
             f"{corpus_root(doc_id)}/{doc_id}/content.lines",
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
            # Every source needs an identifier a reader can follow, but what
            # counts as one depends on the kind of document. A paper has a DOI.
            # A regulatory document has none and never will: it is cited by its
            # issuing body and its application number, which is what a reader
            # actually searches for. Demanding a DOI of an FDA review is how
            # four invented accessdata.fda.gov links got into this file, all
            # four of which returned 404.
            stype = str(src.get("source_type", "")).lower()
            doc = str(src.get("doc_id", ""))
            regulatory = (stype in {"fda", "trials", "registry"}
                          or doc.startswith(("fda_", "NCT")))
            if regulatory:
                if not src.get("url") and not (
                        src.get("journal") and src.get("authors")):
                    fails.append("regulatory source needs a url, or an issuing "
                                 "body and an application identifier")
            elif not src.get("doi") and not src.get("url"):
                fails.append("no DOI and no url")
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

    # Cross-file bibliography consistency. A paper cited from two chapters under
    # two bibkeys becomes two entries in references.bib and two numbers in the
    # rendered book, which reads as two different sources.
    if len(targets) > 1:
        problems += check_bibkeys(targets)

    return 1 if problems else 0


def check_bibkeys(targets: list[pathlib.Path]) -> int:
    import yaml

    by_doi: dict[str, set[str]] = {}
    by_key: dict[str, set[str]] = {}
    where: dict[tuple[str, str], set[str]] = {}

    for path in targets:
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for c in doc.get("claims") or []:
            src = c.get("source") or {}
            doi = str(src.get("doi", "")).strip().lower()
            key = str(src.get("bibkey", "")).strip()
            if not doi or not key:
                continue
            by_doi.setdefault(doi, set()).add(key)
            by_key.setdefault(key, set()).add(doi)
            where.setdefault((doi, key), set()).add(path.name)

    bad = 0
    for doi, keys in sorted(by_doi.items()):
        if len(keys) > 1:
            bad += 1
            files = sorted({f for k in keys for f in where[(doi, k)]})
            print(f"\n  [bibkey] one DOI, {len(keys)} keys: {doi}")
            print(f"           keys: {', '.join(sorted(keys))}")
            print(f"           in:   {', '.join(files)}")
    for key, dois in sorted(by_key.items()):
        if len(dois) > 1:
            bad += 1
            print(f"\n  [bibkey] one key, {len(dois)} DOIs: {key}")
            print(f"           dois: {', '.join(sorted(dois))}")

    shared = sum(1 for d, k in by_doi.items() if len(where[(d, next(iter(k)))]) > 1)
    print(f"\n{len(by_doi)} distinct sources, {shared} cited from more than one area.")
    if bad:
        print(f"{bad} bibkey conflict(s). Resolve before building references.bib.")
    else:
        print("Bibkeys are consistent: every DOI has one key and every key one DOI.")
    return bad


if __name__ == "__main__":
    sys.exit(main())
