# Chapter 9 pass: cross-cutting items from agent reports

## From agent C (long-read catalogues) — a figure in the live chapter is wrong

### The published version of the chapter's anchor dataset has a different number
**The GTEx long-read paper's published version IS in the corpus**, as an
abstract-only record, found by `grep --source abstracts` on the title after
`lookup` failed. The brief's advice was right and the earlier lead was wrong.

**The published abstract says "just over 70,000" novel transcripts for annotated
genes. The preprint says 98,372.** The chapter prints the preprint figure as
"just under 100,000", and **the published paper does not support it.** The
protein validation changed too: published "10 per cent of novel transcripts"
against the preprint's "a similar proportion of novel and annotated".
CAT-221, CAT-222 and CAT-223 carry all three.

**ENCODE4 has no journal version found**, after a corpus grep on the exact title
returning 65 citing papers, every one citing it as a preprint, including papers
ingested in 2026 and one co-authored by a GENCODE lead, plus a SQL sweep over an
author's whole record set. Scoped as not found rather than proven absent.

### A metadata conflict to reconcile at merge
All six new GTEx records carry the **journal** doi under the existing bibkey,
with `preprint: true` on the four read from preprint lines. **The chapter's
existing CAT-038 and CAT-039 still carry the preprint doi under that same
bibkey**, and two dois under one bibkey renders as whichever the builder reads
last. The same inconsistency exists for the Isopedia records, where the new ones
set `preprint: true` and the existing CAT-031 to CAT-033 do not.

### The chapter's novelty range is a corner-to-corner read of a grid
**CAT-273**: the same transcript sets give 26.7 to 45.5 per cent novel against
one annotation release and 42.9 to 51.6 per cent against another, so the novel
fraction moves by up to 16 points **on the reference alone**. The chapter's
existing "27 to 52 per cent" at CAT-032 turns out to be the corners of that grid,
**part platform and part reference**, and the chapter presents it as one quantity.

**CAT-275** is the sharper companion: the two reference annotations agree on only
21.95 and 30.55 per cent of their own transcript content.

### Three more results that make a novel fraction a policy output
- **CAT-241 against CAT-242**: one assembly scored by two classifiers gives 36.5
  per cent known against 28.32 per cent.
- **CAT-248**: using the same tool and annotation raised one catalogue's overlap
  with another by 33.8 per cent.
- **CAT-262 and CAT-263**: 58 per cent of one novel class and 73 per cent of
  another are single-sample against 19 per cent of full matches, and short reads
  on the same RNA detect 89, 62 and 41 per cent by class.

### The ceiling measurements the chapter had one of, now eight
Second donor, second protocol on the same RNA, second cohort, second platform:
CAT-233 to CAT-240, CAT-243, CAT-249 to CAT-251, CAT-254, CAT-260.
**CAT-235 is the one to pair with CAT-234**, because those authors state that
their own rescue rule inflated their reproducibility figure.

**No second-laboratory reproduction of a catalogue was found.** That was the
brief's most-wanted record; what exists is eight weaker designs, and the lead
says which is which.

### Independence inside one contrast
The chicken-against-cattle comparison, 47 per cent novel loci against about 6,
**is the same laboratory**, with five shared authors, which is what makes the
contrast readable rather than suspect. But **the bovine figure in the chapter's
existing CAT-049 and that paper's restatement of it are different quantities**,
so the chapter must not put 61 and 6 per cent side by side.

### The ancestry result now has its denominators, and survives two controls
CAT-265 to CAT-272: 43 cell lines over 8 populations, 59 per cent of 380,519
candidates discarded by class-dependent filters, a spike-in ground truth showing
5.5 per cent of spike-in reads with novel splicing, 73.5 per cent of the final
set already annotated, population-specific transcripts at **1.55 per cent**, and
**the ancestry result surviving both depth equalisation and a change of
reference annotation.** Personalised genomes add 3.6 per cent more
novel-splicing transcripts, most in African samples, 44.4 per cent attributable
to alleles at splice sites.

