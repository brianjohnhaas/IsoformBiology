# Chapter 10 pass: cross-cutting items from agent reports

## From agent B (splicing QTLs) — three live claims in the chapter need qualifying

### 1. The 52-per-cent overlap is partly the authors' own phenotype artefact
**VAR-178**: those authors attribute their 52-per-cent figure **partly to their
own phenotype including transcriptional termini**, and **VAR-177** supplies the
mechanism, since 58 per cent of their splicing QTLs involve first or last exons
and UTRs against about 34 per cent internal exons. **Without VAR-178 the chapter
presents a phenotype artefact as a biological result.**

### 2. The chapter prints a figure-caption explanation as a biological finding
The chapter states the near-nil correlation between allelic imbalance and
splicing-QTL genotype as a result about biology. **That consortium's own figure
caption attributes it to the difficulty of defining splicing direction under the
quantification method used.** A figure caption is not citable in this project, so
the sentence has to be requalified or the statement sourced from the published
supplement. **This is the single best bounding sentence in the corpus for that
section and it cannot be cited as it stands.**

### 3. The independence argument has two independent bounds
**VAR-205** argues the apparent independence of the two maps is an artefact of
comparing **lead variants**, since the top splicing QTL is often a productive
switch and genes have several expression QTLs. **VAR-219** decomposes the
direction of causation: of 155 overlapping splicing QTLs **only 21, about 14 per
cent, are causal, while about 57 per cent are reactive**, with the splicing
change mediated by the expression change. **VAR-203** adds an odds ratio of 24.2
on transcription-rate effects. Neither says the chapter is wrong; both say its
strongest sentence needs a qualifier.

### The phenotype decides the catalogue, and one paper says so outright
**VAR-176**: "the splicing phenotype employed for sQTL mapping is a major
determinant of the resulting sQTL catalog", in those authors' words.
**VAR-170 is the matched-denominator record the chapter needs**: two splicing
phenotypes on the same 2,865 brain transcriptomes give 4,192 and 3,489
phenotype-specific genes, and **2,858 of the 5,113 shared genes are called
statistically distinct by the same test** the chapter uses for the
splicing-against-expression comparison. **So the chapter's 12,794 is the union of
two phenotypes.**

**The counterweight is VAR-172**: 399 of 491 lead transcript-ratio QTLs, 81.3 per
cent, are nonetheless significant in the intron-excision analysis. Cite the two
together; they bound each other.

### Ancestry: the measurement the chapter needs, and the asymmetry in the field
**VAR-214**: cross-population replication is π1 0.63 to 0.94 for expression QTLs
but **only 0.41 to 0.70 for splicing QTLs**, over six African populations and 599
individuals. **VAR-215 and VAR-190** show effect sizes barely differ where both
populations have a signal, so what changes is **which** QTLs are detectable.
**VAR-189 is the companion finding**: the field has quantified the ancestry gap
for expression QTLs at 8.3 per cent unobserved in Europeans and calls the
splicing case only "qualitatively similar". **VAR-186**: the brain map the
chapter leans on **excluded non-European individuals by design.**

### Four incompatible overlap figures are now in one file
52 and 3 per cent, 61 per cent, 11 per cent at a linkage threshold, and a median
46.2 per cent of **expression**-QTL credible sets with no splicing overlap, plus
two further non-comparable quantities. **The only matched-denominator comparison
available is inside VAR-170.** A lead spells out every denominator.

### Provenance, three answers
- **The keystone 2016 paper is still abstract-only**, by four routes on
  2026-11-23, with no authors and no journal in its metadata. **How its 2,893
  splicing QTLs were called cannot be stated from this corpus at all**, and no
  new record asserts it.
- **The GTEx v8 published version IS in the corpus** as an abstract-only record
  with a 2020 Science doi. The body is still unavailable, so ten records cite the
  2019 preprint.
- **The TOPMed work is now published too**, as an abstract-only record with a 2026
  Science doi, while nine records rest on the medRxiv preprint at medium
  confidence.

