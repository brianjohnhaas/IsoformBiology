# Records review, block H: NEU-341 to NEU-379, NEU-381 to NEU-389

Reviewer: records-vs-sources, chapter 7 pass. 48 records.
File reviewed: `/home/unix/bhaas/projects/GITHUB/MDL/IsoformBiology/research/07-neuro-mendelian.yml`
Chapter prose not read. No replacement sentences given anywhere below.

## Reporting convention

The verdict column follows the **claim**, the **source metadata** and the **tier** only.
Defects that live in a `note:` field (an absence asserted where the thing is present, a
wrong independence statement, a wrong number inside a note) do **not** move the verdict,
because the claim itself is sound; they are reported in their own numbered sections
below with the same three-line block. Numbers and facts that are right in the source but
do not sit on a line the record cites are in section 5 and also leave the verdict at `ok`.

Every cited document was opened at its cited lines and read with context. All five
abstract-only records were checked for a full-text counterpart in the corpus by
`sql ... ILIKE` on title and by DOI; none exists, so `text_access: abstract_only` is
correct on all five and the "cannot read beyond the abstract" notes are sound.

## 1. Verdict table

| record | verdict |
|---|---|
| NEU-341 | tier wrong |
| NEU-342 | ok |
| NEU-343 | qualifier lost |
| NEU-344 | ok |
| NEU-345 | ok |
| NEU-346 | scope too wide |
| NEU-347 | ok |
| NEU-348 | ok |
| NEU-349 | ok |
| NEU-350 | ok |
| NEU-351 | ok |
| NEU-352 | ok |
| NEU-353 | ok |
| NEU-354 | scope too wide |
| NEU-355 | ok |
| NEU-356 | ok |
| NEU-357 | ok |
| NEU-358 | ok |
| NEU-359 | ok |
| NEU-360 | ok |
| NEU-361 | scope too wide |
| NEU-362 | ok |
| NEU-363 | ok |
| NEU-364 | ok |
| NEU-365 | ok |
| NEU-366 | ok |
| NEU-367 | ok |
| NEU-368 | ok |
| NEU-369 | ok |
| NEU-370 | ok |
| NEU-371 | ok |
| NEU-372 | ok |
| NEU-373 | ok |
| NEU-374 | ok |
| NEU-375 | ok |
| NEU-376 | ok |
| NEU-377 | ok |
| NEU-378 | ok |
| NEU-379 | ok |
| NEU-381 | ok |
| NEU-382 | scope too wide |
| NEU-383 | ok |
| NEU-384 | ok |
| NEU-385 | number wrong |
| NEU-386 | ok |
| NEU-387 | ok |
| NEU-388 | ok |
| NEU-389 | ok |

41 `ok`, 7 not `ok`.

## 2. Detail blocks for every row that is not `ok`

```
NEU-341  tier wrong
  claim says: "tier: isoform-specific perturbation with phenotype. The perturbation is
    the patient variant and the phenotype is developmental and epileptic encephalopathy."
    (note field)
  source says: the abstract reports seven likely pathogenic non-coding variants and
    "evidence that five of these variants promote inclusion of a 'poison' exon that leads
    to reduced amounts of full-length SCN1A protein". The only outcome measured against
    the variant is exon inclusion and protein amount. Developmental and epileptic
    encephalopathy is the condition by which the patients were ascertained, not an
    outcome measured as a consequence of an isoform-specific intervention, and the
    abstract reports no genotype-to-phenotype experiment. The claim text itself is
    faithful to the abstract; it is the tier string that asserts an organismal phenotype
    where only protein was measured. NEU-346 is the record in this block that does carry
    a measured organismal phenotype (premature mortality, seizures, hyperactivity).
  lines read: 35605822 L1 (whole abstract; abstract-only record, no full text in corpus)
```

```
NEU-343  qualifier lost
  claim says: "the non-coding exon and its flanking intronic sequence are 96 per cent
    identical between human and mouse"
  source says: "the non-coding exon and flanking intronic sequences are 96% conserved
    between human and mouse". The figure comes out of a conservation-score analysis
    (L44 states the companion genome-wide figure was "calculated based on conservation
    scores >=0.8"), not out of a percent-identity alignment. The record's own sibling
    NEU-348 correctly writes "identical" because its source (PMC7790302 L51) does say
    "37.5% identical". The switch from conserved to identical is therefore a lost
    qualifier, not house style. Everything else in NEU-343 is exact on L44, including
    human exon 20x / mouse exon 21x and the ~16 per cent genome-wide figure.
  lines read: PMC7347940 L44
```