### Self-contradictions inside sources, recorded
One catalogue gives an agreement figure two ways on two lines and a read count
two ways; another gives two different new-gene-body counts on adjacent lines.

### A ruling the records reviewer must make
**Seven records share a `(doc_id, lines)` anchor with a sibling**, and one shares
an anchor with an existing record. SCHEMA writes that exception for abstract-only
records, and these are **long full-text paragraph lines with non-overlapping
quotes and different findings.** The agent flagged it as the project's call
rather than deciding it.

## From agent E (what a catalogue costs) — THE CHAPTER'S CLOSING ARGUMENT IS WRONG IN ITS DIRECTION

### The record behind it overstates its source, and the measurements point the other way
The chapter closes by saying a maximal annotation helps gene-level read
assignment and discovery while **degrading** isoform-level quantification by
spreading reads across near-identical models. Three things undo that:

1. **CAT-047 overstates its own source.** That line says a comprehensive
   annotation **"may instead hinder"** isoform-level quantification **and cites
   nothing.** CAT-047 says "degrades".
2. **No measurement found in this pass varies catalogue size and shows an
   isoform-level cost.** **CAT-351 is the bound**: 50 per cent surplus models cost
   about **1 per cent** of correlation, while 50 per cent missing models cost
   **10 per cent**. CAT-388 and CAT-390 agree, and **CAT-349, CAT-355 and CAT-357
   find the larger or extended annotation more accurate**, including one case
   where extending an annotation with sample-supported models **reduced**
   quantification error.
3. **CAT-349 is the record the chapter needs**: the same data against two
   annotations with experimental truth, giving 0.374 and 0.565 against 0.722 and
   0.804. **CAT-350** shows that merely editing transcript ends moved it almost as
   far, and tenfold at one gene. **CAT-389** is the honest complication, since the
   larger annotation scored **below** its authors' own smaller earlier one, for
   UTR-end variation.

**So the chapter's conclusion should be rewritten to the measured shape: the
cost of omission is about ten times the cost of surplus, and the isoform-level
cost of surplus has not been measured at all.**

### A figure in the live chapter conflates two statistics
The chapter says "those authors judged only about 42,000, six per cent, to be
functional loci." **That figure is CHESS's final total gene count, 42,611, not
the output of a filter.** The filter is CAT-371, and a separate statistic, 41,979
novel loci bearing at least one intron at 6.3 per cent, **rounds to the same two
numbers with a different denominator.** Do not conflate them.

### The exclusion policy's justification does not measure what it is cited for
**CAT-381** is a catalogue's exclusion policy, and it cites CAT-341 to CAT-345 as
its justification. Those records **share a first author and both senior authors
with it**. Worse for the argument: **that experiment held the annotation fixed
and varied the reads**, so it does not measure what excluding transcripts buys.
Anyone writing "the catalogue excludes them because they were shown to mislead
software" must carry both facts.

### Two sources the chapter reads as agreeing actually overlap
**CAT-365 to CAT-368 are GENCODE assessing GENCODE**, and that paper's first
author **co-authored the review the chapter's closing argument rests on.** The
chapter currently reads as though two independent sources agree about the
trade-off.

**Nearly every comparison in this area has a stake**: four tools or annotations
assess their own authors' work, and in one the winning annotation is the one
shipped inside the authors' own package. **CAT-388 is the only comparison written
by authors with no stake in either the annotation or the quantifiers.** And the
two best-known "bigger annotation is worse" results **share two authors**.

### The clinical cost is now measured, which the chapter had nothing on
**CAT-362**: over 80 million variants, loss-of-function agreement **44 per cent**
between two transcript sets. **CAT-364 is the control that isolates annotation**,
since swapping the tool instead gives 65 per cent. **CAT-370 is the case**: one
variant is intronic on the canonical transcript and coding on one added to a
reference in April 2016 and absent from both pipelines' builds.