### Independence: one lineage carries three load-bearing things
Two sources **share an author**, and that group's own earlier paper describes the
2016 keystone work as its own. **So the keystone claim, the quantification method
most of the chapter's counts rest on, and the argument that the maps'
independence is artefactual all come from one lineage.** Five other sources share
no authors with it or with each other.

### A ruling needed
**VAR-178 shares a full-text anchor with the existing VAR-012**, different spans
and different findings. SCHEMA's one-line exception was written for abstract-only
documents and this is a long paragraph. `verify_claims.py` has no duplicate-anchor
gate, so nothing fails. If the shared anchor is unacceptable, **fold VAR-178 into
VAR-012 as an amendment, because it has to survive somewhere.**

### A readable in-corpus resource nobody has used
One paper's supplementary tables are present as `.md.lines` renderings and **are
readable**, and they hold numbers two records currently state only as "moderate".

## From agent D (clinical classification) — the chapter's reclassification figure points the wrong way

### Observed reclassification runs opposite to the chapter's projection
The chapter carries a **projection**: treating RNA evidence as one supporting
point would move 31 per cent of 16,965 variants of uncertain significance across
a threshold, **93 per cent of them to the benign side.**

**The observations run the other way.** **VAR-296**: 96 of 177, 54 per cent,
reclassified, with **48 per cent upgraded.** **VAR-299**: 30 of 38, with 18 up
and 11 down. **VAR-303**: 23 of 31, 74 per cent, to likely pathogenic.
**VAR-306**: 9 of 42 to likely pathogenic and **28 of 34 conflicting variants to
likely benign.** **VAR-307**: informative data in 96 per cent of 74 families.

**These are different denominators**, a whole database of uncertain variants
against variants selected for testing, and VAR-296's note forbids lining them
up. But the chapter currently presents the projection alone, and its direction is
the opposite of every observed series.

### The guideline wording changed in peer review, and it narrows a code
**The published version exists**, as an abstract-only record, found by grepping
abstract text for the subgroup's name **after the published title turned out to
differ from the preprint's by one word.** **VAR-282**: the preprint extends one
benign code to intronic and synonymous variants **and to missense variants if
protein functional impact has been excluded**; the published abstract names only
intronic and synonymous. The published body is not readable here, so a changed
threshold inside the paper remains possible.

**Mechanical consequence**: every new record carries the **journal** DOI with
`preprint: true` where the lines read are the preprint's, while **the existing
VAR-027 and VAR-028 still carry the preprint DOI under the same bibkey.** Two
fields on each, or the cross-file check reports one key with two DOIs.

### The calibration is not an external check
**VAR-291 to VAR-294 and VAR-327 share four authors with the recommendations
themselves.** **A sentence saying the recommendations "were later calibrated"
would imply an external check that did not happen.** One further author is on both
the recommendations and the inter-laboratory concordance records.

The calibration is still the chapter's best new material: likelihood ratios of
80.04 and 0.02 for the two bands over two reference panels, with **the middle
bands returning "no evidence"** on five and two reference variants, and
**VAR-293 and VAR-327 are the calibrating authors stating four ways their own
calibration misleads**, including circularity through the database its controls
came from.

### The threshold question has three answers in one period
**VAR-291 and VAR-292** derive 80 and 20 per cent bands with likelihood ratios.
**VAR-312** is a diagnostic laboratory publishing in the same period stating it
uses **no quantitative threshold at all** and decides case by case. A third uses
"residual full-length transcript present" with no percentage.

**And the aberrant fraction is a protocol property, which bounds the bands
directly**: 1.1 per cent rising to 7.0 with decay inhibition in one gene, 27 to
49 per cent in another system, against 80.6 per cent **unchanged** in a third.
**VAR-324 and VAR-325** close it: a variant with about 80 per cent residual
wild-type transcript is in a public database as likely pathogenic, and 15 to 18
per cent of one donor-substitution class retain residual wild-type transcript.

