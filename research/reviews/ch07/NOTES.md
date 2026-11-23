# Chapter 7 pass: cross-cutting items from agent reports

## From agent B (TDP-43)

### Corrections the chapter must carry
- **The 50 per cent TDP-43 loss threshold is the assay's, not the biology's.**
  NEU-142: cycloheximide at the weakest knockdown reveals the cryptic exon, so
  the transcript is already there below that point and is being destroyed.
  Any sentence proposing cryptic exons as early biomarkers has to pass through
  NEU-142, NEU-163 (limit of detection 1.09 in CSF while positivity was called
  at any ratio above 1) and NEU-165 (no sensitivity or specificity reported, and
  the authors say their controls may not be true controls).
- **One cryptic target is not enough.** NEU-171: a 44 bp genomic deletion
  abolishing the mouse Unc13a cryptic exon did not rescue grip strength, weight,
  motor-neuron number or paralysis in TDP-43 conditional-knockout mice, n = 5.
  NEU-172: a chimeric repressor restoring several targets held grip strength and
  weight and left all treated animals alive at 110 weeks against end-stage at
  about 47 weeks, n = 15. Partial rescue is the honest finding.
- A cognitive-rescue claim in one of those papers is attributed to a personal
  communication and **must not be used**, even though it is the natural
  counterweight to NEU-171.

### Independence: three laboratory clusters, never call two of one cluster independent
- **Wong/Ling, Johns Hopkins**: NEU-005, NEU-159, NEU-161..166, NEU-170..172.
  The cryptic-exon concept, the cell-type variability result, the fluid
  biomarker and the rescue experiments are one laboratory's chain of work.
- **Fratta/Ward/Ule, UCL and NIH**: NEU-010..012, NEU-141..151, NEU-157,
  NEU-158, NEU-168, NEU-169, NEU-173..175. **The FUS null and the FUS positive
  come from the same group**, as do the cryptic catalogue and the measurement of
  its own reproducibility.
- **Petrucelli/Gitler/Prudencio, Mayo and Stanford**: NEU-013, NEU-152..156,
  NEU-167.
- Genuinely separate: Ma and Brown share no author, so the back-to-back UNC13A
  papers are independent and the chapter may say so. van Zuiden, Koyama, Dinh
  and Ruf are each unconnected to the rest. Calliari and Irwin are
  semi-independent: different antibody, assay, cohort and matrix, but two
  authors overlap, so state what differs rather than calling it a replication.

### Four disputes, both sides recorded
1. Additive (NEU-151) against non-additive (NEU-155) UNC13A risk alleles.
2. Does the risk allele weaken TDP-43 binding: higher Kd by calorimetry
   (NEU-150) against similar affinity by gel shift (NEU-153), and the second
   paper names the disagreement in print.
3. Loss of nuclear function against gain of cytoplasmic toxicity: only 16 per
   cent of patient-tissue mis-splicing is reproduced by knockdown (NEU-160), and
   cytoplasmic TDP-43 shifts APP splicing where knockdown does nothing
   (NEU-179), against the loss-of-function framing every UNC13A and STMN2 record
   presumes.
4. Whether one cryptic target is enough (NEU-171 against NEU-172).

### Not found, do not search again
- A quantified fraction of neurons of a named type that have lost nuclear
  TDP-43. That is the dilution factor applying to every bulk-tissue
  cryptic-exon measurement, and it has no source.
- The primary paper for the independent mass-spectrometry detection of cryptic
  HDGFL2 in presymptomatic C9orf72 CSF; NEU-166 is a restatement, not an
  anchored independent replication.
- A positive cryptic-exon programme in SOD1 ALS or FTLD-TAU. Only FUS returned
  a characterised alternative programme (NEU-175).
- A humanised UNC13A mouse.

### Mechanical
- Twelve new bibkeys; author strings were reformatted by the agent from
  `meta.json` full names. Run `scripts/resolve_metadata.py --check` before
  publication. Six records carry `preprint: true`.

## From agent A (tau)

### Two corrections to the chapter's existing text
- **The chapter's closing sentence in `#sec-mapt`, "the phenotype is the ratio
  rather than either isoform", is not safe as written.** NEU-115 supports it
  mechanistically, since a 3R/4R mixture polymerises less than 4R alone. NEU-122
  and NEU-123 cut against it: a splice-switching oligonucleotide raising 4R
  alone, with total tau unchanged, in three control human iPSC lines, was
  sufficient for tau hyperphosphorylation, enlarged endosomes and lysosomes,
  lysosomal membrane rupture and caspase-3 cleavage. Report both.
