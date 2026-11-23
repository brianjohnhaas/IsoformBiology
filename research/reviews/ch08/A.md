# Chapter 8 records review — block A: SCS-001..035, SCS-101..139 (74 records)

Reviewer: records against their sources (AGENT-BRIEFS section 2).

**File reviewed.** `research/08-singlecell-spatial.yml`, md5 `1626b5283441f022462eeef1028c4683`,
snapshotted to `snapshot.yml` in this directory. The live file was modified at 13:29:00 on
2026-11-23, 33 seconds before my snapshot: that edit added `preprint: true` to the bioRxiv
sources (SCS-005/006, 022/023, 033/034, 106/107 carried no flag in my first read and carry it
in the snapshot). Claim, quote, note and evidence text are identical between the two reads;
only those flags changed. Re-checked at 13:50:39 — the live file still matches the snapshot
md5, so every verdict below applies to the current file.

**Coverage.** All 74 assigned records. Every cited label opened with `paperclip cat
/papers/<id>/content.lines --lines N-N` and read with its neighbours; 35 distinct documents,
all full text, none abstract-only, so no `cannot check`. Every design detail, author
attribution and number not found on a cited label was chased with a within-document
`paperclip grep -n`. No corpus-wide grep negative is relied on anywhere in this report.

**Scoring rule used, stated so the two blocks are comparable.** `qualifier lost` where the
missing condition changes what the number means, or where the claim states a design detail
the source contradicts. `ok` plus an entry in section B/C/E where the omission narrows
interpretation but the claim's own wording does not assert the wider reading. Section A gives
the detail block for every row that is not `ok`; section F lists which `ok` rows nevertheless
carry a finding, so "60 ok" is not read as 60 clean.

## Verdict table

| id | verdict | | id | verdict |
|----|---------|-|----|---------|
| SCS-001 | ok | | SCS-101 | qualifier lost |
| SCS-002 | ok | | SCS-102 | qualifier lost |
| SCS-003 | ok | | SCS-103 | ok |
| SCS-004 | ok | | SCS-104 | ok |
| SCS-005 | ok | | SCS-105 | qualifier lost |
| SCS-006 | ok | | SCS-106 | ok |
| SCS-007 | ok | | SCS-107 | ok |
| SCS-008 | ok | | SCS-108 | ok |
| SCS-009 | ok | | SCS-109 | ok |
| SCS-010 | ok | | SCS-110 | ok |
| SCS-011 | ok | | SCS-111 | ok |
| SCS-012 | ok | | SCS-112 | ok |
| SCS-013 | ok | | SCS-113 | ok |
| SCS-014 | ok | | SCS-114 | ok |
| SCS-015 | ok | | SCS-115 | ok |
| SCS-016 | ok | | SCS-116 | ok |
| SCS-017 | scope too wide | | SCS-117 | ok |
| SCS-018 | qualifier lost | | SCS-118 | ok |
| SCS-019 | ok | | SCS-119 | number wrong |
| SCS-020 | ok | | SCS-120 | ok |
| SCS-021 | ok | | SCS-121 | ok |
| SCS-022 | ok | | SCS-122 | qualifier lost |
| SCS-023 | qualifier lost | | SCS-123 | ok |
| SCS-024 | ok | | SCS-124 | qualifier lost |
| SCS-025 | ok | | SCS-125 | ok |
| SCS-026 | ok | | SCS-126 | ok |
| SCS-027 | ok | | SCS-127 | ok |
| SCS-028 | ok | | SCS-128 | ok |
| SCS-029 | ok | | SCS-129 | ok |
| SCS-030 | ok | | SCS-130 | qualifier lost |
| SCS-031 | ok | | SCS-131 | ok |
| SCS-032 | qualifier lost | | SCS-132 | qualifier lost |
| SCS-033 | ok | | SCS-133 | ok |
| SCS-034 | qualifier lost | | SCS-134 | ok |
| SCS-035 | ok | | SCS-135 | ok |
| | | | SCS-136 | qualifier lost |
| | | | SCS-137 | ok |
| | | | SCS-138 | ok |
| | | | SCS-139 | ok |

**Counts: 60 ok, 12 qualifier lost, 1 scope too wide, 1 number wrong, 0 direction wrong,
0 proposal as finding, 0 source metadata wrong, 0 tier wrong, 0 cannot check.**

One number in 74 claims is wrong (SCS-119, a flipped percentage base). Every other
percentage, count, correlation and copy number I checked appears on a cited line with the
same denominator, units and arm, subject to the cohort qualifiers in sections A and E.

