# Records review E — NEU-261 to NEU-299 against their sources

Read-only on the repository. Working files in
`/tmp/claude-4108/-home-unix-bhaas-projects-GITHUB-MDL-IsoformBiology/4f6be56d-8db6-4eb1-8900-d1eca34f3bc6/scratchpad/ch07/rev/E/`
(`REPORT.md`, per-document reads `d_*.txt`, greps `g_*.txt`, byline intersections
`authors.json` + `extract.py` + `exact.py`). 39 records, 20 documents opened at the
cited lines and around them. `paperclip skill` run first; no `paperclip git`.

**Convention for the verdict column.** A figure that is correct, and that I verified
elsewhere in the same document, but that does not sit on a line the record cites, gets
`ok` where nothing else is wrong, plus an entry in list 2 at the end. A figure I could
not find at all would get `number wrong` or `cannot check`; none did.

## Verdict for every record

| id | verdict | id | verdict | id | verdict |
|---|---|---|---|---|---|
| NEU-261 | source metadata wrong | NEU-274 | qualifier lost | NEU-288 | scope too wide |
| NEU-262 | ok | NEU-275 | ok | NEU-289 | number wrong |
| NEU-263 | ok | NEU-276 | ok | NEU-290 | scope too wide |
| NEU-264 | qualifier lost | NEU-277 | ok | NEU-291 | ok |
| NEU-265 | ok | NEU-278 | qualifier lost | NEU-292 | ok |
| NEU-266 | ok | NEU-279 | proposal as finding | NEU-293 | qualifier lost |
| NEU-267 | ok | NEU-280 | ok | NEU-294 | scope too wide |
| NEU-268 | ok | NEU-281 | ok | NEU-295 | ok |
| NEU-269 | tier wrong | NEU-282 | number wrong | NEU-296 | ok |
| NEU-270 | ok | NEU-283 | ok | NEU-297 | qualifier lost |
| NEU-271 | ok | NEU-284 | qualifier lost | NEU-298 | qualifier lost |
| NEU-272 | ok | NEU-285 | ok | NEU-299 | ok |
| NEU-273 | ok | NEU-286 | ok | | |
| | | NEU-287 | ok | | |

24 `ok`, 15 not `ok`.

## Blocks