- **Do not write the N-terminal isoform proportions from the review the chapter
  already cites.** Its L16, already NEU-001's anchor, gives about 54 per cent 2N,
  37 per cent 1N and 9 per cent 0N. Targeted long reads (NEU-111, NEU-112) put 2N
  under 3 per cent with 0N and 1N each around 45 per cent, which reverses the
  ordering. The review's figures look transposed, and that could not be
  established from a source, so it is a lead rather than a claim. A sentence
  drawn from the review would state the rarest class as the commonest.

### The Alzheimer 3R:4R question, and why it is unresolved
NEU-109 finds **no** exon 10 PSI difference in Alzheimer or PSP temporal cortex;
NEU-110 finds a significant 4R:3R rise in Alzheimer **at the protein level**, in
the 0N and 2N classes only, from the same individuals. The answer depends on
whether mRNA or protein is measured and on which N-terminal class is counted.
**Any table row asserting an exon-10 direction for Alzheimer disease contradicts
NEU-109.** The safe Alzheimer row is NEU-108: its filaments are mixed 3R+4R.

The same split applies to PSP: 4R up by inclusion staining (NEU-101) against
exon 10 PSI unchanged in bulk transcript (NEU-109). Those authors reconcile it at
their L62 by the dominant 0N isoforms diluting the 1N and 2N increases, which was
read but not recorded, so a chapter sentence offering that explanation needs its
own record first.

### Therapy points both ways, which is the argument
NEU-119 pushes exon 10 **out** in a 4R-excess mouse; NEU-120 and NEU-121 push it
**in** in htau mice, which over-produce 3R. The target is the balance.

### Independence
- **Pick (NEU-104, NEU-105) and CBD (NEU-106, NEU-107) share a laboratory**, so
  the two halves of the seeding asymmetry are not independent.
- **Neurexin SS2/SS4 (NEU-128, NEU-129) share their senior author with chapter
  2's CEL-024 and CEL-025.** A sentence presenting the SS4 knock-in and the SS2
  code as converging evidence from separate groups would be wrong.
- NEU-116 and NEU-117 are abstract-only with no author list, so their
  independence **cannot be checked and must not be asserted**.
- NEU-126 shares no author with the chapter's EST-era tissue source, which is the
  one place independence is positively established here.

### The brain-splices-most claim survives, with a caveat
No modern ranking in the corpus contradicts the brain's top position. What moves
is **liver**, second on EST evidence and last of nine on long reads, and the
metric, which is not the same quantity in the two sources. The nine long-read
tissues exclude testis, so the EST-era top three cannot be fully checked, and the
long-read figures are a reanalysis of the GTEx long-read study rather than new
sequencing.

### A gap worth closing with a targeted follow-up
**SCN1A, its poison exon, and the oligonucleotide developed against it appear
nowhere in the whole repository.** That is the clearest modern addition to this
chapter's list of splicing-directed drugs. Also unread: NIO752 (an
oligonucleotide in PSP, CBS and MAPT-FTLD) and Ezerskiy 2022, which would make
the bound on "ratio, not isoform" independent.

### Mechanical
- 15 `RESOLVE_FROM_DOI` fields in agent A's file need
  `scripts/resolve_metadata.py`.
- Seven records rest on a preprint with no published version in the corpus.
- One metadata error was caught by checking rather than trusting: a DOI written
  from memory was wrong by one digit and is corrected in the file.

## From agent C (SMA and DMD)

### Three corrections to the chapter's existing text
- **NEU-015's framing of the SMN2 C-to-T substitution is one no source uses.**
  The chapter says it is "proposed to weaken its 3' splice site". NEU-181 says it
  disrupts an SF2/ASF-dependent exonic enhancer; NEU-182 says in its own abstract
  that it functions **not** to disrupt an enhancer as previously suggested but to
  create a silencer. Both are abstract-only with no author lists, so independence
  cannot be established. Report the two mechanisms as competing.
- **NEU-017 and NEU-187 must not be mixed.** 37 of 73 against 0 of 37 is the
  published final analysis; 21 of 52 against 0 of 30 is the interim the approval
  rested on. They are the same trial at two analyses.