---

## A. Detail blocks for every row that is not `ok`

```
SCS-018  qualifier lost
  claim says: "Exons that distinguished mouse brain cell types tended to distinguish the
    same cell types in human hippocampus, so cell-type splicing programs are conserved well
    enough to transfer between the two species."
  source says: the cited line supports one direction, inside a subset, and then states that
    the other direction fails. Conservation was tested only among those EVExs whose exon
    sequence and boundaries were conserved and sufficiently expressed in the human data,
    which the line puts at a quarter to a half of them depending on the exon class. Within
    that subset, mouse cell-type-specific exons did tend to be human cell-type-specific.
    Tested the other way round, only about two fifths of human cell-type-specific exons
    behaved similarly in mouse; the majority, and almost all invariable human alternative
    exons, were constitutively included in mouse, which the authors read as human
    gain-of-function exons that mouse does not model well. The claim asserts transfer in
    both directions where the line it cites reports failure in one.
  lines read: PMC11156538 L97 (with L79 and L63 for context)

SCS-017  scope too wide
  claim says: "A mouse and human brain isoform map covering roughly 200,000 cells found that
    about seven in ten genes carry isoforms whose variation across development, region or
    subtype is not explained by variation in the gene's own expression."
  source says: both the cell count and the proportion are mouse-only. The ~205,000-cell set
    on L63 is mouse hippocampus, visual cortex, striatum, thalamus and cerebellum; the 71.9%
    on L79 is computed in that mouse data. The human material is a separate set of six adult
    hippocampi, introduced later at L97. Attaching the count and the proportion to a "mouse
    and human" map states a mouse result at two-species scope.
  lines read: PMC11156538 L63, L79 (human data at L97)

SCS-119  number wrong
  claim says: "the next best, Sicelore2, 8.72 per cent lower"
  source says: the cited line gives 8.72% as Longcell's improvement over Sicelore2, not
    Sicelore2's shortfall against Longcell. Those are different bases: an 8.72% improvement
    on Sicelore2 puts Sicelore2 at about 0.396, which is roughly 8.0% below 0.43, not 8.72%
    below it. The 0.43, the 5,881 Jurkat cells, the 18 genes and the 110 isoforms are all
    exact. Also in this record: the claim's "one 10x 5-prime cDNA library ... was split and
    sequenced on both" is right but is stated in the Fig. 2B caption at L41, not on L44
    (see section B), and the pipeline ranked first is the paper's own tool (section E).
  lines read: PMC12276307 L44 (design at L41)

SCS-102  qualifier lost
  claim says: "libraries built from pooled and re-split RNA of the same cells"
  source says: the pool/split libraries come from a parallel set of cells, not from a
    re-split of the cells that were sequenced individually. L24 describes a pool/split as
    multiple cells pooled and lysed together and then divided into the same number of
    reactions, and the design line for Fig. 1D says this was done "in parallel" with the
    single-cell libraries. What the control isolates is therefore the protocol, not the
    sample. The record's own note says exactly this, so claim and note contradict each other,
    and the claim is the half a writer will use. The 50,000-to-300,000 and 50,000-to-100,000
    ranges and the authors' reading of them are exact.
  lines read: PMC3941114 L40 (design at L24, L15, L21)

SCS-132  qualifier lost
  claim says: "libraries built from pooled and re-split RNA of the same cells"
  source says: the same defect as SCS-102, from the same paper and the same design lines.
    The 282 genes whose dominant splice junction differed between single cells, and the very
    few that differed between split libraries, are exact on L63; the pool/split material is
    a parallel pool of cells. The record's note states this correctly and the claim
    contradicts it.
  lines read: PMC3941114 L63 (design at L24)

SCS-023  qualifier lost
  claim says: "more than five times the count the same framework recovered from long-read
    spatial data of the same tissue"
  source says: 815 is exact, but the ratio divides two counts that are not commensurable,
    and the paper does not state the ratio. The 815 are 3'-end usage events in one short-read
    Visium sample at an adjusted p below 0.01; the 150 being divided into it, from L34, are
    splicing events required to reach significance in both of two long-read replicates at an
    adjusted p below 0.05. Event class, replicate requirement and threshold all differ. The
    same line also attributes the larger short-read count to that platform's greater
    sequencing depth, confirmed by down-sampling, rather than to the platform class, and
    neither claim nor note carries that.
  lines read: bio_8065490174b9 L39 (and L34 for the 150)

SCS-034  qualifier lost
  claim says: "recall of junctions within 500 bp of the 3-prime terminus was 71.4 per cent,
    slightly lower than the 80.2 per cent for junctions 50 to 100 kb away" (as rendered in
    the claim's own words)
  source says: those two figures are recall within one selected cohort, robustly expressed
    junctions seen in at least 95 of the 190 bulk donors, which the claim does not state.
    The same paper's overall recall against its confident bulk junction set is an order of
    magnitude lower, 14.4% rising to 15.4% with annotation-guided realignment (L47), so a
    reader meeting 71.4% without the cohort will take it for the assay's recall. The
    position-independence conclusion itself is well supported, including the transcript-level
    repeat (70.0% versus 81.4%).
  lines read: bio_828796766d83 L48 (context L47)

SCS-105  qualifier lost
  claim says: "a cell barcode could be assigned to 68 per cent of those, and a UMI to 76 per
    cent of the barcode-assigned reads"
  source says: both rates were obtained with a matched Illumina short-read library supplied
    to guide the assignment, not from the Nanopore reads alone. L18 states that barcode
    assignment is guided with Illumina data and reports the 68% as the result of that
    strategy; L20 does the same for UMIs, having first explained that unguided UMI clustering
    on Nanopore reads is error-prone because most UMIs carry at least one error. The claim's
    "under a third of sequenced reads reached the count matrix" is therefore a best case
    that assumes a parallel short-read library, and neither claim nor note says so. The 57%
    poly(A)-plus-adapter figure (L16) and the eight PromethION runs (L17) are unaffected.
  lines read: PMC7423900 L15, L16, L17, L18, L20

SCS-136  qualifier lost
  claim says: "applied to 48 mouse embryonic stem cells in serum, 48 in inhibitor medium and
    48 neural stem cells ... one group fitted two Bayesian models"
  source says: the cited line itself says the modelling set was 107 cells, not 144. L20
    reports 869,000 unique molecules across the 144 sequenced cells and then states that
    after discarding cells with fewer than 1,000 observed molecules, 107 cells went into the
    further analysis. The 48/48/48 are cells put into the protocol; the DIC difference of 393
    and the binomial P of 4.6e-8 rest on 107. Everything else in this long claim is exact:
    95% of molecules unobserved (L37), the two models and the three sources they separate
    (L39), ΔDIC 393 (L41), P = 4.6e-8 from a binomial test against 1,000 simulations of the
    no-preference model (L42).
  lines read: PMC4501847 L20, L37, L39, L41, L42

SCS-124  qualifier lost
  claim says: "When one group simulated one, two, three or four isoforms per gene per cell
    ... more than a fifth of expressed isoforms were missed at both depths"
  source says: the simulation ran only on genes selected for having exactly four detected
    isoforms, which the claim does not say. L18 sets out that gene selection and the four
    scenarios built on it, and L20 repeats the selection step. The best overlap fraction
    under 0.8, and the authors' own reading of it as failing to detect over a fifth of
    ground-truth isoforms, are exact on L24, but they are properties of a multi-isoform gene
    subset rather than of genes in general. The split-cDNA design and the two depths are
    exact on L22.
  lines read: PMC7087381 L22, L24 (design at L18, L20)

SCS-122  qualifier lost
  claim says: "A simulation benchmark of five isoform quantifiers ... while recall sat
    between 0.956 and 0.960"
  source says: that range belongs to four of the five tools. L33 puts eXpress at 0.997 recall
    with 0.378 precision and attributes the 0.956-to-0.960 range explicitly to the other
    quantification tools. A claim that names five tools and then gives one recall range
    asserts of all five what holds for four. The best precision of 0.831, the authors' own
    "nearly one in six" reading, and the best F1 of 0.889 are exact, as are the 271 mESCs,
    SMART-seq2 and the over seven million reads per cell (L31, L32).
  lines read: PMC6223048 L23, L31, L32, L33

SCS-130  qualifier lost
  claim says: "after half of each pair's values were swapped to mimic a switch it detected 86
    per cent of them"
  source says: 86% is the sensitivity across the full spread of ERCC concentrations, and the
    next line reports how far it falls once the swapped pair's levels are close: 85% for
    pairs differing by at most fivefold, then 83%, 79% and 69% at fourfold, threefold and
    twofold (L61). Since a real isoform switch is a change in ratio rather than a
    thousandfold swap, 86% without that decay reads as sensitivity for switches in general.
    The 96 spike-ins, the 4,186 pairs and the 85% specificity are exact (L59, L60). This
    record also carries the circularity in section E: the noise model is fitted from the same
    spike-ins the 85% and 86% are measured on.
  lines read: PMC4856971 L59, L60, L61

SCS-032  qualifier lost
  claim says: "3-prime gene-expression libraries left under a tenth of cells positive for
    either CD45 isoform even at saturating depth"
  source says: the figure comes from one pool of one dataset and is an extrapolated
    asymptote, not an observation at depth. L66 restricts the subsampling to Pool 1 of the
    Lawlor PBMC 3' v2 data because of its size, and the under-10% is read off a fitted
    two-parameter rational function whose half-maximal points lie at 3.8e5 and 1.1e5 reads
    per cell, far above any depth sequenced. The mechanism, the alternatively spliced exons
    lying towards the 5' end, is correctly sourced to L68 and is the authors' own
    generalisation.
  lines read: PMC11496083 L66, L68

SCS-101  qualifier lost
  claim says: "they treat that figure as the single parameter that sets how noisy a
    single-cell measurement is"
  source says: the authors call capture efficiency the key parameter influencing technical
    stochasticity, not the single parameter, and they confine it to the technical component,
    describing it as a parsimonious explanation for the part of between-cell variation that
    is technical in origin. Separating technical from biological stochasticity is this
    paper's whole programme, so "how noisy a single-cell measurement is" absorbs the half the
    authors deliberately exclude. The 0.1 value and the SMART-seq attribution are exact. Low
    severity, but this is the sentence the chapter's limits section will lean on.
  lines read: PMC3941114 L67 (method at L15, L27, L33)
```