### The inter-laboratory record the chapter wanted, and the case that explains it
**VAR-321**: for the persistent differences between laboratories, **they had the
same data, including shared internal data, and 48 per cent of the differences
came down to how the functional data were applied.** **VAR-318 to VAR-320** give
the denominators: 6,169 shared variants, 88.3 per cent concordant, 724
differences in 148 genes, 211 of 242 resolved, and **no consensus on 31, of which
24 were medically significant.**

**VAR-323 is the case, and it is the best single record in the block.** One
variant sits under conflicting classifications because **the forward primer in
the RT-PCR behind the downgrade sat inside the skipped exon**, so the assay could
not see the skipping. A second group with a primer in a different exon saw it and
proposed reinstating the pathogenic call.

### How rarely the assay is even eligible
**VAR-308**: **7.6 per cent of reported variants, 152 of 1,987, were eligible for
RNA analysis at all**, and the uncertain ones among those are 5.2 per cent of
1,035. **VAR-300**: of 38 tested, 21 per cent did not move, three for
inconclusive RNA and five for want of any other evidence to combine with.
**VAR-313**: only 28 per cent of wild-type full-length constructs ever gave one
clean band.

### Source-internal inconsistencies recorded in notes
Two different counts of exon-trapping cases in one paper; eight abnormal
uncertain variants but nine reclassified in another; and one code written two
ways between a paper's text and its own table.

## From agent A (the colocalisation gap) — the chapter's headline is a union of three methods

### What the 8.2 per cent actually is
**VAR-101**: on the **same 147 genes**, the three colocalisation methods give
**4.8, 6.8 and 5.4 per cent**, and **the headline figure of 18 implicated genes
is the union of all three.** **VAR-102** is those authors' own statement that the
earlier 25-to-40-per-cent answers a different question. **So the chapter's
sharpest number is a union across methods that individually agree much less, and
the chapter presents it as one measurement.**

### The methodological control that is worth more than any of it
**VAR-157: colocalising height against height fails.** 66.2 per cent of credible
sets fall below a posterior of 0.01 and 48.9 per cent below 0.001, **and it is
not a power problem.** That is a positive control failing, and it bounds every
colocalisation fraction in the chapter.

**VAR-118** is the companion: that consortium's own methods say its results are
**"highly sensitive to the choice of prior"** and that the defaults were replaced.
**VAR-111** names prior enrichment as the one factor that can severely inflate
false positives, **VAR-112** reports that 22 of 25 applied papers used the
software defaults with only four allowing multiple causal variants, and
**VAR-108** puts realistic false-negative rates at 59.0 and 22.0 per cent by
class.

### The other direction, which the chapter has none of
**VAR-106 and VAR-107**: changing the **quantification resolution** raises the
colocalisation rate from 5.3 to 18.4 per cent at exon level, and to 24 per cent
combining five resolutions, in one cell type. **Changing the method does not do
that; changing what is measured does.** Different denominators, so not a direct
rebuttal, and the lead says so.

**VAR-109** is the third framing: across 4,091 traits, detected colocalisations
are **10.7 per cent of expected**, which is a dispute with the audit about what
the negative result means rather than about the number.

### Context dependence, which the chapter had nothing on, now with a counterweight
**VAR-135**: more than half of one cell type's expression QTLs appear **only on
stimulation**. **VAR-136**: 417 response QTLs, 3 to 18 per cent per condition, 13
to 51 per cent stimulus-specific. **VAR-140 and VAR-141** are the splicing
equivalent: 1,464 splicing QTLs with 9 per cent stimulation-specific, and of 235
stimulation-only ones, 34 at a trait locus and 12 at an immune disease.
**VAR-147 and VAR-148**: 3,155 context-dependent associations of which 2,022 have
**no static effect**, and 197 of 270 colocalised loci **not recovered
statically.**

**VAR-138 is the counterweight, from the same study as VAR-137**: only four loci
resolved by colocalisation across 33 traits. **And VAR-145 and VAR-146**:
environment-dependent allelic effects are **not enriched**, and in one cell type
**depleted**, among catalogued genes.

**VAR-139** is the mechanism that bounds the whole explanation: about 60 per cent
of stimulus-specific QTLs **already alter chromatin in the naive state.**

