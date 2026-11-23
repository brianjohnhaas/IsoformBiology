# Records review — chapter 7, NEU-301 to NEU-339 (reviewer G)

Scope: 39 records in `research/07-neuro-mendelian.yml` (file lines 7464-8787), each checked
against its own cited lines in the cited document. Every cited line was opened and read, with
the lines around it (18 documents; bodies dumped to `docs/` in this directory). Read-only on
the repository; the chapter was not opened.

**Convention used in the verdict table.** The verdict scores the whole `claim:` sentence —
including its lead clause, which the writer will lift — against its cited lines. Defects that
live only in a `note:` are reported in the four lists after the detail blocks and do not change
a row to non-`ok`, because `claim:` is what gets cited. Rows that are `ok` but carry a
note-level or anchoring finding are named by id in those lists, so no record is silently clean.

**Counts: 28 `ok`, 11 not `ok`** — 4 `qualifier lost`, 6 `scope too wide`, 1 `direction wrong`.
No `cannot check`, no `number wrong`, no `proposal as finding`, no `tier wrong`, no
`source metadata wrong`.

## The three findings that matter most

1. **NEU-329 has no independence note and is the same programme as the records it is meant to
   balance.** It exists, by its own note, because the chapter otherwise reports only milasen's
   absence of serious adverse events — so it will be set against milasen as a counterweight.
   Recomputed from the bylines, the KCNT1 report shares sixteen name strings with the
   ATM/atipeksen framework (NEU-325 to NEU-331) and about nine with the milasen report
   (NEU-324/NEU-037), senior author included. All three clinical programmes in this block are
   one group. Nothing in NEU-329 says so. (Details in list 3.)

2. **NEU-331 claims a comparison its lines do not make, and the comparison is probably false.**
   "The splice-switching n-of-1 drug that followed milasen has a longer safety record" — no
   cited line compares the two drugs, and the file's own NEU-038 has milasen's patient treated
   for about three years, the same duration atipeksen reports.

3. **NEU-311's benchmark is misdescribed, and the note makes the error explicit.** The 3,912
   variants behind the headline intron-versus-exon prAUC gap are 2,230 from four MPSA studies
   **plus 1,386 BRCA1 variants from a saturation genome-editing study** plus 296 curated MLH1
   clinical variants. The claim names only the MPSA studies and "a curated clinical variant
   set"; the note says the non-MPSA remainder *is* the curated clinical set, which is wrong by
   more than a thousand variants.

---

## Verdict table

| record | verdict |
|---|---|
| NEU-301 | ok |
| NEU-302 | ok |
| NEU-303 | ok |
| NEU-304 | ok |
| NEU-305 | ok |
| NEU-306 | ok |
| NEU-307 | ok |
| NEU-308 | ok |
| NEU-309 | ok |
| NEU-310 | qualifier lost |
| NEU-311 | qualifier lost |
| NEU-312 | direction wrong |
| NEU-313 | ok |
| NEU-314 | ok |
| NEU-315 | scope too wide |
| NEU-316 | ok |
| NEU-317 | scope too wide |
| NEU-318 | scope too wide |
| NEU-319 | ok |
| NEU-320 | ok |
| NEU-321 | qualifier lost |
| NEU-322 | ok |
| NEU-323 | ok |
| NEU-324 | scope too wide |
| NEU-325 | ok |
| NEU-326 | ok |
| NEU-327 | ok |
| NEU-328 | ok |
| NEU-329 | scope too wide |
| NEU-330 | qualifier lost |
| NEU-331 | scope too wide |
| NEU-332 | ok |
| NEU-333 | ok |
| NEU-334 | ok |
| NEU-335 | ok |
| NEU-336 | ok |
| NEU-337 | ok |
| NEU-338 | ok |
| NEU-339 | ok |

Six rows are `scope too wide` for two related defects that none of the nine strings names
exactly: a comparative or superlative judgement with no support on the cited lines (NEU-315,
NEU-317, NEU-318, NEU-331), and a property of the study design asserted beyond the cited lines
(NEU-324, NEU-329). `scope too wide` is the nearest fit in both cases — the claim reaches past
what its lines establish.