```
NEU-261  source metadata wrong
  The source: fields themselves check out: doc 50091604 is the PUBLISHED abstract
  (meta.json: doi 10.1126/scitranslmed.aal5209, pmid 28424332, pub_year 2017,
  text_access abstract_only), so abstract_only is right and no preprint: true is
  owed. The defect is the claim's comparison.
  claim says: "and adds the reference panel the calls were made against: each
    patient's muscle transcriptome was compared with more than 180 control skeletal
    muscle samples"
  source says: the preprint abstract already carries that panel. Doc 55237691
    (meta.json doi 10.1101/074153, 2016, same title) reads "compared to over 180
    control skeletal muscle samples"; the published abstract reads "compared to more
    than 180 control skeletal muscle samples". The two abstracts differ only in
    wording ("25 to 50%" vs "25-50%", "suggestive of having" vs "suggestive of", the
    preprint's extra One Sentence Summary). The published version adds nothing the
    preprint lacked, so the control panel is not a journal-version addition.
  Also: the claim makes a two-document comparison while the record cites one
    document, so nothing in the cited evidence can support "the same as the
    preprint" or "adds".
  lines read: 50091604 L1; 55237691 L1
```
```
NEU-264  qualifier lost
  claim says: "the range depending on how stringent the coverage requirement was set"
  source says: the read-coverage requirement was held fixed. L91 ends "An 8-read
    junction support parameter was used throughout", and L90/L91 attribute the spread
    to "the stringency of the model" / "dependent on model stringency" (Figure S14).
    The record's own note says the same ("a function of the model parameters"), so
    claim and note disagree. All four figures (7,507; 25.8%; 67.8%; the four tissues)
    are on the cited line.
  lines read: PMC8874219 L90-L91
```
```
NEU-269  tier wrong
  note says: "tier: isoform-specific biochemical or binding difference, no
    organismal phenotype"
  source says: what was measured on the cited lines is gene expression induction and
    junction-read coverage - 193/516 (37.4%) of neurological silent genes expressed
    after transdifferentiation (L26), 6- to 90,000-fold induction of 20/20 genes
    (L26), 17/20 reaching >7 reads across >75% of junctions (L65). No binding or
    biochemical difference between isoforms is measured anywhere on those lines; the
    isoform work is a nanopore amplicon comparison of PAK3 isoform diversity. This is
    a method/assay assessment, and it is the only record in the block carrying one of
    the three canonical isoform tiers, which will read as a tier error to a later
    reviewer. Figures all confirmed.
  Also: "measured against each other" sets 516 neurological silent genes against a
    selected 20 chosen "based on a need for VUS assessment in our laboratory" (L63),
    so the two arms do not share a denominator.
  lines read: PMC11339655 L26, L63, L65
```
```
NEU-274  qualifier lost
  claim says: "which only phenotype matching plus a nearby deleterious rare variant
    brought down to fewer than ten"
  source says: L30 gives that filter a different output - "restricting to
    UNDER-expression outlier genes with HPO matches and a deleterious rare variant
    nearby ... reduce the candidate genes list to less than 1% of the initial set of
    outliers with 80% of cases having at least one candidate gene (Filter 11)". The
    "less than 10 on average for all cases" is a separate sentence attributed to the
    filtering steps as a whole (Fig. 2d), across the eleven filters of Fig. 2c, so
    "only" is unsupported. The 343 is all outliers while the filter is scoped to
    under-expression outliers.
  lines read: PMC6634302 L26, L30, L67 (1,594 and 49 on L26; 899 and 32 on L67 -
    both correct)
```
```
NEU-278  qualifier lost
  claim says: "replacing a false-discovery-rate cutoff of 0.1 with the commonly used
    absolute Z score of 2 produced two orders of magnitude more outlier calls"
  source says: L26 compares two different methods, not two cutoffs on one method -
    "using PCA and a z score cutoff equal to 2, instead of FRASER at FDR < 0.1". L26
    separately credits part of the gap to the statistic itself ("methods that modeled
    covariation and used BB-based P values yielded a higher precision than those that
    used z scores"), so the comparator is PCA + |z|>2 and the change is model plus
    cutoff. The two measurements also come from different panels: the two orders of
    magnitude is "across all GTEx tissues (Supplementary Fig. S11)", the precision
    and recall from the injected-outlier benchmark on suprapubic skin
    (Supplementary Fig. S12); the claim puts both under injected skin. Nothing on
    L26 calls |z| of 2 "commonly used".
  All four figures confirmed on L26 with the right mapping: precision 3% (z) vs 92%
    (FRASER), recall 98% (z) vs 83% (FRASER).
  Tier: note says "cohort measurement of assay performance", but the measurement is
    on artificially injected outliers in a healthy-donor tissue, not a patient cohort.
  lines read: PMC7822922 L25-L27
```
```
NEU-279  proposal as finding
  claim says: "Outlier calls that appear in only one tissue of an individual are
    common for every method tested and are enriched for false positives"
  source says: L34 states the enrichment as an inference, not a result - "This
    SUGGESTS a higher proportion of false positives among the tissue-specific
    outliers" - and then undercuts the artefact reading: "We have investigated the raw
    RNA-seq data of several such tissue-specific outliers with IGV. These calls
    actually appear to be well supported by the raw data ... Further investigations
    ... will be needed to understand the reason for this apparent excess." The 22%,
    11% and the variant-enrichment comparison are all on L34 and correct.
  lines read: PMC7822922 L34
```
```
NEU-282  number wrong
  claim says: "7,622 of them covered by at least ten RNA reads"
  source says: "7,622 were sufficiently covered by RNA-seq to call MAE (more than 10
    reads)". More than 10 is not at least 10, and the claim's threshold is the
    assay's detection floor, so the inequality carries weight. The other figures
    (35,521; 20; adjusted P < 0.05; allele frequency >= 0.8; 6 rare at MAF < 0.001)
    are all on L40 and correct.
  lines read: PMC5499207 L40
```
```
NEU-284  qualifier lost
  claim says: "94 individuals spanning 80 independent rare diseases and 16 disease
    categories ... 6 of the 80 independent cases"
  source says: the two 80s are different quantities. L27: "Patients represented 80
    different diseases and were broadly classified into 16 distinct disease
    categories". L33: "identify and validate the causal gene in 6/80 independent
    cases". The claim fuses "80 different diseases" and "80 independent cases" into
    "80 independent rare diseases", which is the exact collapse the record's own note
    warns against ("Three different denominators appear in one sentence of the
    source ... and the chapter must keep them apart").
  7.5%, 6/80, 16.7%, 5/30, 69 cases and 86% are all on L33 and correct.
  lines read: PMC6634302 L26, L27, L33
```
```
NEU-288  scope too wide
  claim says: "An independent cohort showed the same gradient"
  source says: every figure in this record is exactly on L9 and correct (55 families;
    negative WES/WGS; PHACs; VUS n=7 at 71%; suspected-gene n=10 at 40%;
    unsolved n=38 at 5.2%; 20% vs 9%; 11 positive of which 10 definitive). What the
    numbers do not support is "the same". The gradient here is 71/5.2 = about 14-fold;
    NEU-287's is 60/2.7 = about 22-fold, which NEU-287's own note states. The two
    also measure different things: L9 reports "positive rates", with 10 of 11
    positives then becoming definitive diagnoses, while NEU-287 reports a "diagnostic
    uplift". The direction replicates; the magnitude and the endpoint do not.
  Independence verified from the documents, not the YAML: PMC12781863 L3 (Ren, Dai,
    Meng, Zhang P., Xie, Xiao W., He, Yuan, Li, Zhang Q., Tang, Hu, Chen, Lu, Du,
    Zeng, Lin) against PMC12105386 L3 (Luo, Xiao B., Liang, Zhang K., Xu, Liu H.,
    Liu Y., Yu, Fan) share no surname-plus-initial; affiliations are Changsha
    (PMC12781863 L7-L8) and Shanghai (PMC12105386 L4-L5).
  lines read: PMC12781863 L7-L9; PMC12105386 L3-L5, L9, L11
```
```
NEU-289  number wrong
  claim says: "while among the 61 already diagnosed it reinforced the DNA finding in
    20 and revised it in 2"
  source says: L20 gives one revision, not two - "In 2/61 cases, RNA-seq revised
    diagnoses (EPG5 to LZTR1 in an individual with a Noonan syndrome-like disorder)
    AND discovered an additional relevant gene (CEP120 in addition to SON in an
    individual with ZTTK syndrome)". The second of the two is an additional gene
    beside a standing diagnosis, and L97 calls CEP120 a candidate with no DNA variant
    identified and unclear zygosity. The record's note also says "One revision was
    substantive", implying more than one.
  134, 5/73, ~7%, 20/61 are all on L20 and correct. "none a stated diagnosis" holds
    within the document: L93 - "the application of RNA-seq to cases with no DNA
    findings resulted in candidate genes related to participant phenotypes in 5 out
    of the 73 cases". Prior testing is genome sequencing with reanalysis, diagnostic
    rate 41% (L26). "added almost nothing new" is the record's framing, not the
    source's; L20 says the study "highlights both the benefits and limitations".
  lines read: PMC12215727 L20, L26, L78, L92-L93, L97, L99
```
```
NEU-290  scope too wide
  claim says: "In the largest blood cohort assembled"
  source says: nothing on the cited lines, or anywhere I read in the document, claims
    primacy. L1 says only "We present short-read RNA-Seq data from 5,412 individuals
    with a diverse range of rare disorders recruited to Genomics England's 100,000
    Genomes Project". The superlative is a claim about the evidence landscape and
    belongs, scoped, to a reviewer's note - NEU-270's note has it as "the largest
    blood cohort IN THE CORPUS", which is the defensible version.
  5,412, the 20% outlier rate, the 74 / 35 / 39 split, and the n=78 and n=19 arms are
    all on L1 and L22 and correct.
  lines read: med_530d6f638abe L1, L21-L22, L27, L29
```
```
NEU-293  qualifier lost
  claim says: "Monoallelic expression re-promoted a variant the exome analysis had
    set aside"
  source says: two arms re-promoted it, not one. L40 - "However, RNA-seq-based
    aberrant expression (Supplementary Fig. 7) and MAE analysis prioritized ALDH18A1
    again." The record sits under the topic "Aberrant expression and monoallelic
    expression as separate findings", so attributing the re-promotion to monoallelic
    expression alone is the error that topic exists to prevent.
  Everything else on L40 is right: 18 rare monoallelically expressed variants in
    patient #80256; the ALDH18A1 VUS compound with a nonsense variant; protein
    "severe reduction down to ~2%"; plasma metabolomics in accordance with a proline
    defect; growth defect rescued by proline supplementation.
  lines read: PMC5499207 L40, L106
```
```
NEU-294  scope too wide
  claim says: "showed which variant classes an RNA assay can and cannot see ... and
    none of the 14 genes where a missense variant was causal did"
  source says: L43 scopes both negatives to this pipeline - "only one of the 9
    frame-shift variants did lead to a detectable RNA defect" and "For none of the 14
    genes where missense variants were disease causing, a RNA defect could be detected
    WITH OUR PIPELINE". The claim drops that scope and generalises to RNA assays. The
    chapter's bound rests on this record, so the scope matters.
  All five ratios are on L43, with the source's own units preserved by the claim:
    7/8 cases, 3/6 patients, 3/4 homozygous stop variants, 1/9 frameshift variants,
    0/14 genes. Note that 8+6+4+9+14 = 41 against "40 diagnosed cases", so the
    source's classes are not disjoint; the record does not claim they are.
  lines read: PMC5499207 L43
```
```
NEU-297  qualifier lost
  claim says: "long reads recovered the full-length in-frame ATAD3A-ATAD3C fusion
    transcript with its exon-level breakpoints, establishing the molecular diagnosis"
  source says: on the SAME cited line, L148, the recovery was not the pipeline's -
    "The fusion transcript was initially filtered out by the LR RNA-seq pipeline due
    to internal polyA priming within the 3' UTR. It was also missed by our gene fusion
    pipeline ... However, manual review of the unfiltered BAM and generation of a
    customized genome, recovered the full-length in-frame ATAD3A-ATAD3C fusion
    transcript". That bound is the strongest thing on the line and it lives only in
    the record's note, so it cannot be cited. Per the file's own rule, a qualifier
    that lives in a note needs its own claim.
  Everything else confirmed: 9-day-old neonate, de novo ~69 kb ATAD3-cluster
    duplication, ambiguous DNA breakpoint resolution from cluster homology, SR
    RNA-seq "uninformative due to misalignment and absence of fusion-supporting
    reads", diagnosis established. The cited L92 is a table row; its header (L86) is
    "SampleID | Tissue type | Gene & transcript | variant | Overall consequence | LR
    advantageous to SR? | Prior report", so the row's trailing "No" means not
    previously reported, and its "Yes - fusion detected; clarified junction boundary"
    is the LR-advantage column.
  lines read: PMC13786605 L86, L92, L147-L149
```
```
NEU-298  qualifier lost
  claim says: "Confirmation ran in parallel rather than after the fact"
  source says: part of the confirmation predates this study and belongs to another
    publication. L51 - "all 14 were validated via RT-PCR (RT-PCR results for 6 of the
    14 variants have been previously reported [12])"; L25 - "Eighteen of the 51 VUSs
    have been previously assessed by RT-PCR [12]". Nothing on L51 establishes parallel
    running.
  Second, L51 places the four RT-PCR-only cases immediately after the sentence about
    the 15 unassessable variants - "Out of the 38 VUSs where aberrant splicing events
    were not detected, 15 variants could not be assessed as a result of low gene
    expression in blood ... RT-PCR was able to validate aberrant splicing in four
    additional cases with variants in TERT, PRG4 and TAOK1." A within-document grep
    for TERT|PRG4|TAOK1 returns only L51, so the document never says whether the four
    are inside or outside the 15. The claim presents the two as disjoint clauses and
    the note calls the four "RNA sequencing false negatives, not confirmation
    failures"; neither separation is stated by the source.
  14 of 14 confirmed, the four extra in TERT/PRG4/TAOK1, and 15 of 38 unassessable
    are all on L51 and correct.
  lines read: PMC11382415 L25, L50-L52
```