- **NEU-018's FIREFISH figure came from a review.** The regulator's version is
  now anchored (NEU-189): 7 of 21 and 7 of 17 sitting at least five seconds, by a
  named scoring item, at month 12, **with the whole-cohort denominator of 21**.
  NEU-190 records that the trial was exploratory and the efficacy endpoint was
  adopted mid-trial.
- **The EMA March 2021 approval date could not be re-anchored.** No EU regulatory
  document for risdiplam is in the corpus; two SQL routes returned nothing. The
  chapter must attribute the date to the review that states it or drop it.

### The dystrophin debate is now anchored on both sides, from inside one document
NEU-210 requires about 10 per cent of normal from a Becker extrapolation and
finds no dystrophin-to-function association in the trials; NEU-211 finds no
rational basis for any threshold. Three of four named senior officials opposed
approval and the Commissioner deferred without resolving the science. NEU-212 and
NEU-213 show the next two approvals resting on the first. **NEU-214 and NEU-215
are the empirical test**: one confirmatory trial's primary endpoint was not met
(P = 0.309), and another drug's required confirmatory trial had not started three
years after approval.

### Any table of the four DMD drugs must state the assay per row
NEU-205 with NEU-206: immunohistochemistry rose from 1.1 to 17.4 per cent
positive fibres while western blot gave 0.93 per cent of normal, and NEU-206
records why those are different quantities, since a positive fibre is any
staining above background. NEU-208 is the same problem inside one drug: median
increases of 4.6 and 3.8 per cent by western against 1.7 and 1.9 per cent by mass
spectrometry, **in opposite rank order between doses**.

### The frame rule: two denominators, not a disagreement
91 per cent agreement over more than 4,700 database entries (NEU-216) against 30
per cent out-of-frame among deletions and duplications in a Becker-ascertained
biopsy series (NEU-217). The second also shows that some exceptions are splicing
exceptions.

### Two unanchored items
- **"ENDEAR" and its registration number appear nowhere in the regulatory
  document**, so the identification of the trial the approval rested on with the
  published trial is not anchored. The chapter must not equate them without a
  linking source.
- **Cost-effectiveness has no record on either side.** Two sources were located
  and not read. This was an explicit ask and is unmet.
- No accelerated-approval or Subpart H language appears in either SMA drug's
  review, consistent with full approvals on clinical endpoints, but **no claim
  was recorded from that absence** and the chapter must not assert it.

## From agent E (RNA-seq diagnostics)

### A repo amendment this pass must make
**NEU-031's `doi:` must change** from the preprint `10.1101/074153` to the
published `10.1126/scitranslmed.aal5209`, keeping the **same** bibkey
`cummings2016musclernaseq`, because `build_bib.py` treats a preprint read under
the journal DOI as legitimate only when the one bibkey is shared. Until that is
done, verifying both files reports "one key, 2 DOIs". The anchor and
`preprint: true` stay. The published version is in the corpus as abstract-only
doc 50091604, found only by `search -s abstracts` on the published abstract's own
phrasing after `lookup doi`, `lookup pmid`, `lookup title` and SQL all failed.
The published cohort and yield are unchanged from the preprint (NEU-261).

### The number the chapter was missing
**NEU-263**: of 3,322 disease genes, the fraction adequately covered at 8 reads
across 75 per cent of junctions within 100 million reads is **blood 28.2, LCL
49.4, muscle 43.6, fibroblasts 53.7 per cent, and 64.2 per cent in at least one.**
**NEU-268** is its complement: **1,436 of 4,878 genes, about 30 per cent, are
assayable in no accessible tissue at any depth**, rising above 40 per cent for
dystonia, cardiac and retinal genes.

### Prior testing dominates tissue, and that should lead the section
**NEU-287 and NEU-288 agree on a twenty-fold gradient from two centres with no
shared authors**: 60 per cent yield with a prior variant of uncertain
significance against 2.7 per cent without, replicated as 71 / 40 / 5.2 per cent.
**NEU-289 bounds it further**: after *genome* sequencing, blood RNA-seq produced
candidates and no diagnoses. That gradient is the honest explanation of the whole
2.7-to-60-per-cent spread, and the chapter should lead with it rather than with
tissue.

