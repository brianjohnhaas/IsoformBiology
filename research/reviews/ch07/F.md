# Chapter 7 records review, block F: NEU-001 to NEU-038

Reviewer: claim records against their sources (AGENT-BRIEFS.md section 2).
Date: 2026-11-23.
Assignment: every id present in NEU-001..NEU-038 of `research/07-neuro-mendelian.yml`.
NEU-031 is absent, removed on 2026-11-23 together with NEU-221 per the file's trailing note;
NEU-039 and NEU-040 are likewise absent from the file.
**37 records checked. No record came back `cannot check`.**

Every cited document was dumped in full with `paperclip cat --full /papers/<id>/content.lines`
into `src/` in this directory, so every negative below was re-run inside the specific
document rather than across the corpus. All 25 documents resolved on the first attempt, so
none of the three named corpus quirks bit on this block: no `lookup` was needed, and no
corpus-wide `grep` negative is relied on anywhere in this report. (`paperclip cat` without a
range returns a section index, which is why `--full` was used throughout.)

## Conventions used here

- One verdict per record, the most severe, from the nine permitted strings only.
- A clause that is **correct in the paper but not on a line the record cites** leaves the
  verdict at `ok` and appears in the separate list in section 3.
- Defects in a `note:` have no string among the nine; they are reported in sections 4 and 5
  without changing the claim verdict. No tenth string invented.
- A missing tier is reported as a systematic gap (section 6), not as `tier wrong`.
- "Source says" describes what the lines support, in my own words, and is deliberately not
  a usable replacement sentence.

---

## 1. Verdict table

| record | verdict |
|---|---|
| NEU-001 | ok |
| NEU-002 | ok |
| NEU-003 | qualifier lost |
| NEU-004 | ok |
| NEU-005 | scope too wide |
| NEU-006 | qualifier lost |
| NEU-007 | ok |
| NEU-008 | ok |
| NEU-009 | ok |
| NEU-010 | ok |
| NEU-011 | ok |
| NEU-012 | ok |
| NEU-013 | ok |
| NEU-014 | ok |
| NEU-015 | ok |
| NEU-016 | ok |
| NEU-017 | ok |
| NEU-018 | ok |
| NEU-019 | ok |
| NEU-020 | ok |
| NEU-021 | ok |
| NEU-022 | ok |
| NEU-023 | ok |
| NEU-024 | ok |
| NEU-025 | qualifier lost |
| NEU-026 | ok |
| NEU-027 | ok |
| NEU-028 | ok |
| NEU-029 | ok |
| NEU-030 | ok |
| NEU-032 | ok |
| NEU-033 | ok |
| NEU-034 | ok |
| NEU-035 | qualifier lost |
| NEU-036 | ok |
| NEU-037 | ok |
| NEU-038 | ok |

Counts: **32 ok**, **4 qualifier lost**, **1 scope too wide**, 0 number wrong,
0 direction wrong, 0 proposal as finding, 0 source metadata wrong, 0 tier wrong,
0 cannot check.

### Source metadata

Checked field by field against each document's `meta.json`. Every record's `year` matches
the document's `pub_year`, every DOI matches, and every journal and title matches apart
from case and dash differences ("FTD–ALS" vs "FTD-ALS" at NEU-013; "Nature neuroscience"
vs "Nature Neuroscience" at NEU-006..009; "duchenne" vs "Duchenne" at NEU-021). Two
qualifications:

- **NEU-024's mismatch is deliberate and correct, not a defect.** The record's DOI
  (10.1126/science.adh7688), journal (Science) and year (2024) are the *published*
  version's and therefore cannot match the document read, which is the bioRxiv record
  `bio_cea1c1676f0e` (`pub_date` 2023-03-25, preprint DOI 10.1101/2023.03.25.534016).
  That is exactly the case `SCHEMA.md` requires `preprint: true` for; the flag is set and
  the note says so. I verified the note's one checkable assertion:
  `patowary2024neocortexisoforms` is listed in `research/ALLOCATION.md` at line 208.
  NEU-036 also carries `preprint: true`, and there the journal field is already "bioRxiv",
  so no note is needed.