```
NEU-346  scope too wide
  claim says: "An independent group built the human lesion into a mouse"
  source says: independent of Lim 2020 and of the company, yes; independent of the paper
    that discovered the mechanism, no. The cited line itself reads "we recently identified
    several disease-associated SCN1A mutations in intron 20" - those authors describe the
    2018 discovery (the source of NEU-341) as their own work. Recomputing from the two
    records' bylines, PMC7790302 and 35605822 share four name strings: Cochran, J. N.;
    Myers, R. M.; Cooper, G. M.; Barsh, G. S. Barsh is last on the 2021 byline and also
    appears on the 2018 one. 35605822 is abstract-only and has no authors field in the
    corpus, so the right wording is "shares name strings with", not "shares an author
    with". The measured content of the claim (~50 per cent reduction in brain Scn1a mRNA
    and Nav1.1 protein, premature mortality, seizures, hyperactivity, ~1 per cent 20N
    inclusion in adult wild-type brain, ~5-fold higher in the knock-in) is exact on L9.
  lines read: PMC7790302 L9; bylines of NEU-341 and NEU-346 in the yml
```

```
NEU-354  scope too wide
  claim says: "A laboratory with no connection to the sponsor reproduced the target
    engagement as an incidental control"
  source says: the molecular result is exact on L56 (STK-135 by intracerebroventricular
    injection at P2, brain harvested five days later, improved productive Scn1a splicing
    and expression, no effect on Syngap1 splicing or mRNA). The independence assertion is
    not supported by the document. A within-document grep for "Stoke" returns no matches,
    the corpus text carries no competing-interests or funding declaration, and the paper
    uses two of the sponsor's proprietary oligonucleotides - STK-135 as a positive control
    (L56) and STK-071 as a comparator (L44, L46, L48). The affiliation lines are all
    Pennsylvania and Children's Hospital of Philadelphia (L4-L9) and there is no byline
    overlap with Lim 2020 or with the mouse study at NEU-349, so "no shared author" holds;
    "no connection to the sponsor" does not follow from that and is contradicted in spirit
    by this block's own NEU-370 note, which says the same paper is "NOT a blind
    convergence".
  lines read: PMC10164156 L4-L9, L44, L46, L48, L56; within-document grep for "Stoke"
```

```
NEU-361  scope too wide
  claim says: "seizure frequency by paper diary and a caregiver global impression of
    change, all from screening to six months after dosing"
  source says: the registered time frames differ by measure. Safety and tolerability
    (L9) and seizure frequency (L12) run from "Screening (Day -28) until 6 months after
    single and multiple drug dosing". Plasma pharmacokinetics (L10) and cerebrospinal
    fluid exposure (L11) run from "Day 1 (Dosing)". The caregiver global impression of
    change (L13) runs from "Baseline (Day -1)". "All from screening" is therefore right
    for two of the five measures the claim lists and wrong for three. The design facts
    (non-randomised, sequential, masking none, phase 1/2, actual enrolment 62) are exact
    on L7.
  lines read: NCT04442295 L7, L9, L10, L11, L12, L13 (and L2 for the completion date)
```

```
NEU-382  scope too wide
  claim says: "The Japanese registration of the same phase 3 trial is the one record that
    separates the endpoints"
  source says: the Japanese registration does separate them, and does so structurally -
    L5 sits in the record's `primary_outcome` section and L6 in `secondary_outcome`, which
    I confirmed by listing `/trials/tri_6f267a56f74d/sections/` and reading
    `primary_outcome.lines`. The uniqueness assertion is false. NCT06872125 L5, the
    Detailed Description of the ClinicalTrials.gov record for the same trial, states in
    its own words: "The primary endpoint is the change from baseline in major motor
    seizure frequency. Secondary endpoints include the change in behavior and cognition,
    clinical status, and health-related quality of life in patients with Dravet syndrome."
    The endpoint content of NEU-382's claim (seizure reduction at week 28 by seizure diary
    as primary; seizure reduction at week 52 and the two Vineland-3 measures at week 52 as
    secondary) is exact on L5 and L6.
  lines read: tri_6f267a56f74d L5, L6, plus sections/primary_outcome.lines;
    NCT06872125 L5
```