## The ten items: what I confirmed and what I could not

**1. NEU-261/NEU-262 — partly confirmed, one finding against the record.** Cohort and
yield are unchanged from the preprint: both abstracts give 50 patients with genetically
undiagnosed rare muscle disorders and an overall diagnosis rate of 35%, and both give
27 unsolved patients and ~25% of a collagen VI-like cohort. **The control-panel detail
is not an addition**: the preprint (55237691) already says "over 180 control skeletal
muscle samples"; the published abstract says "more than 180". The journal full text is
**not held** — `ls /papers/PMC5548421/` returns "PMC paper not found", `cat
.../content.lines` returns nothing, and `sql ... WHERE id='PMC5548421' OR doi ILIKE
'%aal5209%'` returns 0 rows; note that `sql` covers only PMC, bioRxiv and arXiv (a
title `ILIKE` for this exact title also returned 0 rows although 50091604 carries it),
so that negative is "not found by `ls`, `cat` or `sql`", not absence of the work.

**2. NEU-263 — fully confirmed on the cited line.** PMC8874219 L86 carries all of it:
3,322 multi-exon monogenic disease genes; "read coverage = 8; proportion of junctions =
75%; MRSD parameter = 95%"; low-MRSD defined as "<100 M reads required"; and all five
percentages — 28.2% (936/3,322) whole blood, 49.4% (1,641) LCLs, 43.6% (1,447) skeletal
muscle, 53.7% (1,784) fibroblasts, 64.2% (2,133) in at least one of the four. The note's
186/295 panels is also on L86.

