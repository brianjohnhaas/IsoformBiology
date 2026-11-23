# Reviewer D -- records NEU-221..NEU-259, research/07-neuro-mendelian.yml, against their sources

NEU-221 no longer exists: the file's own trailing note (research/07-neuro-mendelian.yml L11226)
records it as removed on 2026-11-23 together with NEU-031. Item 1 was therefore checked against
NEU-262, which carries the same finding from the PUBLISHED abstract (doc 50091604). Assigned range
as it stands = NEU-222..NEU-259 = 38 records.

Verdict column holds only the nine permitted strings. Note-level defects that do not change the
claim-vs-source verdict are in section B. One rule applied throughout: the verdict answers
claim-vs-cited-lines, source metadata (including whether the cited lines carry the claim) and tier;
errors confined to `note:` go to section B.

## A. Verdict table

NEU-222  ok
NEU-223  qualifier lost
NEU-224  ok
NEU-225  qualifier lost
NEU-226  ok
NEU-227  qualifier lost
NEU-228  tier wrong
NEU-229  ok
NEU-230  qualifier lost
NEU-231  source metadata wrong
NEU-232  ok
NEU-233  tier wrong
NEU-234  ok
NEU-235  tier wrong
NEU-236  tier wrong
NEU-237  tier wrong
NEU-238  ok
NEU-239  ok
NEU-240  ok
NEU-241  scope too wide
NEU-242  ok
NEU-243  ok
NEU-244  qualifier lost
NEU-245  number wrong
NEU-246  ok
NEU-247  source metadata wrong
NEU-248  ok
NEU-249  ok
NEU-250  ok
NEU-251  direction wrong
NEU-252  ok
NEU-253  qualifier lost
NEU-254  ok
NEU-255  ok
NEU-256  ok
NEU-257  ok
NEU-258  ok
NEU-259  qualifier lost

Plus, for the record: NEU-221  cannot check (record removed from the file).

13 of 38 not ok. Zero arithmetic errors found other than the denominator mismatch at NEU-245.
Every figure in every claim sits on a line the record cites, with two exceptions (NEU-231, NEU-247)
and one partial (NEU-245), reported below.

## Blocks

NEU-223  qualifier lost
  claim says: "the pseudoexon-containing transcripts were 7.2-fold lower than in a heterozygous patient"
  source says: L103 ends the same sentence with "although additional samples would be needed to
    determine statistical significance". The hedge survives only in `note:`, so it cannot be cited.
    n = 1 mosaic patient against 1 heterozygous comparator for this measurement.
  lines read: med_4df3cec76efa L100-L116

NEU-225  qualifier lost
  claim says: "tibialis anterior and gastrocnemius masses at 8 and 24 weeks were significantly lower
    in homozygotes"
  source says: L29 states the same but with an exception the record drops entirely -- "except for
    males' tibialis anterior at 24 weeks in which the muscle masses were decreased but did not reach
    significance". Separately, L33 says grip strength was weaker at all ages 4-20 weeks but
    significant only "at most tested age timepoints"; the claim's "weaker ... at every age tested"
    carries the observation without that significance caveat. Neither qualifier is in claim or note.
  lines read: bio_74a952f870df L24-L38

NEU-227  qualifier lost
  claim says: "94.7 per cent for (TG)10T9, 88.0 per cent for (TG)10T7, 80.9 per cent for (TG)11T7,
    47.5 per cent for (TG)11T5 and 27.6 per cent for (TG)12T5"
  source says: L23 and L28 give exactly these five averages, but the per-genotype group sizes are
    3, 2, 5, 1 and 2 subjects. The (TG)11T5 figure is one subject and the (TG)12T5 average is two
    subjects whose individual values are 36.2 and 19.1 per cent (L28). The claim gives only the
    pooled n = 13; the per-genotype n lives in `note:` alone, so a five-point "stepwise" curve can be
    quoted with no indication that two of its points are n = 1 and n = 2.
  lines read: PMC7911278 L22-L29, L7
  secondary, flagged rather than asserted: the tier string is "correlation of isoform ratio with a
    phenotype only", but the claim measures isoform ratio against genotype and reports no phenotype
    outcome. A descriptive tier ("quantification of isoform ratio by haplotype in nasal brushings")
    would match what the source did.