```
NEU-385  number wrong
  claim says: "together with plasma pharmacokinetics and cerebrospinal fluid exposure of
    STK-001 by hybridisation ELISA over the same window"
  source says: the window named earlier in the same sentence is "from screening at day
    minus 28", which is correct for the safety and tolerability measure. L5 item 2 gives
    plasma pharmacokinetics "from day 1 (dosing) until 6 months after multiple drug
    dosing" and item 3 gives cerebrospinal fluid exposure "from day 1 (dosing) until 6
    months after multiple drug dosing". The hybridisation ELISA assay, the five safety
    sub-measures and the whole secondary list on L6 (seizure diary, caregiver and
    clinician global impression of change, EQ-5D-Y) are exact. The structural primary /
    secondary labelling the note relies on is real: L5 is the record's primary_outcome
    section, L6 its secondary_outcome section.
  lines read: tri_38bd136803ad L5, L6
```

## 3. Notes that assert absence where the thing is present

Four. All four point at the same blind spot: nobody read the Detailed Description or the
Interventions block of NCT06872125, and nobody read the superseded block on LONGWING L5.

```
NEU-360  (claim ok; note defect)
  note says: "The record lists four outcome measures in one Planned_Outcomes section
    WITHOUT labelling any of them primary or secondary, so the chapter must not call the
    seizure endpoint the primary endpoint on this source. A review in the corpus does call
    it the primary endpoint, which is a restatement and not the registry's own wording."
  source says: the first half is true - `/trials/NCT06872125/sections/` has a single
    `Planned_Outcomes.lines` and L9-L12 carry no primary/secondary labels. The conclusion
    is false. L5 of the same record states "The primary endpoint is the change from
    baseline in major motor seizure frequency. Secondary endpoints include the change in
    behavior and cognition, clinical status, and health-related quality of life".
    So the registry record does establish which endpoint is primary, and the review at
    PMC12989007 L76 is reproducing the registry's own wording almost verbatim rather than
    adding a restatement. The chapter may call it the primary endpoint on this source.
  lines read: NCT06872125 L5, L9-L12; sections listing; PMC12989007 L76
```

```
NEU-381  (claim ok; note defect, two parts)
  note says: "the two agree on the week 28 and week 52 structure" and "this record does
    NOT establish which is primary; NEU-382 does, from the Japanese registration"
  source says: on the first part, the CTIS entry's only time structure is "at each visit
    from Week 16 to Week 52 (consisting of nine 4 week intervals)" for the seizure
    endpoint and "at Week 52" for the two Vineland-3 endpoints. Week 28 appears nowhere
    on tri_0dafb76e2f13. The ClinicalTrials.gov record's seizure measures are time-framed
    Week 28 (L9) and Week 52 (L10). The two records are compatible but they do not "agree
    on the week 28 and week 52 structure"; only one of them has a week 28.
    On the second part, it is true that this three-line CTIS entry does not separate
    primary from secondary, but the inference that NEU-382 is therefore needed to
    establish it is wrong for the reason given under NEU-360.
    The claim text is exact on L3, including the unit (number per 28 days), the comparator
    (as compared with sham) and the nine consecutive four-week intervals, and the note's
    account of where the Stoke attribution comes from is correct: 2024-519555-28 appears
    as a EUDRACT_NUMBER secondary identifier on NCT06872125 L1, whose organisation field
    names that company.
  lines read: tri_0dafb76e2f13 L1-L3; NCT06872125 L1, L9, L10
```

```
NEU-383  (claim ok; note defect)
  note says: "It also supplies the eight-week baseline period, which the
    ClinicalTrials.gov record does not state."
  source says: NCT06872125 L8, the Interventions block, reads "Zorevunersen group will
    receive study drug by intrathecal (IT) administration on Day 1 (after the 8-week
    Baseline Period), Day 57 (Week 8), Day 169 (Week 24), and Day 281 (Week 40) at a dose
    level of 70 mg on Day 1 and Day 57, and 45 mg on Day 169 and Day 281." The eight-week
    baseline period is on the ClinicalTrials.gov record, in the same sentence as the
    dosing schedule, and that sentence is word-for-word the one the Japanese record
    carries at its L1. The rest of the note holds: the ClinicalTrials.gov record really
    does say only that the sham group "will have a procedure intended to mimic the drug
    administration", whereas the Japanese record says "Sham group will have a lumbar
    puncture with CSF withdrawal", so the lumbar-puncture detail is genuinely unique to
    the Japanese record. NEU-383's claim is exact on L1.
  lines read: tri_6f267a56f74d L1; NCT06872125 L8
```