**3. NEU-268 — confirmed, with one denominator caveat.** PMC11339655 L58: 4,878 Nijmegen
Disease Gene Panel 3.2.0 genes; "1,436 (~30%) of these Mendelian disease genes are not
sufficiently expressed in any of these CATs to conduct robust analysis of splicing using
srRNA-seq **at any sequencing depth**" (so "no amount of short-read sequencing" is the
source's own wording); "a muscle biopsy sample could be used to obtain sufficient mRNA to
assess a further 166 of them" (direction correct); "The largest proportion of SMGs are
involved in disorders of the nervous system"; "greater than 40% of known **dystonia,
cardiac, and retinal** disorder genes are silent" — the three groups confirmed. Caveat
for the writer: those three proportions are computed against PanelApp Australia disease
panels (L59 legend), not against the 4,878, and L58 gives no n for them.

**4. NEU-278 — all four figures confirmed, benchmark not independent, one defect.**
L26 gives 3% vs 92% precision and 98% vs 83% recall with the right assignment, and "two
orders of magnitude more outliers". The authors **are** the developers: the document is
the FRASER paper itself (PMC7822922 L1 "Detection of aberrant splicing events in RNA-seq
data using FRASER"), so the comparison is the method's own. That fact is note-only. The
defect is in the block: the comparator is PCA plus |z|>2, not the same model at a
different cutoff, and the two measurements come from different panels (S11 across all
GTEx tissues; S12 injected skin).

**5. NEU-294 — all five ratios confirmed on L43, with the scope defect in the block.**
1 of 9 frameshift variants and 0 of 14 genes with a causal missense variant are exactly
the source's figures and units, both scoped by the source to "our pipeline".

**6. NEU-287/288 with NEU-289 — gradient confirmed, "twenty-fold replicated" not.**
Independence is **document-confirmed** (bylines read from PMC12105386 L3 and PMC12781863
L3: no shared surname-plus-initial; Shanghai against Changsha). But the three figures are
not one gradient: 60%/2.7% is about 22-fold on diagnostic uplift, 71%/5.2% is about
14-fold on positive rate. The bound holds and is the cleanest figure in the block: after
**genome** sequencing (PMC12215727 L26, diagnostic rate 41% after GS and reanalysis),
blood RNA-seq gave 5 of 73 undiagnosed cases at least one plausible candidate gene and
no diagnosis — within-document confirmed at L93. One correction: "revised it in 2" is
one revision plus one additional candidate gene (block above). Also note that the
stratifier in both Chinese cohorts is prior-candidate status, not test modality; both are
ES/GS mixed with no split by modality.

**7. NEU-261 against NEU-286 — overlap verified, but it is not where the record puts
it, and the "no reason given" needs rescoping.**
- NEU-286 and **NEU-285** share three authors, document-confirmed: Alba Segarra-Casas,
  Daniel Natera-de Benito and Berta Estévez-Arias are on both bylines (med_f576f2f76edc
  L2 and PMC12257123 L3). The Solve-RD preprint also **cites** the Segarra-Casas paper
  (L232) and lists Hospital Sant Joan de Déu, Barcelona among its centres (L5-L6), which
  is one of NEU-286's affiliations. Neither document states whether patients are shared,
  so "the cohorts may overlap" is a sound inference and **not** a confirmed overlap.
- NEU-261 and NEU-286 share **no** author at all (surname-plus-initial intersection
  empty), so the 35%-against-14.3% pair is not the non-independent one.
- The overlap no record mentions: **NEU-261 shares Gonorazky, H. and Dowling, J. with
  NEU-283** — the other high muscle figure, 36% (9/25). It also shares Bournazos, A. and
  Cooper, S. with NEU-268/NEU-269, and Töpf/Topf, A. with NEU-285. Caveat the caller
  asked for: doc 50091604's `meta.json` carries **no author list and no journal**, so
  every NEU-261 overlap is a match of name strings in a Crossref-filled byline and
  cannot be confirmed in this corpus.
- **Neither record explains the gap, but the Segarra-Casas paper is not silent.** Its
  L57 cites Cummings' 35% and the 7.5%-36% range; its L170 says "RNA studies offer
  greater diagnostic success in cases with strong candidate disease genes", citing
  Cummings. So the honest statement is that the record's cited lines (L28, L30, L32) give
  no reason, and the paper's discussion offers prior-candidate presence as a partial
  account — the same axis NEU-287/288 measure. The record's note says "the lines read do
  not say why", which is accurate as scoped but will read to a writer as "the paper says
  nothing".

**8. NEU-296/NEU-297 against NEU-034 — independence confirmed from the documents, both
limits confirmed, the long-read win confirmed with a defect.** Bylines read from
PMC13786605 L3 and PMC13247170 L3: **zero** shared authors, and zero with NEU-014
(PMC13082330) — so the agent's intersections were computed, not guessed, and they are
right. The limits genuinely differ: NEU-296's are poor capture of short isoforms (median
49 of 69 SIRV isoforms by long reads against median 67 of 69 by short reads, L108) and
uneven coverage in specific long transcripts (L24, mechanism on L109-L111); NEU-034's
are low or absent coverage of the particular gene (PMC13247170 L55: "Three of the four
events missed by LR were due to low/no coverage of the gene (PHF8, COX7B and
KIAA0825)"). NEU-297's win is confirmed, **but the pipeline's two discards and the manual
recovery are on cited L148 and live only in the note** (block above). I could not
exhaustively confirm NEU-296's note-level claim that this is the only case in that cohort
reaching a diagnosis short reads did not reach: L149 reports 15 probands with RNA-level
support and 12 with additional clarity and does not enumerate diagnoses.

**9. NEU-298/NEU-299 — NEU-299 fully confirmed, NEU-298 has the defect above.**
PMC12120114 L8 carries every element of NEU-299 exactly: short-term cultured PBMCs with
and without cycloheximide "enabling detection of transcripts subject to nonsense-mediated
decay"; "up to 80% of the genes in our intellectual disability and epilepsy gene panel";
46 affected individuals (and 15 parents); "splicing defects in six of nine individuals
with splice variants"; "Targeted cDNA analysis confirmed aberrant splicing in four
individuals but **missed intron retention in two**"; "Global analyses (FRASER, OUTRIDER,
and monoallelic expression) supported findings but did not yield new diagnoses". For
NEU-298: 14 of 14 RT-PCR confirmations, the four RT-PCR-only events in TERT, PRG4 and
TAOK1, and 15 of 38 variants unassessable in blood are all correct on L51; what fails is
"in parallel" and the assumed disjointness of the four and the 15.

**10. NEU-273 and NEU-293 — both confirmed; NEU-293 has one attribution defect.**
NEU-273: PMC7822922 L36 gives the 119 samples and "detecting all novel pathogenic splice
events described in the original study (CLPP, TIMMDC1 in two individuals, and MCOLN1)" —
four events, so the count is sound; L38 gives the homozygous synonymous TAZ c.348C>T
creating an upstream donor, "difference psi3 = -0.88", the truncation of the fourth exon,
the WES non-prioritisation because synonymous and not in ClinVar, and the diagnosis for
individual 74116. NEU-293: the residual protein level (~2%) and the proline rescue are
confirmed on L40; the defect is crediting monoallelic expression alone when L40 credits
aberrant expression and MAE together.

## Tiers

38 of 39 records carry a descriptive tier, as sanctioned: 35 "cohort measurement of assay
performance" (NEU-261 to 268, 270 to 272, 274 to 292 as applicable, 294 to 296, 298, 299)
and 3 "single-case measurement from a named variant to its transcript consequence"
(NEU-273, NEU-293, NEU-297). The three single-case tiers match what the sources did.
Checked against the sources, the descriptive strings are a good fit except:

- **NEU-269** carries a canonical isoform tier on a methods record — reported above as
  `tier wrong`.
- **NEU-263, NEU-264, NEU-268** call MRSD output a "cohort measurement of assay
  performance". The output is a model prediction of required sequencing depth, computed
  from control cohorts and applied to a gene list; no patient cohort was assayed. The
  strings are defensible but a writer reading them as measurements will overstate.
- **NEU-278** is a measurement on artificially injected outliers, and **NEU-279** on GTEx
  donors across tissues; neither is a cohort measurement of a diagnostic assay.
- **NEU-262** is a variant-prevalence statistic in an external cohort of unstated size,
  not an assay-performance measurement.

## Group counts and source metadata

Counted from the bylines, not fitted to the brief's "six and five":
- **Gagneur/Prokisch (Munich), 12 records across 5 documents** — NEU-271, 273, 277, 278,
  279, 280, 281, 282, 285, 293, 294, 295 (PMC8981716, PMC7822922, med_d99a1b696d5a,
  PMC5499207, med_f576f2f76edc). This is the largest cluster in the block and larger than
  any note states.
- **Baralle (Southampton), 6 records across 3 documents** — NEU-263, 264 (PMC8874219),
  270, 290 (med_530d6f638abe), 291, 298 (PMC11382415). Plus NEU-034 outside the block.
- **Frésard/Montgomery, 5 records on one document** — NEU-274, 275, 276, 284, 292
  (PMC6634302).
- **Toronto/SickKids, 8 records across 3 documents** — NEU-272, 296, 297 (PMC13786605),
  NEU-289 (PMC12215727), NEU-265, 266, 267, 283 (PMC6407525); the first two share five
  authors, the last four share four authors with NEU-289, all document-confirmed.

Note-level errors in independence statements (notes are not citable, but these will be
read by the writer):
- **NEU-273's note** says the FRASER/Kremer overlap is "Kremer, Gusic, Prokisch and
  Gagneur". Document-confirmed from PMC5499207 L3: **Gusic is not on Kremer 2017, and
  Mertes is**. The shared four are Kremer, Mertes, Prokisch, Gagneur.
- **NEU-289's note** lists four shared authors with NEU-272/296/297. Document-confirmed
  from PMC12215727 L3 and PMC13786605 L3, there are **five**: Hou, Costain, Szuto,
  Mendoza-Londono, Marshall. NEU-272's and NEU-296's notes say five and are right.
- **NEU-294's note** says "All five denominators are single digits"; one is 14.
- **NEU-262's note** says "the quarter has no numerator here"; it has a numerator (27) and
  no denominator.
- Document-confirmed and correct as written: NEU-291's four-author overlap with NEU-034
  (Baralle, Bunyan, Wai, Jaramillo Oquendo); NEU-263's Baralle/Ellingford/Douglas
  overlaps; NEU-270's Baralle/Lord/Jaramillo Oquendo; NEU-285's Yépez/Gagneur/Mertes;
  NEU-268's "author lists do not overlap" with NEU-263 (empty intersection, though
  Denommé-Pichon is shared with NEU-285, which no note mentions).
