# Records review B: SCS-141..159, 161..176, 181..219 against their sources (chapter 8)

74 records, 28 documents (19 PMC, 9 bioRxiv; 21 of the 74 records are
preprint-sourced). Every cited line range was opened with `paperclip cat`,
always as a range, and read with surrounding context. Every numeral and every
number-word in every `claim` was checked against the cited lines, and where one
was missing it was re-searched **inside that document** with `paperclip grep`,
never corpus-wide. `meta.json` was opened for all 28 documents. Every `note:`
absence claim was re-tested by within-document grep; every `note:` independence
claim was recomputed from `meta.json` bylines, including for the eleven records
outside this block that the notes name.

**Scoring rule used here.** The nine permitted strings describe the `claim`. A
defect that lives only in a `note:` has no string among the nine, so the table
verdict scores the claim and the tier, and note defects are reported separately
in §3. The §0 counts therefore exclude note defects, which are counted on their
own line.

Metadata: every record's `authors`, `journal`, `year` and `doi` match its
document's `meta.json` (reformatted only; PMC8563012's record collapses the
long eLife byline to "...; Tabula Sapiens Consortium; Quake, S. R.; Krasnow, M.
A.; Salzman, J.", which is a rendering choice, not an error). All 21
preprint-sourced records carry `preprint: true`; the three whose `doi` is the
journal version (SCS-151, SCS-158, SCS-159) say so in `note:`. No PMC document
in the block is a preprint. Hence **`source metadata wrong`: 0**.

Tiers: every tier in this block is descriptive (`tier: <what was done>`), which
is correct for a measurement chapter, and each matches what its source did.
Hence **`tier wrong`: 0**. One borderline case is in §8.

## 0. Counts

- `ok` — 64
- `qualifier lost` — 6 (SCS-142, SCS-145, SCS-148, SCS-149, SCS-166, SCS-195)
- `scope too wide` — 2 (SCS-143, SCS-144)
- `number wrong` — 2 (SCS-176, SCS-207)
- `direction wrong`, `proposal as finding`, `source metadata wrong`,
  `tier wrong`, `cannot check` — 0 each

Counted separately, not in the table:
- note defects — 4 distinct, carried by 10 records (one is repeated verbatim
  across 7 records)
- claim elements correct in the paper but **not on a cited line** — 12
- claim elements **not in the document at all** — 4
- source-internal inconsistencies worth the writer's attention — 3

## 1. Verdicts

SCS-141 ok                 SCS-164 ok                 SCS-194 ok
SCS-142 qualifier lost     SCS-165 ok                 SCS-195 qualifier lost
SCS-143 scope too wide     SCS-166 qualifier lost     SCS-196 ok
SCS-144 scope too wide     SCS-167 ok                 SCS-197 ok
SCS-145 qualifier lost     SCS-168 ok                 SCS-198 ok
SCS-146 ok                 SCS-169 ok                 SCS-199 ok
SCS-147 ok                 SCS-170 ok                 SCS-200 ok
SCS-148 qualifier lost     SCS-171 ok                 SCS-201 ok
SCS-149 qualifier lost     SCS-172 ok                 SCS-202 ok
SCS-150 ok                 SCS-173 ok                 SCS-203 ok
SCS-151 ok                 SCS-174 ok                 SCS-204 ok
SCS-152 ok                 SCS-175 ok                 SCS-205 ok
SCS-153 ok                 SCS-176 number wrong       SCS-206 ok
SCS-154 ok                 SCS-181 ok                 SCS-207 number wrong
SCS-155 ok                 SCS-182 ok                 SCS-208 ok
SCS-156 ok                 SCS-183 ok                 SCS-209 ok
SCS-157 ok                 SCS-184 ok                 SCS-210 ok
SCS-158 ok                 SCS-185 ok                 SCS-211 ok
SCS-159 ok                 SCS-186 ok                 SCS-212 ok
SCS-161 ok                 SCS-187 ok                 SCS-213 ok
SCS-162 ok                 SCS-189 ok                 SCS-214 ok
SCS-163 ok                 SCS-190 ok                 SCS-215 ok
                           SCS-191 ok                 SCS-216 ok
                           SCS-192 ok                 SCS-217 ok
                           SCS-188 ok                 SCS-218 ok
                           SCS-193 ok                 SCS-219 ok