NEU-228  tier wrong
  claim says: (claim itself is fully supported -- 62/42/13 at L12, the table's 39/10/6/191 at L48,
    sweat chloride 82+-14 (28) against 35+-8 (10) at L58, FEV1 -0.6/+0.17/-1.02 at L33, all on cited
    lines)
  source says: nothing in this paper measures an isoform ratio. The note itself concedes it -- "the
    isoform ratio is not measured here at all, only inferred from the tract length" -- while the tier
    string asserts "correlation of isoform ratio with a phenotype only". Per the brief, forcing one of
    the three isoform strings onto a record whose own note denies it reads as a tier error. A
    descriptive tier (genotype-phenotype correlation in a single-centre registry cohort) matches.
  lines read: PMC5566269 L10-L13, L32-L35, L45-L49, L57-L58, L65, L86-L90
  The note's three-counts caveat (42 at L12, 39 at L48, 37 at L89) is correct, confirmed at all three.

NEU-230  qualifier lost
  claim says: "with TG13T5 homozygotes at 255.7 against 581.7 for carriers of two disease-causing
    variants"
  source says: L42 reports both odds ratios and then states the TG13T5 homozygous genotype was
    enriched "similar (Chi-square statistic, p = 0.56) to the 2xCFvar genotype". The authors say the
    two are statistically indistinguishable; the claim's "255.7 against 581.7" reads as a contrast,
    and the p = 0.56 appears in neither claim nor note.
  lines read: med_c100b8376c2a L10-L11, L33-L35, L41-L42
  Everything else in NEU-230 checks: 548,300, MAF 4.2 per cent, ORs 6.9 / 32.0 / 78.8, the hereditary
  cancer comparison group and the p.Arg117His exclusion are all on the cited L11, L34 and L42.

