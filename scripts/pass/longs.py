"""List sentences in a chapter by length, so a style pass can target the heavy ones."""
import re, sys, pathlib
txt = pathlib.Path(sys.argv[1]).read_text()
lines, keep, incode = txt.split("\n"), [], False
for ln in lines:
    if ln.startswith("```"): incode = not incode; continue
    if incode or ln.startswith(("#", ":::", "|", "!", ":")) or not ln.strip(): continue
    keep.append(ln)
body = " ".join(keep)
body = re.sub(r"\[@[^\]]*\]", "", body)
body = re.sub(r"\s+", " ", body)
sents = re.split(r"(?<=[.!?]) +(?=[A-Z@])", body)
cut = int(sys.argv[2]) if len(sys.argv) > 2 else 30
out = [(len(s.split()), s) for s in sents]
print(f"{len(out)} sentences, mean {sum(n for n,_ in out)/len(out):.1f}")
for n, s in out:
    if n >= cut: print(f"\n[{n}] {s}")