- **The four abstract-only documents returned no `journal` or `authors` field** in
  `meta.json` (64751354, 46565666, 34980441 and 27235986 give only source, title, DOI,
  PMID and `pub_year`). Their journal names and bylines could be checked only against the
  DOI prefix and the record's own fields. That is why the overlaps in section 5 involving
  NEU-005, NEU-017, NEU-028 and NEU-037 are stated as name strings: they rest on the
  records' own `authors:` fields, not on corpus metadata.

Bibkeys shared with records elsewhere in this file are shared consistently -
`liu2008tauexon10` (file lines 20, 48, 71, 93, 1014, 1047, 1076),
`singh2020risdiplam`, `belancic2025smatrials`, `lim2017eteplirsen`, `moriyama2026dmdaso`
and `wiltonclark2024nof1aso` each resolve to one work within this file. I did not check
the other `research/*.yml` files, so this is not a statement about the duplicate-bibkey
gate.

---

## 2. Detail blocks for every row that is not `ok`

```
NEU-003  qualifier lost
  claim says: "raising or lowering SF2/ASF binding, so two neighbouring changes
    push exon 10 inclusion in opposite directions."
  source says: the cited line carries the N279K / delta-280K result and the opposite
    directions exactly, and then closes by restricting the SR-protein work it has
    just reported: it was all done in cultured cells, some observations contradict
    each other, and the review attributes the inconsistency to minigene size, cell
    type and endogenous splicing-factor levels. That closing sentence directly
    follows the "other SR proteins ... summarized in Table 1" sentence, so it reaches
    SF2/ASF through Table 1's own ASF (SRp30a) row at L32, which is the line's summary
    of the same work. Either way the claim states the mechanism with no cell-culture
    scope and no mention that the literature disagrees.
  lines read: PMC2483273 L28 (context L21-L28; Table 1 at L29-L40)
```

```
NEU-005  scope too wide
  claim says: "when it is depleted those exons enter mRNAs, frequently disrupting
    translation and triggering nonsense-mediated decay"
  source says: the abstract attributes that result to one system - TDP-43 depleted
    from mouse embryonic stem cells. The claim gives no species and no cell type, so
    a mouse ES-cell result reads as a general one. The repression-impaired-in-ALS-FTD
    half of the claim is on the line and is correctly hedged by the source's own
    "suggesting".
  lines read: 64751354 L1 (the whole record; abstract_only)
```

```
NEU-006  qualifier lost   [lowest severity of the five]
  claim says: "when TDP-43 levels fall, its binding to the first intron is lost"
  source says: the line reports lowered TDP-43 levels *reducing* its binding to sites
    (plural) within the first intron, not abolishing it, and the paper's discussion
    keeps that graded reading. "Lost" states a stronger lesion than the cited line
    supports.
  lines read: PMC6348009 L12 (context L47-L49)
```

```
NEU-025  qualifier lost
  claim says: "approximately 10 to 14 per cent of cancer exonic mutations"
  source says: both numbers are on the cited line with the same denominators, and the
    record correctly flags them as predicted rather than assayed. But the same line
    closes with the authors' own bound on the cancer figure: the cancer set contains a
    large proportion of passenger variants, which they say will almost certainly make
    the number a serious under-estimate of splicing-sensitive cancer *driver*
    mutations. That direction-bearing caveat is absent from the record, so the cancer
    figure reaches the writer as a symmetric estimate.
  lines read: PMC4054890 L182 (context L180-L183)
```

```
NEU-035  qualifier lost
  claim says: "on NF1 spliceogenic variants, SpliceAI reached an ROC area under the
    curve of 0.972 for de novo or cryptic splice site prediction"
  source says: the AUC, the 0.924 for SpliceRover and the non-significance of the gap
    are all on the cited line, exactly. The dataset is not. An ROC AUC needs both
    classes, and this study's positives are NF1 variants while its negatives are 64
    experimentally validated intronic BRCA variants; the authors call that two-gene
    design a possible source of selection bias, and note the positives come from a
    single gene chosen for its unusually high proportion of splice-affecting
    pathogenic variants. Scoping the benchmark to "NF1 spliceogenic variants" drops
    the other half of the comparison and the authors' own caveat. Minor related point:
    "every other tool tested" is seven tools, not eight - GeneSplicer was dropped
    before the comparison for a 24.7 per cent missing-score rate (HSF, at 6.90 per
    cent, was kept and is reported on the cited line).
  lines read: PMC9584665 L32 (dataset and caveat at L34; exclusion rule at L30)
```

