# Which chapter owns which claim

Several claims were recorded independently by two or three research agents, and
a few topics could sit plausibly in any of three chapters. Without a decision
recorded somewhere, each chapter gets drafted as though it were the only one,
and the book ends up making the same point three times with three different
numbers attached.

So each contested topic gets one home. The home chapter states it fully. Every
other chapter that needs it refers to the home section and does not restate the
figures. Section identifiers are fixed here before drafting, so that a
cross-reference written in chapter 1 still resolves when chapter 9 is written
six commits later.

## Depth per chapter

`CONTRIBUTING.md` has the policy and the arithmetic. In short: the book is a
quarter of the size a book of this kind should be, the 35-claim figure that
shaped every chapter was a research-pass budget rather than a decision, and
there is no cap now.

Deepening order, and why:

| Order | Chapter | Why it is here |
|---|---|---|
| 1 | 12 proteoforms and drugs | Thinnest in the book at 1,426 words, carries the forward argument, and its central review is abstract-only so the research pass fixes that too |
| 2 | 5 long reads | The reader's own field. STYLE.md promises full explanations of EM-based quantification, internal priming and read-support thresholds, and the book explains none of them |
| 3 | 2 animals | STYLE.md calls it the reference implementation and it has the worst provenance: fifteen abstract-only sources, most of the Dscam1 section among them |
| 4 | 6 cancer | Widest audience, and the leads list CD44, RAC1b, EGFRvIII and BRAF splice variants as unanchored |
| 5 | later | 1, 3, 4, 7, 8, 9, 10, 11, 13 |

A chapter is not finished when it hits a word count. It is finished when its
sections cover their subject and its paragraphs hold more than one source each.

## Contested topics

| Topic | Claims | Home | Section id | Referenced from |
|---|---|---|---|---|
| Spliceosome, mechanisms, event classes | FND-001.. | ch1 | `#sec-mechanism` | ch2, ch3 |
| PSI and event-level metrics | FND-026, TECH-035 | ch1 | `#sec-psi` | ch4, ch8 |
| DGE / DTE / DTU as different nulls | FND-028, FND-029 | ch1 | `#sec-dtu` | ch6, ch8, ch10 |
| FSM / ISM / NIC / NNC definitions | FND-031, FND-032 | ch1 | `#sec-transcript-classes` | ch5, ch9, walkthrough |
| AS-NMD as regulated output | FND-024, FND-025 | ch1 | `#sec-as-nmd` | ch2, ch7, ch10 |
| Prevalence: the 95 per cent figure and its denominators | ANM-028, TECH-023/025/026 | ch2 (aside) | `#sec-how-functional` | ch1, ch4 |
| Major-transcript dominance | ANM-033, CAT-005, CAT-023 | ch2 | `#sec-how-functional` | ch1, ch9 |
| Unproductive splicing as volume control | ANM-016, FND-024/025 | ch2 | `#sec-how-functional` | ch1, ch10 |
| Cassette exons vs intron retention across taxa | PFO-020 | ch3 | `#sec-class-balance` | ch1, ch4 |
| Exon skipping as commonest class in early RNA-seq | TECH-022 | ch4 | `#sec-rnaseq-arrives` | ch1, ch3 |
| EST-era concentration of variation in 5' UTRs | TECH-010 | ch4 | `#sec-est-era` | ch1, ch9 |
| Start site / splice chain / end site as three axes | LR-021, LR-022, CAT-003 | ch5 | `#sec-three-axes` | ch1, ch8, ch9 |
| GTEx long-read dataset, as a dataset | LR-023, LR-024 | ch5 | `#sec-gtex-lr` | ch9, ch10 |
| Single-cell long-read chemistry | LR-002, LR-029, LR-030, LR-034 | ch5 | `#sec-sc-longread` | ch8 |
| ENCODE4 long-read collection | LR-021/022, CAT-* | ch9 | `#sec-encode4` | ch5 |
| Catalog per-gene transcript counts | CAT-011/042/051/053 | ch9 | `#sec-per-gene-counts` | ch1, ch5 |
| Novel-isoform fraction and its denominator | CAT-032, CAT-039 | ch9 | `#sec-what-novel-means` | ch5, walkthrough |
| TRAILS and single-cell isoform methods | 08-*, CAT-* | ch8 | `#sec-sc-methods` | ch9 |
| Joglekar 2024 single-cell isoform atlas | LR-019, LR-035, SCS-* | ch8 | `#sec-brain-atlas` | ch5 |
| Isoform-level QTLs in B cells | nagura2025longread | ch5 | `#sec-gtex-lr` | ch10 |
| Mechanism to protein terminus (TSS vs splicing vs frameshift) | PRO-* | ch11 | `#sec-what-changes` | ch1, ch6, ch12 |
| UTR-only isoforms: 5' UTR and translation efficiency | PRO-* | ch11 | `#sec-utr-only` | ch1, ch4 |
| UTR-only isoforms: 3' UTR, stability and miRNA access | PRO-* | ch11 | `#sec-utr-only` | ch1, ch5, ch8 |
| Whether an annotated isoform is translated at all | PRO-* | ch11 | `#sec-is-it-translated` | ch2, ch9 |
| RPS24 microexons and the C-terminal lysines | PRO-* | ch11 | `#sec-rps24` | ch6, ch7, ch8, ch12 |
| Measuring proteoforms (top-down, targeted proteogenomics) | DRG-* | ch12 | `#sec-measuring` | ch5, ch9 |
| Isoform-selective approved drugs (CLDN18.2, FGFR2b) | DRG-* | ch12 | `#sec-isoform-selective` | ch2, ch6 |
| Isoform switching as acquired resistance | DRG-* | ch12 | `#sec-resistance` | ch6 |
| Emerging proteoform-selective modalities | DRG-* | ch12 | `#sec-modalities` | ch6, ch7 |
| Proteoform medicine as a programme | DRG-* | ch12 | `#sec-programme` | ch9, glossary |

