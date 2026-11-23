# Chapter 11 pass: cross-cutting items from agent reports

## From agent E (abundance and the closing question)

### An independence defect in the chapter as it stands
**PRO-386.** The chapter's sentence beginning "Running the same comparison on a
proteome predicted from long reads of a human cell line showed similar trends"
**reads as corroboration from elsewhere and is not**. That long-read proteome
paper **shares its last author with the partition paper, plus two further
co-authors.** Neither result is in question. The chapter must say whose it is.

### The chapter's third mechanism has no independent measurement
A corpus-wide grep for the term the chapter uses returns **exactly two
documents, the published and preprint versions of one paper**. Nobody else has
used it, and no measurement of codon-straddling substitutions was found under any
other name. **The NAGNAG literature is a different quantity**: a codon inserted
or deleted at a tandem acceptor, not a codon rebuilt from different pieces.
Every one of those records says so, and **the chapter must not put the two
percentages side by side without their denominators.**

### Two numbers already in the chapter have incompatible denominators
The chapter states, from PRO-034, that about 80 per cent of single-residue
variants were seen in protein. **PRO-355 reports about 2 per cent of exome and
about 7 per cent of mRNA variants detected in protein across 29 paired
tissues.** Those are not contradictory findings: one is all called variants
across many tissues, the other is variants expected from RNA in deeply covered
genes of six cell lines. **A sentence putting them together without the
denominators will read as an error.**

### The abundance question the chapter ends on, answered as far as it can be
**PRO-341**: one isoform runs from 54.7 to 60.6 per cent of its gene's total
protein in one tissue up to at least 93 per cent in four others, by absolute
targeted mass spectrometry. **PRO-342 is the point of it**: the same assay in
cell lines gave 95.8 to 99.0 per cent, **so the cell-line ratio does not
transfer to tissue**, which is exactly the chapter's closing complaint, now
measured. **PRO-343** adds that total output of that gene varies about five-fold
between tissues, so the denominator of an isoform fraction moves too.

**But the record the closing paragraph asks for does not exist here.** There is
no per-isoform protein quantification across many tissues at once: the deep
tissue atlases are gene-level, the isoform-level correlation work is one brain
region, and the absolute isoform quantification is one gene.

### RNA does not predict protein per isoform
**PRO-345**: per-isoform correlations centred on 0.067 over 7,107 isoforms in 103
brains, with 5.9 per cent above 0.3. **PRO-346 shows part of that is
measurement**, since the unique-peptide subset reached 0.087 against 0.041 for
the ambiguous one, and **PRO-347 bounds the design**, which can only induce a
correlation near 0.053 from the difference it tests.

### Frameshifted tails: three records that must travel together
**PRO-366** (all cases tested destabilised, mouse) against **PRO-362** (7 of 11
human genes differ, **in both directions**). Different laboratories, different
mechanisms, no shared authors. **PRO-363 explains part of the gap**: the earlier
literature compared a tagged reporter against the bare reporter rather than
against the gene's own wild-type tail, **and wild-type tails are themselves
degrons.** The chapter cannot assert that frameshifted tails are discarded.

### Two internal inconsistencies to carry rather than average
One paper's figure is stated over 22 malignant cancers in its results and 25 in
its abstract (PRO-344). Another puts tissue-specific regulation at 73 per cent of
human events (PRO-377) and 28 per cent in mouse, with the strongly regulated
share at 12 to 37 per cent after correction (PRO-378), **in the same paper**.
Quoting the 73 per cent alone would overstate it.

### A possible shared laboratory the chapter must not assume away
**PRO-352** (a dominant protein isoform almost everywhere, the same one
irrespective of tissue) and **PRO-385** (little evidence the annotated
alternatives act as proteins) **may share a laboratory**. Both are abstract-only
with no author list, one's authors appear in corpus reference lists, and the
other's could not be established at all. **Do not present them as two
independent readings until it is checked.**

### Chapter 12 already holds what item 7 asked for
The evidential requirement for isoform-selective targeting is in chapter 12's
records: an isoform-selective antibody approved with a companion test that cannot
see the isoform, the bioinformatic argument used to make that test adequate,
prevalence estimates for one isoform differing by an order of magnitude, and how
rarely two isoforms of one gene are both visible in a bottom-up proteome. **The
chapter cites across rather than asking for another pass.**

### Two corpus traps worth keeping
A guessed PMC identifier returned **a paper about cycle training for children**.
And a `grep --source abstracts` on an exact title returned nothing for a paper
the corpus holds **in full text**, so a failed abstracts grep is not absence
either.

## From agent A (functional divergence) — the chapter's biggest gap, filled with a caveat

### The intended headline cannot be delivered as specified
**The 2016 experimental isoform interactome is abstract-only.** Its abstract says
"hundreds of protein isoform pairs" and gives **no pair count, no count of pairs
sharing most partners, and no count sharing almost none.** A body grep for that
paper's own coined term returns only citing papers. **PRO-104 is the nearest
substitute and its unit is a protein-to-isoform pair, not an isoform pair.**
Before the chapter quotes a pair count, someone with journal access has to read
the published tables.