```
NEU-389  (claim ok; note defect)
  note says: "The locomotor questionnaire and the immunogenicity measure appear in the
    current primary set and NOT in the superseded block printed below it on the same line,
    so the primary outcomes were widened after the study opened."
  source says: the superseded block on L5 ("Previous primary outcome measures") does
    contain the immunogenicity measure, as item 1.5, in the same wording as the current
    set: "Incidence of immunogenicity (anti-drug antibodies) measured using a validated
    assay in serum". The only item that is in the current primary set and absent from the
    superseded one is 1.6, the Gillette Functional Assessment Questionnaire locomotor
    measure. The note's conclusion that the primary set was widened therefore survives,
    but only on the locomotor questionnaire; it is wrong about immunogenicity. The note's
    other assertion, that neither the Vineland-3 nor any cognitive measure is a registered
    outcome of this extension, is correct - a within-document grep for "Vineland" on
    tri_26fa4417684d returns zero matches. The claim itself is exact on L5 and L6, and the
    structural primary/secondary labelling it relies on is real.
  lines read: tri_26fa4417684d L5, L6; within-document grep for "Vineland" and
    "immunogenicity"
```

## 4. Independence statements, recomputed from the bylines

```
NEU-346  (also carried as a verdict row above)
  note says: "This laboratory (Alabama at Birmingham and HudsonAlpha) shares no author
    with Lim 2020 or with the trial sponsor, so it is the independent anchor for the
    mechanism; the 2018 paper recorded at NEU-341 came from a third group again (Carvill,
    Northwestern)"
  source says: the first clause is correct - no name string of PMC7790302 appears on the
    Lim 2020 byline. The second clause is inverted. NEU-341 and NEU-346 share four name
    strings (Cochran, J. N.; Myers, R. M.; Cooper, G. M.; Barsh, G. S.), and PMC7790302
    L9 calls the 2018 finding "we recently identified". The 2018 paper is not a third
    group; it is a large consortium byline that includes the HudsonAlpha and Barsh
    authors who are also on the 2021 mouse paper. Because 35605822 is abstract-only and
    the corpus holds no authors field for it, the chapter should say "shares a name string
    with", not "shares an author with".
  lines read: PMC7790302 L9; 35605822 meta.json (no authors field); the two yml bylines
```

```
NEU-368  (claim ok; note defect, a number inside a note)
  note says: "Fourteen of the twenty-one authors are at Stoke Therapeutics, sharing four
    authors with NEU-342"
  source says: the overlap with NEU-342 is five name strings, not four: Venkatesh, A.;
    Kach, J.; Lim, K. H.; Aznarez, I.; Liau, G. The "fourteen of twenty-one" split cannot
    be verified from the corpus at all - PMC11564677 lists exactly two affiliations, L4
    "Stoke Therapeutics, Bedford, Massachusetts, USA" and L5 "Ophthalmic Genetics and
    Visual Function Branch, National Eye Institute, National Institutes of Health", with
    no per-author mapping in the text and `author_details` null in meta.json. Only three
    authors on the byline are identifiable as National Eye Institute people by name
    (Huryn, Li, Hufnagel), which would make the split eighteen and three, not fourteen and
    seven. The note's conclusion - same programme, not an independent replication - is
    correct and is independently supported by the five shared name strings.
  lines read: PMC11564677 L3, L4, L5, meta.json author_details; NEU-342 byline
```

```
NEU-372  (claim ok; note defect)
  note says: "Senior author Carvill is also the senior author of NEU-341, so the discovery
    of the first exon and of the other two are the same laboratory and not independent."
  source says: the conclusion is right and is in fact understated. Carvill, G. L. is last
    (senior) on the NEU-372 byline but **first** on the byline recorded for NEU-341, so
    "senior author of NEU-341" is wrong against the record's own author field. Two further
    name strings are shared and the note does not mention them: Stamberger, H. and
    Weckhuysen, S. appear on both bylines. Three shared name strings, not one.
  lines read: the two yml bylines
```