## 2. Detail blocks

```
SCS-207  number wrong
  claim says: "out of 15,827 three-prime UTR and 4328 intronic sites called in
    10,176 protein-coding genes, of which 37.6 per cent had multiple 3-prime UTR
    sites and 42.3 per cent multiple intronic sites"
  source says: L30 gives the two percentages as "The proportions of genes with
    multiple PASs in the 3'UTR (37.6%) and introns (42.3%)" and states no
    denominator for either. The claim attaches both to the 10,176 figure. That
    is impossible for the intronic one: 42.3 per cent of 10,176 genes each
    carrying two or more intronic sites would require more intronic sites than
    the 4,328 the same line reports. The 3'UTR percentage is arithmetically
    compatible with 10,176, but the source does not say it is that denominator
    either, and the two percentages need not share one. The record should not be
    read as supplying a denominator the source withholds.
  lines read: PMC11736434 L19, L28, L30 (plus L32, L67, L74, L79 for context)
```

```
SCS-176  number wrong
  claim says: "In 50,792 cells sequenced with a full-length droplet protocol
    from a six-patient hepatocellular carcinoma training cohort"
  source says: 50,792 appears once, in the Figure 2 caption at L56, as "UMAP
    plot showing clustering of 50,792 HCC cells by SCASL based on AS profiles" —
    the source attaches it to the splicing clustering, the claim to the
    sequencing. Clustered cells were of course sequenced, so this is an unstated
    inference rather than a flat contradiction, but no cited line states a
    sequenced-cell count, and L55 says SCASL was run on "up to 2000 cells from
    each of the six patients", which caps the clustered set far below 50,792.
    The source is self-contradictory and the record resolves it silently; the
    record's own note states the contradiction and then asserts the unsupported
    half in the claim. Two further gaps on the same number: 50,792 covers all
    cell types (L56 lists separate CD4 and CD8 panels), and no cell count is
    given anywhere on the cited lines for the T cells behind the two-state
    result, which is what the claim is actually about.
  lines read: PMC13327004 L29, L55-L56, L59, L70, L75 (plus L71)
```

```
SCS-148  qualifier lost
  claim says: "2,811 or 49 per cent were also significantly age-correlated in
    3,227 human endothelial cells"
  source says: L60 defines that significance as "an absolute Spearman's rho >
    0.05 and an adjusted p-value < 0.05". A correlation threshold of 0.05 is
    close to no threshold at all, so the 49 per cent is a replication rate under
    an unusually permissive rule and the word "significantly" carries that rule
    silently. The threshold lives only in the note, which the project's own rule
    says is not citable. (The note's sentence "which the claim keeps because the
    paper states it" is ambiguous about whether its antecedent is the threshold
    or the 49 per cent; either way the threshold is not in the claim.) The 83
    per cent in the same sentence is a fraction of the 2,811, which the claim
    states correctly.
  lines read: bio_71aa4f57720b L23, L35, L57, L60
```

```
SCS-166  qualifier lost
  claim says: "with the two transcripts differing by one exon whose splice
    acceptor carried a heterozygous variant"
  source says: L28 says the isoforms "differ MAINLY by inclusion of a single
    exon", and the same line goes on: "These two annotated isoforms are also
    distinguished by 5' exons with little coverage... Thus, although the
    splice-site variant is strongly linked to the local exon-inclusion event,
    the full 5' isoform structure remains ambiguous, as SCOTCH may assign a
    3'-matched read to ENST00000010132 as a 5'-truncated read, leaving a novel
    isoform unexcluded." The dropped hedge is the one that bears on whether the
    named variant accounts for the whole haplotype difference, which is the
    claim's point. The note does not mention it.
  lines read: bio_bcfece3a72bc L24, L27-L28, L69
```