**CAT-362 against CAT-367** is a real dispute, 44 per cent against about 30 per
cent conflict, with the later authors' own reconciliation, and **the two are not
complements because the papers count different things.**

### Does isoform count drive quantification error
**CAT-346 says yes** and **CAT-347 says no**, far less important than length or
exon count. The two author sets share nobody, and CAT-346's own source explains
why it disagrees with a third study. **CAT-353 and CAT-389 side with CAT-347**:
annotation choice mattered without transcript count mattering.

### Two clean negatives
- **No quantitative projection of transcripts per protein-coding gene**, after
  keyword greps on several phrasings and an evidence query over 264 passages. The
  qualitative "tens or even hundreds" remains the only anchored statement.
- **No curation cost in money or person-years.** CAT-382 to CAT-384 are the whole
  of what exists: a manual gold standard limited to 50 loci per species, one flow
  cell against all of one year's public human sequence, and those authors' own
  statement that manual annotation of further genomes is not practical.

### Method note worth keeping
That agent wrote a check asserting **every digit in every claim occurs on that
record's cited lines**, and **it caught 28 claims carrying a release or a
denominator from an uncited line.** That is the same defect class the chapter 4
corrections found seven of, and it is worth promoting into the project's gates.

## From agent B (annotation as process)

### A lead in chapter 1's file is now half-closed
**CAT-181** gives the counts chapter 1's lead said no source states: **33,750
retained-intron and 20,933 NMD transcripts in GENCODE v41**, from a third party
rather than from the project's own tables. **The processed-transcript half
remains open**, because GENCODE's release tables are tabulated **by gene
biotype**, so the headline transcript totals cannot be broken down that way.

### Curation against automation, which the chapter most needed
**CAT-200**: in the community assessment, **no method predicted more than 45 per
cent of manually annotated coding transcripts exactly**, while gene level was far
easier at 71.6 per cent sensitivity and 80.8 per cent specificity (CAT-201).
**CAT-202 is the bound, from the organisers themselves**: the comparison is
partly circular, because the methods that best reproduced manual curation were
built on the same evidence the curators used.

**CAT-205 is the sharper record**: a later exercise scored the **curators'
rejections**, and found 81 and 63 per cent against **two of nine, both later
shown to be mismapped.** **CAT-207** is the project's own experimental audit: 82
per cent of 5,871 low-confidence junctions confirmed, against 16 per cent from
deep untargeted sequencing. **CAT-206** records that the automated pipeline
publishes **a stopping criterion rather than an agreement rate**, and **no
agreement rate between it and manual curation on the same loci exists**, which
may simply not be published.

### A measured answer to the direction question
**CAT-218**: **an older annotation release beat a newer, larger one** on three
ground truths, and **CAT-219** gives the mechanism, a mappability of 0.58 for the
basic set against 0.44 for the full release.

### A polarity trap in the clinical figures
**CAT-214 reports 44 per cent agreement** and **CAT-216 about 30 per cent in
conflict.** **The like-for-like pair is 56 against 30 per cent disagreement**, and
both records carry the warning. CAT-216 is also **that geneset's own authors
comparing their own geneset.** **CAT-215 is the control**: swapping the tool
instead of the transcript set gives 65 per cent.

### Two figures that look contradictory and are not
**CAT-164 against CAT-208**: 92.5 per cent of transcripts carrying a curated
status against about 45 per cent being model records. **The first counts only the
known subset and the second counts both**, and the chapter must say so if it uses
both. Likewise **CAT-181 against CAT-180**, two counts for one release under
different scaffold rules and different counting units, which **must not be
divided into each other.**

### Deletion and churn, which the chapter had only in aggregate
An average of **2,160 transcript annotations deleted per release** with one
release dropping 11,410 (CAT-184); **56,095 gene identifiers eliminated**, 285 of
them still in the naming authority (CAT-186); **the vocabulary itself moved**,
with 70 biotype terms of which 17 were used in every release and 52 dropped at
some point (CAT-187); and churn under a stable headline, 90 new against 30
deleted protein-coding genes with 89 promoted and 63 demoted (CAT-189).

