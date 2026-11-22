#!/usr/bin/env python3
"""Resolve author and journal metadata for claim sources from their DOIs.

Why this exists: paperclip's abstract-only records carry title, DOI, PMID and
year, but no author list and no journal name. A researcher filling those fields
from memory produces a byline that looks authoritative and cites a real DOI
while attributing the work to possibly the wrong people. That is worse than a
blank field, because nothing downstream can detect it.

This script asks Crossref, which is the authority for DOI metadata, and writes
back what it returns. It also reports every case where the recorded value
disagreed with Crossref, so memory-sourced errors become visible rather than
silently corrected.

Usage:
    python3 scripts/resolve_metadata.py --check          # report only
    python3 scripts/resolve_metadata.py --write          # apply fixes
    python3 scripts/resolve_metadata.py --check research/04-technology-arc.yml

Network: queries api.crossref.org, one DOI at a time, with a courtesy delay.
Sends a generic User-Agent and no personal information.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
UA = "IsoformBiology-metadata-resolver/1.0 (https://github.com/brianjohnhaas/IsoformBiology)"
PLACEHOLDER = re.compile(r"resolve[ _-]?from[ _-]?doi|unknown|TBD|\?\?\?", re.I)


def crossref(doi: str) -> dict | None:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r).get("message")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise
    except Exception:
        return None


def fmt_authors(msg: dict) -> str:
    out = []
    for a in (msg.get("author") or []):
        fam = (a.get("family") or "").strip()
        given = (a.get("given") or "").strip()
        if not fam:
            # Corporate author ("The RGASP Consortium"), kept verbatim.
            if a.get("name"):
                out.append(a["name"].strip())
            continue
        initials = " ".join(f"{p[0]}." for p in re.split(r"[\s\-]+", given) if p)
        out.append(f"{fam}, {initials}".strip().rstrip(","))
    return "; ".join(out)


def personal_surnames(msg: dict) -> list[str]:
    """Surnames of personal authors only, skipping corporate entries.

    Crossref sometimes lists a consortium ahead of the people, so comparing
    raw first entries produces false mismatches.
    """
    return [a["family"].strip().lower()
            for a in (msg.get("author") or []) if a.get("family")]


def journal(msg: dict) -> str:
    for key in ("container-title", "short-container-title"):
        v = msg.get(key)
        if v:
            return v[0] if isinstance(v, list) else str(v)
    # Preprints report their server here instead.
    inst = msg.get("institution")
    if inst:
        name = inst[0].get("name") if isinstance(inst, list) else inst.get("name")
        if name:
            return name
    return ""


def year(msg: dict) -> int | None:
    for key in ("published-print", "published-online", "issued", "created"):
        parts = (msg.get(key) or {}).get("date-parts") or []
        if parts and parts[0] and parts[0][0]:
            return int(parts[0][0])
    return None


def norm_surnames(s: str) -> list[str]:
    """Surnames only, lowercased, for comparison that ignores initial style.

    SCHEMA.md's form is "Surname, A. B.", so the surname is everything before
    the comma and it may contain spaces: "Natraj Gayathri", "Zare Jousheghani",
    "van Dijk", "de Klerk". Splitting on whitespace truncated those to their
    first word and reported a mismatch against Crossref's full family name,
    which made the mismatch count untrustworthy and therefore ignorable.
    """
    out = []
    for part in str(s).split(";"):
        part = part.strip()
        if not part:
            continue
        out.append(part.split(",")[0].strip().lower())
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--write", action="store_true", help="apply fixes in place")
    ap.add_argument("--check", action="store_true", help="report only (default)")
    ap.add_argument("--delay", type=float, default=0.3)
    args = ap.parse_args()

    try:
        import yaml
    except ImportError:
        print("Needs pyyaml:  pip install --user pyyaml", file=sys.stderr)
        return 2

    targets = ([pathlib.Path(f) for f in args.files]
               or sorted((ROOT / "research").glob("*.yml")))

    # One DOI may back several claims; resolve each once.
    seen: dict[str, dict | None] = {}
    n_missing = n_placeholder = n_mismatch = n_unresolved = 0

    for path in targets:
        text = path.read_text(encoding="utf-8")
        doc = yaml.safe_load(text) or {}
        claims = doc.get("claims") or []
        print(f"\n=== {path.name} ({len(claims)} claims) ===")

        for c in claims:
            src = c.get("source") or {}
            doi = str(src.get("doi", "")).strip()
            cid = c.get("id", "?")
            rec_auth = str(src.get("authors", "") or "")
            rec_jour = str(src.get("journal", "") or "")

            blank = not rec_auth.strip()
            placeheld = bool(PLACEHOLDER.search(rec_auth) or PLACEHOLDER.search(rec_jour))
            if blank:
                n_missing += 1
            if placeheld:
                n_placeholder += 1

            if not doi:
                print(f"  [!] {cid}: no DOI, cannot resolve")
                n_unresolved += 1
                continue

            if doi not in seen:
                seen[doi] = crossref(doi)
                time.sleep(args.delay)
            msg = seen[doi]
            if msg is None:
                print(f"  [!] {cid}: Crossref has no record for {doi}")
                n_unresolved += 1
                continue

            true_auth, true_jour, true_year = fmt_authors(msg), journal(msg), year(msg)

            if blank or placeheld:
                print(f"  [fill] {cid}: {true_auth[:70]}  |  {true_jour}")
            else:
                a_rec = [s for s in norm_surnames(rec_auth) if s != "the"]
                a_true = personal_surnames(msg)
                # A recorded "et al." list is a prefix of the full one, which is
                # fine. Only a disagreement on who comes first is a real error.
                if a_rec and a_true and a_rec[0] != a_true[0]:
                    print(f"  [MISMATCH] {cid}: first author recorded "
                          f"{a_rec[0]!r}, Crossref says {a_true[0]!r}")
                    n_mismatch += 1

            if args.write:
                src["authors"] = true_auth
                if true_jour:
                    src["journal"] = true_jour
                if true_year:
                    src["year"] = true_year
                src["metadata_source"] = "crossref"

        if args.write:
            path.write_text(
                yaml.safe_dump(doc, sort_keys=False, allow_unicode=True,
                               width=100, default_flow_style=False),
                encoding="utf-8",
            )
            print(f"  -> wrote {path.name}")

    print(f"\nDOIs resolved: {sum(1 for v in seen.values() if v)}"
          f" / {len(seen)} queried")
    print(f"blank author fields: {n_missing}")
    print(f"explicit placeholders: {n_placeholder}")
    print(f"first-author MISMATCHES against Crossref: {n_mismatch}")
    print(f"unresolvable: {n_unresolved}")
    if not args.write:
        print("\nReport only. Re-run with --write to apply.")
    return 1 if (n_mismatch or n_unresolved) and not args.write else 0


if __name__ == "__main__":
    sys.exit(main())