### Selection as an explanation, with numbers
**VAR-125, VAR-126, VAR-129, VAR-130**: trait genes are more constrained, 26
against 12 per cent, their QTLs sit closer to start sites, 43 against 22 per cent
within 10 kilobases, and the model is that **selection suppresses QTL discovery
at exactly the genes trait studies implicate.** **VAR-121** is the sharpest
single pairing: fine-mapped trait variants are in regulatory DNA at 86 and 68 per
cent, **yet only 20 per cent show an expression effect.**

### Independence: the critique and the figures come from the same statisticians
**The methodological critique of colocalisation and that consortium's own
colocalisation figures come largely from one group of statisticians**, by three
shared names across one block and three more across another. The audit **shares
three authors with its own predecessor**. Two context-mapping methods share an
author and **both reanalyse the same cohort.** **A paragraph treating any of
those pairs as independent voices would be wrong.**

### Numbers that do not reduce, and one preprint error resolved
One paper labels two ratios as 10.3 and 3.7 per cent where the actual ratios are
10.0 and 3.0, so the record omits the percentages and says why. One 61 per cent
is of a subset rather than the total. One paper's 9 per cent and its count **are
not the same set**, and the text read does not say which the percentage counts.
**And a preprint recommending two different priors in two places was resolved
against its published version**, which gives one in both; a 2026 correction to it
exists and was not read.

### No reply to the audit exists
A full-text grep on its exact title returns **100 reference-list hits and nothing
else**, and **no paper recomputes its figure on the same 220 genes.** The review
material in its own record is not present either.

## From agent F (the clinic) — the chapter says two things about a cleared test that its clearance does not

### What the regulatory document actually says
The chapter calls it a **"recurrence-risk and intrinsic-subtype test"**. **The
clearance does not.**
- **VAR-403**: the cleared output is **a score and a three-level risk band.**
- **VAR-402**: the labelling **explicitly excludes diagnosis, therapy-response
  prediction and therapy selection.**
- **The words "intrinsic subtype" appear in neither that clearance nor the later
  one for the same device**, by grep, so that is a lead rather than a claim.

**And "CE marked" has nothing behind it and cannot get it from this corpus.**
The European half of this corpus holds medicine assessment reports, not device
conformity documents, confirmed by searches on the test names and on the marking
wording. **That phrase has to come out of the chapter or be sourced elsewhere.**

**What is now properly anchored**: the clearance itself (VAR-401), its two
retrospective validation studies over 2,485 archived trial patients (VAR-405),
its specimen attrition (VAR-406), the distributed-test clearance against a
single-site predecessor (VAR-451), and its multi-site precision, where **6.75
score units are reliably distinguishable on a 0-to-100 scale** (VAR-450).

### The sharpest tension in the block
**Both cleared signatures are prognostic-only and explicitly not for therapy
selection** (VAR-402, VAR-408, VAR-409). **Both were then tested in 6,693 and
10,273 patients as the basis for withholding chemotherapy** (VAR-442 to
VAR-445), **and a guideline recommends exactly that use** (VAR-446). **So they
are in routine use for something their own labelling excludes.** And **VAR-407
shows the two are not independent**: one is the predicate device for the other.

### The precise negative the chapter needs
**VAR-430**: an approved comprehensive panel reports **splice variants in exactly
one gene, against 517 genes for DNA variants.** **VAR-431** is that single gene's
entire validation: **16 samples, 3 positives, agreement 100 per cent with a
confidence interval from 44 to 100.**

**And no clinical assay anywhere in this corpus reports an isoform ratio or a
percent-spliced-in value.** The honest positive is **binary, single-junction
reporting**, with its gates stated: a sample-level coverage-variation cut above
which **no fusion and no splice result is returned at all**, and an analyte-level
splice score that must be **exactly 1** (VAR-429, VAR-452).