---

## 3. Defect class 1: clauses correct in the paper but not on a line the record cites

**Lead finding for this class: zero numeric figures are off-line.** I enumerated every
number in all 37 claims and located each one on a cited line - the cohort sizes,
percentages, AUCs, Spearman rhos, counts, exon numbers and nucleotide positions alike.
**Every digit in this block sits on a line its record cites.** Nine of the ten entries
below are *descriptors* - species, platform, provenance, cohort label - and the tenth
(NEU-004) is a proportion whose denominator is ambiguous rather than a figure. None of the
ten should be tallied against the twenty-eight numeric cases found in another chapter's
block, which were a different kind of defect. Verdicts stay `ok` throughout.

**Firm (a distinct factual element, on no cited line) - six entries:**

1. **NEU-011** - "post-mortem". L115 says only "brain and spinal cord tissues". The samples
   are called postmortem in the methods at PMC8891020 **L185** ("Confirmed TDP-43 pathology
   postmortem was reported for all FTLD-TDP samples") and **L186** ("flash-frozen postmortem
   tissue"); both lines read in full.
2. **NEU-016** - "Both approved splicing-directed SMA drugs act on the same exon." Neither
   cited line says risdiplam acts on exon 7. The statement is at PMC7691903 **L10**, where
   both approved splicing-modulating compounds are tied to strengthening the 5' splice site
   of SMN2 exon 7. L10 is cited by NEU-015, not by NEU-016.
3. **NEU-018** - "infants with type 1 SMA". L31 gives only "FIREFISH Part 1, which enrolled
   21 infants"; the Type 1 diagnosis and the two-SMN2-copy criterion are at PMC12383623
   **L30** and **L32**.
4. **NEU-026** - "drawn from HGMD". L31 says "4,964 single point mutations"; the HGMD
   provenance is at PMC6679692 **L17** and **L36**.
5. **NEU-034** - "PacBio". L55 says only "LR RNA-seq"; PacBio is named at PMC13247170
   **L10** and **L16**.
6. **NEU-004** - "most such mutations push toward 4R, a minority toward 3R", read with its
   nearest antecedent, the silent and intronic mutations. **Both readings come out `ok`,
   but on different lines, and the record does not say which it means.** On the cited L88
   the majority is over *all* disease-causing tau mutations, and three of the five mutations
   L88 names as pushing to 3R (L266V, G272V, delta-280K) are coding changes, not silent or
   intronic ones. For the narrower silent-and-intronic denominator the statement is still
   true, but it rests on Table 2 at PMC2483273 **L48-L87**, which I counted: nine silent or
   intronic mutations increase exon 10 inclusion (L284L, N296N, S305S, E10+3, E10+11,
   E10+12, E10+13, E10+14, E10+16) against three that decrease it (E9+33, E10+19, E10+29),
   with L315L blank. Flagged because the writer will pick one denominator and the record
   does not fix it.

**Borderline (the cited line carries the sense; the exact element is elsewhere) - four
entries:**

7. **NEU-032** - "exome-undiagnosed". L24's opening sentence frames exome non-diagnosis;
   the word "undiagnosed" attached to the 5-of-48 is at PMC5499207 **L45** (read in full).
8. **NEU-021** - the four approved drugs being *antisense oligonucleotides*. L26 says
   "four FDA-approved exon-skipping therapies"; the ASO identity, the exons (45, 51, 53)
   and the roughly 27 per cent patient eligibility are at PMC13290086 **L24**.
9. **NEU-014** - "targeted long-read RNA sequencing". L50 names the assay only as
   TEQUILA-seq and says "gene panel-wide analysis"; the phrase "targeted long-read RNA-seq"
   is at PMC13082330 **L22** and **L27** (and again at L60-L63).
10. **NEU-022** - "genomically aligned EST evidence". L19 says "EST-based analyses"; the
    alignment and sampling design is at PMC545594 **L17-L18**.

**One derived figure, not a quotation from any line.** NEU-030's "disagree by more than
twofold" is the record's own arithmetic over the four percentages on L55 (17 and 43 give
about 2.5x). The four percentages are all on the cited line; the comparison is not stated
there in any form. Correct, but it is the record's calculation and the writer should know
no sentence in the paper says it.