- Two overlaps the YAML hides and a surname match would miss: Lord's byline carries
  "Oquendo, C. J." for Jaramillo Oquendo, C., and Solve-RD's carries "Benito, D. N. d."
  for Natera-de Benito, D. Both are real; both are Crossref mangling.

**The bibkey/DOI item is resolved and the records are consistent.** Across
`research/*.yml` no bibkey maps to more than one DOI, and `cummings2016musclernaseq`
maps to exactly one, 10.1126/scitranslmed.aal5209, on NEU-261 and NEU-262. But the fix
was **deletion of NEU-031**, not a DOI change, so NEU-261's note is stale in three ways:
it instructs that "NEU-031 must therefore have its doi: field changed", it says the
record "Closes the file's lead that the published version of NEU-031 was not in the
corpus", and it reports the byline and journal as "RESOLVE_FROM_DOI" although both are
now filled from Crossref. The removal is recorded at the file's end (line 11226). A lead
at line 10493 also still names NEU-031 and says the COL6A1 finding "has no record of its
own here", which NEU-262 now contradicts.

Other metadata checks: `preprint: true` is correctly set on NEU-270, NEU-280, NEU-285 and
NEU-290 and correctly absent elsewhere; NEU-261/262's `abstract_only` is right.
`med_530d6f638abe` and `med_f576f2f76edc` carry exactly the DOIs their records record.
**NEU-280's note is wrong on one point**: it says the record carries "the journal DOI the
corpus lists for the published version", but `med_d99a1b696d5a`'s `meta.json` lists only
10.1101/2023.03.31.23287997, and a grep of the whole file for `ajhg|10.1016|publish`
returns nothing. The record's 10.1016/j.ajhg.2023.10.014 is Crossref-sourced and
unverifiable in this corpus. The field is schema-legitimate (preprint read, journal DOI
recorded, `preprint: true` set); only the note's account of its provenance is wrong.