**No published account exists of a reference model deleted and later restored.**
CAT-185's reversals are **biotype reassignments returning to an earlier label**,
and the chapter must not call them restorations.

### Translation evidence as policy, with the standard of proof stated
**CAT-196**: coding status requires only that **coding be the most likely reading
of the evidence**. **CAT-191** records why the projects kept these out and the
circularity they name; **CAT-192** gives recurrence as the test, 3,085 of 7,264;
**CAT-193** is the projects' own statement that **non-replication does not make
the other 4,179 false**; **CAT-195** that only 2.4 per cent of the replicated set
is conservation-positive; and **CAT-197** that mass spectrometry was **recorded as
metadata at face value rather than used as a gate.**

### A measured error rate across three references
**CAT-212**: selenoprotein misannotation at **88 per cent in one reference, 24 in
another and 94 in a third**, with **CAT-213** showing what a dedicated pipeline
buys.

### Three internal inconsistencies, recorded
One source gives its common-gene count two ways and describes a percentage
against two different denominators; another gives its vocabulary size as 70 and
71. And one source's "lncRNA" class **pools 23 sub-biotypes including retained
intron and processed transcript**, which is now in three claims, because without
it the reassignment figures read as protein-coding transcripts becoming long
non-coding RNAs.

### The id range bound again
**About 15 further verified, line-anchored findings were displaced into leads
purely because the range ran out**, including a six-step inclusion funnel, a
variant-concordance asymmetry and biotype-stratified domain-loss figures. Each
lead carries the doc id, the lines and the numbers.

## From agent D (benchmarking) — the answer to the chapter's open question, and a circularity

### The question the chapter has been asking without an answer
Whether one tool's extra transcripts are false. **CAT-302 answers it directly:
two well-performing tools overlap little because they find *different true
positives*.** Not one right and one wrong. **CAT-306** supports it from the other
side: overlap is higher for genes and junctions than for intron chains, and much
of the disagreement is recovered when two high-output tools are dropped.

**The spread itself**: up to tenfold in model counts with little pairwise
overlap (CAT-304); **detection by exactly one pipeline is the commonest class**
across 47 submissions on one sample (CAT-305); long-read coverage of a tool's own
reported models runs from 45 per cent to above 98 by tool (CAT-307); and one
sample gives **about 90,000, 13,000 and 16,000 transcripts under three
pipelines** (CAT-308).

### A circularity the chapter must declare
**CAT-337: the classifier that assigned the structural category of every model in
the consortium exercise shares four authors with that exercise.** **So every
structural-category count the chapter quotes from it comes from one group's
classifier.** Write it as such.

**And the same classifier's filter was evaluated on its own training labels.**
**CAT-310 and CAT-311**: trained with full-splice-match as true and
noncanonical-novel as false, it scores **99.54 per cent area under the curve on
those labels and 82.41 on the PCR-validated set**, with **false discovery of 11
per cent against 53.3 and 58.8.** That is the gap between a filter's self-report
and its performance against experiment.

### Two filter findings that cut against the chapter's current framing
- **CAT-317**: filtering **excluded whole genes despite read support**, and a
  rescue step **put 11,599 of the removed models, 89 per cent, back**, 94.1 per
  cent of them onto reference transcripts, **adding 2,884 genes.**
- **CAT-312**: **short-read support is a weak filter.** 543 of 597 novel
  noncanonical junctions **had short-read support.**
- **CAT-318 is the honest trade**: on a deliberately corrupted reference, 94 per
  cent sensitivity against 32 per cent precision unfiltered, and filters buy
  precision with sensitivity.
- **CAT-315 is the framing to avoid**: it reads a falling novel share as better
  models, **which presupposes most novel calls are artefacts**, and CAT-302 bears
  the other way.