**What can be written instead** is the transcription-factor interactome at
PRO-105 to PRO-115: 693 isoforms of 246 genes across five assays, 3,509
isoform-resolved pairs tested, and **684 of 936 gene-level interactions, 73 per
cent, varying across isoforms.**

### The chapter must not pick a side on the headline comparison
**PRO-103** says alternative isoforms behave like distinct proteins rather than
minor variants. **PRO-109**, the only directly comparable measurement, puts
isoform pairs **more** similar than paralog pairs, which are in turn more similar
than unrelated pairs. **PRO-110** then controls for sequence identity and brings
isoforms back to paralog-level divergence, **and makes them more divergent than
paralogs in DNA binding.** The honest reading is conditional on the control.

### Two things the writer must not do
- **Do not call PRO-113's 59 per cent dominant negatives.** PRO-115 is those
  authors stating they have not shown it, and PRO-114 records that the label is a
  **threshold rule, not a competition experiment.**
- **Do not write prose from the agent's report.** Every number in it has a
  qualifier in a `note:` that the report flattened, above all the assay panel
  behind PRO-105 to PRO-149, which is **all exogenous expression**, and the
  "curated genes with at least one splicing paper" denominator behind PRO-150 to
  PRO-155.

### Does losing a domain explain losing an interaction
**PRO-126** says complete loss of the binding domain always kills it. **PRO-119**
says the same rule predicts only **53 of 171** observed losses. **PRO-127** is the
single-gene counterexample, an isoform losing its partner while keeping the
annotated domain. And **PRO-119 and PRO-120 are one statistical test read two
ways**, as a failure and as a success by its own authors; **cite them together or
the chapter overstates whichever it picks.**

**PRO-121** is the discipline record: 12.9 per cent against 4.4 per cent from the
same method on two interactomes, which those authors attribute to hub proteins
being better domain-annotated in one. It bears directly on PRO-117 and PRO-118.

### How widespread divergence is, by five standards that must be named
Two-thirds differ (PRO-111) and 91 per cent differ in at least one property
(PRO-113), against **4 to 9 per cent of curated genes meeting a loss-of-function
standard** (PRO-151), **under 5 per cent of annotated minor variants having
evidence of existing as proteins** (PRO-136), and the 2007 sceptical conclusion
(PRO-158). **These are not contradictory once the standards are named**, a
binding assay against isoform depletion with a phenotype, and existence against
function. A paragraph that puts them together without the standards **will read
as self-contradictory.**

**PRO-152 is the most telling of them**: 138 studies depleted only one isoform
and **nobody tested a second.** PRO-155: a third of human protein-coding genes
have no isoform-comparison study at all.

### Structure prediction, two measured results that do not cancel
**PRO-133 and PRO-134**: annotated alternative isoforms model at about the
confidence of canonical ones, which is the opposite of the expected answer.
**PRO-135, PRO-140 and PRO-141**: the scores are nonetheless useless for deciding
function, including a case where a threshold would discard a known functional
isoform and one where a non-functional isoform scores higher by omitting a short
disordered stretch. **No accuracy assessment against solved structures exists at
scale**, because solved structures of alternative isoforms are "exceedingly
rare" (PRO-130).

### Localisation has a clean negative pair
**PRO-143**: about half of 189 imaged isoforms differed in localisation or
condensate formation, **over a pre-selected gene set.** **PRO-145**: no
association with the presence of an annotated localisation signal. **PRO-146**:
no association between localisation differences and binding differences.

### Two gaps that stay open
- **Isoform-specific protein degradation: nothing usable.** Six phrasings
  returned nothing triageable. **The stability half of this chapter's question is
  unanswered**, and its only isoform-specific stability result remains the RPS24
  hypoxia work it already carries.
- **No study finds two splice isoforms of one gene interchangeable.** Six hits for
  that phrasing are all about **paralogous gene products**, not splice isoforms.
  The negative evidence the chapter can cite is a different shape, and the
  curators' own warning that a negative result is not evidence of
  interchangeability is probably why the stronger claim does not exist.

### Independence
Two of the eight sources **share two authors** and are not independent; four
records say so. Whether the 2016 interactome shares authors with either **cannot
be checked**, because its corpus record carries no author list. A paper that
would have been a third such source shares three authors with them. Five sources
in the pass are genuinely independent, and **PRO-157 against PRO-113 is the one
cross-check between two groups sharing no authors.**

### The id range bound after all
The agent reports the range **filled and then cost six verified findings**, which
are in its leads with doc ids and line numbers rather than recorded. One record
was dropped to make room for a better source. **Widen the range on any
re-dispatch**: saying "no quota" did not stop a numbering convention from
binding.

## From agent D (the worked case) — two claims in the live chapter are not what they appear

