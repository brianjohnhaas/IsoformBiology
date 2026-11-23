#!/usr/bin/env python3
"""Patch only the `claim` and `note` fields of existing records, by id.

    scripts/pass/patch_claims.py research/04-technology-arc.yml PATCH.yml [...]

`merge.py` replaces whole records, which is right when an agent hands back a
corrected record it has just read from the source. It is wrong for a restatement
pass: the patch file carries each `source` block as it stood when the editor read
it, so a whole-record merge silently reverts anything changed in between, such as
a resolved author list, a renamed bibkey or a corrected DOI. This touches two
fields and leaves the rest of the record alone.

It then prints the check that matters for a restatement: every digit string and
every hedge word in the old claim, against the new one. A restatement is supposed
to change wording and nothing else, so a dropped number or a lost "proposed" is
the failure mode, and it is invisible to every other gate in this project.
"""
from __future__ import annotations

import pathlib
import re
import sys

import yaml

DIGITS = re.compile(r"\d[\d,.]*")
HEDGES = ("propose", "proposed", "suggest", "suggests", "suggesting", "may",
          "might", "likely", "appears", "argue", "argues", "argued", "reported",
          "estimate", "estimated", "potentially", "could", "approximately",
          "about", "roughly", "at least", "at most", "up to")


def hedges(text: str) -> set[str]:
    low = text.lower()
    return {h for h in HEDGES if re.search(rf"(?<![\w-]){re.escape(h)}(?![\w-])", low)}


def main() -> int:
    target = pathlib.Path(sys.argv[1])
    doc = yaml.safe_load(target.read_text(encoding="utf-8"))
    by_id = {c["id"]: c for c in doc["claims"]}

    patched = missing = 0
    problems: list[str] = []
    for path in sys.argv[2:]:
        patch = yaml.safe_load(pathlib.Path(path).read_text(encoding="utf-8")) or {}
        for new in patch.get("claims") or []:
            cid = new["id"]
            old = by_id.get(cid)
            if old is None:
                print(f"  [MISSING] {cid} is not in {target.name}")
                missing += 1
                continue
            old_claim = old.get("claim", "") or ""
            new_claim = new.get("claim", "") or ""
            lost_d = sorted(set(DIGITS.findall(old_claim)) - set(DIGITS.findall(new_claim)))
            gain_d = sorted(set(DIGITS.findall(new_claim)) - set(DIGITS.findall(old_claim)))
            lost_h = sorted(hedges(old_claim) - hedges(new_claim))
            gain_h = sorted(hedges(new_claim) - hedges(old_claim))
            if lost_d or gain_d or lost_h or gain_h:
                problems.append(
                    f"  [{cid}] digits lost {lost_d} gained {gain_d}; "
                    f"hedges lost {lost_h} gained {gain_h}")
            old["claim"] = new_claim
            if "note" in new:
                old["note"] = new["note"]
            patched += 1

    with open(target, "w") as fh:
        yaml.safe_dump(doc, fh, sort_keys=False, width=105, allow_unicode=True,
                       default_flow_style=False)
    print(f"patched {patched} record(s) in {target.name}; {missing} id(s) not found")
    if problems:
        print(f"\n{len(problems)} record(s) where a digit or a hedge moved. "
              f"Read each one before trusting the patch:")
        for line in problems:
            print(line)
    else:
        print("no digit or hedge changed in any patched claim")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
