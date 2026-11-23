# Chapter 8 records review — reviewer C

Assignment: `research/08-singlecell-spatial.yml`, records **SCS-221 to SCS-259** and
**SCS-261 to SCS-299** (78 records; SCS-260 does not exist in the file).

Method: worked per cited document — **37 distinct documents** — opening each cited line
label in `papers/<id>/content.lines`, reading the surrounding lines, and re-running
every absence check as a **within-document** grep rather than a corpus grep. Author and
independence relations were recomputed from the bylines in the records' own `source:`
blocks and checked against `papers/<id>/meta.json` for all 37 documents; title, author,
journal, year and DOI were diffed mechanically against the corpus metadata for all 37.

## How to read the verdict column

The verdict scores the **claim against its cited lines, plus the `source:` block and the
tier**. None of the nine permitted strings describes a defective `note:`, so note
defects are reported separately, with their own counts, in sections D, E and G. The
dispatch's four defect classes are sections C (class 1), D (class 2), E (class 3) and
F (class 4). The verdict table carries an "also in" column so that an `ok` row with a
caution attached is visible at a glance.

One process note, because it changed two findings. On a first pass I read several grep
results through a truncating `cut`, and twice reported a word absent when the matched
text sat past the cut. Every absence statement in this report has since been re-run with
the matching line read in full; section I lists each one and what it returned.

Abstract-only records were not written off as `cannot check`: every element of each such
claim was checked against `L1`, and all of them proved supportable there.

"source says" in the detail blocks is my own summary of what the lines hold, with any
verbatim fragment kept short and used only to pin the discrepancy. None of it is drafted
to be reusable prose.

---

## A. Verdict table (all 78 records)

| id | verdict | also in |
|---|---|---|
| SCS-221 | ok | C (self-flagged), E.2, E.6 |
| SCS-222 | ok | |
| SCS-223 | scope too wide | |
| SCS-224 | qualifier lost | F.4 |
| SCS-225 | ok | |
| SCS-226 | ok | |
| SCS-227 | ok | |
| SCS-228 | ok | C (self-flagged), D.4 |
| SCS-229 | number wrong | E.5 |
| SCS-230 | ok | E (footnote) |
| SCS-231 | ok | |
| SCS-232 | ok | C |
| SCS-233 | ok | F (handled well) |
| SCS-234 | ok | C |
| SCS-235 | source metadata wrong | E.2 |
| SCS-236 | source metadata wrong | C, E.2 |
| SCS-237 | source metadata wrong | C, E.2 |
| SCS-238 | ok | F.3 |
| SCS-239 | ok | C (self-flagged) |
| SCS-240 | ok | C, F (handled well) |
| SCS-241 | ok | C, E.4, F.6 |
| SCS-242 | ok | F.2 |
| SCS-243 | ok | F (handled well) |
| SCS-244 | ok | |
| SCS-245 | ok | G |
| SCS-246 | ok | |
| SCS-247 | ok | D.2 |
| SCS-248 | ok | |
| SCS-249 | ok | D (verified correct) |
| SCS-250 | ok | |
| SCS-251 | ok | |
| SCS-252 | ok | |
| SCS-253 | ok | H.2 |
| SCS-254 | ok | H.2 |
| SCS-255 | ok | H.2 |
| SCS-256 | scope too wide | C (self-flagged), G |
| SCS-257 | ok | E (footnote) |
| SCS-258 | ok | |
| SCS-259 | source metadata wrong | E.2 |
| SCS-261 | ok | E (verified correct) |
| SCS-262 | ok | |
| SCS-263 | ok | C |
| SCS-264 | qualifier lost | D.5 |
| SCS-265 | ok | E (verified correct) |
| SCS-266 | ok | |
| SCS-267 | ok | G |
| SCS-268 | ok | C |
| SCS-269 | ok | C |
| SCS-270 | ok | G |
| SCS-271 | ok | |
| SCS-272 | qualifier lost | |
| SCS-273 | ok | |
| SCS-274 | qualifier lost | |
| SCS-275 | number wrong | F.5 |
| SCS-276 | ok | |
| SCS-277 | ok | G |
| SCS-278 | ok | |
| SCS-279 | ok | |
| SCS-280 | ok | C |
| SCS-281 | ok | E.1, G |
| SCS-282 | qualifier lost | D.3, E.1, G |
| SCS-283 | ok | C |
| SCS-284 | ok | C |
| SCS-285 | ok | E (verified correct) |
| SCS-286 | ok | E.3 |
| SCS-287 | ok | E (wording) |
| SCS-288 | ok | |
| SCS-289 | ok | |
| SCS-290 | ok | C |
| SCS-291 | ok | C |
| SCS-292 | ok | |
| SCS-293 | ok | F.1, G |
| SCS-294 | ok | |
| SCS-295 | ok | E.6 |
| SCS-296 | ok | E.6 |
| SCS-297 | ok | F (handled well) |
| SCS-298 | source metadata wrong | E.3, H.3 |
| SCS-299 | ok | C, D.1, E (wording) |

### Counts

| verdict | n |
|---|---|
| ok | 64 |
| qualifier lost | 5 |
| source metadata wrong | 5 |
| scope too wide | 2 |
| number wrong | 2 |
| direction wrong | 0 |
| proposal as finding | 0 |
| tier wrong | 0 |
| cannot check | 0 |
| **total** | **78** |

Note-defect counts, reported separately: **class 1 — 16 entries across 15 records**
(SCS-234 contributes two), plus 4 that the records flag themselves; **class 2 — 5
cases**; **class 3 — 6 cases**; **class 4 — 6 cases**; **section G — 10 smaller items**.

### Tiers

Tallied mechanically (`grep -o "tier: [^.]*" | sort | uniq -c`) over all 78 `tier:`
strings in the block:

- **2** records use one of the brief's three biology strings verbatim: SCS-253
  (`tier: isoform-specific perturbation with phenotype`) and SCS-244
  (`tier: isoform-specific biochemical or binding difference, no organismal phenotype`).
  `tier: correlation of isoform ratio with a phenotype only` is used **0** times.