### Fusion detection: two numbers that look alike and are not
**VAR-412's 99.99 per cent and VAR-415's above 99.9 share no denominator**, the
first being gene-by-sample outcomes against a three-method composite and the
second calls confirmed by a second assay. **VAR-413 and VAR-414 are the raw
counts, and they differ between arms**, zero false positives in 5,280 outcomes on
unselected samples against four in 840 on pre-selected ones.

**The opposite impression comes from VAR-421**: on a 14-fusion standard,
**precision of 35 per cent at two-caller consensus and 1.1 per cent for one
caller**, rising to 80 after filtering. **Same analyte, opposite impression**: one
counts pre-filter calls with every non-synthetic fusion scored false, the other
an approved pipeline's post-filter reports. **VAR-422** makes the filtering
visible: 1,909 candidate calls per case against 71 at the same sensitivity.

**VAR-416 is the detection limit the chapter lacked**, and it is set by **fusion
transcript abundance rather than by tumour purity alone.** **VAR-420** names
read-through transcripts as a false-positive source. **VAR-417 and VAR-418** are
the interlaboratory failures: fusions missed because **the partner gene was not
in the panel design** in 10 of 16 laboratories, and **only 6 of 11 fusions
detected by every laboratory.** **VAR-425**: 6 of 40 positive calls in a 517-case
series were **unconfirmable by Sanger sequencing.**

### Specimen quality, with a care pathway attached
**VAR-426**: **a third of an approved assay's own bridging cohort was untestable**,
26.0 per cent for no or insufficient sample and 7.2 per cent for sequencing
failure. **VAR-428** is the record that makes it clinical: RNA integrity above 6
is sequenced, below 3 is impossible, and **a trial policy excludes below 5.5**.
Routine dropout in a working service is far lower, 2.4 and 2.1 per cent, at six
to nine working days (VAR-427).

### Cost and time
**VAR-439**: **€5,273 per case at 300 cases a year falling to €3,455 at 2,000**,
excluding tax and a 20 per cent overhead. **VAR-440**: the transcriptome
consumables are **€279, 11.3 per cent of consumables.** **VAR-441**: **44
calendar days from sample reception to the molecular tumour board report.**

### Two measurements the chapter still cannot make
- **VAR-033's "adoption remains limited" still has no number.** Everything
  measured counts **adopters** (17 laboratories, 16 laboratories) and **never the
  denominator of all laboratories.** No survey of how many offer the assay exists
  in this corpus.
- **No reimbursement rate, tariff or coverage policy**, and the agent records this
  as **not searched** rather than absent, which is the right distinction.
- **VAR-447**: the guideline itself states there is **no prospective head-to-head
  comparison of the five assays**, and **VAR-448** turns that into procedure: a
  second assay may not adjudicate the first.

## From agent C (heritability and TWAS) — the chapter's "63 per cent more" is two overlapping intervals

### The live defect
The chapter reports that an isoform-level association study explains about **63
per cent more heritability** than its gene-level counterpart. **VAR-262: the two
numbers are 19.2 plus or minus 10.3 per cent against 11.8 plus or minus 5.7 per
cent.** **The intervals overlap**, and they come from **the same estimator as the
chapter's existing VAR-003**. A ratio of two point estimates whose intervals
overlap is not a 63 per cent improvement, and the chapter must either state the
intervals or drop the ratio.

**VAR-261 does the same for the chapter's 52 per cent**: 622 LD blocks, 288 found
by one method, 439 by the other, 249 by both. **VAR-263 is those authors' own
ceiling**: isoform expression alone does not reconcile most of the heritability
they set out to explain.

### What bounds isoform-level association testing, from its own developers
- **VAR-255**: **gene-level testing is clearly more powerful when the effect runs
  through the gene total.**
- **VAR-257**: about **four times more tests, no difference in inflation, and an
  effective sample size gain of only 10 to 20 per cent.**
- **VAR-256**: its fine-mapping credible sets are **undercalibrated**, worse when
  isoform-level QTLs are shared.
- **VAR-259**: the method's own statement that **its false positives concentrate
  inside trait loci**, which is exactly where they do the most damage.