---

## 4. Defect class 4: the sentence the same passage closes on

**Five records take one half of a cited line and drop what the same line goes on to say.**
Two of the five are the basis of a verdict in section 2 (NEU-003, NEU-025). One (NEU-005)
is a verdict row for a different reason. **Two leave the verdict at `ok`** but change how
the writer would present the result.

- **NEU-003** (verdict reason). L28 closes on the cultured-cell and contradictory-results
  restriction covering the SF2/ASF work the record uses.
- **NEU-021** (verdict `ok`). The record takes the limitation half of L26 - accelerated
  approvals resting on a biomarker, significant debate - and drops the same line's own
  positive clause, that establishing proof of concept for ASO-mediated dystrophin
  restoration led to the FDA approvals and brought hope to eligible patients and to people
  with other intractable genetic disease. The omitted clause *precedes* the quoted one on
  the line.
- **NEU-025** (verdict reason). L182 closes on the passenger-variant under-estimate.
- **NEU-018** (verdict `ok`; the omission runs the other way, favourable half kept). The
  record takes the efficacy half of L31 - 41 per cent sitting at 12 months - and drops the
  same line's closing sentences: three patients died during treatment and one more died 3.5
  months after discontinuation. L31 also carries 59 per cent sitting at 24 months and 90
  per cent alive and ventilation-free at 12 months, so the record has selected within the
  line as well as truncated it.
- **NEU-005** (verdict `scope too wide` for a different reason; omission also favourable).
  The abstract's own rescue result - enforced repression of cryptic exons prevented cell
  death in TDP-43-deficient cells - is the strongest thing on the line and is recorded
  nowhere in this block.

**One adjacent-line case, not a class-4 instance.** NEU-030 uses L55 in full and fairly,
but the discussion continues at L56 to say the non-canonical contribution estimate is
likely a lower bound and the 35-40 per cent under-ascertainment may be conservative. L56
is not cited, so this is information for the writer rather than a defect in the record.

---

## 5. Defect classes 2 and 3: the notes

### Class 2, notes asserting absence where the thing is present: none found

The block contains only **four** `note:` fields in 37 records. Three are identical
housekeeping notes recording that an eight-word span was removed from a claim (NEU-023,
NEU-028, NEU-037). The fourth is NEU-024's preprint note, whose one checkable assertion
holds (see section 1). No note in this block asserts that a paper does not report
something, so there is nothing of this class to find here.

### Class 3, independence notes wrong or inverted: none found, because the block has no independence note at all

**No record in NEU-001..NEU-038 carries an independence statement**, so no such note can be
wrong or inverted. What I did instead was recompute the overlaps from the records' own
`authors:` fields and then test, by grep over the whole 11,233-line file, whether anything
records them. **Scope of that search:** I grepped the file untruncated for every reference
to an id in the range (`NEU-0[0-3][0-9]` outside `- id:` lines) and for the six surnames
that matter (Yokota, Jaganathan, Prokisch, Gagneur, McRae, Farh), and read the notes the
hits landed in. I did not re-read every independence note in the file, so each "recorded
nowhere" below is scoped to what that search covers.

**A. NEU-032 (Kremer 2017) and NEU-033 (Yépez 2022) are one consortium. Neither record
carries it, and no note found by this search states it.** Fourteen surnames with matching
initials are on both bylines: Kopajtich, Mertes, Terrile, Schwarzmayr, Strom, Meitinger,
Gagneur, Prokisch, Mayr, Rötig, Taylor, Ghezzi, Distelmaier, Freisinger. Both documents
are full text, so these **share authors**, not merely name strings. Nothing links the
10-per-cent-of-48 yield to the 16-per-cent-of-205 yield as one group's work, even though
NEU-033's own claim already says "the same approach". The string "NEU-032" appears nowhere
in the file outside its own `- id:` line. Several later records do cite the Kremer document
PMC5499207 (file lines 7150, 7545, 7586) and several flag same-group relations *to* NEU-033
(lines 7103, 7280, 7647) - I read those notes - but none of them states that Kremer and
Yépez are the same group. The nearest thing, at line 6871, is a same-group statement naming
Kremer about a *different* paper (a PMC7822922 reanalysis). **This is the most load-bearing
unrecorded overlap in the block.**

