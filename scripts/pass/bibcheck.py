"""Book-wide: one DOI must not sit under two bibkeys, and one bibkey not under two DOIs."""
import yaml, glob, collections
bydoi = collections.defaultdict(set); bykey = collections.defaultdict(set)
for p in sorted(glob.glob("/home/unix/bhaas/projects/GITHUB/MDL/IsoformBiology/research/*.yml")):
    d = yaml.safe_load(open(p)) or {}
    for c in d.get("claims") or []:
        s = c["source"]; k = s["bibkey"]; doi = (s.get("doi") or "").lower().strip()
        bykey[k].add(doi)
        if doi: bydoi[doi].add(k)
bad = 0
for doi, ks in bydoi.items():
    if len(ks) > 1: bad += 1; print(f"[!] DOI {doi} under bibkeys {sorted(ks)}")
for k, ds in bykey.items():
    if len(ds) > 1: bad += 1; print(f"[!] bibkey {k} carries DOIs {sorted(ds)}")
print(f"{bad} problem(s); {len(bykey)} bibkeys, {len(bydoi)} DOIs")