NEU-231  source metadata wrong (cited lines do not carry the claim's scope)
  claim says: "a 5' nuclease assay on patient lymphocyte RNA found the correct E1 transcript reduced
    about twofold and the E2 transcript raised about 1.4-fold against three healthy controls"
  source says: the two fold-changes are on cited L63. But the assay name is at L49/L51, the "three
    healthy female control individuals" and the three biological replicates at L50, and lymphocyte
    RNA at L11/L32 -- none of which the record cites (it cites L13, L63 only). The content is all
    true; three of the claim's four scope elements are not on the cited lines.
  lines read: PMC3729535 L11-L15, L32, L49-L53, L61-L68
  Everything in the claim is otherwise correct, including "de novo", which is the paper's own word
  at L9 (L61 hedges it to "likely to be de novo").

NEU-233  tier wrong
  claim says: (supported -- the knock-ins, the Prpf31 heterozygote, basal infolding loss,
    vacuolisation, deposits to Bruch's membrane, two years / one year, and the authors' RPE-as-primary
    inference, all on L1)
  source says: the tier string is "isoform-specific perturbation with phenotype", and the note then
    states the record "does not satisfy criterion 2 of the project's inclusion test". The perturbation
    is a single-codon knock-in or a gene-dose change in a spliceosome component; a descriptive tier is
    what the brief asks for.
  lines read: 100274596 L1 (abstract-only)
  secondary, flagged: the claim says "with decreased rod function reported for the Prpf3-T494M line".
  L1's sentence is "These changes were more severe in the homozygous mice, and were associated with
  decreased rod function in the Prpf3-T494M mice", which reads as attaching the rod deficit to the
  homozygotes. The claim and note both state it of the line without a genotype.

NEU-235  tier wrong
  claim says: (supported verbatim -- "no degenerative phenotype on fundus examination" in both
    heterozygotes, both homozygous genotypes embryonic lethal, and the authors' two conclusions)
  source says: the tier is "isoform-specific perturbation with phenotype", which the note then denies
    ("Like NEU-233 it does not meet criterion 2 ... the perturbation is of a splicing factor's gene
    dose, not of an isoform").
  lines read: 104814022 L1 (abstract-only)
  The record's scoping to fundus examination is correct and narrower than "no retinal phenotype at
  all": the abstract also says ERG and retinal morphology were done, and reports only
  "Generation of the mouse models is presented, as are results of ERGs and retinal morphology".

NEU-236  tier wrong
  claim says: (supported -- PRPF8 Y2334N = p.Tyr2334Asn, thinner outer segment layer, minor mRNA
    changes across retinal cells, and the authors' RPE-independent reading, all on L14)
  source says: tier "isoform-specific perturbation with phenotype", which the note denies in the same
    breath ("again not isoform-specific in the sense criterion 2 ... requires").
  lines read: bio_e7db55d16d24 L14
  secondary, flagged: "splicing changes concentrated in genes linked to neural and retinal disease".
  L14 says only "We found splicing alterations in genes associated with neural and retinal diseases";
  "concentrated" asserts an enrichment the cited line does not quantify.

NEU-237  tier wrong
  claim says: (supported -- 3 or 4 MSR1 copies, 50 to 115-fold in vitro repression, the 4-copy allele
    absent from symptomatic carriers and tracking asymptomatic-carrier rates, all on L8)
  source says: tier "correlation of isoform ratio with a phenotype only", which the note denies
    ("strictly it is not an isoform ratio at all ... does not meet criterion 2").
  lines read: PMC4725990 L8
  Minor: L8 says 3 copies "can repress"; the claim states "repressed".

NEU-241  scope too wide
  claim says: "for 91 variants with both kinds of data, minigene and patient-derived RNA results
    showed complete or high concordance in the predominant transcript in 89 per cent of cases, 81 of 91"
  source says: the 89 per cent (81/91) is on cited L13, but the traditional-minigene dataset it comes
    from is 673 variants "in seven cancer susceptibility genes (ATM, BRCA2, CHEK2, PALB2, RAD51C,
    RAD51D, and TP53)" from 14 publications (L11, L27, L35). Neither the claim nor the note states the
    seven-gene restriction; the note gives only "673 variants across 14 studies". A reporter-against-
    patient concordance figure measured on seven cancer-predisposition genes is presented as a
    general one.
  lines read: PMC13753216 L11, L13, L23, L27, L35

NEU-244  qualifier lost
  claim says: "the assays they used excluded deep-intronic variants ... and plasmid-borne assays
    cannot register effects that come from transcription elongation rate or nucleosome positioning"
  source says: both halves are verbatim on cited L53, but the same L53 ends "Despite these potential
    issues, minigene assays are often well correlated across cell lines ... and have a sufficient
    track record of concordance with blood RNA analysis that they are often deemed acceptable as
    functional evidence during clinical variant interpretation ... Moreover, even when minigene assays
    misidentify a variant's aberrant splicing outcome(s), they may still correctly flag the variant
    itself as splice disruptive." The record takes the limitation half of a passage whose authors close
    by defending the assay, and neither claim nor note carries the defence. NEU-256's note handles the
    same situation correctly on a different paper, which is the contrast that makes this a defect.
  lines read: PMC10734170 L53

NEU-245  number wrong (denominator)
  claim says: "Among 24,445 variants in the extended acceptor region reported to ClinVar and the
    Leiden Open Variation Database across 2,100 genes, only 11.7 per cent of the pathogenic variants
    lay outside the essential AG"
  source says: the 24,445 and the 2,100 genes are the study's extended-acceptor set (L19). The 11.7
    per cent / n = 638 is a fraction of the pathogenic variants in a DIFFERENT set: L47 gives
    "the 30,042 intronic variants located at the acceptor splice-site, PPT, or branch-site", of which
    18.2 per cent were pathogenic, and L17 gives that count as n = 5,463. 11.7 per cent of 5,463 = 639,
    which is the 638. The two totals cannot be combined as the claim combines them: within the 24,445
    extended-acceptor set essentially every pathogenic variant is by definition outside the essential
    AG, so 11.7 per cent is not a fraction of anything in that set. The real denominator (5,463
    pathogenic of 30,042) is on L17 and L47, neither of which the record cites.
  lines read: PMC9284458 L11, L17, L19, L47-L48
  The three mechanism percentages are right and are the results figures, not the abstract's -- see
  item 9 below.

NEU-247  source metadata wrong (cited lines do not carry the claim's premises)
  claim says: "Taking inborn errors of metabolism screened in newborns as a test case, where a
    pathogenic genotype found in a healthy adult is almost certainly an error of classification, the
    set HGMD marks disease-causing points to roughly a hundredfold more sick people among 1000 Genomes
    participants than the set ClinVar marks pathogenic or likely pathogenic does"
  source says: the hundredfold comparison is on cited L15 ("two orders of magnitude"). But the
    newborn-screened-IEM model system and the premise that such a genotype in a healthy adult implies
    misclassification are at L13 ("We considered inborn errors of metabolism (IEMs) screened in
    newborns as a model system ... Due to the rarity of IEMs, nearly all such classified pathogenic
    genotypes indicate likely variant misclassification") and are developed at L27. The record cites
    L15 only, so the two clauses that make the claim interpretable rest on uncited lines.
  lines read: PMC10347827 L13, L15, L25-L27

NEU-251  direction wrong
  claim says: "those authors say both sit closer to their 27 per cent than the ClinVar figure of
    about 17 per cent does"
  source says: L55 says "These values are closer to our 27% estimate than to the ClinVar proportion of
    ~17%" -- each of the two database figures is nearer to 27 than it is to 17. The record turns this
    into a comparison of each database figure's distance from 27 against ClinVar's distance from 27,
    and in that form it is false for one of the two: |43-27| = 16 while |17-27| = 10, so the ~43 per
    cent is further from 27 than ClinVar's ~17 per cent is. The note repeats the same inversion
    ("It says the opposite, that they are closer to it than ClinVar's is"), so the error is in both
    fields. The ordering of the databases is not reversed; what is wrong is which two distances are
    being compared. The claim also omits the same line's two characterisations: L55 calls the ~30 per
    cent "consistent with our data" and the ~43 per cent "above our upper bound".
  lines read: PMC6360807 L55

NEU-253  qualifier lost
  claim says: "and the authors say they cannot state that what a minigene shows would hold in the
    patient's full genetic, developmental and cellular context"
  source says: cited L58 does say that, but it opens the sentence with the counterweight the record
    drops -- "Although the accuracy of minigene assays compared with patient RNA is generally high
    (Bonnet et al. 2008; Thery et al. 2011; van der Klift et al. 2015), known limitations ... mean we
    cannot definitively state ...". Neither claim nor note carries the authors' "generally high", and
    the claim also drops "definitively". Same defect as NEU-244, on a different paper.
  lines read: PMC6360807 L58
  The 5-of-6 PolyPy result, the don+5 variant, the one negative PolyPy and the one VUS are all exact
  on L58, and the note's "eight variants only, chosen as the potentially diagnostic ones" is right.

NEU-259  qualifier lost (unlabelled fraction)
  claim says: "99 per cent of the variants one assay reported as abnormally spliced carried a SpliceAI
    score of 0.2 or more, where for the other massively parallel assays that proportion ran from 9 to
    66 per cent"
  source says: L60 supports both figures, and names the assay -- ParSE-seq. The claim names no assay
    and gives no numerator or denominator for either figure, in a section whose whole argument is that
    a fraction means nothing without its ascertainment. The assay identity is recoverable only from
    `note:`, where it is also absent (the note says "one assay" too); it has to be reconstructed from
    NEU-249 or NEU-258. This is the least citable fraction in the assigned range.
  lines read: PMC13753216 L60

## B. Note-level defects (claim verdict unaffected)

1. Notes that misstate their own source.
   - NEU-246. The note says the SpliceAI pair could not be recorded because "the sentence is truncated
     in the corpus text before the matching specificity, so the pair could not be read together".
     PMC9284458 L55 carries the whole sentence: "To discriminate pathogenic from benign AG-creating
     variants with 95% sensitivity, we found that using a SpliceAI acceptor delta cutoff of 0.48 ...
     provided the highest specificity at 69%", and L56's Fig. 3C legend repeats both numbers with
     n = 262 pathogenic and n = 198 benign. A true finding was left out on a false premise.
   - NEU-229. The note's contrast "the sweat chloride and pancreatic status differences did [reach
     significance]" is not supported for the comparison the record is about. PMC5566269 L65 lists the
     Bonferroni-corrected significant comparisons as ##: 5T vs p.Phe508del; para-para: 7T vs
     p.Arg117His/p.Gly551Asp; ++: 7T vs p.Phe508del; section-section: p.Gly551Asp vs p.Phe508del. The
     sweat chloride row (L58) carries ##, para-para and section-section and the pancreatic row (L60)
     carries ##, ++ and section-section -- 5T vs 7T is in neither. The paper never states that 5T vs 7T
     sweat chloride was significant; the record's note infers it from the four-group p < 0.0001. (The
     paper also never states it was non-significant, so the right wording is "not marked significant
     in the L65 legend".) NEU-229's claim itself -- that only two pairwise FEV1 comparisons reached
     significance and 5T vs 7T did not -- is exact at L35, including the p = 0.03 and p = 0.004.
   - NEU-262 (checked for item 1). "The denominator of the external cohort is not given in the
     abstract, so the quarter has no numerator here." Inverted: 27 IS the numerator and is stated;
     what the abstract withholds is the denominator.

2. Notes asserting RESOLVE_FROM_DOI for fields the record now carries. In each case the bibliographic
   fields are present and correct with metadata_source: crossref, and `paperclip grep` on the
   corresponding meta.json confirms the note's description of meta.json; the note is simply stale and
   will mislead the next reader about what still needs resolving.
   - NEU-222 ("The author list in meta.json is truncated mid-name, so authors is left as
     RESOLVE_FROM_DOI") -- the record now carries the full 60-plus-name Foley author list.
   - NEU-233, NEU-234 (by reference), NEU-235 -- "no author list and no journal in meta.json, so both
     are RESOLVE_FROM_DOI"; both records now carry authors and journal.
   - NEU-239 -- same wording; the record carries Chong, Insigne, Yao ... Kosuri and Molecular Cell.
   The title-derived bibkeys those notes mention are still title-derived, which is consistent.

3. Dead cross-references to the removed NEU-221.
   - NEU-222 claim: "The international cohort assembled for the same COL6A1 intron 11 variant" -- "the
     same" has no antecedent left in the file.
   - NEU-222 note: "Not independent of NEU-221: the author list ... carries Foley, Bolduc, Cummings,
     Lek and Donkervoort, who are also on NEU-221".
   - NEU-224 note: "which is why NEU-221's claim does not use those words" and "Shares a laboratory
     with NEU-221 to NEU-223".
   The independence statements are still true of NEU-262 (Cummings, Foley, Bolduc, Donkervoort,
   Bonnemann all appear on doc 50091604's author list), but they point at an id that is gone.

4. Independence declarations missing where five or six records share one paper.
   - PMC13753216 carries NEU-240, NEU-241, NEU-249, NEU-258, NEU-259. Only NEU-249 lists all four
     others. NEU-258's note declares no shared source at all. NEU-259's note lists NEU-240, NEU-241
     and NEU-258 but omits NEU-249.
   - PMC6360807 carries NEU-250, NEU-251, NEU-252, NEU-253 (plus the existing NEU-029 and NEU-030).
     NEU-252 and NEU-253 declare no shared source.
   - PMC10734170 carries NEU-242, NEU-243, NEU-244. NEU-244 declares none.
   - PMC6679692 carries NEU-254, NEU-255, NEU-256, NEU-257 (plus NEU-026, NEU-027). None of the four
     says so explicitly, though each cross-references NEU-026 or NEU-027 by id.

5. Retinal independence, now checkable. NEU-236's note says "Whether the two groups are independent
   could not be checked, because the author lists for NEU-233 and NEU-235 are not in the corpus and
   are marked RESOLVE_FROM_DOI." The lists are in the records. Reading them:
   - NEU-233 (Graziotto et al.) and NEU-235 (Bujakowska et al.) share Bujakowska, K. and
     Bhattacharya, S. S. The mouse-RPE result and the no-fundus-phenotype result are therefore NOT
     independent of each other, and NEU-235's note calls them "in tension" without saying so.
   - NEU-237 (Rose et al.) also carries Bhattacharya, S. S., so three of the four retinal records
     share a senior author. NEU-237's note says nothing about it.
   - NEU-236 (Zimmann et al.) shares no author with any of the three. The organoid result is the
     independent leg of the disagreement, which is the opposite of what its note implies.

6. NEU-249's note goes slightly beyond its paper in two places.
   - "What follows is a caution about the score as a continuous measure, not a refutation of the 513
     calls". PMC13753216 L60 does bear on the calls, not only the score: it compares SpliceAI against
     each study's assay-DEFINED spliceogenic and non-spliceogenic variants and says "All other MPSA
     studies had notable overlap of SpliceAI score distributions between reported spliceogenic and
     non-spliceogenic variants, suggesting misclassification". The distinction is the record's own
     inference and is narrower than the paper's reading.
   - "which were made by requiring an effect in two independent assays" is the record's wording.
     PMC6679692 L31 says "in vivo and in vitro", and its L36 shows one 200-mer oligo library was used
     to generate both reporters, so the two readouts share their input library.

7. Records with no tier line at all, neither one of the three strings nor a descriptive or "No tier"
   statement: NEU-229, NEU-241, NEU-242, NEU-243, NEU-246, NEU-255, NEU-259. Absence is a different
   gap from a mismatch, so these are not scored `tier wrong`, but seven of 38 is worth a pass.

8. Smaller, reported for completeness, each checked.
   - NEU-226 calls the two extra cohorts "two cardiac cohorts". med_fab8675f75f5 L18 says "focused on
     aortopathy and dilated cardiomyopathy"; aortopathy is not cardiac.
   - NEU-227's note gives "a standard deviation of 12.1 percentage points" for the (TG)12T5 pair. The
     paper states only the two values 36.2 and 19.1 (L28); 12.1 is the record's own computation.
   - NEU-240's claim says the datasets "generally did not report which transcript a variant induced".
     L56 is stronger: "All seven published MPSA datasets lacked information on specific splice
     isoforms produced by each variant assayed." The record understates its source.
   - NEU-252 drops "explicitly" from L56's "nor did it explicitly include branchpoints, splicing
     enhancers and suppressors, or deep intronic mutations", turning a hedged exclusion into a flat one.
     The lower-bound conclusion and the "may be conservative" are the authors' own words, verbatim.
   - NEU-254 says exons of "100 nucleotides or fewer" (L36 "<= 100 nucleotides"); NEU-256 says "shorter
     than 100 nucleotides" (L32 "fewer than 100 nucleotides"). Each follows its own cited line; the
     paper is internally inconsistent, and a chapter printing both will look wrong.
   - NEU-257's claim calls the one-third "the share ... that an algorithm expects to mis-splice".
     PMC6679692 L15 says only "are predicted to confer some degrees of missplicing"; "an algorithm" is
     the record's gloss, defensible from reference 7's title but not stated at the cited line. The
     independence content of that note is exactly right and was verified: L88 is Lim, Ferraris,
     Filloux, Raphael and Fairbrother (2011), sharing its last author with the assay paper;
     research/06-cancer.yml L4067 gives rhine2018hereditary as Rhine, Cygan, Soemedi, Maguire, Murray,
     Monaghan, Fairbrother (three shared authors, not one); and research/06-cancer.yml L4099 gives
     soukarieh2016exonic with no shared author, as the note claims.
   - NEU-248's final clause, "so a fraction computed over HGMD has no benign denominator available to
     it", is the record's own inference. L26 supports the premise verbatim; the conclusion is not in
     the paper. It is sound, but it is the record talking.
   - Preprint flags: all five preprint-sourced records in range carry preprint: true
     (NEU-222/223 med_4df3cec76efa, NEU-224/225 bio_74a952f870df, NEU-226 med_fab8675f75f5,
     NEU-230 med_c100b8376c2a, NEU-236 bio_e7db55d16d24) and each says so in `note:`. The two 2026
     journal records (PMC13753216 Genome Medicine, PMC13061089 Science Translational Medicine) are not
     preprints and correctly carry no flag. Every bibkey in range maps to exactly one DOI across
     research/*.yml.

## C. The ten items

Confirmed.
1. Confirmed, but against NEU-262, not NEU-221, which no longer exists. Doc 50091604 L1, verbatim:
   "We identify this pathogenic variant in a total of 27 genetically unsolved patients in an external
   collagen VI-like dystrophy cohort, thus explaining approximately 25% of patients clinically
   suggestive of having collagen VI dystrophy in whom prior genetic analysis is negative." The
   denominator is exactly as the dispatch states and is much narrower than a whole COL6 cohort. The
   abstract gives the numerator (27) but not the denominator; NEU-262's note has that backwards.
2. Confirmed in full, every figure and both p-values, all on the single cited line PMC6360807 L54:
   27 per cent with 95 per cent CI 18-39; ClinVar P/LP on the same splicing positions with
   nonsynonymous consequences removed, 83.5 per cent canonical and 16.5 per cent non-canonical; 17.5
   per cent after adjusting for submission count; "Fisher's exact test P = 1.22 x 10-15 and
   P < 2.2 x 10-16, respectively", so 1.22e-15 pairs with 16.5 and <2.2e-16 with 17.5, which is the
   order the claim uses; and the authors' own "underascertainment of noncanonical splicing variants by
   ~35%-40% in clinical databases". NEU-252 confirmed at L56: the four excluded classes are exonic
   missense, branchpoints, splicing enhancers and suppressors, and deep intronic mutations, and the
   lower-bound and "may be conservative" readings are the authors'. NEU-251's general caution is
   confirmed verbatim at L55 -- but its comparative clause is wrong; see the NEU-251 block.
4. Confirmed. PMC13753216 L53 identifies the seven MPSA datasets exactly as NEU-249 enumerates them,
   L190-L196 resolve the references (17 Vex-seq/Adamson, 18 MFASS/Chong, 19 ParSE-seq/O'Neill,
   20 TTN/Patel, 21 Rhine, 22 Rong, 23 Soemedi), L195 is Soemedi et al. 2017 Nat Genet doi
   10.1038/ng.3837 PMC6679692 -- the paper behind NEU-026 -- and L58 names the two separable studies as
   18 and 19, so the three MaPSy datasets including Soemedi are among the five. The note's distinction
   between a caution about the score and a refutation of the discrete calls is present but is the
   record's own inference and narrower than L60; see section B6.
5. Confirmed. NEU-247's hundredfold is L15's "two orders of magnitude", and NEU-248's structural
   reason is L26 verbatim on both halves (">93%" of ClinVar submissions from clinical laboratories
   using standardised guidelines, ClinVar cataloguing benign and uncertain variants, HGMD curated from
   publications and not recording variants reported as benign or uncertain). Two caveats: NEU-247's
   cited line does not carry its own scope premises (block above), and NEU-248's "no benign
   denominator" conclusion is the record's, not the paper's.
6. Confirmed. Four records fail criterion 2 -- NEU-233, NEU-235, NEU-236, NEU-237 -- and each note
   says so in its own words. All four are scored `tier wrong` because the tier string asserts what the
   note denies. The three-way disagreement is confirmed: RPE as primary in the three mouse models
   (100274596 L1), photoreceptor damage called RPE-independent in the human organoid
   (bio_e7db55d16d24 L14), and no degenerative phenotype in either Prpf31 heterozygote
   (104814022 L1). On the third leg the record is correctly scoped to "fundus examination"; the
   dispatch's "no retinal phenotype at all" is wider than the source. Two of the three legs are not
   independent -- see section B5.
7. Confirmed, all five. Population-variant disruption 3.8 per cent = 1,050 of 27,733 ExAC variants in
   and around 2,198 exons, 83 per cent of them outside canonical sites (36760475 L1). Five of seven
   assay score sets could not separate aberrant from natural splicing (PMC13753216 L13, mechanism at
   L58). Minigene against patient RNA 89 per cent, 81 of 91, for the predominant transcript (L13) --
   but on a seven-gene cancer-predisposition dataset, which is the NEU-241 defect. The three canonical
   dinucleotide figures are exact on L61: ParSE-seq 97 per cent (30/31) with the single exception
   SCN5A c.3957_3963+1dup also predicted neutral, MFASS 83 per cent (180/217), Vex-seq 76 per cent
   (16/21). The predictor comparison is exact on L60: 99 per cent of ParSE-seq's abnormal calls at
   SpliceAI >= 0.2 against 9 to 66 per cent for the others -- but unlabelled in the claim, which is the
   NEU-259 defect.
8. Confirmed with one correction. NEU-245's creation-as-largest-category figures are right as results
   figures; its denominator sentence is not (see block). NEU-246's window result is exact on its single
   cited line L51 -- 1,077 AG-creating variants, 262 pathogenic, 198 benign, 496 VUS, 121 conflicted,
   93.1 per cent of pathogenic against 44.9 per cent of benign in the >6nt-from-branchpoint and
   >5nt-from-acceptor window. On the dispatch's question: the last step is the AUTHORS' arithmetic, not
   the record's. L51 states "only 5.8% of naturally occurring AG dinucleotides fall within the
   high-risk zone", and L52's figure legend repeats it. The record computes nothing.
9. Confirmed, and the record used the results. PMC9284458 abstract L11 gives 41.9 / 28.4 / 15.1 per
   cent with no denominator; results L48 gives 41.9 / 28.2 / 16.6 per cent with n = 638. NEU-245 uses
   28.2 and 16.6 and states n = 638, as its note says. The note's account of this is correct.
10. Confirmed, with the exception noted. Retention percentages by genotype confirmed at PMC7911278 L23
   and L28 (though on n = 1 and n = 2 for two of the five genotypes -- the NEU-227 defect). Sweat
   chloride 82+-14 in 28 measured against 35+-8 in 10 measured at PMC5566269 L58; FEV1 %pred decline
   -0.6, +0.17, -0.26 and -1.02 at L33. The paper's own non-significance statement confirmed verbatim
   at L35 for the FEV1 comparison, which is what NEU-229's claim says -- but NEU-229's NOTE claims
   significance for sweat chloride and pancreatic status that the L65 legend does not mark. Large-cohort
   odds ratios and the p.Arg117His exclusion confirmed at med_c100b8376c2a L11, L34, L42, with the
   p = 0.56 omission flagged. HGVS exon numbering handled correctly: PMC7911278 L7 and L26 state
   "exon 10 (in the HGVS name; exon 9 in the legacy name)" and "intron 9 (in HGVS name; intron 8 in
   legacy name)"; the records use the HGVS numbers consistently.

Could not confirm.
3. Not confirmable as stated. NEU-254 scopes ONLY the 4,964, and for that it is exact: PMC6679692 L36
   reads "Nonsynonymous mutations classified as disease-causing (DM) were downloaded from Human Gene
   Mutation Database (HGMD, accessed in May 2012) ... mapped to internal exons with <= 100 nucleotides
   in length and selected for those that fit into 170 nucleotide genomic windows ... (n = 4,964)" --
   non-synonymous, the access date, the exon-length limit and the window, all on the one cited line.
   The dispatch's other half, that the machine-learning fraction is a rate among non-synonymous
   variants in internal exons of 100 nucleotides or fewer at a stated access date, is not in NEU-254,
   which never mentions NEU-025 or MutPred Splice, and I could not confirm it from NEU-025's source:
   PMC4054890 L9 says "coding region substitutions" and "human disease-causing exonic mutations" and
   L182 says "approximately 16% of inherited disease and approximately 10 to 14% of cancer exonic
   mutations", with no exon-length restriction, no access date and no statement either way about
   synonymous variants. So the correction exists for one figure (NEU-026's 10 per cent), not two, and
   no record in the file states the variant class or the access date behind NEU-025's 16 per cent.
   Nothing in the chapter was read to reach this; NEU-025 and NEU-026 were read as records only.

## D. Fractions missing a denominator, a numerator, a variant class or an ascertainment source

Mechanical pass over every percentage and ratio in all 38 claims. Worst first.

1. NEU-259. "99 per cent" and "9 to 66 per cent": no numerator, no denominator, no assay named for
   either. The source names the assay (ParSE-seq) on the cited line.
2. NEU-245. "11.7 per cent of the pathogenic variants": the stated denominator (24,445) is the wrong
   set; the real one (5,463 pathogenic of 30,042) is on uncited lines.
3. NEU-250. 27 per cent, 83.5, 16.5, 17.5 and 35-40 per cent all carry a confidence interval, two
   p-values and a clear ascertainment, but no counts at all for any of the five. L54 gives none
   either, so this is a limit of the source, not of the record -- worth saying in the chapter rather
   than fixing in the record.
4. NEU-251. ~30, ~43, 27 and ~17 per cent: no counts, and one of the four ascertainments is given only
   as "a different curation" in the claim (Caminsky et al. 2014, named in the note).
5. NEU-227. Five retention percentages with a pooled n = 13 but no per-genotype n; two of the five
   rest on one and two subjects.
6. NEU-241. 89 per cent, 81 of 91: numerator and denominator present, ascertainment absent (seven
   cancer susceptibility genes, traditional minigene assays only).
7. NEU-224. 7.6-10.6, 15.0-20.8 and 24.7 per cent: denominators are stated as a share of transcripts,
   but the sample sizes (n = 4 animals per genotype and tissue, n = 3 human biopsies) are in `note:`
   only, and the alternative per-allele denominator (~50 per cent from the +189T allele) is in `note:`
   only too.
8. NEU-258. 97, 83 and 76 per cent all carry their counts, but the three assays are identified only
   functionally in the claim; the names are in `note:`.
9. NEU-239. "83 per cent of those": denominator is the 1,050 SDVs and is clear from the sentence, but
   no count is given. The 3.8 per cent itself is fully labelled (1,050 of 27,733 ExAC variants).
10. NEU-230. The five odds ratios need no numerator, but the sizes of the two referral groups they
    compare appear in neither claim nor note.
11. NEU-246. "5.8 per cent" of naturally occurring AG dinucleotides has no count; the source gives
    none either.

Fully labelled, for contrast: NEU-226 (54 of 353 families, 15.3 per cent, with the prior-testing
status of each cohort), NEU-238 (16 of 18 with the full selection rule in the claim), NEU-254 (4,964
with variant class, exon-length limit and access date), NEU-255 (26 of 32 with the tissues and the
positives-only design), NEU-257 (the one-third with its provenance and its status as a prediction).