```
SCS-195  qualifier lost
  claim says: "with pairwise correlations above 0.9 on 10x Chromium data for
    sites all ten methods found, and correlations near 0.8 against bulk 3-prime
    end or RNA-seq data"
  source says: L109 reads "In 10X Chromium datasets WITH SUFFICIENT
    HIGH-CONFIDENCE pAs, pairwise expression correlations among MOST methods
    exceeded 0.9" and "MOST methods achieved correlations near 0.8 across
    datasets". Three restrictions are dropped: which 10x datasets, and twice
    that it is most methods rather than all. The same line adds that the number
    of overlapping APA genes "varied widely", with scraps detecting dramatically
    fewer. The note carries the gene-set restriction (>=6 methods, top 60 per
    cent by deviation from ground truth) but not these.
  lines read: PMC13161560 L54, L109, L113
```

```
SCS-149  qualifier lost
  claim says: "although splicing alone predicted worse than expression alone"
  source says: L43 reads "gene expression alone was OFTEN a stronger age
    predictor than splicing alone". The claim states as a general result what
    the authors state as a tendency, and it does so in the very clause the note
    says "must travel with the number". Everything else in the record (80,557
    cells, 76 tissue-cell-type pairs, n>=50 in both age groups, 46 of 76,
    FDR < 0.05) is exact on L43.
  lines read: bio_71aa4f57720b L23, L25, L43
```

```
SCS-142  qualifier lost
  claim says: "the benchmark cannot credit a method for recovering a cell
    population that the expression-based annotation does not contain"
  source says: L57 reads "it MAY UNDERESTIMATE scenarios in which AS captures
    biologically meaningful cell populations that are NOT WELL REPRESENTED by
    expression-based annotations", and L55 "this concordance-based evaluation is
    inherently conservative and MAY give lower scores". Two hedges become an
    absolute: "may underestimate" becomes "cannot credit", and "not well
    represented" becomes "does not contain". This record exists to say what a
    concordance benchmark can and cannot settle, so the strength of the authors'
    own wording is its load-bearing part.
  lines read: PMC13217931 L55, L57
```

```
SCS-145  qualifier lost
  claim says: "Comparing junction-level splicing ratios between two human and
    two mouse bulk RNA-seq datasets of five sorted naive immune cell types,
    62 to 67 per cent... used a significantly different ratio in the two species"
  source says: L24 does say two human and two mouse datasets were used, but L26
    states which comparisons were actually run: human H1 vs H2, mouse M1 vs M2,
    and cross-species "between human dataset H2 and mouse dataset M1". The 62-67
    per cent therefore rests on ONE human dataset against ONE mouse dataset,
    chosen (L15) because they came from the same laboratory "to minimize
    technical differences"; the second dataset of each species supplies only the
    within-species control. The claim's framing makes the species difference
    look like a two-against-two comparison. The within-species figures (54-61
    per cent, 29-37 per cent) are exact. The note does not mention the H2/M1
    design.
  lines read: bio_8a2c7d9f0d7b L8, L24-L25, L27, L30 (plus L15, L26)
```

```
SCS-143  scope too wide
  claim says: "In Smart-seq2 data from hepatocellular-carcinoma-infiltrating
    lymphocytes, an independent group found the PTPRC intron 3-5 usage ratio low
    in natural killer cells and higher in CD4 and CD8 T cells"
  source says: the cited L22 says the leukocyte data are "data from a single
    donor in Zhang et al., 2019", and L101 names that donor (D20170327). The
    NK-against-T contrast is Figure 4D, whose caption at L40 is "based on the
    Zhang et al. 2019 dataset" with no all-donor marking, while panels 4E-4G are
    explicitly labelled "including all donors" — and L46 says "we extended our
    analysis to all donors", which only makes sense if what preceded it was not.
    So the contrast is one patient's cells, stated in the claim as a property of
    HCC-infiltrating lymphocytes. Neither claim nor note carries the donor
    scope, although it sits on a line the record cites. Mitigating: the
    naive-to-activated half of the claim is the one result L46 says was
    reproduced across all donors — in the opposite isoform direction, which the
    note correctly reports as an unresolved source contradiction.
  lines read: PMC13217931 L22, L46 (plus L38, L40, L101)
```