---

## Detail blocks

```
NEU-310  qualifier lost
  claim says: "There is no single defensible cut-off: when the threshold maximising Youden's J
    was fitted separately on each massively parallel splicing assay dataset, the best cut-off
    moved substantially between exons, between regions of one exon and between variant classes"
  source says: the cited line scopes that variability to "most tools", and then names the
    exceptions — the three tools whose thresholds moved least are SQUIRLS, SpliceAI and
    Pangolin, while the wide movers are HAL and ConSpliceML. Stated without the scope, the
    claim reads as covering the two tools the chapter cares about most, which are the named
    exception. That exception survives only in the record's note, which cannot be cited. The
    same line also fits thresholds on each dataset individually, which includes the BRCA1
    saturation-genome-editing and curated MLH1 sets, not only the MPSA datasets.
  lines read: PMC10187268 L22-L40 (claim rests on L32)
```

```
NEU-311  qualifier lost
  claim says: "across a benchmark of 1,060 splice-disruptive and 2,852 neutral variants, pooled
    from four saturation massively parallel splicing assay studies and a curated clinical
    variant set"
  source says: every number is right, but the benchmark has a third component the claim drops.
    The two counts sum to 3,912, and the cited L22 assembles that total from three sources:
    2,230 variants from four saturation MPSA studies, 1,386 BRCA1 variants from a saturation
    genome-editing screen that mutated the endogenous locus with CRISPR and read splicing out
    by RNA sequencing, and 296 MLH1 variants curated by hand from clinical databases. The SGE
    set is about a third of the benchmark and is not an MPSA. The record's note compounds it:
    it states that the non-MPSA remainder of the benchmark is the curated clinical variants,
    when the remainder is 1,386 SGE variants plus 296 curated ones.
  lines read: PMC10187268 L22, L23, L27 (L9 and L39 for the dataset description)
```

```
NEU-312  direction wrong
  claim says: "four current predictors separated barely at all"
  source says: on the reading a writer will most likely take in a section about where
    predictors fail — that the four tools barely discriminated — the cited lines say the
    opposite. They report good discrimination for all four on these 243 variants, the best of
    them near the top of the scale and the worst still well above chance, with the four
    separated from each other by only small margins and the source describing the runner-up as
    following "closely". There is a second reading on which the clause means the four barely
    separated from one another, and that reading is supported; the record's note shows its
    author read the data correctly, since it calls the discrimination inflated by the fact that
    the 202 variants were referred because a tool had already flagged them. The clause is
    therefore ambiguous in a way that inverts its meaning, and the inverted reading is the one
    the surrounding topic invites.
  lines read: PMC12547740 L49-L51
  not a defect, recorded so it is not re-raised: the source year is right. Crossref gives
    volume 7, issue 1, January 2026 for 10.1016/j.xhgg.2025.100521, matching the record's
    `year: 2026` and its `metadata_source: crossref`; the corpus `pub_date` of 2025-09-22 is
    the online-first date, and the 2025 inside the bibkey comes from the DOI string.
```

```
NEU-315  scope too wide
  claim says: "Tissue is where quantitative prediction is weakest even in the newest model"
  source says: the two cited lines support the tissue numbers and the fine-tuning input, and
    nothing else. They do not rank tissue prediction against the model's other tasks, and the
    comparison the superlative implies is not available there: it would have to set the
    tissue-pair Pearson coefficient against Spearman coefficients for cryptic-site usage and
    for sQTL effect sizes, which sit on a line this record does not cite, are a different
    correlation statistic, and are measured on a different task. The cited lines also push
    mildly the other way, reporting that fine-tuning beat training from scratch and that
    biologically distinct tissue pairs did better than the overall figure.
  lines read: bio_6f0a212282bb L7, L10, L11, L12 (claim cites L10, L12)
```