**B. NEU-036 is the SpliceAI authors benchmarking their own successor against their own
earlier model. Recorded in the file, but not on either record.** NEU-028 (SpliceAI,
abstract-only) and NEU-036 (SpliceAI2 preprint) have four matching name strings including
first and last author: Jaganathan K., Farh K.K.-H., McRae J.F., Sanders S.J. Because
NEU-028 is `abstract_only` and its `meta.json` carries no author list, this is stated as
**shares a name string with**, not as a verified laboratory. The Spearman 0.59-versus-0.55
comparison in NEU-036 is therefore a self-comparison. A later record says so in its own
note, at file lines 7944-7946: "the authors are the SpliceAI team (Jaganathan, Farh and
colleagues, as at NEU-028), so SpliceAI2's comparisons against SpliceAI are a group
assessing its own earlier model. Existing record NEU-036 cites the same document at L8."
Neither NEU-028 nor NEU-036 carries it. (A separate note at file lines 7820-7822 also says
"the two tools' developers are not independent", but I read it: that record is the Pangolin
paper PMC9022248, so it is about Pangolin and SpliceAI, a different pair.)

**C. Three records share an author, and no note found by this search mentions it.**
Yokota, T. is on NEU-020 (Lim 2017), NEU-021 (Moriyama 2026) and NEU-038 (Wilton-Clark
2024). All three documents are full text, so these **share an author**. The three records
carry, respectively, the Becker-phenotype rationale for exon skipping, the
four-approvals-resting-on-a-biomarker verdict, and the milasen clinical outcome - three
different places in the chapter's argument, one recurring byline. The surname grep over the
whole file found "Yokota" only inside `authors:` fields, never in a note.