- **76** carry a descriptive tier of the form `tier: <what was actually done>`, which is
  the correct form for a measurement chapter. There are 70 distinct strings, so the
  tiers are written per record rather than copied.

Every one was scored against what the source did. **No tier claims more than was done**,
so there is no `tier wrong` row. The nearest thing to a stretch is SCS-244's use of
"biochemical or binding difference" for an RT-qPCR fractionation ratio: the string fits
the experiment awkwardly, but it denies the organismal phenotype correctly, which is the
part that could overstate. One tier is slightly ahead of its experiment in a way that is
noted in section G rather than scored (SCS-267).

---

## B. Detail blocks for every row that is not `ok`

```
SCS-223  scope too wide
  claim says: "Among barcoded-array platforms the finest spot pitch is Stereo-seq at
    500 nanometres against Visium HD at 2 micrometres"
  source says: the cited line compares exactly two platforms and makes no claim about
    the class. Its sentence is that Stereo-seq "offers a higher resolution compared to
    Visium HD", introduced as the two higher-resolution assays released since Visium.
    No other array platform is named, so nothing on the line ranks Stereo-seq finest
    overall. The doublet half of the claim is sound and is the authors' own: nuclei-only
    ssDNA staining and roughly 10 micrometres of z-sampling can still produce doublets.
  lines read: PMC13545012 L19-L21
```

```
SCS-224  qualifier lost
  claim says: "neighbouring barcodes are so similar that long reads could not be placed
    reliably at that pitch"
  source says: the line reports a difficulty, scoped to Oxford Nanopore error rates, not
    an impossibility — the similar barcodes "make it challenging to assign reads to the
    exact location, especially for ONT data". The same line then says their own barcode
    caller beat 10x's Space Ranger on precision at comparable recall, and that they did
    keep 2-micrometre resolution for section V1, grouping spots afterwards by cell
    segmentation; only V2 and V3 went into 8-micrometre bins. The claim's second half,
    two of three sections in 8-micrometre bins, is exact.
  lines read: PMC13545012 L61, L64
```

```
SCS-229  number wrong
  claim says: "returned a similar percentage of significant genes as the analysis over
    all cells"
  source says: the cited line's unit is isoforms, not genes — "a similar percentage of
    significant isoforms for each comparison" — which is also the record's own stored
    quote, so claim and quote now disagree about what was counted. The paper's usage
    nearby is itself inconsistent (the Fig. 3 heading and L40 talk about genes
    differentially spliced between regions), so "genes" cannot be taken from this line,
    and in a chapter about gene-level versus isoform-level resolution the swap is
    substantive. The confidence-interval half is exact: every region pair overlapped
    except cortex versus midbrain and thalamus versus white matter.
  lines read: PMC13545012 L39-L41
```

```
SCS-235  source metadata wrong
  claim text is accurate; the defect is in source: authors
  record says: "Eamon, M.; Morgane, F.; Marine, G. I.; Marie, P.; Marie-Jeanne, A.;
    Hugo, C.; Romain, B.; Bernard, M.; Pascal, B.; Kevin, L."
  source says: the corpus byline for this document is in surname-first order, and the
    record has taken each given name for a surname. All ten entries are inverted. The
    surnames are McAndrew, Fierville, Gautier-Isola, Pignol, Arguel, Cadis, Barres,
    Mari, Barbry, Lebrigand. The bibkey (mcandrew2026imaging) is right, so the author
    field and the bibliography key now disagree with each other, and the field as it
    stands hides the author overlap in section E.2.
    Separately, the claim's "leaves cassette exons, mutually exclusive exons and cryptic
    exons out of reach" is firmer than the source, which says those classes "remain
    difficult to interrogate". The 4-6 probes and the 120-nucleotide minimum are exact.
  lines read: bio_c5d1158a6fe7 L4; papers/bio_c5d1158a6fe7/meta.json
```

```
SCS-236  source metadata wrong
  claim text is accurate; the defect is in source: authors
  record says: the same inverted byline as SCS-235
  source says: as SCS-235. Everything measured in the claim is exact on the cited line:
    1,348,351 cells, a mean of 1,124 transcripts per cell, roughly 100-nanometre
    resolution, Xenium Prime 5K, six postnatal stages, two biological replicates per
    stage, one hemisphere per animal.
  lines read: bio_c5d1158a6fe7 L7; meta.json
```

```
SCS-237  source metadata wrong
  claim text is accurate; the defect is in source: authors
  record says: the same inverted byline as SCS-235
  source says: as SCS-235. The claim is exact on the cited line: 27 of 96 probes with a
    median quality value below 20, which the authors say precluded using the full panel.
  lines read: bio_c5d1158a6fe7 L29; meta.json
```

```
SCS-256  scope too wide
  claim says: "A reporter assay that tiled endogenous 3' UTRs in cultured mouse neurons"
  source says: the localisation assay was run in immortalised mouse neuronal cell lines,
    not in neurons, and the paper says so in those words. The Figure 1 outline (L102)
    states that for the RNA localisation measurements "the final reporter library is
    transfected into differentiated neuronal cell lines grown on microporous membranes",
    and reports the neurite-versus-soma measurements in CAD and Neuro-2a cells. The
    localisation methods section (L43) names those two: CAD cells (ATCC CRL-11179) and
    Neuro-2a, a neuroblastoma line, seeded on hanging culture inserts in differentiation
    medium, three biological replicates. (L46, which also names CAD, is the separate
    Actinomycin D stability assay, not this measurement.) "Cultured neurons" appears
    elsewhere only as the provenance of the published transcriptomics used to choose
    which genes to tile.
    Second, smaller point on the same record: the cited line presents the 200-nucleotide
    result as confirmation rather than discovery. It says prior work had already
    annotated most of Camk2a's dendrite-localizing potential to a stretch at the end of
    the 3'UTR present only in the longest isoform, and that their own tile measurements
    are "consistent with these prior findings". The claim keeps the 200 nucleotides and
    the long-isoform specificity, which are right, but drops that framing and the CPEB
    binding sites reported in the same sentence.
  lines read: PMC9561380 L27, L41, L43, L46, L102, L112
```

