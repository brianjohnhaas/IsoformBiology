"""Replace sentences in a wrapped markdown file by flat text, then rewrap the paragraph.

Usage: edit.py FILE  with pairs on stdin as:  OLD <TAB> NEW  (one per line, flat text)
Reports every pair that did not apply, and applies the rest.
"""
import sys, re, pathlib, textwrap

def flat(s): return re.sub(r"\s+", " ", s).strip()

path = pathlib.Path(sys.argv[1])
pairs = []
for line in sys.stdin.read().split("\n"):
    if not line.strip(): continue
    old, new = line.split("\t")
    pairs.append((flat(old), new.strip()))

paras = path.read_text().split("\n\n")
misses = list(pairs)
for i, para in enumerate(paras):
    # A fenced div or a table must not be rewrapped: joining its closing ":::"
    # onto a prose line silently breaks the callout, which cost one render.
    if para.lstrip().startswith(("#", ":::", "![", "|", ":")): continue
    if ":::" in para or "\n|" in para: continue
    f = flat(para)
    changed = False
    for old, new in list(pairs):
        if old and old in f:
            f = f.replace(old, flat(new), 1)
            changed = True
            if (old, new) in misses: misses.remove((old, new))
    if changed:
        paras[i] = "\n".join(textwrap.wrap(f, width=78, break_long_words=False,
                                           break_on_hyphens=False))
path.write_text("\n\n".join(paras))
for old, _ in misses:
    print("MISS:", old[:80])
print(f"{len(pairs)-len(misses)}/{len(pairs)} applied")