## List 1 — yield figures missing cohort, tissue, prior testing or diagnosis criterion

Prior testing is the element that fails most, as expected.

- **NEU-261** (35%): prior testing is only "genetically undiagnosed". The source abstract
  gives no more, and the record's note carries the rest — "genetically undiagnosed on
  prior sequencing, with candidate variants already in hand for part of the cohort" —
  which is note-only and is also the most likely explanation of the gap with NEU-286.
- **NEU-262** (~25%): no cohort size for the external collagen VI-like cohort (the source
  gives none) and no tissue.
- **NEU-285** (7.7%): prior testing only "undiagnosed"; the source's "DNA analyses had
  been inconclusive, not uniformly exome or genome" is note-only. Tissues are "a mixture
  that varied between the contributing centres" without naming them (the source names
  whole blood, fibroblasts, muscle, PBMC); the five disease groups are not named.
- **NEU-286** (14.3% and 12.9%): no statement of what counted as a diagnosis.
- **NEU-287** (60% and 2.7%): no disease group ("suspected Mendelian disorders" in the
  source); prior testing is ES/GS mixed with no split, so the gradient is by
  prior-candidate status, not by modality.
- **NEU-288** (71/40/5.2/20/9%): no disease group; ES/GS mixed with no split.
- **NEU-289** (~7%): no disease group (the source gives epilepsy, global developmental
  delay, multiple congenital anomalies and others).
