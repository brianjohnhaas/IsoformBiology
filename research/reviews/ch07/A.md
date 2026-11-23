# Records review: NEU-101..NEU-133 (33 records), chapter 7

Verdict table

NEU-101  scope too wide
NEU-102  ok
NEU-103  ok (minor, see minor list)
NEU-104  ok
NEU-105  ok (minor)
NEU-106  ok
NEU-107  ok (flagged: hedge)
NEU-108  ok
NEU-109  ok
NEU-110  ok
NEU-111  ok
NEU-112  ok
NEU-113  proposal as finding
NEU-114  ok
NEU-115  ok (minor: anchor)
NEU-116  ok (independence note stale)
NEU-117  ok (independence note stale)
NEU-118  ok
NEU-119  ok
NEU-120  ok
NEU-121  ok
NEU-122  scope too wide + note unsupported
NEU-123  ok
NEU-124  ok (minor)
NEU-125  ok (minor)
NEU-126  ok (minor: anchor, no tier string)
NEU-127  ok (flagged + no tier string)
NEU-128  ok (minor: anchor; note incomplete on independence)
NEU-129  ok
NEU-130  ok (minor)
NEU-131  ok
NEU-132  ok (minor)
NEU-133  ok (minor)

Zero arithmetic errors. Every number in every claim was found at the paper with
the same denominator, units, cohort and arm, with the anchor exceptions listed.

## Findings

NEU-101  scope too wide
  claim says: "The tau isoform composition of the inclusions differs between tauopathies rather than
    being shared: ... while in progressive supranuclear palsy and corticobasal degeneration the majority
    of cases show up-regulated 4R-tau."
  source says: the review names inclusions only for Pick disease. For PSP and CBD it says only "Changes
    of 3R-tau/4R-tau ratio are also seen in PSP and corticobasal degeneration, in which 4R-tau is
    up-regulated in majority of the cases [63]" and names no assay at all. The note's blanket statement
    "The assay is inclusion composition by staining, not an mRNA ratio" is therefore unsupported for two
    of the three diseases in the claim.
  lines read: PMC2483273 L89 (context L88-L91)

NEU-113  proposal as finding
  claim says: "Two splicing factors act on tau exon 10 by binding the pre-mRNA itself"
  source says: the pull-down percentages are measured, but the regulatory role is the authors' inference:
    "suggesting that these factors may regulate MAPT exon 10 splicing via a direct interaction with its
    pre-mRNA." The only regulation evidence in the paper (overexpression shifting the 4R:3R and exon-2
    ratios in SH-SY5Y) sits in the Figure 2 caption at L41 and the record deliberately excludes it, so
    the claim asserts a mechanism the record itself declines to anchor.
  lines read: bio_facc27446c19 L40 (context L39-L41)

NEU-122  scope too wide, and the note asserts a result the source does not report
  claim says: "Raising 4R tau on its own is enough to produce a disease phenotype in human neurons"
  source says: the intervention is a 3R-to-4R splice-switching ASO, i.e. a ratio shift that lowers 3R
    as it raises 4R; the paper calls the outcome "4R tau dominance" (L54) and "an increase in 4R tau"
    (L48-L49), never an isolated 4R increase. The record's own note concedes "the comparison is a ratio
    shift in both arms", which contradicts "on its own".
  note says: "here an excess of 4R, with no change in total tau, is sufficient"
  source says: total tau unchanged is reported only for VCP-mutant neurons - "a marked increase in 4R tau
    levels in neurons carrying VCP mutations with no changes in total tau levels" (L43). For the ASO arm,
    total tau was blotted (Fig 4B, caption L47) but no result for it is stated anywhere in the text or
    caption; only 4R tau and phospho-tau are reported as significantly raised.
  lines read: PMC10907086 L43, L47, L48, L49, L54

## Flagged, uncertain

