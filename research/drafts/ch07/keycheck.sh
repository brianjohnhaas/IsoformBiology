#!/bin/bash
# Every @key in a draft must be a bibkey in the chapter's own research file,
# or a @sec-/@fig-/@tbl- cross-reference. Written because four bibkeys in the
# chapter 4 draft were reconstructed from memory: the papers existed, the keys did not.
f="$1"; yml="${2:-research/01-foundations.yml}"; bad=0
for k in $(grep -oE "@[a-zA-Z0-9_-]+" "$f" | sed 's/@//' | sort -u); do
  case "$k" in sec-*|fig-*|tbl-*|eq-*) continue;; esac
  grep -q "bibkey: $k\$" "$yml" || { echo "MISSING BIBKEY: $k"; bad=1; }
done
[ $bad -eq 0 ] && echo "ok: every citation key in $(basename $f) is a bibkey in $(basename $yml)"