### The gold standard is 50 loci, and they are not random
**CAT-290**: the manual gold standard is **50 human and 50 mouse loci**, limited
by curation speed. **CAT-291 is the record that matters**: those loci are random
**within constraints** that include being compact, excluding long introns,
capping reads, maximising alternative splicing, and **pre-screening on short-read
intron support.** That last constraint is **circular for any question about novel
discovery.**

**CAT-293 is the good news in the same exercise**: models that failed PCR were
re-reviewed **and the annotation upheld.**

### Every ground truth, with what it cannot test
**CAT-284**: the spike-in panel has limited complexity and **its annotation was
known to submitters**, so it **cannot evaluate novel predictions.** **CAT-285**:
simulation reproduces error profiles, **not library-preparation bias.**
**CAT-286**: against a reference annotation the truth **"is not entirely known"**
and exhaustive validation is not possible. **CAT-287**: the long unspliced
spike-ins measure **end variability, not splicing.** **CAT-288**: tools reported
**28 to 136** of the spike-in transcripts above zero. **CAT-334**: no endogenous
truth exists at all, which is why one benchmark used two proxy metrics.

### A discrepancy in the book's own records, now resolved
**CAT-328 gives 6 of 30 for novel-not-in-catalogue validation; the existing
CAT-028 gives 50 per cent.** **The gap is partly a criterion difference rather
than a different sample**: adding the nine transcripts that amplified from one
cDNA preparation but failed the other control gives **15 of 30, which is the 50
per cent.** Both numbers are real and the chapter can now state why they differ.

### And a contradiction inside the consortium's own words
**CAT-321 against CAT-323**: the results text says the validated isoforms were
**"randomly selected"**, and the methods say they were chosen
**"semi-systematically"** with expression above 10 TPM prioritised. **Both are
that consortium's own words about the same experiment.** **CAT-324** shows why it
matters: validation rate tracked abundance in both groups.

**CAT-325** is the one to handle carefully: a platform-preferential group
validated completely, **and those authors decline to generalise from it.**

### Quantification against identification
**CAT-331**: an inaccurate annotation gives **2.74 times the error of the
long-read tools and 3.27 times its own error with an accurate one.** **CAT-332 is
the concrete version**: swapping a 160,000-transcript reference for an
11,970-transcript sample-specific one **changed the dominant transcript for 1,433
of 5,409 genes**, and in 470 of those **the new call was the manually curated
one.**

### Standing caution
**Every statement that the consortium exercise settled something needs CAT-281
and CAT-282**: no aligner was benchmarked at all, submissions were
self-configured, modalities were self-chosen so the data are unbalanced, and
prominent tools were absent.

## From agent A (representative transcripts) — a circularity in a live claim, and the best record in the chapter

### The circularity: two agreement figures the chapter cites are agreement with an input
**CAT-140 is the record to read before writing any agreement sentence.** The
pipeline that nominates the representative transcript **takes concordance with
one of those other conventions as an explicit scoring component**, and **prior
clinical-reporting use is the top-ranked parameter** of the companion pipeline.

**So the chapter's existing CAT-022 (agreement with that convention) and CAT-130
(agreement with clinical submission practice) are both partly agreement with an
input.** Neither is an independent check, and the chapter currently reads as
though they are.

**CAT-150 is a third pattern of the same kind**: a cross-database disagreement on
267 translations, **resolved mostly by the other database moving to match.**

### The best single record: the alternative rule is unstable against itself
**CAT-148**: ranking transcripts by expression gives **19,591 top-ranked genes in
one data release and 18,516 in the next, with only 13,542 unchanged and 4,974
reassigned.** So the obvious alternative to a curated representative transcript
**fails the same stability test** the chapter applies to curation.

**CAT-144 is the companion**: of the transcripts that differ from the
expression-ranked choice, **1,010 match under a 54-tissue panel and not under a
9-tissue one.** Much of the apparent disagreement is the tissue panel.

