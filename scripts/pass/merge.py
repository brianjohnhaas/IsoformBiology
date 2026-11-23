#!/usr/bin/env python3
"""Merge research-agent claim files into a chapter's research file.

    scripts/pass/merge.py research/01-foundations.yml AGENTDIR/*.yml

An incoming record whose id already exists REPLACES the existing one, loudly,
because a correction pass sends back amended versions of records that are
already in the file. Everything else is appended, and leads are concatenated.

The backup goes to $PASS_BACKUP_DIR (default: the system temp directory), never
beside the file in the repository, because `git add -A` swept one up once.

It then prints the two things that have gone wrong on past merges: two records
sharing one (doc_id, lines) anchor, and one bibkey carrying two DOIs.
"""
import sys, os, yaml, pathlib, shutil, collections, tempfile, datetime

target = pathlib.Path(sys.argv[1])
backup_dir = pathlib.Path(os.environ.get("PASS_BACKUP_DIR", tempfile.gettempdir()))
backup_dir.mkdir(parents=True, exist_ok=True)
stamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
backup = backup_dir / f"{target.stem}-before-merge-{stamp}.yml.bak"
shutil.copy(target, backup)
print(f"backup: {backup}")

base = yaml.safe_load(open(target))
claims = list(base.get("claims") or [])
leads = list(base.get("leads") or [])
index = {c["id"]: i for i, c in enumerate(claims)}
added = replaced = 0
for p in sys.argv[2:]:
    d = yaml.safe_load(open(p)) or {}
    for c in d.get("claims") or []:
        if c["id"] in index:
            claims[index[c["id"]]] = c
            replaced += 1
            print(f"  [replace] {c['id']} from {p}")
        else:
            index[c["id"]] = len(claims)
            claims.append(c)
            added += 1
    leads.extend(d.get("leads") or [])
claims.sort(key=lambda c: c["id"])
base["claims"] = claims
base["leads"] = leads
with open(target, "w") as fh:
    yaml.safe_dump(base, fh, sort_keys=False, width=105, allow_unicode=True,
                   default_flow_style=False)
print(f"merged {added} new, {replaced} replaced -> {len(claims)} total; leads {len(leads)}")

anchors = collections.Counter((c["source"]["doc_id"], c["evidence"]["lines"]) for c in claims)
dup = [k for k, v in anchors.items() if v > 1]
print(f"reused (doc_id, lines) anchors: {len(dup)}")
for k in dup:
    print("   ", k, anchors[k])
bibk = {}
for c in claims:
    bibk.setdefault(c["source"]["bibkey"], set()).add(c["source"].get("doi"))
for k, v in bibk.items():
    if len(v) > 1:
        print(f"  [!] bibkey {k} carries {len(v)} DOIs: {v}")