```
NEU-317  scope too wide
  claim says: "Against a reporter assay of rare variants rather than curated clinical ones,
    discrimination is much lower"
  source says: the cited line gives the two area-under-precision-recall values for this assay
    and nothing comparative. It does not report what the same tools achieve on curated clinical
    variants, so "much lower" is a comparison across records rather than across lines. The
    comparison is also not like for like: area under a precision-recall curve moves with how
    common the positive class is, and the positive class here is 3.8% of variants, against the
    heavily enriched referral and challenge sets the other benchmark records in this block use.
    Everything after the colon is exactly on the cited line.
  lines read: PMC9022248 L14, L15 (claim cites L15)
```

```
NEU-318  scope too wide
  claim says: "The strongest evidence that sequence models can quantify comes from a single
    well-measured exon"
  source says: the cited line reports the two FAS exon 6 correlations and nothing about how
    they rank among other evidence. No line in the paper ranks this result against
    transcriptome-scale quantification, and the ranking would again cross tasks and datasets.
    The record's own note already has the honest version — one exon in one reporter construct,
    bounding what is achievable rather than describing typical performance — which is a
    statement the cited line can carry, unlike the superlative in the claim.
  lines read: PMC9022248 L16, L49 (claim cites L16)
```

```
NEU-321  qualifier lost
  claim says: "SpliceAI and Pangolin, which those authors describe as sharing model
    architecture and training data"
  source says: those authors write that the two share *similar* architectures and training
    sets, not the same ones. Dropping "similar" turns a hedge into an identity, and it also
    undercuts the record's note, which says the shared-training-data characterisation is
    contradicted by Pangolin's own paper. On "similar" it is not contradicted: Pangolin's
    paper itself says its architecture resembles SpliceAI's, and both models learn splice-site
    labels from RNA sequencing and annotation, differing in species count and in whether the
    label is binary or continuous. The contradiction the note asserts holds against "the same
    training data" and dissolves against "similar training sets". The measured correlation of
    0.97, which is the claim's substance, is on the cited line.
  lines read: PMC10187268 L25; PMC9022248 L11, L13
```

```
NEU-324  scope too wide
  claim says: "which is a single-arm, unblinded comparison against the patient's own
    pre-treatment state"
  source says: the document is one line of abstract. It supports the absence of serious adverse
    events, a seizure reduction the authors call objective, ascertained by
    electroencephalography and by parental report, and an n-of-1 design, from which single-arm
    follows. It says nothing about blinding. The record's own note says nothing beyond the
    abstract may be asserted from it, and "unblinded" is asserted beyond it. Low severity:
    unblinded is a fair inference from parental reporting in an n-of-1, but it is an inference,
    and a reader following the anchor cannot confirm it.
  lines read: 27235986 L1 (abstract-only; the whole document is that line)
```

```
NEU-329  scope too wide
  claim says: "in two single-patient studies of a knockdown oligonucleotide for KCNT1 epileptic
    encephalopathy"
  source says: this was one protocol under one investigational new drug application, which two
    patients joined ten months apart, not two studies. The uncited narrative line describes a
    single investigational clinical protocol and a single IND number, with the first patient
    starting in September 2020 and the second in June 2021. The line the record does cite says
    patient 2 entered *the* investigational protocol — the same one. The methods line names one
    IND and two institutional review board protocol numbers, and those two numbers are the only
    support for "two studies"; they are not on a cited line. The contrast with NEU-332 is
    instructive: there the methods genuinely report separate research INDs authorised for
    single-patient studies, plural. Every clinical fact in the rest of NEU-329 is correct and
    anchored.
  lines read: PMC13099374 L47, L69-L72, L114; PMC13472884 L101 for the contrast
```

```
NEU-330  qualifier lost
  claim says: "an effect an oligonucleotide designed against intronic silencers failed to
    avoid"
  source says: the cited line notes, in parentheses, that oligonucleotides aimed at intronic
    splicing silencers might in principle avoid the exon-skipping side effect, and that the one
    built to explore that idea showed no promising activity at all. The source does not report
    that it was active and still caused exon-53 skipping, which is what "failed to avoid" that
    effect states. What failed was the strategy, for want of a working oligonucleotide. The
    rest of the claim — untreated baseline, the two post-treatment levels, both leads
    increasing exon-53 skipping, and the figures already adjusted for that skipping — is
    exactly on the cited line.
  lines read: PMC10371869 L65, L127
```

