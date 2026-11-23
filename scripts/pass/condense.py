import yaml, sys, textwrap
d = yaml.safe_load(open(sys.argv[1]))
def sq(s):
    return ' '.join(str(s).split())
out=[]
for c in d.get('claims',[]):
    s=c.get('source',{}); e=c.get('evidence',{})
    line=f"{c['id']} [{s.get('bibkey')}] ({e.get('text_access','?')}, conf={c.get('confidence')}, {s.get('year')})"
    if s.get('preprint'): line+=" PREPRINT"
    out.append(line)
    out.append("  claim: "+sq(c.get('claim','')))
    if c.get('note'): out.append("  NOTE: "+sq(c['note']))
    out.append("")
print("\n".join(out))
print("=== LEADS ===")
for l in d.get('leads',[]):
    print(" - "+sq(l.get('note','')) + "  || why: "+sq(l.get('why','')))