```
SCS-259  source metadata wrong
  claim text is largely accurate; the defect is in source: authors
  record says: the same inverted byline as SCS-235
  source says: as SCS-235. The Clta narrative is well supported on the cited line: the
    exon-5-only to exon-5-6 switch, the sharpest change between P5 and P7, Cajal-Retzius
    neurons and caudate-putamen medium spiny neurons on the exon-5-6 form throughout.
    Two softenings: the source pairs microglia with CNS macrophages, and says those cell
    types "predominantly expressed" the form lacking both exons rather than simply used
    it.
  lines read: bio_c5d1158a6fe7 L17; meta.json
```

```
SCS-264  qualifier lost
  claim says: "the two cases confirmed by single-molecule imaging in one 2017 study both
    lay between two characterised cell types, while a third confirmed case sat in a gene
    whose expression marked a hidden difference between mature and maturing cells"
  source says: the cited line attributes those confirmations to two different papers,
    not three cases in one. It gives two smFISH-confirmed cases to Song et al. 2017,
    then begins a fresh sentence with "Similarly, Shalek et al., 2013 confirmed one case
    of splicing bimodality". The third case is Shalek 2013 — the same work this block
    records as SCS-266 and SCS-267 — and a writer who reads "in one 2017 study" and then
    "a third confirmed case" will attach all three to the 2017 study.
  lines read: PMC7498265 L63 (context L16)
```

```
SCS-272  qualifier lost
  claim says: "Per-cell isoform ratios are held tight by regulation and not by
    arithmetic"
  source says: the cited line hedges that causal step and then limits it. The authors
    call the increased spread "likely caused by" fluctuations in the regulatory splicing
    machinery, and immediately add that although knockdown was apparent across all
    cells, variability in residual SRSF1 may have contributed as well. The measured
    content of the claim is exact — SRSF1 knockdown, roughly 250 per cent above the
    binomial minimum, immunofluorescence showing knockdown across transfected cells — so
    the defect is confined to the flat causal framing of the opening clause.
  lines read: PMC3159976 L36 (context L31-L33)
```

```
SCS-274  qualifier lost
  claim says: "measured by the UMI-based 3-prime end protocol BATSeq in 48 mouse
    embryonic stem cells in serum, 48 in two inhibitors and 48 neural stem cells"
  source says: those are the cells the protocol was applied to, and the same cited line
    states the filter that removed a quarter of them: 869,000 unique transcript
    molecules were seen across "the 144 sequenced cells", after which cells with fewer
    than 1,000 observed molecules were discarded and "107 cells were included in the
    further analysis". Everything downstream in this paper, the 493-gene set and the
    headline comparison the claim ends with, rests on 107 cells. In a chapter arguing
    about depth, 48/48/48 reads as an analysed n of 144.
    The 493 genes, the 8-to-1,000 molecules per cell per isoform, the 95 per cent
    unobserved, and the high-versus-low expression comparison are all exact.
  lines read: PMC4501847 L20, L36, L37
```

```
SCS-275  number wrong
  claim says: "The same BATSeq data from the same 144 mouse stem cells were used to
    partition the per-cell variance"
  source says: 144 is the number sequenced, not the number partitioned. The same paper
    states that after the 1,000-molecule filter "107 cells were included in the further
    analysis", and the BATBayes fit sits downstream of that filter.
    A second, independent slip in the same sentence: as written, "found genes whose
    observed variance exceeded the no-preference model at p equal to 4.6 times ten to
    the minus 8" invites the reading that individual genes reached that p-value. The
    source reports it as one enrichment test over the gene set, by a binomial test.
    Everything else checks out: a deviance information criterion difference of 393,
    preference variance different from zero in all three stem cell populations, a
    simulated value recovered to within one per cent, and robustness to mis-specified
    and isoform-specific capture efficiencies.
  lines read: PMC4501847 L20, L41, L42
```

```
SCS-282  qualifier lost
  claim says: "Within that one locus the answer differs between exon groups ... although
    both groups are spliced onto the same constant exons"
  source says: the abstract's comparison spans two clusters, not one locus. It describes
    investigating allelic regulation "in the Pcdh-alpha and -gamma clusters, including
    the C-type variable exons (C1 to C5)" and the gammaA and gammaB variable exons, and
    its closing sentence places the monoallelic-versus-biallelic contrast across those
    two clusters. The abstract never assigns C1 to C5 to a single cluster, so the
    record's "within that one locus" — and the note's firmer "inside one transcription
    unit with one set of constant exons" — goes past what the line supports.
    The measured content is exact: almost all P21 Purkinje cells biallelic for all
    C-type isoforms, Pcdh-alpha isoforms both monoallelic and combinatorial.
  lines read: 123334332 L1 (abstract_only)
```

```
SCS-298  source metadata wrong
  claim text is accurate; the defects are in source: preprint and title
  record says: "preprint: true", and title "Single-cell RNA counting at allele- and
    isoform-resolution using Smart-seq3"
  source says: the lines read are the published abstract, not a preprint's. The corpus
    document's metadata gives its source as pubmed with the published title, and the
    abstract carries the journal's superscript reference markers. text_access
    abstract_only is right and the DOI is the journal's, so preprint: true is the one
    wrong field — and it is wrong in the direction SCHEMA.md says the gates cannot see,
    because verify_claims.py will check the quote against a preprint while build_bib.py
    emits the journal.
    The title is also mis-punctuated against both the corpus metadata and the reference
    entry for the same paper inside PMC7498265: the published form is "allele and
    isoform resolution", not "allele- and isoform-resolution".
    The claim's figures are exact: thousands of molecules reconstructed per cell, 60 per
    cent assigned to allelic origin, 30 to 50 per cent to a specific isoform, and
    substantial isoform-usage differences between mouse strains and human cell types.
  lines read: 21851338 L1; papers/21851338/meta.json; PMC7498265 L233
```

---