**CAT-121 is the positive result the chapter needs beside it**: 12,375 of the
representative transcripts rank first by expression, and **only 125 fall outside
the top ten.**

### The cost of release churn, now quantified in expression
**CAT-138**: for **171 of 497 medically relevant genes, 34.4 per cent, isoforms
added between two releases carry more than a quarter of the gene's expression in
all nine tissues measured**, and 50 genes exceed three quarters in at least one.
**CAT-139 is the case**: one transcript new between 2019 and 2023 is **100 per
cent of that gene's expression in one brain region** and above 80 in two more.

### A trap: two different quantities are both called protein-coding transcript counts
**The release tables count by *gene* functional biotype** — 167,599 and 170,270 —
so **every transcript at a protein-coding gene whatever its own biotype**
(CAT-115, CAT-116, CAT-117, CAT-146). **One study counts transcripts whose *own*
biotype is protein-coding** — 79,431 rising to 89,374 (CAT-114). **The gap is
about 82,000 models** in the retained-intron, CDS-not-defined and NMD biotypes.

**Any table that puts these side by side must print each one's counting rule, or
it will read as an error.** And CAT-142's 87,814 sits on the second series, not
the first.

### The chapter's own thesis, demonstrated on itself
**CAT-102 against the existing CAT-017: coverage of 78 per cent and 97 per cent,
one month apart.** Both from the same annotation group, so not independent, and
**no source read states how one release counter maps to the other** — the
annotation release, the convention version and the reference annotation release
are three separate counters. CAT-149 and CAT-110 then give 99.1 and above 99 per
cent at later versions. **This is the chapter's best worked example of its claim
that a count without its release is not a number.**

**And the same trap in miniature**: the clinical-supplement set is **55 genes at
one version, 58 transcripts at the next, 64 transcripts at the one after.** Three
version-labelled points, **two of them comparable. Do not join them with a
line.**

### Two leads closed
- **The Ensembl Canonical rule is now anchored in body prose** (CAT-101): one
  default transcript for every gene in every species, same ranking pipeline, so
  identical wherever the other convention has an entry. The agent **refused the
  figure-legend version** that states the same rule, which is correct under this
  project's own ban on captions.
- **The 83,725-against-87,852 inconsistency is anchored** (CAT-118): one figure
  cited from earlier reports, the other derived from that paper's own
  integration. **No winner picked.**

### A negative that shapes the chapter's figure
**No per-release transcript count series exists in prose anywhere.** All ten
annual database papers from 2015 to 2024 were grepped, and **none carries a human
gene or transcript count in prose**; the statistics are figures. The same is true
of the annotation project's own reports. **So a growth curve has to come from the
distribution files, which makes it the book's own computation rather than a cited
one**, and must be labelled as such.

**Also not found**: a replacement rate for either convention between releases.
The comparison exists — one paper **describes exactly that analysis**, binned
into identical, UTR-only, CDS-changed and no-equivalent-pattern — **but its
result is in supplementary material, not the body.** Only policy exists in prose,
not behaviour.

### What the selection rule costs, measured three ways
**CAT-122**: the principal coding exons hold **99.03 per cent** of pathogenic
variants. **CAT-123** is the gradient: wholly alternative coding nucleotides take
2.43 per cent of the sequence and **1.6 per cent of variants, falling from 2.3
per cent of benign to 0.37 of pathogenic and 0.05 of expert-reviewed.**
**CAT-125** is the comparison that matters: **47 misses against 143 for the
longest-coding-sequence rule**, a threefold difference. **CAT-124**: 67 of 33,736
missed before curation.

**CAT-128 and CAT-129 are the non-clinical cost**: a **1 to 2.5 per cent
false-negative rate** in a knockdown screen from alternative start-site use, and
**17 per cent of genes having a start site within a kilobase of another gene's.**

### Mechanical
**Eleven new source blocks carry author strings in the corpus format rather than
the project's.** `resolve_metadata.py --write` must run over the merged file
before the bibliography is built, or it will carry two author formats.