```
SCS-144  scope too wide
  claim says: "intron 1 of the T-cell-receptor adaptor gene FYB was used at a
    ratio of 10 per cent in myeloid cells against 83 per cent in natural killer
    cells and 71 per cent in CD8 T cells"
  source says: these are Figure 4D values (L44), from the same single-donor
    subset as SCS-143 — cited L22 says "a single donor in Zhang et al., 2019".
    Three percentages from one patient's cells are stated with no cohort. The
    note is unusually careful about what cannot be said here (it explains why no
    cell count is recorded and why the uncorrelated-expression clause rests on
    the authors' reading of their own panel) and still does not mention that the
    data are one donor's.
  lines read: PMC13217931 L22, L40, L44
```

## 3. Note defects

**3a. An independence note that overstates, repeated verbatim across 7 records.**
SCS-181, SCS-182, SCS-183, SCS-184, SCS-193, SCS-194 and SCS-195 all end with:
*"Two of the ten tools evaluated and part of the yardstick come from the
evaluating group."* The sentence can be parsed either as "two of the ten
tools" or as "two things: one tool plus part of the yardstick", so it is
ambiguous rather than flatly false — but on the first reading, the one a writer
will take, it is wrong. Recomputed by reading **all ten** tool references
(PMC13161560 L165-L174) against the benchmark byline (Xingyu Bi; Zhen Chen;
Mengmeng Ye; Tao Zhang; Danni He; Xiaohui Wu):

- ref 19 Shulman/Elkon (scAPA), 20 Patrick et al. (Sierra), 22 Zhou R/Xiao X/He
  P (SCAPE), 23 Kowalski et al. (polyApipe), 24 Li WV et al. (MAAPER), 25
  Fansler/Mitschka/Mayr (scUTRquant), 26 Li G-W et al. (SCAPTURE), 27 Kang B et
  al. (Infernape), 28 Fu R et al. (scraps) — no name-string match. (Ref 22's
  "He P" shares only a surname with "Danni He", not surname plus initial.)
- ref 21 Wu X, Liu T, Ye C (scAPAtrap) — "Wu X" matches the benchmark's last
  author Xiaohui Wu. **One** of the ten.
- PolyAseqTrap (ref 43, L189: Ye W, Cheng X, Bi X) matches the benchmark's first
  author Xingyu Bi, but it is **not one of the ten evaluated tools**; L53 uses
  it to quantify pAs where no known annotation exists, so it is yardstick only.

Correct statement: one of the ten tools, plus part of the yardstick. Two
smaller points in the same note: it calls Wu X "the same corresponding author",
but `content.lines` for this document carries no correspondence statement (0
hits for "orrespond"), so only last-author position is a read fact; and it
omits that L53 names QAPA as the alternative fallback in the same sentence.
Related and not in any note: a second yardstick component, movAPA (ref 35,
L181: Ye W, Liu T, Fu H et al.), used at L54 to define proximal and distal
sites, shares its first author with PolyAseqTrap — "Ye W", which is *not* the
benchmark's own "Ye M".

**3b. SCS-170 cites a record that does not exist.** The note says "The chapter
should not merge it with SCS-160 on that point." `grep -rn "SCS-160" research/`
returns exactly one hit: that note. The ids run SCS-159 then SCS-161; there is
no SCS-160 anywhere in `research/`.

**3c. SCS-212 asserts a method the document never states.** "Cell-cycle phase is
inferred from expression rather than measured." A within-document grep of
PMC10691540 returns no hit for "cell cycle" or "cell-cycle", and the only
occurrence of "phase" is L37 itself. The paper never says how phase was
assigned. The assertion is probably true of the software used, but it is not
anchored. Same note: it says the authors at L56 call their result "consistent
with the earlier reports that proliferation shortens 3-prime UTRs"; L56 says
"consistent with previous reports that cell proliferation AFFECTS 3'-UTR
lengths (Sandberg et al. 2008)".

