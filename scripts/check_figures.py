#!/usr/bin/env python3
"""Check that every figure in figures/ is recorded in figures/MANIFEST.yml.

The manifest is the only place a figure's provenance lives. A figure that
reaches the book without an entry is a figure nobody has stated the origin of,
which is exactly the case the licensing rules in CONTRIBUTING.md exist to
prevent. Catching it by hand works until it does not.

Checks, in both directions:
  - every light-mode SVG in figures/ has a manifest entry
  - every manifest entry names a file that exists, including its dark variant
  - every generated entry names a script that exists
  - every reused entry carries a licence, a licence URL and a source

Usage:
    python3 scripts/check_figures.py
Exit 1 on any failure.
"""
from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FIGDIR = ROOT / "figures"


def main() -> int:
    import yaml

    manifest = FIGDIR / "MANIFEST.yml"
    if not manifest.exists():
        print("figures/MANIFEST.yml is missing")
        return 1

    doc = yaml.safe_load(manifest.read_text(encoding="utf-8")) or {}
    entries = doc.get("figures") or []
    recorded = {str(e.get("path", "")) for e in entries}

    fails: list[str] = []

    on_disk = {f"figures/{p.name}" for p in sorted(FIGDIR.glob("*.svg"))
               if not p.stem.endswith("-dark")}
    for path in sorted(on_disk - recorded):
        fails.append(f"{path} has no entry in MANIFEST.yml")

    for e in entries:
        path = str(e.get("path", ""))
        if not (ROOT / path).exists():
            fails.append(f"MANIFEST lists {path}, which does not exist")
        dark = e.get("dark")
        if dark and not (ROOT / str(dark)).exists():
            fails.append(f"MANIFEST lists dark variant {dark}, which does "
                         "not exist")
        route = e.get("route")
        if route == "generated":
            script = str(e.get("script", ""))
            if not script or not (ROOT / script).exists():
                fails.append(f"{path} is route: generated but names no "
                             "existing script")
        elif route == "reused":
            for field in ("licence", "licence_url", "source_doi"):
                if not e.get(field):
                    fails.append(f"{path} is route: reused and is missing "
                                 f"{field}")
        elif route != "original":
            fails.append(f"{path} has unknown route {route!r}")

    for f in fails:
        print(f"  - {f}")
    print(f"{len(fails)} figure manifest issue(s); "
          f"{len(entries)} entries, {len(on_disk)} figures on disk.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