---

## B. Figures correct in the paper but not on a line the record cites

Sixteen cases. In each the fact is in the paper and in the right paper, but not at the cited
label, so `verify_claims.py` passing says nothing about it and the next checker will not find
it where the record points. Verdicts unaffected.

1. **SCS-002** — "Unsupervised clustering" is k-means with k fixed at 3, and the endothelial
   compartment was excluded for having under 5% of cells in both donors. Both are on L236,
   which the record does cite; what is *not* anywhere in the record is that the accuracies
   are scored against the atlas's own expression-based compartment labels (section E).
2. **SCS-007** — "two large mouse single-cell atlases" and "annotation-free" are on L77; the
   cited L78 carries only the no-new-subpopulations sentence.
3. **SCS-029** — "a small GTPase that shapes neuronal morphology" and "the two last-exon
   isoforms" are on L15; the cited L16 gives only the neurite-versus-soma mRNA result.
4. **SCS-030** — "A simulation study that modelled dropout and quantification error
   explicitly" describes the design, which is on L18 and L20. The cited L11 is the
   Conclusions paragraph and contains only the recommendation.
5. **SCS-101** — the spike-in route to capture efficiency is on L15, L27 and L33; the cited
   L67 does not mention spike-ins.
6. **SCS-102** — the cited L40 attributes the ~80,000 average to RNA mass and mean mRNA
   length; the spike-in calibration behind the per-cell absolute counts is on L15 and L27.
