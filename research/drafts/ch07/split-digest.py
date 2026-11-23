#!/usr/bin/env python3
"""Split the chapter 7 digest into one file per writer section.

Routing is by keyword over the topic string, with an explicit catch-all, and
the script FAILS if any record is unrouted or routed twice. On an earlier
chapter a topic fell between two writers and its records were never written
up at all, which is invisible in the finished prose.
"""
import re, sys, pathlib

src = pathlib.Path(sys.argv[1]).read_text()
out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)

# (section, [lowercase substrings]) -- first match wins, so order matters.
ROUTES = [
 ("s11-poison", ["scn1a", "poison exon", "zorevunersen", "emperor", "admiral",
   "tango", "opa1", "longwing", "first-in-patient", "platform", "redosing",
   "mutation independence", "who the approach cannot treat",
   "why the approach needs a functional second allele",
   "which cell type the oligonucleotide rescues", "splice-switching oligonucleotides as",
   "delivery", "off-target splicing", "open-label extension", "secondhand",
   "how much of scn1a", "developmental window", "measured ceiling",
   "seizure frequency was a secondary", "baseline population", "adverse events in the",
   "disease modification", "preclinical", "how many genes", "independent group raising",
   "independent corroboration", "poison-exon variant", "how often the drug has to be given",
   "whether there is a window for the drug"]),
 ("s2-tau", ["mapt", "tau ", "tauopath", "3r", "4r", "other neurodegenerative",
   "mecp2", "a named drug in trial"]),
 ("s3-tdp43", ["tdp-43", "stmn2", "unc13a", "cryptic exon", "cryptic-exon",
   "cryptic splicing", "fus, sod1"]),
 ("s4-sma", ["smn1", "smn2", "iss-n1", "risdiplam", "firefish", "sunfish", "endear",
   "cherish", "presymptomatic", "branaplam", "small molecule shifts",
   "gene replacement"]),
 ("s5-dmd", ["dmd ", "dystrophin", "reading-frame rule"]),
 ("s6-fraction", ["fraction of pathogenic", "massively parallel splicing assays",
   "published fractions", "synonymous, intronic", "deep-intronic",
   "splice-gain against splice-loss"]),
 ("s7-diagnosis", ["diagnostic", "rna sequencing as a diagnostic", "tissue choice",
   "aberrant expression", "long reads in diagnosis",
   "long reads and targeted rna assays", "confirming a candidate", "reanalysis"]),
 ("s8-prediction", ["splice-prediction", "splice predictors", "calibration and thresholds",
   "ranking variants"]),
 ("s9-nof1", ["n-of-1", "tractable for a splice-switching", "one-patient oligonucleotides"]),
 ("s10-retina", ["retinitis"]),
 ("s1-brain", ["brain", "neuronal isoform", "neurexin"]),
]

blocks = re.split(r"\n(?=## )", src)
header, routed = blocks[0], {}
unrouted = []
for b in blocks[1:]:
    topic = b.split("\n", 1)[0][3:].strip()
    low = topic.lower()
    for sec, keys in ROUTES:
        if any(k in low for k in keys):
            routed.setdefault(sec, []).append((topic, b))
            break
    else:
        unrouted.append(topic)

total_in = len(re.findall(r"\[NEU-", src))
total_out = sum(len(re.findall(r"\[NEU-", b)) for v in routed.values() for _, b in v)
if unrouted:
    print(f"{len(unrouted)} UNROUTED TOPIC(S):")
    for t in sorted(unrouted):
        print("   ", t)
for sec, items in sorted(routed.items()):
    body = "\n".join(b for _, b in items)
    (out / f"{sec}.md").write_text(header + "\n" + body)
    print(f"{sec:14} {len(items):3} topics {len(re.findall(r'\[NEU-', body)):4} records"
          f" {len(body.split()):6} words")
print(f"\n{total_in} records in digest, {total_out} routed")
if unrouted or total_in != total_out:
    sys.exit(1)