- **VAR-274 is the independent application**, and the agent found it only after
  **overturning its own earlier negative** by opening all fourteen grep hits
  rather than nine: single-cell long-read lung, 74 isoforms at 23 loci, **47.8 per
  cent outside trait-significant regions.**

### Estimator trouble that the chapter treats as settled
**VAR-240 is the strongest finding in the block: two leading methods both
returned large contributions for tissues simulated to contribute zero.** And
**that critique comes from the group whose own method it also condemns**, which
makes it harder to dismiss rather than easier.

**VAR-271 to VAR-273 are an independent published critique** running the other
way: prediction error in the expression scores biases the mediated-heritability
estimate **downwards**, residual bias remains at a panel of 2,500, and **the
stratification said to rescue the method was tested on only a weak violation.**
VAR-240 and VAR-271 **point opposite ways and bear on different quantities**, a
single-tissue share against an all-tissue total, and should be recorded as such
rather than reconciled.

**VAR-244 is the sentence the chapter needs and does not have, and a source says
it outright: a colocalisation fraction does not estimate a contribution to
heritability.** **VAR-245**: both colocalisation and association testing have
highly inflated false-positive rates when molecular traits share QTLs or sit in
high linkage.

**VAR-247 is the audit**: seven named methods **all** had high false-positive
rates at stringent thresholds. **VAR-249 and VAR-250**: polygenicity alone
inflates the null, linearly in cohort size and trait heritability, **it is not
caused by prediction error**, and it reproduces in two implementations, so it is
**intrinsic to the design.** **VAR-251** names what the correction does not fix.

### Whether splicing beats expression: the dispute is now properly framed
**And my dispatch premise was wrong.** I told the agent the blood partition puts
protein QTLs above splicing per unit size. **It does not.** The source's own
per-SNP figures are **splicing 27.2, protein 25.5, expression 13.6 times**, and
the prediction-based ordering agrees. **Protein leads only in absolute share, on
an annotation twice the size.** The chapter as written does not make this error;
my dispatch did.

**The real dispute**: **VAR-229** finds splicing's unique contribution **vanishes
when conditioned on expression**, with splicing and expression LD scores
correlating 0.56 to 0.57. **VAR-243** finds it **barely falls** in a joint model.
Different method, different splicing dataset, different trait set, **and the
author groups share nobody**, so this is a real disagreement.

**VAR-233 to VAR-236 reframe it as a denominator problem**: per-SNP enrichment
**reverses the absolute ordering**, matched sample size and shared genes make the
three comparable, **those authors state why the three datasets are
incommensurable**, and they reconcile with the opposing results by pointing at
one model assuming many small effects and the other few large ones. **VAR-227 is
the cleanest demonstration**: the same QTL data under three annotation rules
gives 1.80, 2.75 and 5.84 times.

**VAR-224 and VAR-232 are the confound under all of it**: annotation
informativeness and single-tissue estimates both track **sample size**, at
R-squared 0.69 and 0.71, which the authors themselves call downward bias.

### Protein, where the gap is widest
**VAR-265**: on identical data, one method flags **2,217 genes** and
colocalisation supports **170**, with 293 by the two combined. **About 95 per cent
of the first method's genes are unsupported by the second.**

### Mechanical items
- **The cancer isoform study is published.** Journal version located, every
  quoted figure byte-identical. **The chapter's VAR-020 and VAR-021 should be
  re-pointed and their confidence raised.**
- **The association-inflation critique is published too**, and **the wording
  shifted between versions**, so the preprint must not be cited beside it.
- **No record in the chapter 10 research file carries `preprint: true`, and ten
  are affected**, including five for one widely cited dataset that appears five
  times in the chapter by grep.
- **Two abstract-only author lists were readable only from another paper's
  reference list**, which is not good enough. **No sentence should say the
  critiques come from outside that field**: five of the groupings share authors.

## From agent E (isoform-level QTLs) — the chapter may not say "replicated"