```
NEU-331  scope too wide
  claim says: "The splice-switching n-of-1 drug that followed milasen has a longer safety
    record"
  source says: none of the three cited lines compares the two drugs. They give this drug's
    route, its expanded-access setting, the age at first dose, the escalation then the
    maintenance dose and interval, three years of tolerability without serious adverse events,
    and the exploratory serum biomarkers. The comparison is also probably wrong in direction:
    this file's own NEU-038 records that milasen's patient died three years after treatment
    began, so the two records cover about the same length of exposure, and nothing in either
    source makes one record longer than the other. Everything after the colon in NEU-331 is
    anchored.
  lines read: PMC10371869 L22, L69, L170; and NEU-038 in this file for milasen's duration
```

---

## 1. Figures correct in the paper but not on a line the record cites

Claim-level. The figure or the named set is right; it sits on an uncited line.

| record | figure in the claim | where it sits | lines cited |
|---|---|---|---|
| NEU-313 | "In a blinded community challenge" | bio_4a00b60c6d50 L52 establishes it in substance — entrants received a tab-delimited file of coordinates and alleles only, plus 256 previously published validated variants for development, so they did not have the 56 outcomes. The word "blinded" appears only at L63, about assessors being blind to the entrants' method descriptions until after assessment. | L34, L49, L77 |
| NEU-314 | "the same 86 patient-validated variants" | PMC9925382 L41 (events induced by 86 of 88 variants scorable by both methods), also L36 and L37 | L42, which carries "Eighty-six percent (38/44)" of activated cryptics — a different quantity that happens to read as 86 |
| NEU-320 | "across eight tools" | PMC10187268 L25 and L9 | L22, L26 |
| NEU-325 | "from 209 families" | PMC10371869 L22 and L31 | L29, L50 |
| NEU-335 | the five tier names | PMC12120168 L108, which introduces the five tiers by name | L109, which defines "eligible" only |

Note-level. The note is right about the paper but rests on an uncited line. Listed because a
later pass may try to promote one of these into prose, and the anchor is not where the record
points.

- NEU-302 — the continuous, RNA-seq-derived nature of Pangolin's usage label is at PMC9022248
  L32, cited by NEU-301 but not by NEU-302.
- NEU-306 — the cohort of 140 individuals, 88 verified variants and 74 genes is at PMC9925382
  L16 and L20; the drop from 88 to 86 scorable variants is at L36. Record cites L41, L42.
- NEU-311 — the eight tool names are at PMC10187268 L25. Record cites L22, L27.
- NEU-313 — the assessors' blinding is at bio_4a00b60c6d50 L63. Record cites L34, L49, L77.
- NEU-318 — the calibration curve fitted on 24 mutants is at PMC9022248 L49. Record cites L16.
- NEU-332 — the allele-selective mechanism, targeting a heterozygous SNP on the reference
  haplotype, is at PMC13472884 L83 and L93. Record cites L42, L43, L56.
- NEU-335 — the "likely eligible" definition is at PMC12120168 L111; the three rounds of
  piloting are at L59, L65 and L67 (the third round, 19 external volunteers, 15 test
  variants). Record cites L109.
- NEU-336 — the ATMP hospital-exemption template is the section heading at PMC9058873 L59.
  Record cites L58.

## 2. Notes that assert absence where the thing is present

**NEU-338 — the absence assertion is partly answered by the record's own cited line.** The note
says the paper does not report how many of the 78 accepted applications were dosed. The cited
line reports median and mean time from acceptance to initial dose and says those statistics
rest on the first eight INDs the FDA approved — so at least eight had reached a first dose at
the cut-off, and those eight are the denominator of the 23-month figure the claim already uses.
This is an inference from the line rather than a count the paper states, so the note is too
absolute rather than flatly wrong. The other half of the note — that the denominator of the
173, 78 and 57 counts is applications and not treated patients — holds.