7. **SCS-105** — "10x Chromium 3-prime": L15 says only 10x Genomics Chromium.
8. **SCS-107** — "with abundant transcripts depleted beforehand" (CRISPRclean/Jumpcode) is on
   L26, which SCS-106 cites and SCS-107 does not. The 2,912 and 1,004 medians belong to that
   depleted library, so the qualifier is load-bearing.
9. **SCS-108** — "369 mouse fibroblasts": L22 gives 369 cells with no cell type; primary
   mouse tail-explant fibroblasts are at L44 and L50.
10. **SCS-116** — "In 10x 5-prime libraries": the 5' toolkit is named in the Fig. 1A caption
    at L26; the cited L25 says only that the 10-mer sits next to the cell barcode.
11. **SCS-119** — the split-library design is in the Fig. 2B caption at L41, not on L44.
12. **SCS-120** — "corrects UMI sequences with a graph algorithm" is on L135.
13. **SCS-124** — the one-to-four-isoform design is on L18 and L20 (section A).
14. **SCS-126** — the real dataset is MPNST1 PromethION, named on L130; L131 gives only the
    percentages.
15. **SCS-134** — that the pseudobulk methods are exactly six of the fourteen is on L36 and
    L73; L22 says only that all six top performers shared the aggregation property. I
    confirmed the six at L73 and L74 (DESeq2-LRT, DESeq2-Wald, edgeR-LRT, edgeR-QLF,
    limma-trend, limma-voom), so the claim is true.