**3d. SCS-145 is wrong about where the per-cell-type counts live.** "the
per-cell-type comparable counts sit in the source's Table 1 rather than its
text" — L30 prints 748-908 differentially spliced and 271-349 unchanged in the
running text.

Minor, same family: SCS-175's note says "The authors report the same pattern for
TPM1 at L252"; L252's TPM1 contrast is capillary endothelial against smooth
muscle, not the stromal-and-endothelial against epithelial compartment pattern
the claim is about. It is a conserved cell-type splicing pattern, not the same
pattern.

**Absence notes checked and found CORRECT** (each re-tested by a within-document
grep, never a corpus grep): SCS-156 (PMC7935992 never names the chemistry of
the HCC T cell data — the only "Smart-seq" hit, L37, is about future
technology, and L40 gives only GSE98638/EGAS00001002072); SCS-173 and SCS-174
(PMC8563012 never names the chemistry of the Hermann 2018 sperm data, only SRA
run accessions at L354-L359, and never reports a gene-expression control for
the 170 pseudotime genes); SCS-197 (PMC10691540 nowhere tests agreement between
its single-cell and its Visium 3'-end calls); SCS-176 (PMC13327004 never says
where the seven-patient validation dataset came from); SCS-151 (the filtered
gene total behind 2,172 is not in the text); SCS-167 (the ACTV>=0.5 denominator
is not stated); SCS-163, SCS-165, SCS-214 (cell counts absent as stated);
SCS-182 (MAAPER really is absent from both of L86's lists, and the note's three
counter-examples all check out: scAPA's 4,328 intronic sites at PMC11736434 L30,
Infernape's intronic PAs in its own abstract at PMC10691540 L7, SCAPE's
pre-emptive intronic removal at bio_802472217144 L62).