**NEU-301 — minor.** The note says the SpliceAI record at NEU-028 "carries no architecture
description". Its abstract does describe a deep neural network predicting splice junctions from
pre-mRNA sequence. That is thin, but it is an architecture-and-output statement, and it sits in
mild tension with the claim's "SpliceAI reports only whether a dinucleotide is a splice site",
which the claim does correctly attribute to Pangolin's authors.

**NEU-304 — the absence holds, but the writer needs one pointer the note does not give.** "No
primary description of SpliceAI's training labels is held in this corpus" is right: the SpliceAI
paper is abstract-only (its metadata says so), a `paperclip sql` ILIKE match on its published
title returns 0 rows across PMC, bioRxiv and arXiv, and a within-document grep of the SpliceAI
team's own successor preprint — 27 mentions of SpliceAI — finds no statement of what the
original was trained on. But a *secondary* description does exist in the corpus and is cited
elsewhere in this block: PMC9925382 L35 states how many annotated donor-acceptor pairs SpliceAI
was trained on. That is the SpliceVault authors describing a competitor, like the Pangolin and
Smith/Kitzman descriptions the chapter already treats as contested, so it does not change the
verdict — but the chapter should not say the corpus holds no description at all.

Absence assertions checked and holding, with the scope they should carry:

- NEU-328 — no test of variants the taxonomy called unlikely. Holds: a within-document grep of
  PMC10371869 for "unlikely" returns only the taxonomy definition, its figure caption, and one
  extended-data caption.
- NEU-323 — the review does not name the prediction tool used or say what was predicted. Holds
  for the cited line, which says only that the candidates were designed using in silico
  predictions.
- NEU-337 — no docket number anywhere in the document. Holds: a within-document grep for
  "docket" returns nothing. The date on the cover and running head is January 2021, and FDA
  media number 144872 is in the document's own retrieval URL, as the note says.
- NEU-322 — the primary milasen report is held only as an abstract. Holds.
- NEU-309 — the paper's own false-positive counts at the 0.2 threshold differ between the two
  lines the note names. Verified; both read.
- NEU-339 — no systematic search was run for other treated splice-switching n-of-1 cases. A
  statement about the research process, correctly scoped.

Every negative above was established by a grep inside the specific document, never by a
corpus-wide grep.

## 3. Independence notes that are wrong, inverted, or missing

**NEU-329 — missing, and it is the one that matters.** No independence note at all, on the
record whose purpose is to balance milasen's safety result. Recomputed from the bylines as the
records carry them:

- Against NEU-325 to NEU-331 (the ATM/atipeksen framework): sixteen shared name strings —
  Nakayama T., El Achkar C. M., de Gusmao C. M., Friedman D. A., Lentucci C., Suslovitch V.,
  Riccardi O., Faour K. N. W., Kuniholm A., Zhao B., Chin D. H., DiDonato R. L., Hu C. A.,
  Bush L. W., Berde C. B., Yu T. W.
- Against NEU-324 and NEU-037 (milasen): Yu T. W., Berde C. B., Grant P. E., DiDonato R. L.,
  Kuniholm A., Goodlett B. D., and, allowing for changes of form, Moufawad El Achkar C. /
  El Achkar C. M., Soucy A. / Soucy Verran A., Hu C. / Hu C. A. — about nine, the senior author
  of both among them. NEU-324 is abstract-only, so this should be written as sharing name
  strings, not as a verified shared laboratory.

So milasen, atipeksen and valeriasen are one programme by byline, and the chapter has no record
saying it.

**NEU-313 — the note names one overlap and misses the one that bears on the result.** It
records that the first author also wrote the splice-region constraint paper at NEU-029 and
NEU-030 (verified). But the byline also carries four authors of SPiP — Leman R., Martins A.,
Houdayer C., Krieger S., verified against the SPiP paper in the corpus, PMC10946553 — and SPiP
is one of the two approaches that the record's own cited line reports as reaching the maximum
overall accuracy and as best on sensitivity. Danis D., also on the byline, is by name SQUIRLS'
first author (name match only; not confirmed from a corpus document). The uncited L63 explains
why: entrants supplied their own method descriptions, so entrants are co-authors by design.
This is not an outside assessment of SPiP, and "blinded community challenge" is the phrase a
reader would lean on.