- **NEU-290** (20% with an outlier, 39 candidates): **prior testing absent, and it is
  genome sequencing** — all 5,412 were 100,000 Genomes Project participants (L21 runs
  Exomiser "on multi-sample GS files for the 5412 samples"), and 368 of 5,412 already had
  a confirmed diagnosis (L29). No disease group.
- **NEU-291** (14/48, four new diagnoses): prior testing only "prior DNA testing"; the
  source is no more specific ("previous genetic testing was negative"); no disease group.
- **NEU-292** (six validated diagnoses): no cohort named at all — the claim opens "in
  that cohort" — no size, no prior testing, no disease group.
- **NEU-294** (sensitivity by variant class): the tissue is absent from the claim; the
  source says fibroblast cell lines. No disease group (suspected mitochondrial disease).
- **NEU-295** (16% of cases): no cohort size, no prior testing, no disease group; the
  claim relies on a cross-reference to NEU-033 for all three, and the claim carries two
  different 16 per cents.
- **NEU-299** (6 of 9, no new diagnoses): prior testing absent from the claim and not
  stated on L8.
- **NEU-271** is not itself a yield record but its claim opens "In the fibroblast workflow
  behind the 16 per cent clinical yield" with no cohort size and no prior testing, so a
  writer quoting that phrase inherits the gap.