### 1. "Beside the mRNA entry channel" is not a structural claim
The chapter states that the protein lies beside the channel through which
messenger RNA enters the ribosome, as a structural fact. **It is not one.**
**PRO-304 to PRO-306**: one source infers it from **proximity proteomics of a
translation initiation factor**, the other carries exactly one reference for it,
and that reference is the same proximity paper, **which is abstract-only here and
whose abstract mentions neither this protein nor the channel.** A corpus-wide
search for any sentence placing this protein at the entry channel returns only
those two, plus four paragraphs about entirely different ribosomal proteins.
**PRO-318** is the one line cutting the other way, and its own citation is an
abstract naming no individual ribosomal protein.

**PRO-303** is the record to use instead: the human structure cited for it **did
not include the C terminus**, the yeast one was uninformative, and the terminus
is not strongly conserved.

### 2. The lysine proposal is the same laboratory, four years earlier
**PRO-302**: the proposal that lysines matter here because cells attach fate-
controlling tags to them is **four years older than the chapter's source and from
the same laboratory.** So the chapter's PRO-051 and this are **not two groups.**

**And there is no measurement of a modification on the alternative terminus, in
either direction.** Three exhaustive greps found nothing. **PRO-300 and
PRO-301**: the curated protein entry's only modified residues are at positions 1
and 9, with **none in the last three**, while the keyword set does record two
modification types, so the protein is modified elsewhere. The one curated lysine
modification sits about a hundred residues from the variable end.

### The naming problem has a sharper reason than the chapter gives
**PRO-294 is the strongest single finding for the refusal**: the unifying scheme
**states that it excludes the human three-base-pair exon.** That is a declared
scope limit, not an ambiguity, so **the scheme cannot be applied to the
four-junction human results without extension.**

Three more reasons, each anchored:
- **PRO-291 against PRO-296**: the letters **a and b are swapped between the 1994
  and 2025 schemes**, by the 2025 paper's own statement, while c is stable.
  Letter-level agreement between papers on this gene is not safe.
- **PRO-292**: the reconciliation paragraph equates one exon with the 18-base-pair
  exon and then, two sentences later, with the 22-base-pair one.
- **PRO-289 against the chapter's existing source**: the microexon lengths are
  given as 19 or 22 nucleotides in one paper and 18 and 22 in another.

**And the missing link is now named.** No paper on this gene names a database
transcript, confirmed by within-document greps across all seven. **The sequences
give protein end to accession, the papers give exon label to protein end, and
nothing joins a paper's exon label to a database transcript.** The chapter's
refusal should name that rather than the exon numbering alone.

### The coding consequence of each junction IS now anchored, from the coining group
**PRO-285 to PRO-287**, from a seventh paper this pass found: all-skipped gives
the terminus ending in three named residues, the 22-base-pair exon alone puts a
stop inside itself, and the two-exon form differs by one lysine. **PRO-287** adds
that the three-base-pair junction never occurs without the 22-base-pair exon.

**But do not assert which form carries which lysine count.** That paper says the
two differ by one lysine without saying which, the curated entries do not
reconcile with it, and the agent recommends against the assertion.

### The Alzheimer denominator cannot be resolved, and now says why
**PRO-283 and PRO-284**: the text says three sections and **both figure legends
say two**, with the method naming no donor count and no donor table in the
supplement. **Only Alzheimer conflicts**; the other two diseases are mutually
consistent. **A third source has the same text-against-legend problem** on a
different count, so the chapter's aside is true of two sources rather than one.

### The second worked case exists, and it is better evidenced than the first
**PRO-310 to PRO-315**: a 38-nucleotide penultimate microexon, out of frame, with
a premature stop that **escapes decay**, replacing the canonical last 41 residues
with a distinct 10-residue tail. **The new terminus is demonstrated by targeted
mass spectrometry against synthetic standards**, at 6.4 times higher in one
muscle than another and about 47 against 3 per cent of immunoprecipitated
protein. The four forms are **indistinguishable by blot with no antibody to the
new tail**, and there is **a measured negative: localisation unchanged.** The
same gene's in-frame microexon is the contrast.

### Independence, three ways
**The entire hypoxia strand is one laboratory** (PRO-288, PRO-302, PRO-304,
PRO-307, PRO-308, PRO-316, PRO-317), **including the lysine proposal and the
entry-channel inference.** Four of five authors are shared across two other
sources. And the structural claim rests on one paper that cannot be read, cited
by both of the other strands.

### Three mechanical items before merge
- **PRO-282 will break the bibliography gate.** The neurodegeneration work has a
  journal version, and reusing the existing bibkey puts two DOIs under one key.
  **Repoint the existing PRO-052 to PRO-062 to the journal DOI in the same pass.**
- **PRO-298 to PRO-301 are the first `source_type: proteins` records in the
  book.** The verifier resolves them; the bibliography builder keys entry type off
  the journal string, so they render as articles in a database. **Decide whether
  to cite them publicly at all.**
- Both published versions are **abstract-only**, so neither the hypoxia figures
  nor the Alzheimer denominator can be re-checked against them.