**D. The competing "how much of disease is splicing" estimates are not all independent;
not recorded for this pair.** NEU-028 (Jaganathan 2019, 9-11 per cent) and NEU-029/NEU-030
(Lord 2019, 27 per cent non-canonical) have the matching name string McRae, J. F.; NEU-036
has it too. NEU-028 is abstract-only, so again **shares a name string with**. This matters
because NEU-025's own `figure_idea` proposes putting these estimates on one axis, and such
a figure would imply four independent attempts at one question. A later record does state a
Lord relation (file line 8223: "The first author Lord, J. also authored the splice-region
constraint paper recorded at NEU-029 and NEU-030, so these are not independent groups"),
but I read it and it concerns that record's own preprint, not NEU-028. Nothing connects
NEU-028 to NEU-029/NEU-030.

**E. Lower weight.** NEU-006..NEU-009 (Melamed 2019) and NEU-010..NEU-012 (Brown 2022)
have the matching name string Ravits, J., whose appearance on the Brown byline is via the
NYGC ALS Consortium membership list rather than as a bench contributor. Melamed also shares
the name string Bennett, C. F. with NEU-017 (ENDEAR, abstract-only), which bears on nothing
either record claims. Worth a line, not worth a caveat.

**F. The one pair that looks independent shares its sample resource. Confirmed by
reading.** NEU-010/011/012 (Brown 2022) and NEU-013 (Ma 2022) **share no author**: the only
common surname is Miller, and the initials differ (Miller, T. M. on Brown; Miller, G. on
Ma). Both documents are full text and both carry `pub_date` 2022-02-23. But the byline is
not the whole question, and the data overlap. I read PMC8891019 **L30** and **L78** in
full: Ma downloaded the **NYGC ALS Consortium** RNA-seq from GEO (GSE137810, GSE124439,
GSE116622, GSE153960), took the 1,658 quality-controlled samples, filtered them to 1,151
tissue samples from 413 individuals suitable for UNC13A splice-variant analysis, and
derived from that set the result that the cryptic exon appears in about half of
FTLD-TDP cortical tissues and in none of the FTLD-FUS (n = 9), FTLD-TAU (n = 18),
ALS-SOD1 (n = 22) or control (n = 197) samples. Brown's NEU-011 claim is 1,349 tissues from
377 individuals from that **same consortium resource** (PMC8891020 L115, L185). The two
sample sets are differently filtered, not identical - 1,151 of 1,658 against 1,349 - but
they come from one resource, and the two papers' population-level specificity findings are
therefore not independent observations. Ma's genuinely separate material is a 117-sample
Mayo Clinic Brain Bank series (L30-L31). NEU-013's verdict is unaffected: the record cites
only the abstract-level statement at L19.

---

## 6. Systematic findings about the block as a whole

1. **No record in NEU-001..NEU-038 declares an evidence tier.** `grep -c "tier:"` returns
   **0** for this block and **268** for the whole file. Nothing here can be scored against
   brief 1's three tier strings or against a descriptive tier, and a later reviewer asked to
   check tiers in this block will find no field to check. Many of these records would need a
   descriptive tier rather than one of the three biology strings - NEU-014, NEU-022,
   NEU-025 to NEU-030 and NEU-032 to NEU-036 are method, annotation or prediction records
   with no isoform to perturb - which is probably why the field was skipped. But the gap is
   uniform and total, and it is the largest structural difference between this block and the
   rest of the file. Later records use descriptive tiers for exactly this kind of source
   ("tier: none of the three tiers applies; this is a method benchmark against measured
   splicing", file line 8226; "tier: cohort measurement of assay performance", line 7107),
   so the convention exists and this block does not use it.
2. **Eleven of the 37 records cite a review for a primary finding**, which
   `CONTRIBUTING.md` line 147 forbids ("Reviews may be cited as reviews ... Do not cite a
   review for a primary finding"). I confirmed each document self-labels: PMC2483273 carries
   a bare "Review" line at L7, PMC7691903 at L6, PMC5338848 at L7, PMC12383623 at L9,
   PMC11275492 at L7, and PMC13290086 calls itself "this review" on the cited L26. The
   eleven records are NEU-001 to NEU-004 (Liu & Gong 2008, whose cited lines attribute the
   ~1 ratio to refs 8 and 20, the eleven stem-loop mutations to ref 35 and the SF2/ASF
   result to ref 45); NEU-015, NEU-016 (Singh 2020); NEU-018, NEU-019 (Belančić 2025, whose
   FIREFISH numbers on L31 are attributed to refs 15 and 16); NEU-020 (Lim 2017); NEU-021
   (Moriyama 2026); NEU-038 (Wilton-Clark 2024, whose milasen outcome on L24 is attributed
   to ref 34 throughout). I have **not** called any of these `proposal as finding`, because
   in each case the claim states the biology rather than crediting the cited authors with
   the discovery, and for NEU-038 the review is the only source in the corpus for the facts
   claimed - the brain-volume loss and the death are absent from the NEJM abstract at
   27235986 L1.
   **Already flagged in the file:** its own leads and later notes raise the secondhand
   sourcing of NEU-018, NEU-019 and NEU-038 (file lines 8586, 10860-10861, 11002) and the
   unbounded rule at NEU-020 (line 4815). **No flag found by this search** for the review
   status of the other seven claims, which rest on three reviews: NEU-001 to NEU-004 on
   Liu & Gong 2008, NEU-015 and NEU-016 on Singh 2020, NEU-021 on Moriyama 2026. Two of
   those records are commented on by later records for other reasons without the review
   issue being raised (line 3564 on NEU-015's framing of C6U, line 3639 on NEU-016 carrying
   the ISS-N1-to-nusinersen link). The convention for handling it does exist in this file:
   a NEU-1xx record citing the *same* Liu & Gong document opens its note "Review, cited as a
   review: both the Pick 4R observation and the PSP and corticobasal statements rest on a
   single reference in this review (its [63]), which was not read" (file line 1024). NEU-027
   is the other model, recording the one-third figure explicitly as the authors' summary of
   previous studies and saying it should not be counted as an independent estimate.
3. **Denominator caveats that sit one line away from a cited line.** Not defects, but each
   bounds a number the writer will use. NEU-022's "more than 40 per cent of genes" is 40 per
   cent of genes with at least 20 tissue-derived ESTs, sampled at 20 ESTs each (PMC545594
   L18), not of all expressed brain genes. NEU-026's ~10 per cent is over a panel restricted
   to internal exons of 100 nucleotides or fewer, which the authors say leaves half of human
   exons inaccessible to the assay (PMC6679692 L32, L36).
4. **One arithmetic gap.** NEU-034 accounts for 18 + 3 + 4 = 25 of the 27 outcomes on
   PMC13247170 L55. The fourth category on that line - two splicing events supported by a
   low number of reads - is not in the record, so the categories do not sum to 27 and a
   writer reconstructing the table will come up two short.
5. **Two minor readings, both left at `ok`.** NEU-002 states the exon 10 / intron 10 stem
   loop as a structure; the cited L23 infers it from self-complementarity ("suggesting the
   presence of a stem loop"), though the Figure 2 legend at L22 asserts it outright, which
   is why this is not `proposal as finding`. NEU-015 records the 3' splice-site weakening as
   the proposal for C6U, correctly hedged with "proposed", but the same line lists three
   further proposed mechanisms (enhancer abrogation, silencer creation, a strengthened
   extended inhibitory context), so "the" proposal is one of several. A later record in the
   file (line 3564) independently calls NEU-015's framing "a third and weaker framing that
   neither of these two papers uses".

---

## 7. What was read

Lines listed as read were opened and read in the dumped document, not taken from a grep or
`map` summary. Where a class-1 pointer rests on a within-document grep rather than a full
read, the table says so.

| document | record(s) | lines read |
|---|---|---|
| PMC2483273 | NEU-001..004 | L1-L40, L44-L92 (Table 2 counted at L48-L87) |
| 64751354 | NEU-005 | L1 (whole record) |
| PMC6348009 | NEU-006..009 | L10-L13, L35-L39, L43-L51 |
| PMC8891020 | NEU-010..012 | L100-L104, L113-L116, L122-L124, L185-L189 |
| PMC8891019 | NEU-013 | L17-L21, L30, L31, L78 |
| PMC13082330 | NEU-014 | L48-L52; L22 and L27 by within-document grep |
| PMC7691903 | NEU-015, 016 | L4-L15 |
| 46565666 | NEU-017 | L1 (whole record) |
| PMC12383623 | NEU-018, 019 | L28-L32 |
| PMC5338848 | NEU-020 | L16-L20 |
| PMC13290086 | NEU-021 | L24-L27 |
| PMC545594 | NEU-022 | L17-L21 |
| PMC10063607 | NEU-023 | L10-L12 |
| bio_cea1c1676f0e | NEU-024 | L30-L32 |
| PMC4054890 | NEU-025 | L180-L184 |
| PMC6679692 | NEU-026, 027 | L10-L12, L30-L32; L17 and L36 by within-document grep |
| 34980441 | NEU-028 | L1 (whole record) |
| PMC6360807 | NEU-029, 030 | L20-L22, L54-L56 |
| PMC5499207 | NEU-032 | L23-L25, L45 |
| PMC8981716 | NEU-033 | L43-L47 |
| PMC13247170 | NEU-034 | L53-L57; L10 and L16 by within-document grep |
| PMC9584665 | NEU-035 | L30-L34 |
| bio_6f0a212282bb | NEU-036 | L6-L9 |
| 27235986 | NEU-037 | L1 (whole record) |
| PMC11275492 | NEU-038 | L22-L26 |

All four abstract-only records (NEU-005, NEU-017, NEU-028, NEU-037) have their full
abstract at L1, and every clause of NEU-017, NEU-028 and NEU-037 is on that line, which is
why none of them is `cannot check`.

Notes read inside `research/07-neuro-mendelian.yml` while testing the "recorded nowhere"
claims in section 5: file lines 1018-1028, 3560-3568, 3634-3642, 6865-6875, 7095-7108,
7150-7175, 7545-7552, 7586-7612, 7640-7652, 7818-7824, 7944-7946, 8218-8226, 10886-10894,
11558 onward (the trailing removal note). The repository was not modified.