## The closing chapter is an explicit exception to the one-home rule

`chapters/13-accounting.qmd` restates figures that belong to chapters 6, 8, 9,
10, 11, 2 and 1. That is the point of it: the book states the thesis one study
at a time and never totals it, which is the fault it charges the 95 per cent
figure with. One chapter has to put the figures in one place.

The exception is bounded. The closing chapter adds no new source and no new
number. Every row restates a figure its home chapter states in full, in the
unit the source used, and names that home section. It must not compute a range,
an average or a total across rows, because the rows have different
denominators, different assays and different units, and the leads in
`research/10-variants-qtl.yml` record that these fractions must not be
averaged. A row carries the provenance of its source, so a preprint or an
abstract-only figure says so in the table itself.

If a number in that chapter disagrees with its home chapter, the home chapter
is right and the table is the bug.

## Sources recorded in more than one area

Each of these has one bibkey, verified consistent by `scripts/verify_claims.py`.
Where two areas anchored different lines of the same paper, both anchors are
kept in the records and the prose cites the paper once, from its home chapter.

```
glinos2021transcriptome              05, 09     preprint only in this corpus
gonzalezporta2013dominanttranscript  01, 02
inamo2024trails                      08, 09
joglekar2024singlecell               05, 08     different lines in each
nagura2025longread                   05, 10
pan2008deepsurveying                 02, 04
reese2023encode4                     05, 09     preprint only in this corpus
tardaguila2018sqanti                 01, 05
wang2008alternative                  01, 02, 04
```

## What was actually read, and in which version

The preface says every statement traces to the lines it was read from. For a
large minority of sources those lines are an abstract, and for seventeen the
document is a preprint. Counted 2026-11-22, and regenerable:

```
# preprint-only in this corpus (emitted as @misc by build_bib.py)
grep -c '^@misc' references.bib

# distinct sources whose claims are all abstract_only
python3 - <<'EOF'
import yaml, pathlib
ab = {c['source']['bibkey'] for p in pathlib.Path('research').glob('*.yml')
      for c in (yaml.safe_load(p.read_text()).get('claims') or [])
      if (c.get('evidence') or {}).get('text_access') == 'abstract_only'}
print(len(ab)); print(*sorted(ab), sep='\n')
EOF
```