**NEU-312 — the note declines a check that is available, and the check comes out clean.** It
says no author list was checked against the four tools' developers, so independence is not
asserted. Recomputed: the 52-name byline (verified against the document's metadata) shares no
name string with the recorded developers of SpliceAI (NEU-028), Pangolin (Zeng, Li), SPiP
(PMC10946553) or, by name, SQUIRLS. On the bylines this benchmark is independent of the four
tools' developers. The non-independence the note *does* establish is correct and is the
important one: the 243-variant set contains all 56 CAGI6 variants, so NEU-312 and NEU-313 are
not independent benchmarks.

**NEU-333 — the count is one short.** The note says nine of this paper's authors also wrote the
guidelines at NEU-335. Recomputed from the two recorded bylines, ten name strings are shared:
Cheerie D., Lauffer M. C., Newton L., Beijer D., Haque B., Meserve (M. / M. M.), Aartsma-Rus A.,
Synofzik M., Yu T. W., Costain G.

**NEU-335 — "shares many authors" is right for two of the three records it names.** Ten shared
names with NEU-333 and NEU-334, which are the same document; only two with NEU-336 (Synofzik
M., Aartsma-Rus A., of seven authors). NEU-336's own note names that pair correctly.

**NEU-301 and NEU-305 — phrasing against an abstract-only record.** Both assert shared
authorship with NEU-028, whose byline is crossref-resolved rather than read from the document.
NEU-301's statement is correct as a name string: Li, Y. I. appears in the recorded NEU-028
byline and is Pangolin's senior author. NEU-305's is correct too: Jaganathan K., Farh K. K. H.,
McRae J. F. and Sanders S. J. all appear in both bylines. Both should say "shares a name string
with", since a crossref byline on an abstract-only record is not a verified laboratory.

Independence notes recomputed and found correct: NEU-302, NEU-304 and NEU-307 (Smith and
Kitzman built none of the eight tools, and CAN-314 in `research/06-cancer.yml` does share both
of them — its byline is Scott, Hernandez, Chamberlin, Smith C., Karam, Kitzman J. O.), NEU-306
(300K-RNA is these authors' own resource), NEU-316 (SpliceAI2 assessed by SpliceAI's own
developers), NEU-317 (the winning tool is the authors' own; the MFASS assay is another group's,
cited as a reference on the line read), NEU-319 (Cygan K. J. and Fairbrother W. G. are on both
the MMSplice byline and the MaPSy byline at NEU-026), NEU-321 (the characterisation is Smith
and Kitzman's, though see the detail block on "similar"), NEU-325 (same group as the milasen
report; the note names two shared authors where there are about ten, but the direction is
right), NEU-332 (six names shared with the n-Lorem paper: Crooke S. T., Gleeson J. G., Mignon
L., Douville J., Berry-Kravis E., Glass S.), NEU-336.

One observation rather than a defect: NEU-338 and NEU-339 carry no conflict note, and the paper
states one itself at its L100 — the organisation's position that it is fully independent of a
named pharmaceutical company, while its lead author was that company's chief executive and lead
scientist and several of its leaders trained there. Both records do say these are one
organisation's programme statistics, and NEU-339 says it is a statement about the authors' own
portfolio.

## 4. Trial or cohort results stated without arm, denominator or timepoint

| record | what is missing |
|---|---|
| NEU-332 | The two estimated reductions in seizure count carry no observation window. The windows are short and asymmetric on the pre-treatment side — three months before against two years after for the first patient, six weeks against sixteen months for the second — and they survive only in the note, as does the fact that each comparison is within-patient and unblinded. Arm and denominator are stated and correct (two single-patient studies, one patient each, verified in the paper's methods). |
| NEU-324 | The seizure reduction the claim reports has no magnitude, no timepoint and no treatment duration. The abstract supplies none of the three, so this is the limit of an abstract-only source rather than a dropped qualifier — but the chapter must not borrow the magnitude from NEU-038, which took it from a review. The design descriptor problem is in the detail block above. |

Checked and adequately specified: NEU-309 (variant count, validated positives, both
thresholds), NEU-323 (three multiples of the intended dose, 70 days, high-dose cohort named),
NEU-325 (both fractions with the 235 denominator), NEU-326 (26 of 36, the 4% exome yield, and
the 3.5-fold multiplier with the case counts behind it in the note), NEU-328 (11 of 11, 6 of
6), NEU-329 (weeks from the ninth dose, months from the final dose, the length of the pause —
all anchored), NEU-331 (age at first dose, dose and interval, three years, one patient,
expanded access), NEU-333 (532 patients, six years, 4.9%, and the split by ASO mechanism),
NEU-338 (173 applications at a stated cut-off date, 78, 57, and the 23-month median against an
18-month target with its eight-IND basis stated in the claim).

---

## Method and corpus notes

- Bodies were read with `cat --full` on `papers/<id>/content.lines`. A plain `cat` returns a
  truncated preview plus a usage hint that looks exactly like a short document — the first
  three dumps came back at 25 to 31 lines for documents of 101, 200 and 181 lines.
- Line labels match positions in all eighteen documents, including the FDA draft guidance,
  whose first line is labelled L1 — so the `L0` hazard in `SCHEMA.md` does not bite on
  NEU-337. The stray in-document line number inside that record's quote is byte-exact in the
  source, as its note says.
- `preprint: true` is correct on the six Smith and Kitzman records (NEU-304, 307, 310, 311,
  320, 321) even though the doc_id is a PMC id: that PMC record is the bioRxiv deposit — its
  own metadata gives bioRxiv as the journal and a 10.1101 DOI — while the records cite the
  published Genome Biology DOI, which is the arrangement `SCHEMA.md` prescribes. The other
  preprint flags all match their document's source, and no unflagged document is a preprint.
- DOIs, journals and years were checked against each document's metadata, and the one
  disagreement (NEU-312) was adjudicated against Crossref, which supports the record. One
  cosmetic difference remains: NEU-335 records "The American Journal of Human Genetics" where
  the metadata says "American Journal of Human Genetics".
- Tiers: every record uses a descriptive tier ("none of the three tiers applies; this is a
  method benchmark against measured splicing...", "tier: clinical outcome") except NEU-328 and
  NEU-330, which use tier 2, correctly, for minigene and patient-fibroblast oligonucleotide
  work with molecular readouts and no organismal phenotype. Per brief 1 a descriptive tier is
  what a methods-and-treatment block should carry, and each matches what its source did. No
  tier is wrong.
- Lead clauses I read and found supported, recorded so a later reviewer need not redo it:
  NEU-302, NEU-303, NEU-304, NEU-305, NEU-306 ("performs comparably", carried by the matched
  call-rate comparison), NEU-307, NEU-308 ("differ sharply", 15 percentage points on the cited
  line), NEU-311, NEU-314, NEU-316 (the two statistics genuinely come from one line, one
  variant set, one ground truth), NEU-319, NEU-320, NEU-322, NEU-323, NEU-325, NEU-326,
  NEU-327, NEU-328, NEU-330, NEU-332, NEU-333, NEU-334, NEU-335, NEU-336, NEU-337, NEU-338.
  Three I read and let stand with a caution rather than a verdict: NEU-301's "two tools that
  are routinely compared" is unanchored on the cited lines but is carried by the uncited line
  above them; NEU-309's "trades most of the sensitivity away" overstates a move from 75% to
  50%, which the same sentence then prints, so the claim corrects itself for any reader who
  finishes it; NEU-339's "the splice-modulating half of this field is thinner than the case
  reports suggest" generalises one organisation's portfolio to the field, which the claim's own
  attribution and the record's note both pull back.
