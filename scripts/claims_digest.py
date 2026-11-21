#!/usr/bin/env python3
"""Print a research area's claims with the source quotes removed.

This is the tool that makes the research/writing separation structural instead
of a matter of discipline. A claim record holds two statements of the same
fact: the researcher's own sentence, and a byte-exact quote kept only so
scripts/verify_claims.py can prove the sentence was read from the paper. Draft
prose must be written from the first and never from the second, because prose
written next to source wording ends up echoing it.

So this prints the claim, the topic, the bibkey and the figure idea, and
withholds the quote and the anchor. Nothing here can be copied from a paper
because none of it came from one verbatim.

Usage:
    python3 scripts/claims_digest.py 01-foundations
    python3 scripts/claims_digest.py 01 --leads
"""
from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
RESEARCH = ROOT / "research"

WITHHELD = {"quote", "anchor"}


def resolve(name: str) -> pathlib.Path:
    cands = sorted(RESEARCH.glob(f"{name}*.yml")) or sorted(
        RESEARCH.glob(f"*{name}*.yml"))
    if not cands:
        sys.exit(f"no research file matching {name!r}")
    if len(cands) > 1:
        sys.exit("ambiguous: " + ", ".join(p.stem for p in cands))
    return cands[0]


def main() -> int:
    import yaml

    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    show_leads = "--leads" in sys.argv
    if not args:
        sys.exit(__doc__)

    path = resolve(args[0])
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}

    print(f"# {doc.get('area', path.stem)}")
    print(f"# source record: {path.name}")
    print("# Quotes and line anchors are withheld by design. Write from the")
    print("# claim sentences below, which are already original prose.\n")

    by_topic: dict[str, list[dict]] = {}
    for c in doc.get("claims") or []:
        by_topic.setdefault(str(c.get("topic", "untopiced")), []).append(c)

    for topic in sorted(by_topic):
        print(f"\n## {topic}")
        for c in by_topic[topic]:
            s = c.get("source") or {}
            ev = c.get("evidence") or {}
            access = ev.get("text_access", "?")
            flag = "" if access == "full_text" else "  [ABSTRACT ONLY]"
            print(f"\n[{c.get('id')}] @{s.get('bibkey')} "
                  f"({s.get('year')}) conf={c.get('confidence')}{flag}")
            print(f"  {' '.join(str(c.get('claim', '')).split())}")
            if c.get("figure_idea"):
                print(f"  FIGURE: {' '.join(str(c['figure_idea']).split())}")

    if show_leads:
        print("\n\n## leads (scouted, not cited)")
        for l in doc.get("leads") or []:
            print(f"\n- {' '.join(str(l.get('note', '')).split())}")

    n = sum(len(v) for v in by_topic.values())
    print(f"\n# {n} claims, {len(by_topic)} topics")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        # Piping into head closes the stream early; that is not an error.
        sys.exit(0)