### The statistical threshold is worth more than another yield figure
**NEU-278**: a Z-score cutoff instead of a false-discovery threshold gives two
orders of magnitude more calls, at **precision 3 against 92 per cent** and recall
98 against 83. **NEU-294** gives sensitivity by causal variant class: splicing 7
of 8, monoallelic expression 3 of 6, expression 3 of 4 homozygous stops, **1 of 9
frameshifts and 0 of 14 missense.** A reader cannot evaluate any yield figure
without those two.

**NEU-278's authors are the method's developers**, so that benchmark is not
independent of the dispute it settles, and its note says so.

### Three disputes
1. **Muscle against muscle, same prior testing, half the yield**: 35 per cent of
   50 (NEU-261) against 14.3 per cent of 70 (NEU-286). **Not independent in the
   helpful direction**: three authors are shared with the Solve-RD record and the
   cohorts may overlap. The lines give no reason for the gap, so report the
   discrepancy rather than explain it.
2. **What limits long reads**: the existing NEU-034 says coverage of the specific
   gene; NEU-296 and NEU-297 say transcript length and uneven coverage within
   long transcripts, and the one unambiguous long-read win turns on homology, not
   coverage. **Two independent comparisons naming different limits**, with author
   intersections computed from the bylines rather than guessed.
3. Z-score against false-discovery control, above.

### Laboratory clusters, computed from bylines
Six records are one Munich pipeline (NEU-033, 271, 277, 280, 281, 285) and five
are one Southampton group (NEU-034, 263, 270, 291, 298).

### Unmet
**No measurement exists in this corpus of diagnostic transcriptomes solved later
by reanalysis against a newer annotation**, after four phrasings. And no
systematic fraction of disease genes assayable in iPSC-derived tissue.

## From agent F (prediction and n-of-1)

### Two things the chapter must not say
- **Do not name what the milasen variant does to splicing.** Four secondhand
  sources give three answers: intron 6 inclusion, a cryptic splicing variant, and
  pseudoexon inclusion. The primary is abstract-only in this corpus and **its
  abstract does not name the event or the variant**. NEU-322 is scoped to "on the
  account of a 2024 review" and the dispute is in its note. The majority favour
  cryptic splicing over intron retention, which is not the same as knowing.
- **Do not say SpliceAI and Pangolin share training data.** One benchmark
  describes the leading predictors as trained on gene-model annotations; Pangolin's
  own paper says it was trained on RNA splicing measurements in four species and
  that SpliceAI saw human sequence alone. NEU-302 follows the primary, NEU-304 and
  NEU-321 attribute the other description to its authors. **What the chapter may
  say** is that they share architecture and score almost identically, r = 0.97.

### The record the chapter's heading needs
**NEU-316**: on the same 4,545 variants, auPRC 0.77 for *detecting* a splicing
effect against Spearman 0.63 for *quantifying* usage. That is the ranking-against-
quantifying claim measured on one variant set. NEU-320 generalises it: median
Pearson 0.53 between score and measured effect across eight tools and four assay
studies. NEU-318 is the evidence for quantification (Spearman 0.79 and 0.80 at one
exon) and NEU-319 against (Pearson 0.57 in vitro, 0.37 in vivo).

### Calibration, which the chapter has none of
NEU-308: threshold 0.20 against 0.50 gives 88 against 73 per cent on 86
patient-validated variants. NEU-309: on deep-intronic variants in one gene, the
clinically recommended 0.5 threshold **halves** sensitivity. NEU-310: the
optimal threshold moves between exons, regions and variant classes. NEU-311: the
tools do far worse on exonic than intronic variants (median prAUC 0.773 against
0.419) **at equal measured disruption rates**. NEU-307: four of eight tools need a
gene model, and 18.0 per cent of protein-coding genes have a used splice site
missing from the default annotation.

### Almost none of these benchmarks is independent
- Three are **self-assessments**: SpliceAI2 assessed by SpliceAI's team (NEU-305,
  315, 316), Pangolin by Pangolin's authors (NEU-317), MMSplice on one assay by two
  of that assay's own authors (NEU-319). A fourth comparison is by the makers of
  the resource being compared (NEU-306, NEU-314).
- **Two benchmarks that look independent are not**: one pooled its 202 diagnostic
  variants with the other's 56, so they share those 56.
- **The n-of-1 programmes are three faces of fewer groups.** Two authors are on
  milasen, atipeksen and the KCNT1 case. Six span one foundation's cohort and the
  SCN2A pair. Six span the eligibility guidelines, the cohort that applies them
  and the European perspective, **so the 4.9 per cent eligibility screen is not an
  independent test of the criteria it uses.**