NEU-107  possible hedge drop
  claim says: "The seeding asymmetry runs in both directions, which is what makes the isoform the
    determining variable"
  source says: "Templated misfolding of this type may explain why only 4R tau is incorporated into CBD
    filaments." The cell-based result is as recorded; the step from it to "the determining variable" is
    the hedged part. Reporting it because the chapter will lean on this sentence.
  lines read: PMC7148158 L20

NEU-127  framing not in the source
  claim says: "What separates the brain from the other tissues is less its total than what only it
    expresses"
  source says: cerebellar hemisphere has both the highest total (22,522) and the largest unique set
    (3,726); the paper's own framing is "These stark differences mark the cerebellar hemisphere as a
    truly unique tissue in this study". The "less its total than" contrast is the record's, not the
    paper's, and is in tension with NEU-126 from the same paper.
  lines read: PMC12679790 L47, L48, L38

## Independence

NEU-116 / NEU-117  notes are now stale
  Both notes say independence "cannot be assessed" / "cannot be checked" because the fields were
  RESOLVE_FROM_DOI. The fields have since been filled from Crossref and the two bylines now share three
  name strings - Jordan, M. A.; Wilson, L.; Feinstein, S. C. Both documents are abstract-only and their
  meta.json carries no authors field (confirmed by reading both), so this cannot be verified in corpus:
  it is the same name string, not a verified laboratory. The practical reading is the opposite of what
  the notes suggest to a writer - these must not be presented as independent, and the notes should not
  be read as leaving the question open.

NEU-128  note incomplete
  The note names only CEL-024 as sharing the senior author. The leads block (research/07-neuro-mendelian.yml
  around L10565) correctly names both CEL-024 and CEL-025. CEL-025 rests on PMC9586558, full text, authors
  Dai; Liakath-Ali; Golf; Sudhof. A writer reading only NEU-128's note would miss the second one.
  NEU-128/129's own byline is confirmed in corpus with affiliation visible: Trotter; Wang; Zhou; Nakahara;
  Sudhof, Stanford University School of Medicine and HHMI (PMC10063607 L3-L5, meta.json authors).

NEU-104/105/106/107  shared laboratory confirmed from the bylines
  PMC6204212 (Falcon et al. 2018) and PMC7148158 (Zhang et al. 2020) share Murzin, Falcon, Vidal,
  Garringer, Ghetti, Goedert and Scheres. Both bylines are in corpus meta.json. The notes are right.

## Minor and anchor notes (no verdict change)

NEU-103  the review calls the ISS+ISM pair "bipartite elements composed of the ISS (E10+11 to E10+18) and
  the intronic splicing modulator (ISM) (E10+19 to E10+26)". The claim attaches "bipartite" to the
  silencer alone. Everything else on L21 checks out, including 14 mutations in six elements and the
  13.6 kb / 3.8 kb intron sizes. The note's "at least 7 cis-elements" cross-reference is at L94.
NEU-105  V300 is described in the claim as "bulkier"; the source calls it a Cbeta-branched residue and
  reserves "bulkier" for K294. The three-experiment denominator is at L30 and L53 as the note says.
NEU-115  the cited line L6 (abstract) names only "4R preparations alone" as the comparator. The claim's
  lead "that either alone does not" is true but rests on L32: "mixing equimolar amounts of these 3R and
  4R tau isoforms resulted in a significant decrease in tau assembly relative to 3R or 4R tau alone",
  which the record does not cite.
NEU-124  the corpus trial document nowhere labels an outcome "primary"; the text has no Primary/Secondary
  headers (grep "Outcome" returns nothing) and L9 is simply the first entry in sections/Planned_Outcomes.
  "The primary endpoint" is an inference from position. "aged 50 to 80" comes from the Brief Title at L1,
  not from the cited L7 or L9, and 416 is the Enrollment Count (ACTUAL), not a randomised count.
  Everything else - quadruple masking, parallel group, the four arms with their intervals, up to 72 weeks,
  CDR-SB change from baseline to week 76 - is on L7 and L9. Other Names ISIS 814907 and BIIB080 are on L8.