**Seventeen sources are preprint-only here.** `aguet2019gtex`,
`chang2025isoform`, `cummings2016musclernaseq`, `french2020asnmdsurvey`,
`glinos2021transcriptome`, `hong2019dscamsplicingbias`,
`jaganathan2026spliceai2`, `kolev2026transsplicing`, `liu2025transcriptional`,
`magadi2025rps24`, `mantri2026splice`, `reese2023encode4`,
`saferali2026framework`, `su2025splisosm`, `tzaban2025rna`,
`walker2023application`, `zheng2026isopedia`. The bibliography emits them as
`@misc`, the prose must not describe them as published, and every number taken
from one needs re-checking against the peer-reviewed version.

Two of those have a published version the corpus does not hold:
`cummings2016musclernaseq` appeared in Science Translational Medicine in 2017,
and `glinos2021transcriptome` in Nature in 2022. Preprint-only in this corpus
does not mean unpublished.

`aguet2019gtex` deserves separate notice. GTEx v8 is here only as the 2019
preprint, and chapter 10 rests a large share of its argument on it: VAR-004,
VAR-006, VAR-007, VAR-008 and VAR-024 were all read from preprint lines.

**Nine sources were read in one version and are cited as another.** The record
and the bibliography carry a journal DOI, but the lines read were a preprint:
`kerry2024rps24hypoxia` (FEBS Letters), `betz2024mycorrhizal` (Nature
Communications), `alkhafaji2024highthroughput` (Nature Biotechnology),
`abood2024longread` (AJHG), `islam2026ezh2` (Genes & Development),
`patowary2024neocortexisoforms` (Science), `cohen2025whole` (Cell), plus the two
above. This is a provenance defect no gate can see: `verify_claims.py` checks a
quote against the document it was taken from, which is the preprint, and
`build_bib.py` emits the journal. Either confirm each number against the
published text or cite the preprint.

**Forty-two sources are abstract-only**, and none appears with fuller access
anywhere else in the records. Fifteen are pre-2000 and fall under the corpus
limitation recorded in `research/04-technology-arc.yml`. The other twenty-seven
do not, and they are concentrated:

```
04-technology-arc      18
02-animals             15
07-neuro-mendelian      5
06-cancer               2
03-plants-fungi-other   1
10-variants-qtl         1
12-proteoforms-drugs    1
```

Chapter 2 is the worst case and STYLE.md names it the reference implementation.
Its Dscam1 section stands on abstracts for homophilic binding, stochastic
expression, the docking and selector mechanism, the 22,176-isoform allele, the
dendrite self-avoidance result and the splicing-bias result; both CD45 sources
are abstracts as well. Chapter 6 calls the H3B-8800 phase 1 outcome "the
counterweight to everything above" from an abstract. ENDEAR's 37 of 73 and
SpliceAI's 9 to 11 per cent are abstracts too.

Chapters 2 and 4 now say so in their first-draft callouts. The ordered fix is
full text for chapter 2 first, then chapter 7, then chapter 4, whose
abstract-only count is largest but whose claims are mostly historical firsts
rather than live quantities.

## Changes made while drafting

The reading order was changed once chapters 11 and 12 existed. Those two were
appended as new parts, which left chapter 12 closing on a section called "Where
this leaves the argument" with two more chapters after it, and left the book
ending on reference-annotation policy.

The order is now 1, 2, 3, then 4, 5, 9, 8, then 11, 10, then 6, 7, 12: the tree
of life, then measurement and what it produced, then what an isoform difference
does to a protein, then variation, disease and targeting. Measured on
cross-chapter `@sec-` links, forward references fall from 13 to 11. Three
dependencies that previously pointed forward now point back: chapter 11 on
chapter 8's single-cell 3' ends and compartment result, chapter 11's
`#sec-is-it-translated` on GENCODE's own admission in chapter 9 that its coding
annotation is permissive, and chapter 5 on the brain atlas.

Reading order lives in `_quarto.yml` and not in the filenames, which record the
order chapters were added. Do not renumber files to match.

Two rows moved once the chapters existed.

The B-cell isoform-QTL result went to chapter 5 rather than chapter 10. It is
the strongest single demonstration that a long read answers a question a short
read cannot, so it closes that chapter; chapter 10 refers to it when it reaches
isoform-level QTLs rather than restating the figures.