### The harms, which the chapter currently omits entirely
NEU-329: hydrocephalus, withdrawal and death in one patient, status dystonicus
and a shunt in another, and a two-year dosing pause, in a knockdown-mechanism
programme that the record labels as such. NEU-330: correction is partial, 0 to 5
per cent rising to 29 per cent functional transcript, with increased skipping of
another exon as an off-target effect. NEU-323: the milasen design route included
rat toxicology at 42 times the dose, with dorsal-root-ganglion toxicity and gait
disturbance.

### The timeline claim needs its counterweight
Milasen opened within a year. **NEU-338**: across one foundation's first eight
applications the median from acceptance to first dose was 23 months against an
18-month target, from 173 applications of which 78 were accepted and 57 declined.
**NEU-339**: that foundation states it has no splice-altering oligonucleotide with
enough clinical exposure to judge benefit. **NEU-333**: of 532 sequenced patients,
4.9 per cent were eligible for any individualised oligonucleotide and **only three
by splice correction**.

### Boundary offers to other chapters
A platform-level oligonucleotide adverse-event meta-analysis (101 studies) is
chapter 12's; two variant-reclassification findings are chapter 10's. All three
are in this file's leads with their figures, offered on rather than recorded.

## From agent D (the Mendelian fraction)

### Three corrections, one of them to this brief
1. **The COL6A1 denominator in this brief and in the research file's own lead is
   wrong.** Both say the recurrent variant explains "roughly a quarter of a
   collagen-VI-like dystrophy cohort". The source says roughly 25 per cent **of
   patients clinically suggestive of collagen VI dystrophy in whom prior genetic
   analysis was negative**, which is a much smaller denominator. Fix the lead.
2. **NEU-026's "3 per cent of common SNPs" carries no denominator.** It is 7 of
   228, at that paper's L31. Amend the existing record.
3. **CFTR numbering.** The new records use HGVS: exon 10, intron 9. The legacy
   names for the same features are exon 9 and intron 8, so a source quoted as
   saying "exon 9 skipping" means the exon these records call 10.

### The section's spine
**NEU-250**: the trio paper recomputes ClinVar on matched splice positions and
gets 16.5 per cent non-canonical, 17.5 adjusted, against its own trio-based 27
per cent (CI 18 to 39), at Fisher p = 1.22e-15 and below 2.2e-16, which those
authors read as 35 to 40 per cent under-ascertainment. **That is one source doing
the reconciliation the chapter currently attributes to ascertainment in general.**
NEU-251 carries their own caution that such estimates rest on clinically
interpreted variants, and NEU-252 that their estimate excludes exonic missense,
branchpoints, splicing elements and deep-intronic variants, so it is a lower
bound. NEU-247 and NEU-248 give the structural reason two databases disagree:
one records no benign or uncertain variant, so it has no benign denominator.

### Two scope corrections to figures the chapter already uses
- **NEU-254**: the machine-learning 10 per cent is a rate among **non-synonymous**
  HGMD disease-causing variants in internal exons of 100 nucleotides or fewer,
  accessed May 2012. The chapter states it without those bounds.
- **NEU-249 against the chapter's NEU-026**: an audit of seven construct-based
  datasets puts the assay behind the chapter's 10 per cent among the five whose
  scores could not separate aberrant from natural splicing. NEU-249's note
  explains that this is a caution about the score as a continuous measure rather
  than a refutation of the 513 calls. **NEU-254 also shows the 4,964 were
  non-synonymous, so synonymous variants are not in that denominator at all.**

### Four records fail the inclusion test on purpose, and the chapter must say so
NEU-233, NEU-235, NEU-236 and NEU-237 perturb a spliceosome component's sequence
or dose, not an isoform. They are kept because they are the only anchored evidence
on the retina-restricted phenotype, which is one of the field's open questions.
**The chapter must not present them as isoform-specific experiments.**

Their disagreement is three-way: pigment epithelium as primary in three mouse
models (NEU-233) against photoreceptor damage the authors call
epithelium-independent in a human organoid (NEU-236), against **no retinal
phenotype at all** in either heterozygote (NEU-235). Whether the mouse and
organoid groups are independent **could not be checked**, because two author
lists are not in the corpus.