Passing in full: **NEU-283** (25 cases, muscle, exome and/or panel negative, monogenic
neuromuscular, and it says explicitly that genetic resolution is the only definition the
line gives) and **NEU-284** (94/80/30, blood, 88.8% uninformative exome, 80 diseases in
16 categories, causal gene found and separately validated).

## List 2 — claims whose figures are not on the lines the record cites

- **NEU-261**: the whole preprint-versus-published comparison needs doc 55237691, which
  the record does not cite.
- **NEU-265**: cites L115; "9,932 **protein-coding** genes ... in patient muscle biopsies"
  is established on **L95** ("In our cohort of muscle biopsies, 9,932 protein-coding genes
  were expressed, on average, at >1 RPKM"). L115 reuses the number inside a
  GTEx blood-versus-muscle comparison. The attribution is correct — I checked this
  specifically because L115 alone reads as GTEx on both sides — but it rests on an
  uncited line, and the "25-patient" framing is the record's: L91 reports 26
  skeletal-muscle biopsies and L98 "our 25 polyA purified muscle-biopsy transcriptomes".
- **NEU-266**: same 9,932 provenance; the cited L120 does carry the number, but
  "muscle biopsies" as the source of that set is on L95.
- **NEU-270**: cites L32; the cohort size 5,412 and the tissue (blood) are on L1 and L27.
- **NEU-271**: cites L168/L169/L172; "the 16 per cent clinical yield" is on L44/L46.
- **NEU-281**: cites L98/L168/L176; "303 fibroblast samples" is on L44/L46.
- **NEU-283**: cites L15; the tissue is on L91 and L98, not on L15, which names no tissue.
- **NEU-284**: cites L26/L33; "88.8 per cent had had an uninformative exome" and the "80
  different diseases" reading are on **L27**.
- **NEU-287**: cites L11; the 121-proband test cohort, the 128 recruited probands and the
  ES/GS prior testing are on **L9**.
- **NEU-290**: "the largest blood cohort assembled" is on no line in the document.
- **NEU-298**: cites L51; "86-patient" is on L25.

## Judgement

The block is in good shape on arithmetic: every figure I checked against the lines was
right to the digit, including all five MRSD percentages, all four FRASER benchmark
figures, all five variant-class ratios, the whole NEU-288 stratification and the whole
NEU-299 abstract. The defects cluster in exactly the place the standing instruction
predicts — sentences about the evidence rather than about the biology. Four claims
overstate what a comparison shows (NEU-261's "adds", NEU-288's "the same gradient",
NEU-290's "largest", NEU-278's cutoff-only framing); three drop a scope or an attribution
the source states on the cited line (NEU-294's "our pipeline", NEU-293's two arms,
NEU-298's prior RT-PCR); one leaves the tightest bound on its cited line in a note
(NEU-297). The independence notes are the block's strongest feature and its weakest: the
NEU-034/NEU-296 intersections, the Chinese-cohort separation and the NEU-285/NEU-286
overlap are all document-confirmed and correctly stated, but three notes miscount shared
authors, and the 35%-against-36% muscle pair at NEU-261/NEU-283 shares two authors that
no note mentions. Finally, prior testing is missing or vague in the claim of eleven yield
records, and in two of them — NEU-290 after genome sequencing, NEU-261 with candidates
already in hand — the missing status is precisely what would stop a reader comparing the
figure with the wrong thing.

