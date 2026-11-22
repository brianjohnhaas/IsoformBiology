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

## Three sources are preprints

`reese2023encode4`, `glinos2021transcriptome` and `magadi2025rps24` exist in
this corpus only as preprints. A fourth, `kerry2024rps24hypoxia`, was read as
its preprint although the FEBS Letters version exists and is what the
bibliography cites; its numbers need the same re-checking. The research records say so, the bibliography emits them as `@misc`,
and the prose must not describe them as published. Every number taken from
either one needs re-checking against the peer-reviewed version when it appears.

## Changes made while drafting

Two rows moved once the chapters existed.

The B-cell isoform-QTL result went to chapter 5 rather than chapter 10. It is
the strongest single demonstration that a long read answers a question a short
read cannot, so it closes that chapter; chapter 10 refers to it when it reaches
isoform-level QTLs rather than restating the figures.

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