### Internal discrepancies, recorded not resolved
One paper's abstract gives 28.4 and 15.1 per cent where its results give 28.2 and
16.6, and only the results state the denominator of 638; the record uses the
results. One CFTR paper gives three different counts of its 5T group, 42, 39 and
37. One mouse paper's authors state their homozygous mice are milder than
heterozygous patients.

### Gaps
- **No single source reconciles all four published fractions on one denominator**;
  NEU-250 does it for two. The two primaries behind the roughly 30 and 43 per cent
  figures were not looked up and are named in the leads.
- **No variant-by-variant concordance between two massively parallel splicing
  assays.** The chapter must not imply the assays have been cross-validated
  variant by variant, nor that no such study exists anywhere.
- The primary for the COL6A1 pseudoexon mechanism and its antisense rescue is
  cited in eleven corpus reference lists and **is not in the corpus**.

## From agent G (poison-exon oligonucleotides) — the gap is closed

### The number everyone will want is two numbers
**NEU-342 gives 89 per cent** of SCN1A transcript as the poison exon in neural
progenitors **after decay was blocked**; **NEU-346 gives about 1 per cent** at
steady state in adult wild-type mouse brain. Both are right and **they are not
the same quantity**. NEU-377 explains why the honest number cannot be obtained in
tissue at all: the fraction cannot be measured in living tissue because decay
destroys it. **A sentence putting 89 and 1 per cent side by side without saying
one was measured with decay blocked will read as an error.**

### Do not state a fold change for this drug class
Two review-level figures are irreconcilable: one gives 1.5-fold transcript with
protein restored to wild-type levels, the other up to 25-fold transcript with
only about 30 per cent of protein. Different oligonucleotide, different animals,
probably a different denominator, and **both are reviews while both primaries are
abstract-only.**

### The drug is investigational, and the chapter must not imply otherwise
**No FDA, EMA or PMDA document for it exists in the corpus**; a grep of the
regulatory corpus returns only Freedom of Information logs recording a third
party's request for the IND dossier. **No registration has posted results.** The
seizure figures are uncontrolled, open-label, within-patient, and **the abstract
gives no subgroup denominator**, which NEU-356's claim states. NEU-361 establishes
that the programme's primary analysis was safety and pharmacokinetics, and
NEU-358 is the review that says the evidence "supports a hypothesis of disease
modification but does not establish it".

### Three numbers for one phenomenon, to keep apart
Elevated cerebrospinal-fluid protein: 45 per cent in the extensions counting any
attribution; about 27 per cent counting only drug-related events; and roughly
three-quarters counting any transient elevation above a threshold.

### Conservation cuts both ways inside one drug class
96 per cent conservation is why a mouse model existed for one target (NEU-343),
while rodents lack the exon entirely for another (NEU-371) and a third poison
exon is primate-only, inside a transposable element (NEU-372). **Whether a poison
exon is modellable is a property of the exon, not of the method.**

### Independence: four clusters, two of which look independent and are not
- **The company**: NEU-342 to NEU-345, NEU-364 to NEU-369, NEU-371 and every
  trial record. One paper is sixteen authors at one company; another shares four
  of them; the sponsor is the same throughout.
- **One academic laboratory**: NEU-341 and NEU-372 to NEU-376 share a senior
  author, so **the discovery of the first poison exon and of the other two are one
  laboratory, not a replication.**
- **The genuine independent anchor for the mechanism** is NEU-346 to NEU-348,
  sharing no author with either.
- A second group's work (NEU-354, NEU-370) used the company's own compounds as
  comparator and positive control, so the right description is **"a second group
  extending a published strategy", not a blind convergence.**

### Records that belong to other chapters, for my decision
A PD-L1 record and the whole ophthalmic programme (NEU-368, NEU-369, NEU-371) may
be chapter 12's. A lead records that the second programme **has reached
patients**, located but not read, which is what turns a platform claim into a
platform.

### NEU-379 is the record chapter 7's tau section needed
It is the splice-switching experiment that makes the bound on "ratio, not
isoform" independent, and it should be read alongside NEU-122 and NEU-123 rather
than instead of them. It is **not** independent of the earlier 4R work from the
same laboratory.

### What was rejected, and why it matters for the chapter's list
The oligonucleotide in progressive supranuclear palsy **fails the inclusion
test**: it is a gapmer that lowers total tau, not an isoform-specific
intervention, and the corpus calls it exactly that. **It must not be listed beside
nusinersen, risdiplam and zorevunersen.** Its full registry details are in that
file's leads.
