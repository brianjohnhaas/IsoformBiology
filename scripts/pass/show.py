import sys, yaml
f = sys.argv[1]
ids = set(sys.argv[2:])
d = yaml.safe_load(open(f))
for c in d["claims"]:
    if c["id"] in ids:
        s = c["source"]
        print("="*70)
        print(c["id"], "|", s["bibkey"], "|", s.get("year"), "| conf:", c.get("confidence"),
              "| preprint:", s.get("preprint"), "|", c["evidence"].get("text_access"),
              "|", c["source"]["doc_id"], c["evidence"]["lines"])
        print("AUTHORS:", str(s.get("authors"))[:160])
        print("CLAIM:", c["claim"])
        if c.get("note"): print("NOTE:", c["note"])