NEU-125  the claim says "post-hoc analyses"; the source says "exploratory analyses" throughout. Everything
  else on L7 matches to the digit, including every arm size. Ionis Pharmaceuticals appears as an
  affiliation at L6, so the note's sponsor/originator point is visible in the document.
NEU-126  22,522 and 12,435 are on the cited L11; the gene counts 13,236 and 8,857 are at L38, and the
  threshold "median unique count >= 1 and median CPM > 1" is at L78. Neither is at L11. The note's
  CPM-10 figures (3,815 liver, 7,916 cerebellar hemisphere) are at L38 and correct.
NEU-128  the cited L14 supports only "either SS2 or SS4 need to lack an insert". The two-clause pattern in
  the claim, including the short SS2 insert, rests on L64: "SS2 is dominant in this combinatorial splice
  code because even when SS4 is spliced out, the longer insert in SS2 (SS2ab) blocked the function of
  Nrxn3alpha", plus the dystroglycan binding rule at L11.
NEU-130  the tier string says "with a phenotype" but the groups were assigned by repeat-expansion genotype,
  which the note states. "Commonest genetic cause" is not on L10. Every number on L10 is exact.
NEU-132  the ASO work is in GrnR493X mice and the UPF3b deletion is in Grn+/R493X brains; the claim runs
  them together as one genotype.
NEU-133  "the exon that makes big tau" (4a) is the record's gloss; L29 names only the exons.

## Source metadata

All DOIs in the block match the corpus meta.json exactly, as do journal and year, with these exceptions,
all explicable:
 - bio_facc27446c19 and bio_b9e258806e26 carry bioRxiv DOIs in corpus (10.1101/2021.09.23.461598 and
   10.1101/2025.05.06.652428) while the records carry journal DOIs - which is exactly what SCHEMA.md
   requires preprint: true for, and both records set it.
 - PMC10907086: corpus pub_year is 2023 (pub_date 2023-10-26) and the bibkey is hung2023vcp4rtau, but
   source.year says 2024. One of the three is wrong. Authors "Christy Hung; Rickie Patani" and journal
   Brain are confirmed in meta.json, so the two-name byline is right.
 - bio_b9e258806e26's journal DOI 10.1126/scitranslmed.ady6759 and year 2026 cannot be checked inside
   the corpus, which holds only the preprint.
No DOI in the block is wrong by a digit.

## Preprint flags

Nine records in the block carry preprint: true - NEU-109 to NEU-114 and NEU-133 on bio_facc27446c19, and
NEU-118 and NEU-119 on bio_b9e258806e26. All nine are correct: the corpus document is a preprint in both
cases and the lines read are the preprint's. All nine also record a located journal DOI, so none of them
is the "preprint with no published version located" case; grep for "no published version" in the file hits
only records outside this block (around lines 4778, 4867, 10757, 10759). The dispatch's count of seven does
not match anything in NEU-101..133.

## Tier strings

Seven records carry "No tier applies" with a reason: NEU-103, NEU-111, NEU-112, NEU-124, NEU-125, NEU-132,
NEU-133. Each stated reason matches what the source did - a review's element inventory (103), iso-seq
isoform proportions with no significant disease comparison (111, 112), a registration with no posted result
(124), an exon-level RNA-seq expression pattern (133), and a transcript-directed intervention read out as
transcript abundance, negative (132). NEU-125 is the one that does not fall in any of the three sanctioned
categories: it reports clinical outcomes. Its stated reason - a tau-lowering rather than isoform-selective
drug, and a trend in an exploratory analysis - is accurate to the source, so I am not scoring it wrong, but
it is a fourth category.
NEU-126 and NEU-127 carry no tier statement at all, neither one of the three strings, nor a descriptive
tier, nor "No tier applies". They say only "Not a case record". Brief 1 asks for a descriptive tier in that
situation.