```
NEU-349  (claim ok; independence note missing entirely)
  note says: nothing about shared authorship. The note's emphasis is that the paper is
    abstract-only.
  source says: NEU-349 shares four name strings with NEU-342 (Han, Z.; Ji, S.;
    Aznarez, I.; Liau, G.) and a fifth, Lin, Q., with NEU-368. The commentary that
    NEU-350 to NEU-352 rest on says so outright at PMC7863313 L13: "Lori Isom's group at
    University of Michigan teamed up with Stoke Therapeutics". The record the chapter will
    read as "the decisive animal result" is a sponsor co-authored study, and no note on it
    says so, while the two records either side of it (NEU-346, NEU-354) both carry
    explicit independence statements. This is the gap most likely to turn into a sentence
    about independent corroboration in the chapter.
  lines read: PMC7863313 L13; the NEU-342, NEU-349, NEU-368 bylines
```

Independence statements I checked and found **correct**: NEU-342/343/344/345/364/365/366/367
("All sixteen authors are at Stoke Therapeutics" - PMC7347940 has a single affiliation line,
L4, and sixteen authors, so this is right); NEU-347 ("the human equivalent is NEU-373 from a
different group" - no name string is shared between the Voskobiynyk and Tang bylines);
NEU-354's "no shared author with Lim 2020 or with the mouse study in NEU-349"; NEU-369 and
NEU-371 ("same company authorship as NEU-368", same paper); NEU-370 ("Independent of the
company programme, but NOT a blind convergence", with STK-071 and STK-135 as the evidence -
verified at L44, L46, L48, L56); NEU-379 ("Frank Rigo is at Ionis Pharmaceuticals and the
rest of the group is at Washington University" - PMC8765054 L4, L5, L6 give exactly those
three affiliations, and L93 adds that Ionis provided the oligonucleotides).

## 5. Facts and figures that are right in the source but do not sit on a line the record cites

Verdict left at `ok` in every case. Listed because the anchor will not survive a reader
following it.

- **NEU-342** - "in neural progenitor cells" is not on L19 or L26, which say only "in
  cells". The cell type is at L73 ("ReNCell VM: SCN1A") and L77. The cycloheximide and the
  18.6%-to-89% range are on L19; the post-NMD-inhibition footnote is on L28 as the note
  says.
- **NEU-359** - "multicentre" is not on L7 or L8. It is in the official title at L1 and in
  the Detailed Description at L5. The EU CTIS number 2024-519555-28 is also on L1, as a
  EUDRACT_NUMBER secondary identifier. Everything else (1:1 allocation, ~52 weeks,
  quadruple masking, 170 estimated, all eligible patients treated in period 2) is on
  L7-L8.
- **NEU-360** - cites L9 only. L9 carries the week 28 seizure measure and nothing else.
  The week 52 seizure measure is L10, the multi-component Vineland-3 is L11, the subdomain
  Vineland-3 is L12, and the entire dosing and sham description in the second half of the
  claim is L8. Roughly four fifths of this claim sits on uncited lines.
- **NEU-361** - the completion date of 14 November 2023 is on L2. Plasma pharmacokinetics
  is L10, cerebrospinal fluid exposure L11, seizure frequency by paper diary L12, caregiver
  global impression of change L13. Cited lines are L7 and L9.
- **NEU-366** - "exon 14X of PCCA" is at L31, not on L23, L24, L25 or L37. The three
  percentages (30, 47, 20) are exact on L23, L24 and L25 and the dose-response results are
  exact on L37.
- **NEU-370** - "in HEK293T cells" is at L40 ("For high-throughput screening of
  steric-blocking ASOs we utilized HEK293T cells"), "exon 11x" at L41 and L46, and the
  rescue in patient neurons ("modestly but significantly increased SYNGAP1 mRNA",
  "multiple Site 1 and Site 2 targeting ASOs increased SYNGAP1 expression") at L55. Cited
  lines are L45 and L52; L52 establishes only the 50 per cent reduction.
- **NEU-375** - "1 micromolar" is at L60 (methods: ASOs transfected into HEK293T "at a
  concentration of 1 muM") and "five transfections per construct" at L85 (Figure 3B and
  3D captions, "n = 5 biological replicate transfections"). Cited lines are L26 and L27.
- **NEU-378** - "because they further impair the interneurons the disease already weakens"
  is at L9, and the extension studies' exclusion of maintenance sodium channel blockers is
  at L11 (and, as a registered criterion, on tri_26fa4417684d L3). L10, the cited line,
  carries only the EMPEROR half and the disease-modification argument.
- **NEU-379** - "all six human tau isoforms". The cited line L17 says "express all isoforms
  of hTau". The number six does not appear anywhere in PMC8765054; a within-document grep
  for "six isoform", "all 6" and "6 isoform" returns nothing. Unlike the other entries in
  this section the digit is not recoverable from the source at all, only from outside it.
- **NEU-384** - "sponsor study STK-001-DS-102". A within-document grep of
  tri_38bd136803ad for that string returns zero matches; it does not appear anywhere on
  the ADMIRAL registration. It appears repeatedly on the LONGWING record,
  tri_26fa4417684d L2, L3 and L4, which identify the roll-in study as
  "ADMIRAL (STK-001-DS-102)". Everything else in this long claim is exact on L4, including
  "Up to 60 participants are anticipated to be enrolled in approximately 5-7 centres
  across the UK", the 30/45/70 mg proposed levels, the two optional cohorts, three
  separate dosing days, 40 weeks or up to 48, and the 4/12/24-week period structure.
- **NEU-386** - the extension half of the claim ("both ADMIRAL and its extension exclude")
  rests on tri_26fa4417684d L3, which the note says was read but which the evidence block
  does not cite. The ADMIRAL half is exact on tri_38bd136803ad L3, items 2 and 6. I
  verified the extension's L3 independently: items 2 and 5 carry the same two exclusions.
- Note-level only, same pattern: **NEU-365**'s "validated fourteen events by RT-PCR and
  took four forward" is at L19 and L20; **NEU-368**'s group sizes (n = 4 per dose at week
  4, n = 2 per dose at week 8) are at L43 and are exactly right; **NEU-369**'s Seahorse
  detail (20, 40, 60 nM, three biological replicates) is at L75 and is exactly right;
  **NEU-373**'s "one brain sample per developmental time point" and "at least 500 reads per
  sample" are at L84, which **is** cited, and the amplicon-length caveat is at L34 and is
  quoted almost exactly right.

## 6. Two places where the source contradicts itself and the record did not register it

These are not record defects - each claim is faithful to its cited line - but a chapter
sentence built on either will be contradicted by the paper's own figure caption.

```
NEU-375  which splice junction the working oligonucleotide targets
  claim says: "an oligonucleotide against the exon's 5-prime splice junction at 1
    micromolar significantly reduced the 22N-containing products relative to the canonical
    isoform"
  source says: L27, the cited line, does say ASO1 "targets the 5' splice junction" and did
    significantly reduce 22N, with ASO2 showing a non-significant trend. But L85, the
    Figure 3C caption of the same paper, says the opposite: "ASO1 targets the acceptor
    splice site with the 3' end of the upstream intron, whereas ASO2 targets the donor
    splice site with the 5' end of the downstream intron." The acceptor site is the exon's
    3-prime junction. The main-text sentence at L27 is also garbled in the corpus text
    ("cells treated with a scrambled ASO (ASO1), which targets the 5' splice junction"),
    and the Figure 3D caption's statistics are internally inconsistent too (it reports
    "P = 0.038, no ASO vs. ASO2" and in the next clause "NS, not significant for no ASO
    vs. ASO2"). The record's derived point - that of two oligonucleotides only one worked -
    is safe; which junction it hit is not.
  lines read: PMC11981616 L27, L85
```

```
NEU-372  how far 22N is conserved
  claim says: "22N conserved in only some mammals"
  source says: L21, a cited line, says exactly that - "22N is only conserved in some
    mammalian species". L83, the Figure 1D caption, says "22N only shows limited
    conservation in primates". Mammals and primates are not the same scope, and the
    contrast the claim draws between 1N (primate-restricted) and 22N (some mammals)
    collapses on the figure caption's reading. The claim follows its cited line and is
    `ok`; the chapter should not lean on the mammal/primate contrast for 22N.
  lines read: PMC11981616 L21, L83
```

## 7. Smaller items, in descending order of how likely they are to reach the page

- **NEU-350**, scope of one denominator. The claim says "85 per cent survival for mice
  treated at postnatal day 14 against 64 per cent of untreated littermates". L13 says
  "compared to 64% survival of untreated Scn1a +/- mice"; the word "littermates" belongs to
  a different comparison on the same line, the PBS-treated littermates in the
  electroencephalography experiment. The note's warning that the two survival contrasts
  have different denominators is correct and valuable, and this is a third, smaller version
  of the same hazard.
- **NEU-363**, which reference carries which block. The note says the review "attributes
  this block to a conference abstract listing rather than to a publication (its reference
  72, an American Epilepsy Society abstract page)". Reference 72 is indeed an aesnet.org
  abstract listing (PMC12989007 L170) and it does carry the 11/81 and 20/74 cerebrospinal
  fluid figures. But the baseline-population figures the same claim reports (85 per cent on
  three or more antiseizure medications, 54 per cent on four or more, median 17 seizures
  per 28 days in 77 evaluable patients) and the 22 per cent serious adverse events sit in
  the part of L75 that carries reference 73, which is a sponsor-hosted PDF
  ("MONARCH-and-ADMIRAL-Interim-Analyses.pdf", L171). Both are outside the peer-reviewed
  literature, so the note's thrust holds, but the chapter should not attribute the baseline
  figures to the AES abstract.
- **NEU-363 against NEU-357**, a death count the records do not reconcile. The review at
  L75 says "One patient died from SUDEP, although this was deemed unrelated to the
  treatment"; the trial publication's abstract says "2 died from sudden unexpected death in
  epilepsy, and 1 died from malnutrition". Neither record states the other's number, so
  neither is wrong, but the two sources disagree and nothing in the records says so.
- **NEU-350 / NEU-351 / NEU-352**, source metadata. The records give
  `year: 2021` for the Epilepsy Currents commentary while their own `bibkey` is
  `wagnon2020tangocommentary` and the corpus metadata gives `pub_year: 2020`,
  `pub_date: 2020-12-04`. Online-first 2020, issue 2021; the record is internally
  inconsistent either way. Low severity, but a bibliography gate may see it.
- **NEU-366**, event-type wording. The claim calls the CD274 event a "non-productive
  retained intron". Table 1 at L25 calls it "Alternative intron (exitron)" and L37 calls it
  "the non-productive alternative intron". Retained intron is a distinct annotation class
  from an exitron; the paper never uses it.
- **NEU-372**, a replicate count attached to the wrong experiment. The note's "Three
  control stem cell lines, six biological replicate wells" reads as the denominator of the
  discovery experiment. "Hundreds to thousands of reads" is on L20 and the three control
  iPSC lines are at L29, but "n = 6 biological replicate wells of iNeurons per condition"
  belongs to Figure 2B, the NMD-inhibition experiment (L84), while Figure 4B uses n = 5
  (L86). The Figure 1 caption at L83 gives no n at all.
- **NEU-348**, an unanchored assertion inside a note. "SCN8A encephalopathy is a
  gain-of-function disease treated by lowering the gene, which is the opposite logic" is
  not in PMC7790302 and is not sourced anywhere in the record. It happens to be supported
  elsewhere in the corpus - PMC7863313 L12 says gapmers "have been used successfully in
  mouse models of epilepsy caused by gain-of-function mutations, such as SCN8A
  encephalopathy" - but that is a different record's document.
- **NEU-364**, an inference presented as the note's own. "The correlation rests on four
  genes, so it is a four-point regression" is not stated by the paper; L48 gives only
  "Supplementary Fig. 10, R2 = 0.9886, p = 0.0057" and the four targets are named in the
  preceding clause. The inference is almost certainly right and the note's advice to the
  chapter is sound, but the paper does not say how many points the regression had.
- **NEU-388**, an absence note that holds. "A grep of /fda/ for this drug returns only
  Freedom of Information logs for an investigational new drug dossier" - verified.
  `grep -i "zorevunersen" /fda/` returns no matches; `grep -i "STK-001" /fda/` returns four
  paragraphs across four documents, all Freedom of Information request letters asking for
  "Stoke Therapeutics: STK-001 drug candidate IND dossier / Pharmacology and toxicology
  data (21 CFR 312.23(a)(8)) part only (NCT04442295)". Scoped as a corpus-grep negative.

## 8. What I verified and found clean, so it need not be rechecked

- All five abstract-only records (NEU-341, NEU-349, NEU-353, NEU-355 to NEU-357, NEU-358)
  reproduce their abstracts exactly. Checked digit by digit: 81 enrolled, 75 into the
  extensions, 30 May 2025, post-lumbar-puncture syndrome 25 per cent, cerebrospinal fluid
  protein 45 per cent, one suspected unexpected serious adverse reaction, one withdrawal,
  two SUDEP deaths, one malnutrition death, -58.82 per cent to -90.91 per cent across
  one-month intervals in the first 20 months, 94.7 per cent at month 36, Vineland-3
  least-squares means 7.56 and 6.06. NEU-356's statement that the 70 mg subgroup's
  denominator is not given in the abstract is correct, and NEU-358's statement that the
  94.7 per cent and the two Vineland numbers are absent from the trial publication's
  abstract is correct.
- No full-text counterpart exists in the corpus for 35605822 (the 2018 AJHG paper; its
  meta.json names pmcid PMC6288405, but `cat`, `lookup pmc` and
  `sql ... WHERE doi = '10.1016/j.ajhg.2018.10.023'` all come back empty), 18196724,
  160612293 (meta names PMC10994531, also absent), 185828452 or 1000755297. Checked by DOI
  and by title ILIKE, not by `lookup title` alone.
- Tiers. Most of the forty-eight tier strings are descriptive tiers of the form the
  brief allows for methods, trials and registry records, and each matches what its source
  did. The thirteen tiers that name a perturbation were checked against the measured
  outcome in each case:
  NEU-346 and NEU-349 carry organismal phenotypes that were measured (mortality, seizures,
  hyperactivity; electrographic seizures, SUDEP) and are right; NEU-344, NEU-345, NEU-353,
  NEU-366, NEU-368, NEU-369, NEU-370, NEU-374, NEU-375, NEU-379 all state explicitly that
  the outcome was molecular or cellular and all are right. NEU-341 is the single tier
  defect.
- Registry structure. Primary/secondary labelling is structural and real on
  tri_6f267a56f74d (confirmed by reading `sections/primary_outcome.lines`),
  tri_38bd136803ad and tri_26fa4417684d. It is genuinely absent from the Planned_Outcomes
  sections of both ClinicalTrials.gov records - which is why the NEU-360 note went wrong
  in the direction it did, having looked in the right place and stopped there.
- Numbers checked against their lines and exact: NEU-342 (18.6 per cent, 89 per cent,
  fourteen events), NEU-343 (96 per cent, 16 per cent), NEU-345 (0.3 to 20 micrograms, four
  doses, five days), NEU-346 (~50 per cent, ~1 per cent, ~5-fold), NEU-347 (~70 per cent at
  E14.5, under 10 per cent by P30), NEU-348 (37.5 per cent, 57 per cent), NEU-350 (70, 97,
  85, 64 per cent; P22-P46), NEU-351 (fifteen-fold, six-fold, thirty days, twenty-five-fold,
  30 per cent), NEU-363 (85, 54, 17 per 28 days, n = 77, 11/81, 20/74, three-quarters,
  50 mg/dL, one discontinuation, 22 per cent), NEU-364 (144 oligonucleotides, R-squared
  0.9886, p 0.0057), NEU-365 (7,757 and 1,246), NEU-366 (30, 47, 20 per cent), NEU-368
  (53, 12, 6 per cent; 31, 47, 44 per cent; 0.1, 0.3, 1.0 mg per eye), NEU-372 (two exons,
  introns 1 and 22), NEU-373 (under 5 per cent), NEU-374 (under 1 per cent, sixteen-fold,
  3 to 6 per cent), NEU-377 (3.8 and 3.57 per cent), NEU-381 (28 days, week 16 to week 52,
  nine intervals), NEU-383 (70/70/45/45 mg, days 1, 57, 169, 281, eight-week baseline),
  NEU-384 (30/45/70 mg, 60 participants, 5-7 centres, 40 and 48 weeks), NEU-387 (every four
  months, weeks 16 and 32, 24 weeks, 15 months).