16. **SCS-138/SCS-139** — the three-way replicate construction is on L34 and L38, and the
    0.1 threshold's provenance in bulk expression QC practice is on L34; the cited
    L33/L35/L38/L40 carry only the values. L34 also says the CV was computed in the single
    largest sample of each dataset.

Not a mis-anchor but worth one line: **SCS-031** says "In the same human individual" of both
the 1,416 and the 9,802. L271 attaches the individual to the droplet figure only and leaves
the plate-based figure's individual unstated; the paper's own sentence is equally ambiguous.

---

## C. Notes that assert an absence, or an inference, the source does not bear out

Reported because a note cannot be cited and three such notes have already proved wrong.

1. **SCS-118** — note: "the independent benchmark at SCS-120 and SCS-121 partly corroborates
   in direction while ranking the tools differently." That benchmark does not include
   Longcell. A within-document grep of PMC13335474 returns exactly one occurrence of
   "Longcell", in a background sentence at L20 listing methods that demultiplex barcodes and
   cluster UMIs from long reads alone; it is absent from every ranking (L97, L100, L124,
   L129). "Ranking the tools differently" invites the reading that Longcell was independently
   ranked, which is the one thing it was not.
2. **SCS-122** — note: the simulator worked from the annotation the tools were given, "with
   **no dropout**, no amplification bias and no unannotated isoform." The same paper's L43,
   the line SCS-123 cites, stratifies those simulations by dropout rate and reports the
   resulting rank correlations. The note and its sibling use "dropout" in two senses (no
   modelled technical loss process; observed zeros inherited from the real data), and the
   explicit modelling of dropout is what the record set says distinguishes the 2020 paper
   (SCS-030, SCS-124). Needs rewording, not re-anchoring.
3. **SCS-131** — note: "Of the 797 genes, 124 are accounted for by cell cycle phase, so the
   great majority were not explained by any annotated state." The cited lines do not make the
   124 a subset of the 797. L65 gives 797 genes with significant biological variation in
   isoform usage; L67 then runs a separate Kruskal-Wallis test across G1, S and G2/M on the
   SingleSplice isoform proportions and returns 124, with no statement that the tested set
   was the 797. The claim is correctly silent on this; the note's inference, and the "great
   majority unexplained" conclusion drawn from it, are unsupported by these lines.
4. **SCS-125 and SCS-121** — both notes take the complement of an F1 score for a miss rate.
   SCS-125's "roughly a quarter to a third of them are not recovered" comes from F1 figures
   of 73% and 70%, while L129 gives Isosceles recall of 69% against precision of 50 to 57%,
   so the unrecovered fraction is the complement of recall, not of F1. SCS-121's "on the older
   chemistry a fifth of it was wrong" does the same with an F1 of 0.80 and an ARI of 0.81.
   Both claims state the metrics correctly; only the notes slip.
5. **SCS-136** — note: "the sequencing depth per cell is not stated in the lines read." True
   per cell, but the cited L20 gives total depth (42.3 million read pairs, 10.3 million
   passing filters) and 869,000 unique molecules across 144 sequenced cells, so a per-cell
   figure is one division away and sits on a cited line. Borderline; listed so the writer
   does not treat depth as unknowable here.

Absences I checked and found sound: SCS-130 (cell count genuinely absent from L59–L61);
SCS-135 (the paper does say only "many" falsely called spike-ins on L30); SCS-110 (the author
does state at L42 that no comparable negative control exists for plate-based methods);
SCS-112 (immune gene families do stay zero-inflated after clustering — L19 names IG C, TR C
and HLA genes).

---

## D. Independence, recomputed from the bylines

Every explicit independence statement in these 74 notes is **correct**. I recomputed each
from the `source.authors` strings and, where the statement was about a citation rather than a
byline, read the citing text.

- SCS-101 / SCS-103 / SCS-109, "not independent estimates": confirmed. PMC7498265 L27 cites
  Marinov 2014 first among four references for the ~10% capture efficiency, and lists it at
  L243. SCS-103's finer point also holds: Marinov's per-gene copy numbers are spike-in
  calibrated estimates of molecules present (L15, L27), while SCS-109's 7–10 are recovered
  molecules, so they are not the same quantity.