**Independence notes checked and found CORRECT**, including the records outside
this block that they name (bylines pulled from `research/*.yml` and, for
in-block documents, from `meta.json`; all are `full_text`, so these are verified
bylines and not bare name strings): SCS-141 and SCS-172 (Jiang/Li/Xing/Zhang/Sun
share no name string with Olivieri..Salzman, PMC8563012, or with
Benegas/Fischer/Song, PMC8975553); SCS-143 and SCS-153 (no name string shared
with Michalik/Niederlova/Stepanek, PMC11496083, or with
Hagemann-Jensen..Sandberg, bio_c92559d26c1b); SCS-148 ("no relation to the
authors of SCS-018" — SCS-018 is PMC11156538, Joglekar..Tilgner; Isaev/Knowles
share no name string with it); SCS-166 (Xu Z/Wang K share none with
bio_c92559d26c1b); SCS-171 ("two laboratories" — SCS-016 is PMC7815907,
Joglekar..Tilgner, against Xiang/He/Zhang/Yang: no shared name string);
SCS-164 and SCS-165 ("same paper as SCS-003, SCS-004, SCS-032" — all four are
PMC11496083); SCS-186 and SCS-199 (Zavolan is on both PMC11701536 and
PMC8594477, correctly called not independent); SCS-203 and SCS-217 (Mayr is on
both PMC11094166 and PMC5928244, correctly called not independent); SCS-191
(PMC11655283 L51 does say "A.E.G. oversaw the development of the scraps
workflow", and Gillen A.E. is an author of the scraps preprint at L75);
SCS-147, SCS-155, SCS-162, SCS-174, SCS-175, SCS-200, SCS-213 (all "same
paper", all confirmed). Every cross-reference in every note in the block
resolves to an existing record except SCS-160 (§3b).

**An open independence question in SCS-169's note, now partly resolved and
partly re-scoped.** The note says: "These authors also analyse a hepatocellular
carcinoma immune dataset elsewhere in the same paper; whether it is the dataset
SCS-156 and SCS-157 rest on was not checked." It is not the same dataset:
PMC10925056 L32/L59 use ref 61 (L215: "Zhang Q, Landscape and dynamics of
single immune cells in hepatocellular carcinoma, Cell 2019", 2,349 immune
cells), while PMC7935992 L40 uses GSE98638/EGAS00001002072 = its ref 1 (L102:
"Zheng C, Landscape of infiltrating T cells in liver cancer revealed by
single-cell sequencing, Cell 2017", 5,063 T cells). Different datasets,
different sizes, different accessions, and SCS-169 is the TNBC analysis in any
case. **But** a second question opens that the note did not ask: PMC10925056's
own byline (`meta.json`) is "Xianke Xiang; Yao He; **Zemin Zhang**; Xuerui
Yang", so one of the reanalysing authors shares a name string with the surname
of the Cell 2019 dataset's first author and, on the chapter's likely reading,
with the laboratory that produced both HCC datasets. Both papers' reference
lines in this corpus print first authors only, so whether Zemin Zhang is a
senior author of either dataset paper **cannot be settled from these
documents**. Anything the chapter says about PMC10925056 being independent of
the data it reanalyses needs that checked outside the corpus.

**Not re-checked**, flagged so it is not mistaken for verified: SCS-199's note
makes specific claims about PMC6821429 L41/L43 (that SCS-026's 868
polyadenylation shifts came from the same Pace et al. dataset, out of 9,611
3'UTR peaks, using 970 proliferating against 1,958 naive cells). PMC6821429 is
SCS-026's document, outside this block, and those lines were not opened.

## 4. Claim elements correct in the paper but NOT on a cited line

**No numeral in any of the 74 claims sits off its cited lines** — the dispatch's
class 1 came up empty for numbers. The rows below are descriptors and
definitions: true, anchored in the document, but outside the cited range, so a
later verifier re-reading only the cited lines will not find them. All these
records are `ok` or scored for something else.

| record | element | sits on | cited |
|---|---|---|---|
| SCS-141 | "a mean over the five datasets" stated as such | PMC13217931 L27 (Fig 2A caption); L26 says only "average" | L22, L25-L26, L111 |
| SCS-143 | "hepatocellular-carcinoma-infiltrating" | PMC13217931 L79 ("HCC lymphocyte"), L101 | L22, L46 |
| SCS-145 | "sorted", "naive" immune cell types | bio_8a2c7d9f0d7b L15, L38 | L8, L24-L25, L27, L30 |
| SCS-145 | the cross-species comparison is H2 vs M1 | bio_8a2c7d9f0d7b L26 | (see §2) |
| SCS-168 | lineage order "from basal cells through precursors to mature neurons" | PMC13724654 L18, L21 (HBC to mature OSN) | L16, L27, L57 |
| SCS-194 | the "and no annotation confirmed" half of the unique-pA definition | PMC13161560 L46, L101 | L102 |
| SCS-206 | the "pairwise" comparison scheme | PMC10691540 L44 | L42, L43 |
| SCS-207 | the two ratio indices' definitions | PMC11736434 L81, L100 (the note says so) | L19, L28, L30 |
| SCS-205 | "tandem UTR leaves the protein unchanged / alternative last exon can truncate it" | PMC12401049 L13 (Introduction, citing others) | L19, L21 |
| SCS-210 | "CD4", and that the data are a reanalysis of the group's own published RNA-seq (GSE135118) | PMC11094061 L20, L50 | L22 |
| SCS-217 | "lymphoid tissue" as the source of the tissue-derived naive B cells | PMC5928244 L34, L35 | L8, L22 |
| SCS-218 | "human neuroblastoma line" (SH-SY5Y), "retinoic acid and BDNF", "poly(A) tail sequencing" (PAT-seq) | PMC10450200 L21, L23, L45 | L48, L64 |

## 5. Claim elements not in the document at all

- **SCS-164: "isotype-specific oligo-tagged anti-CD45 antibodies".** The CITE-seq
  antibodies at PMC11496083 L46 are anti-CD45RA and anti-CD45RO: *isoform*-
  specific, not *isotype*-specific. "Isotype" is an antibody class (IgG, IgM);
  as written the claim names a different reagent. "Oligo-tagged" is true of
  CITE-seq but appears on no line of the document.
- **SCS-152: "the metalloproteinase inhibitor gene TIMP1".** `grep
  "metalloprotein"` inside bio_c92559d26c1b returns no matches. Correct biology
  from outside the source. (Contrast SCS-144, whose "T-cell-receptor adaptor
  gene FYB" gloss *is* on its cited L44.)
- **SCS-159: "downstream starts" / "an upstream start".** bio_374c7f3a6fe2 L42
  says only that Tnnt2_4 belongs to the longer isoform while MB nuclei use TSSs
  belonging to shorter isoforms. Upstream/downstream is the record's inference —
  sound, but not read.
- **SCS-210: "deep RNA-seq".** PMC11094061 characterises the depth on no line
  read.

## 6. Performance figures and benchmark circularity (defect class 4)

Scored as defects above: SCS-148 (a 49 per cent replication rate without its
|rho| > 0.05 threshold), SCS-195 (0.9 and 0.8 correlations without "most
methods" or the dataset restriction), SCS-176 (a cell count attached to the
wrong quantity, and no T cell count at all), SCS-207 (a percentage attached to
an impossible denominator).

Handled **well**, recorded because the writer needs to know which figures
already carry their own warning:

- SCS-141 and SCS-172 state the parameter sweep and the composite index in the
  claim, and the circularity — the ground truth is the datasets' own
  expression-derived annotation — gets its own record, SCS-142, rather than
  being left in a note. That is the right shape. What SCS-141 does *not* carry,
  in claim or note, is that its 0.89/0.88 accuracy was never compared with
  gene-expression clustering on the same cells; that observation currently lives
  only in SCS-154's note.
- SCS-154's note says the labels were "experimentally validated" — confirmed at
  bio_310271736e0b L47 and L49 — so that benchmark is *not* scored on its own
  authors' labels, worth stating explicitly because its neighbours are.
- SCS-215's claim carries its AUROC > 0.8 rule and its 4,269-gene denominator.
- SCS-191's percentages carry their denominator (exonic UMIs per library), and
  the note correctly distrusts polyApipe's own ~20 per cent mispriming flag
  because PMC11655283 L43 reports the flag firing *more* often with the shorter
  read 2.

One circularity stated **nowhere** in the records: **SCS-202.** The 60 per cent
(human) and 52 per cent (mouse) are fractions of "multi-UTR genes" as
classified by the same group's own scUTRquant pipeline against the same group's
own Microwell-seq cleavage-site annotation (SCS-203, PMC11094166 L16 and L32:
at least two cleavage sites in the last exon with an isoform reaching 10 per
cent of the gene's 3'UTR counts in some cell type). Both the switch rule and
the denominator are the authors' own constructs. SCS-202 states the rules,
which is why it is `ok` and the best-anchored record in the block, but neither
it nor SCS-203 says that the annotation the classification rests on is also
theirs. The chapter will set this 60 per cent beside counts from other atlases,
and that is the fact that makes them incomparable.

## 7. Source-internal inconsistencies the writer should know about

Contradictions *in the source*, not record defects; in each case the record
follows its cited line and should not be "corrected".

1. **PMC13327004**: L55 ("up to 2000 cells from each of the six patients")
   against L56's caption (50,792 cells clustered by SCASL). This produced
   SCS-176's `number wrong`.
2. **PMC11736434**: L74 filters intronic peaks on eight consecutive adenines
   10-140 nt downstream; L79 on seven adenines 1-200 nt downstream. SCS-190
   flags this correctly and is `ok` for doing so.
3. **PMC7935992**: L20 says the 5,063 T cells were "assigned to 11 T cell
   subsets"; L40 says the dataset "contained 5063 T cells assigned into 12
   clusters". SCS-156 follows L20 (11).

Two apparent inconsistencies that reconcile on a closer read, recorded so a
later pass does not re-open them:

- **PMC10925056** L52 lists six hepatocyte-lineage clusters (C2, C10, C3, C1,
  C8, C5) and three cholangiocyte-lineage ones (C0, C9, C6) while the Figure 4B
  caption at L53 says seven and four. The clusters are C0-C10, i.e. eleven =
  7 + 4; L52's 6 + 3 lists lineage members, and L55 shows C4 sitting off-lineage
  between them. The pseudotime panel covers all eleven. Not a contradiction, and
  SCS-170's "six" and "three" are right for what it claims.
- **bio_310271736e0b** L22 and L44 give five-fold cross-validation "across all
  datasets" while L30-L32 give a 70/30 split, and for the two datasets under 500
  cells a 40/60 split with bootstrap augmentation of the training set. Reading
  L28-L33 settles it: the 70/30 and 40/60 protocols belong to the **external
  annotation tools** (SCS-155), not to ICON's own cross-validation (SCS-154). So
  SCS-154's "five-fold cross-validation on four datasets" is right, and the
  train/test protocol is a missing condition on SCS-155 rather than a conflict —
  a weak one, because L28 says "Identical preprocessing, training, and
  evaluation procedures were applied in both cases", so SCS-155's gene-against-
  isoform comparison is within one protocol.

Also: bio_374c7f3a6fe2 L32 names the first comparison group "0hr myoblast (MB)
cells (L1-L3)" and then reports the counts "between MB nuclei and ...". SCS-158
follows the results sentence ("nuclei").

## 8. Minor and borderline, reported because a false positive is cheap

- **SCS-152**: "every other annotated cell type was dominated by the full-length
  isoform" against L28's "the long, full-length isoform was dominant across
  other cell types". A universal where the source has a general; below my bar
  for `scope too wide`.
- **SCS-187**: "at the expense of every other genomic region" against L42's "at
  the expense of other types of genomic regions". Same shape.
- **SCS-143's tier** reads "measurement that resolves isoforms rather than
  genes, with cell-state assignment as the outcome". Nothing was assigned by the
  isoform measurement: the subtype labels came from gene expression and the PSI
  was plotted against them, which the note itself says. The tier is descriptive
  and survives a charitable reading, so I did not score `tier wrong`, but the
  phrase inverts which variable was measured and which was given.
- **SCS-217**: the claim opens "Measured by 3-prime end sequencing of sorted
  primary human cells rather than single cells", then quotes a figure for ovary.
  PMC5928244 L18 says the atlas combines whole normal tissues (ovary, brain,
  breast, skeletal muscle, testis), cell types, cell lines and newly generated
  primary immune profiles. The claim's later clause ("4 to 8 per cent in complex
  tissues") does carry the distinction, so the numbers are not misleading, but
  the opening descriptor does not fit all the data it introduces.
- **SCS-201**: "which those authors took as grounds to recommend SCAPE" —
  bio_2b5540eb6c78 L32 bases the recommendation on "the best balance of
  accuracy, efficiency, and resource usage", not on concordance alone.
- **SCS-188**: "the artefact that most inflates false intronic polyadenylation
  calls" is a superlative; L61 says internal priming is "the primary source of
  intronic reads" and "can increase false-positive sites, especially false IPA",
  without ranking artefacts against one another.
- **SCS-197**: "Where one study measured 3-prime end usage in the same adult
  mouse brain both ways" — the single-cell side (PMC10691540 L42) is a
  reanalysis of Zeisel et al. 2018 and the Visium side is the authors' own
  tissue. Same tissue type, not the same brain. The record's substantive point
  (the design transfers labels from one to the other, so disagreement could not
  surface) is exact.
- **SCS-200**: the claim reproduces L24's "146 of 165" alongside "171 events",
  and L24 is itself ambiguous about whether 165 is the shortened subset or a
  slip for 171. Following the source is right; the chapter should not do
  arithmetic on these two numbers.