The droplet-versus-full-length chemistry comparison moved from chapter 8 to
chapter 5 `#sec-sc-chemistry`, which is where this table already assigns
single-cell chemistry. It had been sitting in chapter 8's limits section, framed
as a caveat about droplet data, which left the book arguing hard for long reads
in bulk and leaving the single-cell case implicit. The same figures read as a
capability where they now sit, and chapter 8 points at them. The Saferali
counter-result moved with them, because it qualifies that comparison and nothing
else.

The single-cell long-read row was split. Chapter 5 keeps the chemistry and what
it costs. What was found with it, which is the Joglekar brain atlas and the
CD8 T cell atlas, belongs to chapter 8 with the rest of the single-cell
biology.

## Checked after drafting

Two rows needed correcting once every chapter existed.

The CD8 T cell atlas claim was assigned to chapter 8 and had not actually been
written there. It is now in `#sec-isoform-only` with the rest of the
isoform-only evidence.

The prevalence row said chapter 2 owns the 95 per cent figure. Chapter 4 also
states those numbers, and that is deliberate rather than a duplication: chapter
2's aside is about what the figure counts and under which thresholds, while
chapter 4 is about how it was obtained, which is the provenance chain through
EST and cDNA data and the sigmoid extrapolation. Chapter 4 points at
`#sec-how-functional` for the conditions rather than restating them.

## Procedure while drafting

Write back-references as you go. Leave forward references until every chapter
exists, then add them in one pass, because a `@sec-` that points at an unwritten
chapter renders as a broken link and Quarto does not fail the build over it.

## Boundaries for the two protein-level chapters

These were fixed before either chapter was drafted, because four of their
topics already had homes and would otherwise have been written twice.

**Chapter 1 keeps the taxonomy.** `#sec-ends` states where isoform differences
sit: that alternative polyadenylation yields isoforms with no splicing
difference, that tandem 3' UTR choice and an upstream poly(A) site have
different consequences, and that splicing explains a minority of
tissue-dependent isoform differences. Chapter 11 does not restate any of that.
It starts from the consequence instead: what the difference does to the protein,
and what it does when there is no protein difference at all.

**Chapter 5 keeps isoform stability as a measurement.** That isoform-level
stability cannot be estimated from short reads, and that individual isoforms of
one gene do not share a stability, belong to `#sec-ends`-adjacent material in
chapter 5. Chapter 11 cites the regulatory mechanism, not the method.

**Chapter 8 keeps single-cell three-prime ends.** `#sec-sc-apa` owns the
cell-type 3' UTR switching numbers. Chapter 11 refers to it.

**Chapter 2 keeps the functionality argument.** `#sec-how-functional` owns the
three-way disagreement about how much alternative splicing matters. Chapter 11's
`#sec-is-it-translated` adds only the protein-level evidence that bears on it,
and points back rather than re-running the argument.

**Chapters 6 and 7 keep their therapeutics sections.** `#sec-drug-targets`,
`#sec-cancer-therapeutics`, `#sec-sma`, `#sec-dmd` and `#sec-nof1` stay where
they are, because the glossary and several chapters already point at those
identifiers. Chapter 12 cross-references them and adds only what is new:
isoform-selective biologics, resistance by isoform switching, the measurement
problem at the protein level, and the forward programme.

## One verdict needed reconciling

Chapter 6 closes by saying the isoform-level view of cancer "has changed what
counts as a driver. It has not yet changed what counts as a treatment." That
was written from a corpus in which the splicing-modulator trials had failed and
the isoform-defined targets were MET exon 14 and AR-V7.

It does not survive the chapter 12 material. Zolbetuximab plus chemotherapy is
approved for CLDN18.2-positive gastric and gastro-oesophageal junction cancer,
and CLDN18.2 differs from CLDN18.1 by an isoform-specific first exon. That is an
approved drug whose epitope exists in one isoform of a gene and not the other.
The verdict in chapter 6 is therefore narrowed to the claim it can carry, which
is about splicing-modulator therapy specifically, and chapter 12 states the
counter-case.
