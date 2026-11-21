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

## Two sources are preprints

`reese2023encode4` and `glinos2021transcriptome` exist in this corpus only as
preprints. The research records say so, the bibliography emits them as `@misc`,
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
