"""Flag 8-gram overlap between a record's own claim sentence and its audit quote.
A claim that echoes its quote causes check_overlap failures later, in the book prose."""
import sys, yaml, re
N = 8
def words(t):
    return re.findall(r"[a-z0-9']+", t.lower())
bad = 0
for path in sys.argv[1:]:
    d = yaml.safe_load(open(path))
    for c in d.get("claims") or []:
        cw = words(c.get("claim",""))
        qw = words((c.get("evidence") or {}).get("quote","") or "")
        qg = {tuple(qw[i:i+N]) for i in range(len(qw)-N+1)}
        hits = [" ".join(cw[i:i+N]) for i in range(len(cw)-N+1) if tuple(cw[i:i+N]) in qg]
        if hits:
            bad += 1
            print(f"[{c['id']}] {len(hits)} shared {N}-gram(s):")
            for h in dict.fromkeys(hits):
                print(f"    {h}")
print(f"\n{bad} record(s) whose claim echoes its own quote at {N} words")
sys.exit(1 if bad else 0)