### The precise correction
The chapter's opposite-direction argument — that a variant can push two isoforms
of one gene the opposite way, which gene-level analysis cannot see — rests on one
B-cell study. **Three records are independent of it in cohort, platform and
authorship. None of them replicates its statistical test of a difference between
isoform effects.** They measure three different things: sign agreement of effect
estimates, one paper's own partition of 606 genes, and effect sizes at a single
named locus.

**"Seen repeatedly under different definitions" is true. "Replicated" is not.**

**The three are still worth their place.** **VAR-369** is the strongest: **88.3
per cent of genes found only by an isoform-aware test have opposite-sign isoform
effects, against 50.1 per cent of genes found by both**, and 47.9 against 22.1
when significance is required. **VAR-370** is the named case with both effect
sizes, one isoform up about 5 and another down 3 to 7 at the same variant.
**VAR-372** adds opposite allelic direction in different cell types.

### The honest bound is now eleven records against the chapter's one
**The count depends on the test, not the data.** **VAR-342**: the same 87 samples
give **1,294 to 9,364 genes** depending on which test is run, a sevenfold spread.
**VAR-344**: on a 494-sample tissue, 9,659 to 16,975. **VAR-356**: one map's own
count **moved 27.5 per cent on a change of regression model.**

**And two of those procedures have measured error inflation.** **VAR-343**:
calling a gene on "any isoform significant" has about **20 per cent empirical
false discovery.** **VAR-347**: a ratio-phenotype test with **true false
discovery of 0.464** under a permutation null, **worsening with transcript
sequence overlap.**

**The compositional problem is unavoidable, not a choice of method.**
**VAR-345**: one transformation depends on an arbitrary reference isoform and
another gives a singular covariance. **VAR-346**: the third **is undefined at
zero and unstable near it, and zeros are the common case.** **VAR-363**:
single-isoform genes are excluded from a ratio phenotype altogether, **so the
annotation sets the denominator.**

### A direction conflict the chapter should carry rather than resolve
**VAR-383 and VAR-367 both report *fewer* associations at isoform level than at
gene level** on the same samples. Three other maps report more. **The difference
is phenotype and era, not biology**, and the chapter should say so rather than
pick a side.

### An unresolved dispute at the heart of the chapter's mechanism
**VAR-348 says a variant linked to several transcript changes is normally an
artefact of incomplete annotation**, and that most of the coupling **vanishes
when promoters, splicing and ends are quantified directly.** **VAR-371 reports
the same pattern at shared splice junctions and reads it as genuine
reciprocity.** Both are plausible, **the two papers never meet**, and the chapter
should carry the pair.

**VAR-349 and VAR-384 bear on it with numbers**: promoter and 3' end usage are
**55 per cent** of transcript-usage QTLs in one cell type, and a transcript-ratio
association is **mostly not exon skipping** — 15 per cent skipping against 48 per
cent 5' end and 43 per cent 3' end. **VAR-352** shows the three classes enriched
in different features.

### A confound in the design most of these studies use
**VAR-377**: one study's gene and splicing phenotypes came from short reads while
its isoform phenotypes came from long reads, **so read length and phenotype are
confounded**, and its headline is presented as what short-read mapping misses.
**The one study that holds platform constant and varies phenotype is VAR-357**,
whose short- and long-read data came from the same cDNA and the same cell
barcodes, and there **250 of 466 colocalise with the gene-level signal.**

### Two figures from which no count may be derived
**VAR-374's 17.5 per cent does not resolve to a whole number of its 168 loci, and
VAR-371's 64.5 per cent does not resolve to a whole number of its 60
associations.** Both are recorded as the sources give them with the inconsistency
named. **Do not back-compute either.**

### Two apparent absences were lookup failures, again
**The flagship study of this field returned nothing from a title lookup and
nothing from an abstract grep, and the corpus holds it in full text**; two other
routes found it. A second paper had the identical pattern. The agent had
**reported one as absent in its first draft and corrected itself.** Its own
conclusion is the right standing rule: **treat any single-route negative as
unproven.**

### Not independent
**VAR-364 shares two authors with the isoform-level association study behind the
chapter's existing VAR-020 and VAR-021.**