- SCS-105 "different group" from SCS-106: confirmed, no shared name string between
  Lebrigand/Magnone/Barbry/Waldmann and the fourteen Scoones authors.
- SCS-110 "the three sets of authors are independent": confirmed. Svensson, V. alone;
  Kim, T. H./Zhou, X./Chen, M.; Choi, K./Chen, Y./Skelly, D. A./Churchill, G. A. The two
  Chens differ in initial, so the note stands rather than inverts.
- SCS-111 and SCS-114's cross-references to SCS-110: correct, including SCS-114's careful
  "disagree on whether zero inflation exists at all and agree on what causes zeros", which
  matches L33 and L59.
- SCS-120 "These authors are not the developers of any tool they rank": **scoped to what I
  ran** — no Hamraoui byline name recurs in this paper's own description of the ranked tools,
  and a within-document grep finds no "we developed" or equivalent for any ranked tool; the
  differential-isoform package it used (Isoswitch, github.com/ucagenomix, L53) is third-party
  as well. I did not open the tool papers, so this is a byline-and-text check, not a
  verification of every tool's authorship.
- SCS-122 "the same first author's later simulation ... not independent": correct and
  understated; Westoby, Hemberg and Ferguson-Smith all appear on both papers.
- SCS-128 "reached independently by a different group" from SCS-035: correct, no shared names
  between the Fu and Joglekar bylines. (Its "on long-read rather than exon-level data" is a
  loose contrast, since SCS-035's exon test was also run on long reads.)
- SCS-131 and SCS-132 "share no authors" with SCS-013: correct, and SCS-132's point that
  PMC7498265 reinterprets Marinov is confirmed at L16 and L22.
- SCS-136 "must not be cited as a second independent finding alongside SCS-011": correct,
  same paper.

Three non-independences that **no record states**, each one a chapter sentence about the
evidence waiting to go wrong:

1. **SCS-014 is the same laboratory as the atlases it summarises.** The record that reports
   what the literature concluded about bimodality (Joglekar, A.; Foord, C.; Jarroux, J.;
   Pollard, S.; Tilgner, H. U.) shares Joglekar, A. and Tilgner, H. U. with SCS-015, 016,
   019 and 035 (Joglekar 2021) and with SCS-017 and 018 (Joglekar 2024). None of those seven
   records carries a note at all, so nothing warns the writer that the survey and part of
   the surveyed are one group.
2. **SCS-104 and SCS-137 share a first author with SCS-110, and SCS-110 partly rests on their
   paper's data.** Svensson, V. is first author of the 2017 power analysis and sole author of
   the 2020 droplet paper. L29 of the droplet paper names its five negative controls and
   attributes two of them to Svensson et al. 2017. SCS-110's note asserts independence only
   among the three dropout papers, which is true as far as it goes; the chapter must not
   present Svensson 2017 and Svensson 2020 as two independent measurements.
3. **SCS-105's own dataset is the dataset reanalysed in SCS-133, and SCS-010, SCS-022 and
   SCS-133 all rest on data from that one group.** Checked against the reference lists rather
   than from memory. In PMC12276307, reference 19 is Lebrigand, Magnone, Barbry and Waldmann
   2020 *Nat. Commun.* — the paper behind SCS-105 — and L59 cites it as the source of the
   mouse embryonic brain data behind SCS-133's 268 meta-sites in 156 genes. Reference 27 is
   Lebrigand et al. 2023 *Nucleic Acids Res.*, cited at L70 and L72 as the source of the
   olfactory bulb Visium slice behind SCS-010 and behind SCS-133's 185 meta-sites in 131
   genes. Reference 18 of bio_8065490174b9 is that same 2023 paper, whose byline (L399)
   includes Lebrigand, Barbry and Waldmann, and whose two coronal sections are the data
   SCS-022 reanalyses. So the reanalysing groups are independent of each other and of the
   data's producers, but SCS-010, SCS-022 and SCS-133 are not independent measurements of
   tissue: three of them trace to two datasets from one laboratory, whose own protocol paper
   is SCS-105. SCS-023's 815-gene short-read Visium sample comes from a different reference
   and is not part of this. SCS-119's claim is the Jurkat benchmark only and is not part of
   it either.

---

## E. Performance figures missing a dataset, a cell count, a depth or a comparison

Beyond SCS-032, SCS-034, SCS-105, SCS-122 and SCS-130, which are scored in section A:

1. **SCS-130 — circular, and the circularity is not stated.** The 85% specificity and 86%
   sensitivity are measured on pairs built from the same 96 ERCC spike-ins the noise model is
   fitted from: L36 is captioned as fitting a technical noise model using spike-in
   transcripts, and L57 describes the logistic and gamma regressions fitted to that data. So
   a method's own authors scored it on the data its model was trained on, and neither the
   claim nor the tier ("validation of a technical-noise model against spike-ins of known
   constant amount") says so. The claim does at least disclose both halves separately, which
   is why the circularity is visible at all.
2. **SCS-002 — accuracy against the atlas's own labels.** The 78/84/95 and 70/100/49 figures
   are classification accuracies against compartment assignments that the Tabula Sapiens
   annotation produced from gene expression, and Tabula Sapiens Consortium is on this paper's
   own byline, so the labels are partly the authors' own product. L236 also fixes k at 3 and
   drops the endothelial compartment for having under 5% of cells. The claim names the three
   compartments and both donors and so does not assert the wider reading, but a chapter
   sentence of the form "splicing alone assigns a cell to its compartment" would need all
   three qualifiers.
3. **SCS-022 — the method's authors against a prior count, with no ground truth.** "More
   than doubled ... from 61 to 150" compares SPLISOSM's own output with the count previously
   published on the same data. There is no independent answer in that comparison, and the
   claim and note do not say that the new count is the proposing method's.
4. **SCS-119 — self-ranking not stated.** Longcell reaching the best mean per-cell
   correlation is the Longcell authors ranking Longcell. The note gives three good limits
   (best of the pipelines tested, the PacBio reference is itself a measurement, 18 targeted
   genes rather than a transcriptome) but not that the winner is the paper's own tool, which
   SCS-118's note does say for its number. Both numbers are from one paper, so the chapter
   needs that qualifier on both or on neither.
5. **SCS-123 — range excludes a tool.** The 0.977-to-0.996 band is for Sailfish, Salmon,
   Kallisto and RSEM only (L43). The claim does not name a tool count, so unlike SCS-122 it
   does not assert the wider reading, but the exclusion is unstated.
6. **SCS-117 — tier wording.** The tier says "exons whose true inclusion is known to be one".
   It is known to be one *by annotation*: L28 says the authors expected ψ near 1 because the
   exons are constitutive in the annotation. The claim is correctly phrased ("exons that the
   annotation calls constitutive"); only the tier overstates, and not enough to score.

---

## F. Which `ok` rows still carry a finding

So that 60 ok is not read as 60 clean. `ok` rows with an entry above: SCS-002 (B, E),
SCS-007 (B), SCS-014 (G), SCS-008 (G), SCS-022 (E), SCS-029 (B, G), SCS-030 (B, G),
SCS-031 (B), SCS-103 (D), SCS-107 (B), SCS-108 (B), SCS-109 (D), SCS-110 (D), SCS-112 (C),
SCS-116 (B), SCS-118 (C), SCS-120 (B, D), SCS-121 (C), SCS-123 (E), SCS-125 (C),
SCS-126 (B), SCS-131 (C), SCS-133 (D), SCS-134 (B), SCS-138 (B), SCS-139 (B, G),
SCS-117 (E), SCS-104 (D), SCS-137 (D).

Clean on every axis I checked: SCS-001, 003, 004, 005, 006, 009, 010, 011, 012, 013, 015,
016, 019, 020, 021, 024, 025, 026, 027, 028, 033, 035, 106, 111, 113, 114, 115, 127, 128,
129, 135.

---

## G. Tiers, source metadata, and smaller observations

**Tiers.** No `tier wrong`. All 39 records SCS-101..139 carry a descriptive tier of the form
the brief allows for a measurement chapter, and I scored each against what the source did
rather than against the three biology strings. None claims an organismal phenotype or any
outcome beyond the measurement performed; the design-naming tiers ("negative-control test of
a distributional assumption", "pool/split", "hold-out test of novel-isoform recovery",
"practitioners' own statement of a limitation") all match their cited lines. The only two
that drift are SCS-117 and SCS-130, both in section E, both too mild to score.

**Block-level gap, reported because it is not a verdict.** None of the 35 records SCS-001 to
SCS-035 records a tier at all: SCS-001 to SCS-019 and SCS-022 to SCS-035 have no `note:`
field whatsoever, and SCS-020 and SCS-021 have a note carrying only the preprint explanation.
The whole first block therefore gives a tier reviewer nothing to score while the second block
is complete. Several of those records have a qualifier worth having: SCS-003 and SCS-004 are
reanalyses of public datasets rather than new measurement, SCS-008 rests on one donor's
sorted subsets, SCS-014 is a review, SCS-029 is mESC-derived neurons rather than tissue, and
SCS-002's accuracies are scored against the atlas's own labels.

**Source metadata — checked, not assumed.** I read `meta.json` for all 35 documents and
compared title, DOI, `pub_year`, journal and `source` against each record's `source` block.
No PMC document is a preprint server record mislabelled as a journal: all 25 PMC docs carry
`source: pmc` and their DOI, title and year match the records. The ten `bio_` documents carry
`source: biorxiv`, no `journal` and no `pub_year`, and their DOI is the preprint DOI while
the records carry the journal DOI where one exists (SCS-020 Cell, SCS-108 and SCS-110 Nature
Biotechnology, SCS-115/138/139 Genomics Proteomics & Bioinformatics) or the bioRxiv DOI
where none does. Every one of those ten records carries `preprint: true` in the snapshot and
`metadata_source: crossref`, which is the pattern SCHEMA.md prescribes, so I score none of
them wrong. Title mismatches were typographic only (curly versus ASCII apostrophes and
primes). One discrepancy I cannot settle from the corpus: **SCS-029** records `year: 2019`
while PMC6411841's `meta.json` says `pub_year: 2018` and the bibkey is
`ciollimattioli2018alternative`. The DOI matches and the NAR issue is 2019 with a 2018
advance publication, so 2019 is defensible, but record year and bibkey disagree and
`resolve_metadata.py` should settle which the bibliography will print. The same bibkey-year
pattern appears benignly on the preprint records (SCS-020 `cohen2025whole` with `year: 2026`,
SCS-115 `dai2025precision` with `year: 2025`).

**Smaller observations.**

- **SCS-014 is a review reporting another paper's number.** The ~20%-of-exons figure is the
  review's one-sentence summary of its own reference 12 (PMC10807471 L14). The claim is
  honest about its source ("A review ... records that"), which is why I scored it `ok`, but a
  reviewer could defensibly call it `proposal as finding` under the brief's "someone else's
  result cited by them", and I flag it so the choice is the orchestrator's rather than mine.
  Either way CONTRIBUTING's rule against citing a review for a primary finding applies: the
  chapter should not print ~20% on this citation alone, and the primary should be chased.
- **SCS-008**: the 29 immune subsets came from one donor, a 42-year-old healthy female, with
  a second donor used only to validate isoforms (L22). The claim does not overreach, but the
  single-donor basis appears nowhere in the record.
- **SCS-030** calls the source "short-read single-cell RNA-seq" where the paper says
  full-length scRNA-seq throughout. Both are true of Smart-seq-style data and the
  recommendation is quoted exactly, but the chapter should not let "short-read" imply
  3'-tag droplet data, which this paper did not test.
- **SCS-139**'s "a level no other cell type ... **because** none had 500 cells sequenced"
  makes causal what L40 states as a conjunction. The causal reading is the authors' own
  argument elsewhere (L38's −0.66 and −0.78 correlations between cells per replicate and
  median CV, L35's −0.88 between CV and abundance), so I did not score it.
- **SCS-010 is the model for how the per-cell records should read.** It states the Mapre3
  result and then adds that the measurement is per spot rather than per cell, which is
  exactly the correction L74 needs, since the source's own sentence says "each single cell"
  of Visium spot data.
- **SCS-111**'s note flags the paper's internal denominator inconsistency (zero proportions
  across 15,568 genes, then the model comparison as 257 of 5,568). Both numbers are on that
  one line; the note's instruction to resolve it against the methods before printing is the
  right call.
- **SCS-120**'s note flags that the text calls the metric MSE (L100) while the figure caption
  calls it RMSE (L93). Confirmed, both on cited lines.
- **SCS-129**'s note that the simulated 20% gain used an auxiliary feature correlated 0.8
  with the truth by construction is confirmed at L21 and L56. That is the single most
  important caveat on any method record in this block and it is correctly recorded.

---

## H. Constraints observed

Read-only on the repository; nothing created or modified outside this directory;
`research/*.yml` untouched (verified by the unchanged md5 above); no replacement claim
sentences anywhere in this report; the chapter was not opened. `paperclip skill` was run
before the first paperclip command. Working files in this directory: `snapshot.yml`,
`records.txt`, `records2.txt`, `preprint.txt`, `meta_*.json` (35 files).