## C. Defect class 1 — a figure correct in the paper that does not sit on a cited line

All of these keep verdict `ok`: the fact is right and the paper holds it, but not on a
line the record cites, so the gates cannot see it and a reader following the anchor will
not find it. **16 entries across 15 records that the record does not itself flag**, then
4 it does.

| id | the element | where it actually is | cited |
|---|---|---|---|
| SCS-232 | "with segmented single cells as the unit" | L115, which opens "Cell segmentation was performed using a two-step approach" and describes segmenting the MERFISH DAPI volume; the cited line says only "individual cells" | L13 |
| SCS-234 | "scrambled non-targeting probes" | **L149**, which lists "sequences for 5 scrambled, non-targeting control probes for evaluating nonspecific signal". The cited line says only "non-targeting FISH probes" | L25 |
| SCS-234 | note's "five or one probe per set" for the two-colour test | **L149** again, which gives the two-colour colocalisation probe sets as "consisting of 5 or 1 probe(s) per set" — so the note is right, and only its anchor is missing. The cited line gives 30, 5 or 1 probes for the single-colour titration and no count for the two-colour test | L25 |
| SCS-236 | "padlock probes spanning an exon-exon junction, one probe per isoform" | L11 (96 exon-exon junction probes arranged as mutually exclusive pairs across 45 genes) and L29 (single-probe-per-probeset strategies targeting exon-exon junctions) | L7 |
| SCS-237 | note's "96 alternative splicing events across 45 genes" | L11 and L12 | L29 |
| SCS-240 | "the four datasets ... two single sections, their combination and a targeted re-run of one of them" | L48 ("all ONT datasets"), L168 (S1 (AE), S2 (AE), S1 (3.3 K)) and the 3.3 K description, one ONT run on cDNA enriched for 3,378 brain-disease and synaptic genes | L50 |
| SCS-241 | "a Visium HD section the authors treat as a biological replicate" | L60 (V1 theirs, V2 and V3 public) and L175 (V1 cDNA received from 10x Genomics; male mouse, 8 weeks, Charles River) | L66 |
| SCS-263 | "plate-based" | L112, which calls the reanalysed sets "the smart-seq and smart-seq2 datasets" | L38 |
| SCS-268 | the cell count | **L25: 15 single GM12878 cells** | L41, L62 |
| SCS-269 | the cell count; also the pool/split control that strengthens the 282 | L25 for the count; the pool/split control is on cited L63 but unused | L63 |
| SCS-280 | the cell counts | L27: 16,660 cells profiled, 2,737 of them sequenced by both long and short reads | L38, L90 |
| SCS-283 | note's TPM on/off thresholds 2.11 and 20.21 | L25 (2.11, 6.28 and 20.21 TPM by three dichotomisation methods, for Pcdhac2) | L20, L31, L40 |
| SCS-284 | "whose exclusivity held in more than one cell type"; note's "exclusivity suppressed in most of the cell types examined" | L35 (bottom 2.5 percentile of the statistic in at least two cell types, plus a confidence interval below one in at least one) and L33 | L36 |
| SCS-290 | "ERCC spike-in transcripts"; "whose cell-cycle stage had been determined before sequencing" | L61 names ERCC; L65 states the stage was determined experimentally before sequencing | L67 |
| SCS-291 | "because every cell came from one cell line the authors read that variation as dynamic state rather than genotype" | **L65**, which says the cells are all from the same cell line so the variation is most likely dynamic state rather than genetic differences. The 797 figure is on both L65 and cited L71 | L56, L68, L71 |
| SCS-299 | the unambiguous per-cell-type n | **L18**: the 88 isoforms were measured "in 27 single cells for each of the three cell types", i.e. 81 cells in all. Cited L37 gives 27 without saying per what | L14, L15, L35, L37 |

Already flagged by their own notes, recorded for completeness: SCS-221 (the "only half
of the captured molecules contain all exons of a Gencode isoform" bound is on L85),
SCS-228 (the 282-isoform denominator is on L48), SCS-239 (the segmented-cell unit is on
L27), SCS-256 (the roughly 50,000 sequences and the 1,203 tiles from 33 genes are on L15
and L27).

The two sharpest for the chapter are **SCS-268/SCS-269** and **SCS-291**. The Marinov
cell count is 15 — the smallest denominator in this block except Shalek's 18 — and it
sits a few lines from the cited text in a record whose own note calls it "the most
directly useful record in this group". SCS-291's isogenic argument is the entire reason
its 797 genes mean "state" rather than "genotype", and it is on an uncited line.

---

## D. Defect class 2 — notes that assert absence where the thing is present

**5 cases.** Verdicts unchanged; these are `note:` defects.

1. **SCS-299.** Note: *"the number of cells per type is not stated in the lines read."*
   The record cites L37, and L37 ends by saying that single cells were sorted one per
   well into a 384-well plate and **"27 single cells were subjected to the single-cell
   RT-qPCR assay."** So a cell count is on a cited line.
   The paper then states it unambiguously one line outside the citation. **L18**, which
   the record does not cite, says the 88 isoforms of the two conservation groups were
   measured "in 27 single cells for each of the three cell types" — so 27 per cell type,
   81 cells in all, by microfluidic multiplex RT-qPCR. That is the figure the note says
   does not exist, and it is the smallest per-condition n in this block.
   Two things I checked and will not assert beyond the text. On relatedness the paper
   gives two statements that pull different ways: cited L37 says the tested cells came
   from single sub-clones propagated for about ten divisions, while L17 says "the tested
   cells were isolated from distinct sub-colonies". So the cells came from sub-cloned
   populations, and how clonally related they were is not something I can settle from
   the text. And on cell type as a variable, L19 reports that in their mixed model cell
   type "was found not to contribute significantly" (P = 0.91), which supports the
   claim's three named predictors and is worth having beside them.
   This is the most load-bearing absence error in the block: the record is the file's
   anchor for the gene-dependent reading, its note says the depth is unavailable, a
   depth figure is on its own cited line, and the exact per-type figure is one
   uncited line away.

2. **SCS-247.** Note: *"authors and journal are RESOLVE_FROM_DOI: the corpus metadata
   for this record carries no author list."* The corpus metadata carries both the full
   two-author byline and the journal, which is also what the record's own `source:`
   block now holds. The note is stale and sends a later pass to resolve something
   already resolved.

3. **SCS-282.** Note: *"neither record holds an author list in the corpus, so whether
   the two share a laboratory could not be checked here."* It can be checked from the
   records' own bylines — see E.1.

4. **SCS-228.** Note: *"the paper does not say which 8 isoforms were dropped from the
   permutation test."* True of the identities, but it presents as unexplained a
   denominator change the paper does explain: L170 says the cell-type-constrained
   permutation could use only cells carrying a cell-type label, and L171 says the
   comparison p-values were recalculated with ten thousand permutations over just those
   cells rather than a hundred thousand over all of them. The note's further inference
   that "the 45 isoforms that did not survive are the composition-explained remainder"
   also goes past the source: failing a restricted permutation at FDR 0.05 is not the
   same as being explained by composition.

5. **SCS-264.** Note: *"the corpus holds that work only as an abstract with no author
   list, so the identification is not anchored here."* The corpus document does lack
   authors — confirmed in its meta.json — but the identification is anchored by the very
   record the note points at: SCS-288 carries that paper's title, its crossref byline
   ending in Yeo, its journal and its year. The note also omits that the cited line
   names a second paper for the third confirmed case, Shalek 2013, recorded in this same
   block as SCS-266 and SCS-267.

**One absence note verified correct, worth saying so.** SCS-249's note states that the
word isoform does not occur anywhere in that paper's text as held in the corpus, scoped
to that paper. A within-document grep of PMC13284241 returns no match, case-sensitive or
not. Fact and scoping both right.

Two further absence notes are correctly scoped to the searches run rather than to the
world, and I did not try to refute them: SCS-230 ("No source found in these searches
validates a deconvolution method on isoform rather than gene measurements") and SCS-275,
which corrects a lead in the file by naming a study that does partition the variance.

---

## E. Defect class 3 — independence notes wrong, inverted, or missing

**5 cases.** Verdicts unchanged.

1. **SCS-281 and SCS-282 — "could not be checked" is wrong; they share four name
   strings.** SCS-282's note says the shared-laboratory question could not be checked.
   Recomputed from the two records' own bylines:
   - SCS-281: **Esumi, S.**; Kakazu, N.; Taguchi, Y.; **Hirayama, T.**; Sasaki, A.;
     **Hirabayashi, T.**; Koide, T.; Kitsukawa, T.; Hamada, S.; **Yagi, T.**
   - SCS-282: Kaneko, R.; Kato, H.; Kawamura, Y.; **Esumi, S.**; **Hirayama, T.**;
     **Hirabayashi, T.**; **Yagi, T.**

   Four shared name strings — Esumi, Hirayama, Hirabayashi, Yagi — with Yagi last on
   both. Both documents are abstract-only in the corpus, so the correct wording is that
   SCS-282 **shares four name strings with** SCS-281, not that independence is unknown.
   It matters because SCS-282's note sells the record as "the sharpest available answer
   to what the answer depends on" by contrast with SCS-281, and the chapter would be
   presenting one group's follow-up to its own earlier result as a second look at the
   locus. SCS-281's note has the same gap from the other side.

2. **SCS-235, SCS-236, SCS-237 and SCS-259 share two name strings with SCS-221, and no
   note says so.** Read correctly from meta.json, bio_c5d1158a6fe7's last two authors
   are **Barbry Pascal** and **Lebrigand Kevin** — the sixth and the first author of
   SCS-221's source. So the Xenium junction-probe work in SCS-236, SCS-237 and SCS-259
   comes from the same group as the Visium spot-resolution bound in SCS-221. SCS-235's
   note handles independence only in the other direction, calling the authors a rival
   group developing a competing approach, which is true of their stance toward Cohen et
   al. but reads as though the group were new to the chapter. If the chapter uses SCS-221
   to bound spot-based spatial isoform measurement and SCS-236/237 to introduce the
   imaging alternative, it will be citing one group twice and calling it a change of
   method. The author inversion in section B is what hides this: "Pascal, B.; Kevin, L."
   does not look like Barbry and Lebrigand.

3. **SCS-298 shares five name strings with SCS-286, and the note stops one step short.**
   The note says Smart-seq3 "is the chemistry used in SCS-286". It is also the same
   laboratory:
   - SCS-298: Hagemann-Jensen, M.; **Ziegenhain, C.**; Chen, P.; Ramskold, D.;
     **Hendriks, G. J.**; **Larsson, A. J. M.**; Faridani, O. R.; **Sandberg, R.**
   - SCS-286: **Larsson, A. J. M.**; **Ziegenhain, C.**; **Hagemann-Jensen, M.**;
     Reinius, B.; Jacob, T.; Dalessandri, T.; **Hendriks, G. J.**; Kasper, M.;
     **Sandberg, R.**

   Five shared name strings, Sandberg last on both. SCS-298 is abstract-only in the
   corpus, so: shares five name strings with SCS-286. As the file stands, SCS-298 sets
   the ceiling on how deep a phased isoform-resolved measurement can go and SCS-286 is
   the deep measurement — the same laboratory's method paper and its application.
   SCS-265's note already records a third link into that group (its bursting parameters
   come from Larsson et al. 2019, which I verified in PMC7498265's reference list at
   L237 with Sandberg last author), so three records in this block lean on one
   laboratory.

4. **SCS-241 — the note's "both datasets came from the same laboratory" is imprecise in
   a way that flatters the record.** The analysis half of the note is right: one
   software stack, so the replication does not test the analysis. On the generation
   half, L175 says of the Visium HD section in that comparison that the authors
   *received cDNA from 10x Genomics*, who prepared it from a different animal (male, 8
   weeks, Charles River). So the replication crosses platform, animal and library source
   while staying inside one analysis pipeline — a slightly stronger claim than the note
   makes, and a different one. I am leaving the record `ok`: its claim attributes the
   replicate status to the authors ("a Visium HD section the authors treat as a
   biological replicate"), and the sections genuinely are different biological samples.
   The caution is for the writer, not a fault in the claim: the claim's opening word
   "independent" will read as independent evidence if the note's correction is not
   carried with it.

5. **SCS-229 invites a comparison across two studies from one laboratory without
   recording it.** The note says the result "bears on SCS-015, which charged three
   quarters of pooled-tissue isoform differences to one compartment". SCS-015's byline
   (Joglekar, A.; **Prjibelski, A.**; ...; **Tilgner, H. U.**) shares Prjibelski and
   Tilgner with this record's source (Michielsen, L.; **Prjibelski, A. D.**; ...;
   **Tilgner, H. U.**), and L52 of the newer paper says in its own words that "in
   previous work, we proposed three models" for splicing across brain regions. So
   SCS-228 and SCS-229 revisiting SCS-015 is one laboratory revising its own earlier
   model, not an outside check. SCS-222's note records the relationship in general terms
   — "made by the group that generated the earlier Visium-based spatial isoform data" —
   but a writer working from SCS-229 alone will not see it.

6. **SCS-296 reanalyses the very dataset SCS-221 reports, and no note says so.** Fu et
   al.'s spatial section is not a second spatial isoform experiment. Its L70 opens: "we
   revisit the VISIUM Nanopore sequencing of the MOB slice from the experiment conducted
   by Lebrigand et al. [27]", and reference 27 at L166 is "Lebrigand K ... The spatial
   landscape of gene expression isoforms in tissue sections. Nucleic Acids Res. 51, e47
   (2023)" — SCS-221's source. L45 adds the detail that Lebrigand et al. recovered
   40,142 isoforms in 18,724 genes for 918 cells on that sample and that Fu et al.
   benchmarked against that quantification. So SCS-221 and SCS-296 are one mouse
   olfactory bulb section, described by the group that generated it and then reanalysed
   by a second group. The *analysis* is independent — Fu, Zhang and colleagues share no
   name string with Lebrigand, Barbry and colleagues — but the *data* are the same
   section, which is the opposite of what two records about one slice usually mean. The
   same holds for SCS-010 outside this block, which cites the same lines.
   SCS-295's dataset traces to the same group: L59 cites reference 19, which L158 gives
   as "Lebrigand K, Magnone V, Barbry P, Waldmann R. High throughput error corrected
   Nanopore single cell transcriptome sequencing. Nat. Commun. 11, 4025 (2020)". That
   also settles SCS-295's wording: ScNaUmi-seq is 10x Chromium plus Nanopore, so
   "10x-barcoded" is right.
   Taken with E.2, four of this block's spatial records — SCS-221, SCS-295, SCS-296 and
   the SCS-235/236/237/259 group — trace to the Lebrigand and Barbry laboratory, either
   as its own papers or as reanalyses of its data. No note in the block records that.

**Independence notes I recomputed and found correct**, so the next pass need not redo
them: SCS-261 (Yosef is second author of PMC7498265 and an author of Shalek 2013 =
SCS-266/267 — correct, and a good catch); SCS-265 (Larsson 2019, Sandberg last author,
verified at PMC7498265 L237); SCS-246 (same laboratory and same experiment as SCS-244
and SCS-245); SCS-253 ("a different laboratory" from SCS-029 — Lee and Twiss versus
Ciolli Mattioli et al., no shared names); SCS-279 (independent of SCS-009 = Fu et al.
and SCS-029 = Ciolli Mattioli et al.); SCS-280 (no names shared with Fu, Velten or Buen
Abad Najar); SCS-268 (independent of SCS-011 and SCS-013); SCS-292 (Welch et al. and
Westoby et al. share no authors); SCS-293 ("three of its four authors wrote SCS-013" —
exact: Buen Abad Najar, Yosef, Lareau of four); SCS-294 (Horn et al. share no names with
Buen Abad Najar et al.); SCS-299 (Faigenbloom et al., Song et al. and Buen Abad Najar
et al. share no names); SCS-240 (the four datasets are correctly described as not
independent of one another).

**SCS-285 and chapter 2's ANM-004, checked on request.** SCS-285's note says chapter 2
records the same gene's per-neuron isoform count as ANM-004 from an earlier study.
ANM-004's byline in `research/02-animals.yml` is Neves, G.; Zucker, J.; Daly, M.;
Chess, A. (Nature Genetics, 2004); SCS-285's is Miura, S. K.; Martins, A.; Zhang, K. X.;
Graveley, B. R.; Zipursky, S. L. **No shared name strings**, so the chapter can set the
two Dscam1 results side by side. Worth adding to the record, since the note does not say
it either way.

**Two wording points under the dispatch's name-string rule.** SCS-287 ("reached by a
laboratory sharing no authors with SCS-011 or SCS-013") and SCS-299 ("reached by three
laboratories that share no authors") are substantively right on the bylines, but each
involves an abstract-only record with no authors in the corpus, so "laboratory" asserts
more than a crossref byline proves. The findings are sound; only the noun is too strong.

**One cross-record relationship no note in the block records.** SCS-230 and SCS-257 cite
Boileau et al., whose last author is **Dieterich, C.**, who is also an author of SCS-015
and SCS-019. If the chapter sets the heart result beside the brain results as separate
laboratories, that is worth checking.

---

## F. Defect class 4 — a performance figure without its dataset, cells, depth or
## comparison, and benchmarks computed on the method's own labels

**6 cases.** Verdicts unchanged. In each, the missing element lives in `note:` or
nowhere, and `note:` is not citable.

1. **SCS-293 — a benchmark on labels the method itself produced, with the circularity
   absent from the claim.** The claim pairs 798 recovered exons with a sequence
   contrast: the exons it recovered "were more likely to preserve the reading frame and
   had a median conservation score of 2.27 near their splice sites against 1.72 for the
   exons it called cell-state-independent". Both classes in that comparison are the
   method's own output — the cited line contrasts cell-state-associated against
   cell-state-independent cassette exons, both as assigned by the method under test — so
   the sequence features are measured on labels the method produced. The claim carries
   no cell count for the dataset and no denominator for the 798 (both acknowledged only
   in the note, hence uncitably), and the captured-molecule counts the method conditions
   on are not counted but derived from TPM by a modified Census normalisation. Three of
   the four authors also wrote the argument this record extends.

2. **SCS-242 — the comparison is the method's own simulation, and the claim does not
   say so.** The claim reports that t-tests, multivariate correlation and generalised
   linear models all showed inflated p-values under spatial confounding in simulation,
   and that a mixed model controlled the inflation only in part. The scenarios, the
   calibration criterion and the favoured alternative are all the method's own; the
   claim gives neither the simulation design (six scenarios, a thousand genes each,
   which is on the figure line and in the note) nor whose simulator it is. The record is
   otherwise careful: its tier says the assessment is "by the authors of the method being
   compared favourably".

3. **SCS-238 — "no false discoveries" with no simulation parameters and no statement of
   whose simulator.** The claim gives a false-discovery rate of zero for a spatial
   autocorrelation test on simulated null data; the test and the simulation are both the
   authors'. The claim states neither the number of simulated cells nor the number of
   isoforms. The recall half is given qualitatively, which matches the source's own
   limit rather than being the record's doing. The note does supply the right caveat —
   that a zero rate on a null simulation is weaker than it sounds because the simulation
   has no cell-type structure and no coverage artefact — in the wrong field.

4. **SCS-224 — the barcode-placement conclusion rests on a self-benchmark the claim does
   not mention.** "Long reads could not be placed reliably at that pitch" comes from a
   comparison of the authors' own barcode caller against 10x's Space Ranger, on the
   authors' own simulated data with an Oxford Nanopore error profile, with the
   precision/recall trade-off set by their own minimum alignment score. None of the
   comparator, the simulation or the fact that their tool won is in the claim; the note
   mentions only the simulated error profile.

5. **SCS-275 — model-selection figures against the authors' own alternative, with the
   cell count wrong.** The deviance difference of 393 and the p-value of 4.6 times ten
   to the minus eight both compare the authors' preferred model with their own
   no-preference model on their own data, and the claim's stated n is the sequenced
   count rather than the analysed one (section B). To its credit the claim does carry
   the recovery of a simulated value to within one per cent, which is the right kind of
   control to print.

6. **SCS-241 — a p-value of 1.8 times ten to the minus 110 described as cross-platform
   replication.** The two sets that overlap at that p-value (214 and 303 of 2,907
   tested, 149 shared) were both called by the same software, with the same upstream
   pipeline, on data this group sequenced. The note gives the analysis caveat; E.4 gives
   the generation caveat. The record stays `ok`; the caution is that the claim's word
   "independent" and that p-value together will read as stronger evidence than one
   pipeline on two sections can supply.

**Records that handle class 4 well**, for contrast: SCS-233 gives the specificity
control and its note says plainly that a blank-barcode estimate bounds false-positive
decoding and not probe cross-hybridisation between two isoforms of one gene, which is
the error that matters for an isoform call; SCS-240 puts the 87.3-per-cent-explained-by
-depth result in the claim rather than burying it; SCS-243 is explicitly a comparison by
a group that authored none of the six packages, which I verified (the six are SpatialDE,
SPARK-X, Squidpy, Seurat, SpaGCN and scGCO, none of them by Charitakis et al.); SCS-297
carries its concession about depth in the claim itself.

---

## G. Smaller observations, not scored

- **SCS-270, note number wrong.** "other rows range from 105 to 306 cells" — the table
  runs to **345** (PMC3159976 L105, MKNK2 Rpe1 experiment 2). The claim's own 191 and
  163 are exact.
- **SCS-256, note number conflated.** "The library held about 50,000 sequences in
  150-nucleotide tiles" merges two figures: roughly 50,000 sequences is the whole MPRA
  (L15), while the endogenous-3'UTR tiling sublibrary of 150-nucleotide tiles was 13,754
  tiles after deduplication (L27).
- **SCS-293, note attribution loose.** "by the same normalisation SCS-013 introduced".
  L43 says the estimate uses a modification of the Census normalisation of Qiu et al.
  2017 as described by Buen Abad Najar et al. 2020 — SCS-013 described a modification of
  somebody else's normalisation.
- **SCS-282, note count wrong.** "one of only two phased per-cell isoform measurements
  here, with SCS-286" — SCS-281 is also allele-resolved, and SCS-298 reports 60 per cent
  of molecules assigned to allelic origin. At least four, not two.
- **SCS-232, "a MERFISH run" singular.** The roughly 33,000 RNAs were imaged with three
  codebooks back to back (L146 and L147); the record's note says so, the claim does not.
- **SCS-245, a hedge tightened.** "the delta-isoform signal almost entirely in the cell
  body", where the cited line says the signal was mostly restricted to the cell soma
  and, later in the same line, that the imaging was "indicative of relative more"
  delta-isoform message in the central part of the cells.
- **SCS-277, a hedge dropped.** "mean molecules per cell, average ratio and variance all
  matching the model's predictions"; the cited line says the *tendencies* of those three
  quantities matched.
- **SCS-267, tier slightly ahead of the experiment.** The tier reads "amplification-free
  imaging of two isoforms in the same cell". On the cited line that holds for Acpp, where
  two probes detect mutually exclusive final exons, but for Irf7 the probes were
  constitutive plus isoform-specific — which the claim itself states correctly, so only
  the tier overreaches. "dual-colour" is also not on the cited line, though it is the
  obvious reading.
- **SCS-281, a method word from the companion paper.** "multiple reverse-transcription
  reactions split from single Purkinje cells" — split RT is SCS-282's abstract's word;
  this abstract says multiple RT-PCR reactions. Everything else on the line is exact,
  including the two mouse strains that anchor the species.
- **SCS-281 and SCS-282, Greek letters normalised.** Both record titles spell out
  "alpha" and "gamma" where the corpus titles carry the Greek characters. Benign, but
  `lookup title` will not match either record's stored title.

---

## H. Metadata diff over all 37 cited documents

Title, authors, journal, year, DOI and corpus source were compared mechanically for
every cited document. Three findings beyond the five `source metadata wrong` verdicts:

1. **No other mismatch.** The comparison normalised case, punctuation and diacritics,
   so it would not catch a stray hyphen on its own; SCS-298's title error was found by
   reading, not by the diff. DOI, journal and year agree with the corpus metadata for
   all 37 documents. Title agrees for **34**; the three exceptions are the two
   Greek-letter normalisations in section G, which are benign, and the SCS-298
   punctuation error scored in section B. Bylines agree for all documents except
   bio_c5d1158a6fe7. For the five bioRxiv documents whose author field is
   comma-separated in the corpus, I re-extracted the full list and confirmed
   name-for-name agreement with the records: bio_654e1f147131 (12 names, in a different
   order from the corpus preprint — I did not check which published version matches
   that order), bio_6b4afd596f2e (3), bio_8065490174b9 (13), bio_e2e721a46c39 (23),
   bio_e34cad4f6cf8 (6).

2. **SCS-253, SCS-254, SCS-255 — the preprint read is three years older than the journal
   version the record cites, and no note says so.** The corpus document is dated
   **2018-07-10** with DOI **10.1101/366369**, while the records carry the 2021 Journal
   of Cell Science DOI and year. `preprint: true` is set and the note says the lines were
   read as a bioRxiv preprint with no journal version in the corpus, so SCHEMA.md is
   satisfied and the verdict stays `ok`. But a three-year gap spans at least one round
   of review: the quoted rescue result may not read the same way in the published paper,
   and `research/ALLOCATION.md` should list this source among those where preprint and
   journal diverge. The same pattern, with a shorter gap, applies to bio_e34cad4f6cf8
   (posted 2025-08-27, cited as Cell 2026) and bio_6b4afd596f2e (posted 2020-08-24,
   cited as Frontiers 2021); both of those notes do state the divergence.

3. **`preprint:` flags.** Correctly set on bio_e34cad4f6cf8, bio_c5d1158a6fe7,
   bio_654e1f147131, bio_8065490174b9, bio_e2e721a46c39 and bio_6b4afd596f2e — each
   confirmed from its meta.json `"source": "biorxiv"` and bioRxiv DOI or posting date,
   not from the id prefix. Correctly absent from PMC13545012, PMC13284241, PMC13585551
   and PMC12276307, each of which is the journal version (their L2 reads "Nature Methods
   (2026)", "Nature Communications (2026)", "Nature Plants (2026)" and "Nature
   Communications (2025)"). Wrongly set on 21851338, which meta.json gives as a pubmed
   record of the published paper — scored in section B. SCS-236's note that
   bio_c5d1158a6fe7's corpus posting date is a placeholder is right: meta.json gives
   2026-01-01 against a DOI of 2026.09.22.

## I. Other checks run that came back clean

- Each record's stored quote was located on the line label the record cites, in the text
  I pulled for that document. I did this by eye while reading each line, not by script,
  and byte-exactness is `verify_claims.py`'s job, not mine — so the claim here is only
  that no cited label had moved and no cited line had stopped holding the quoted span.
  That is why there is no `cannot check` row.
- SCS-290 was re-read to the end of L67 after an initial truncated read: the line
  carries the whole Rbm25 result, including that the two splice variants' distribution
  across single cells is "bimodal, with modes at 0 and 1, indicating that most cells
  almost exclusively express either one form or the other", and that the variant with
  two internal exons is used far more in G2/M than in the other phases. Verdict `ok`
  confirmed against the full line.
- Absence checks re-run **inside** the specific document rather than across the corpus,
  and with the matched text read in full rather than truncated — my first pass on two of
  these reported an absence that a truncated grep window had hidden, so each result
  below is from reading the matching line:
  - "isoform" in PMC13284241: **absent**, confirming SCS-249's note.
  - "scrambled" in bio_e34cad4f6cf8: **present**, at L149 — so SCS-234's wording is
    supported by the paper and belongs in section C, not in section G. The same line
    also supports that record's note.
  - the cell count in PMC4704489: **present**, on cited L37 and unambiguously on
    uncited L18, contradicting SCS-299's note.
  - "segment" in bio_e34cad4f6cf8: **present**, at L115, supporting SCS-232's claim off
    its cited line.
  - the cell counts in PMC3941114 (15, L25) and bio_e2e721a46c39 (16,660 and 2,737,
    L27): present, off the cited lines.
  - the analysed cell count in PMC4856971: **not found in a within-document search of
    its main text and methods** (lines 1-120 of 139, the remainder being references),
    scanning for two-to-four-digit figures next to "cells", for "n =" next to "cells"
    and for "number of cells"; the only numeric hit is a generic remark that as many as
    96 cells are usually sequenced in one HiSeq run. So SCS-290's and SCS-291's
    scoping holds, within that search.
- Cross-record figures the notes assert and I confirmed: the 2,731-exon pool behind
  SCS-299's 44 exons (L14); the 96 junction probes across 45 genes behind SCS-237 (L11);
  the "only half of the captured molecules contain all exons of a Gencode isoform" bound
  behind SCS-221 (L85); the 274-versus-282 denominator behind SCS-228 (L48 with L170 and
  L171); Shalek's roughly 27 million reads per cell named by Westoby, which SCS-297's
  note identifies as SCS-266 (PMC7087381 L24); the Larsson 2019 bursting-parameter
  provenance behind SCS-265 (PMC7498265 L237).
- Dataset provenance for SCS-295 and SCS-296, traced through Fu et al.'s own reference
  list rather than assumed: reference 19 at L158 (Lebrigand et al., Nat. Commun. 2020)
  for the mouse embryonic brain single-cell data, which confirms "10x-barcoded", and
  reference 27 at L166 (Lebrigand et al., Nucleic Acids Res. 2023) for the olfactory
  bulb Visium slice. The second is the finding in E.6.
