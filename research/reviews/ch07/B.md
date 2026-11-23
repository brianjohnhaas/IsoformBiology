# Records review: NEU-141 to NEU-179 (research/07-neuro-mendelian.yml)

Reviewer B, chapter 7 deepening pass. 39 records, 14 source documents, all read at the
cited lines plus surrounding context. Read-only on the repository.

A tenth verdict label, `note wrong`, is used for a defect that lives in a `note:` field
rather than in `claim:` — none of the nine labels fits an independence or pipeline
statement that the source contradicts, and the brief asks explicitly for those.

## Verdict table

| id | verdict |
|---|---|
| NEU-141 | qualifier lost |
| NEU-142 | ok |
| NEU-143 | ok |
| NEU-144 | ok |
| NEU-145 | ok |
| NEU-146 | tier wrong |
| NEU-147 | ok |
| NEU-148 | ok |
| NEU-149 | ok |
| NEU-150 | ok |
| NEU-151 | ok |
| NEU-152 | ok |
| NEU-153 | qualifier lost |
| NEU-154 | ok |
| NEU-155 | number wrong (in note) |
| NEU-156 | ok |
| NEU-157 | note wrong |
| NEU-158 | ok |
| NEU-159 | ok |
| NEU-160 | note wrong + source metadata wrong |
| NEU-161 | proposal as finding |
| NEU-162 | ok |
| NEU-163 | ok |
| NEU-164 | number wrong |
| NEU-165 | ok |
| NEU-166 | note wrong |
| NEU-167 | ok |
| NEU-168 | ok |
| NEU-169 | qualifier lost + tier wrong |
| NEU-170 | ok |
| NEU-171 | ok |
| NEU-172 | ok |
| NEU-173 | source metadata wrong |
| NEU-174 | ok |
| NEU-175 | qualifier lost + note wrong |
| NEU-176 | qualifier lost |
| NEU-177 | source metadata wrong |
| NEU-178 | ok |
| NEU-179 | scope too wide + note wrong + source metadata wrong |

24 ok, 15 with at least one defect. No arithmetic error anywhere in the block.

## Defect blocks

NEU-141  qualifier lost
  claim says: "The cryptic exon is a threshold phenomenon rather than a graded one"
  source says: L109 reports only the two detection points (>50% loss for the UNC13A CE,
    >90% for the UNC13B FSE and intron retention) in the doxycycline dose series. The
    paper never frames this as threshold against graded; L104 says the opposite for the
    i3Neuron series ("CE expression ... correlated with the level of TDP-43 knockdown"),
    and the paper's own next paragraph (L110) attributes the apparent floor to decay
    ("supporting the notion that its occurrence may be underestimated owing to efficient
    degradation"). The record's own caveat survives only in `note:` ("Bounded by NEU-142,
    which shows the 50 per cent figure is a detection threshold"), so the citable sentence
    is the unhedged one. Everything else in the claim checks: doxycycline-inducible shRNA
    in SH-SY5Y (L148), n = 3 biological replicates (L108), UNC13B exon annotated and
    frameshift-inducing between exons 10 and 11 (L102).
  lines read: PMC8891020 L102, L104, L108-L110, L148

NEU-146  tier wrong
  claim says: note reads "tier: isoform-specific biochemical or binding difference, no
    organismal phenotype"
  source says: what was done is BaseScope in situ hybridisation of the cryptic junction in
    post-mortem frontal cortex, compared across neuropathological groups (9 FTLD-TDP, 5
    control, 4 FTLD-TAU; L114, L119). No perturbation, no binding measurement — this is a
    correlation of an isoform with a phenotype, the tier used by the neighbouring records
    NEU-144, NEU-145 and NEU-147 for the same cohort. The numbers, the probe identity and
    both P values (0.021, 0.010) are correct.
  lines read: PMC8891020 L114, L119

NEU-153  qualifier lost
  claim says: "bound the reference and risk versions of the cryptic-exon probe with similar
    affinity, lower affinity appearing only for the repeat variant rs56041637"
  source says: L40 reports three results, not two: "TDP-43 binds the reference and risk
    versions of the CE probe with similar affinity but the intronic risk allele results in
    a minor reduction in affinity ... TDP-43 had lower affinity for the probe containing
    the risk allele at rs56041637". The word "only" excludes a reduction the paper reports.
    The rest of the record is exactly right, including the naming of the disagreement in
    print and its stated cause: "We note that these in vitro binding results are somewhat
    different from those reported in the accompanying Article by Brown and colleagues. Our
    use of full-length TDP-43 ... differs from the one used by Brown and colleagues, which
    contains only the TDP-43 RNA-recognition motifs (RRMs)."
  lines read: PMC8891019 L40; PMC8891020 L127, L212 (His-TDP-43 aa 102-269, i.e. RRM1+RRM2)

NEU-155  number wrong (in note)
  claim says: note reads "The two experiments differ in the system (TDP43-null HEK 293T
    against TDP-43-knockdown SH-SY5Y), in the number of variants tested (three against two)
    and in the readout ...; neither paper tests the other's configuration."
  source says: Brown tested the same three variants. L125: "To examine whether the CE SNP,
    intronic SNP or short tandem repeat expansion rs56041637 ... are responsible for
    promoting the CE inclusion, we generated minigenes featuring different combinations of
    these genomic variants (Fig. 4c)." L206 confirms the construct: "The repeat expansion,
    containing four extra copies of the CATC repeats (ten instead of the six found in the
    reference genome), was added via Gibson assembly ... Plasmids with all four possible
    combinations of the SNPs were then generated". So "three against two" is wrong, and
    "neither paper tests the other's configuration" is unsupported on the variant
    dimension; what does differ is the cell system, the minigene backbone and the readout.
    Brown's text reports effect sizes only for the two SNPs, which may be what the note
    meant, but that is not what it says. The claim sentence itself is accurate: the
    non-additive reading is at PMC8891019 L39 and the additive one at PMC8891020 L130.
  lines read: PMC8891020 L124-L125, L130, L206; PMC8891019 L39

NEU-157  note wrong
  claim says: note reads "a different pipeline and a different cell model from the
    179-event count in NEU-010, so the two catalogue sizes are not directly comparable"
  source says: the pipeline and the cell model are the same. Seddighi L62: "For differential
    splicing analysis, all samples were run through MAJIQ in the same manner using a custom
    Snakemake pipeline (https://github.com/frattalab/splicing)"; L60: CRISPRi knockdown "in
    the WTC11 iPSC line harboring stable TO-NGN2 and dCas9-BFP-KRAB cassettes ... lentiviral
    -expressed sgRNA targeting the transcription start site of TARDBP". NEU-010's paper used
    MAJIQ on CRISPRi-depleted WTC11 i3Neurons too (PMC8891020 L103). The real reasons the
    counts differ are the event definition (340 abnormal events of all classes across 233
    genes out of 498, against 179 called cryptic exons) and total-RNA sequencing, not the
    pipeline or the model. The claim's numbers are exact (L35: 340 -> 230 -> 122), and the
    rest of the note is right, including the non-independence (Brown and Wilkins are authors
    of Seddighi; Seddighi is an author of Brown) and the preprint caveat.
  lines read: PMC9900763 L27, L35, L60, L62, L74; PMC8891020 L102-L103

NEU-160  note wrong + source metadata wrong
  claim says: note reads "These authors share no author with NEU-157's paper."
  source says: they share at least two. Jonathan D. Glass and Nicholas T. Seyfried appear in
    the byline of the version read (bio_2d481f216c17 L2: "... Jonathan D Glass, Adam N
    Trautwig, Nicholas T Seyfried, Johnathan Cooper-Knock, Eran Hornstein") and in the
    corpus byline, and both are authors of NEU-157's paper (PMC9900763 metadata: "Jonathan
    D. Glass; Alessandro Ori; Nicholas T. Seyfried"). The 38-name byline recorded in the
    record adds Prudencio, M., a third shared name. The 16 per cent itself is exact and its
    denominator is right (L41: "only 16% of the mRNA species that displayed aberrant
    splicing in TDP-43-negative ALS/FTLD-TDP brain nuclei were affected by TDP-43 KD"), and
    the note's claim that the preprint's own title line differs from the metadata title is
    confirmed (L1: "... through splicing dysregulation" against "... via mis-splicing").
  also: the author string reads "Morato, J. G."; the corpus byline is "Garcia Morato, J."
    The surname is Garcia Morato, so the reformatting demoted half the surname to an initial.
  lines read: bio_2d481f216c17 L1, L2, L41; PMC9900763 meta.json

NEU-161  proposal as finding
  claim says: "about 3 per cent of the non-conserved cryptic exons that appear when TDP-43
    splicing repression is lost are spliced in frame"
  source says: L21 is an introduction sentence citing two earlier studies — "Loss of TDP-43
    splicing repression leads to the inclusion of numerous nonconserved cryptic exons, of
    which about 3% produce in-frame neoepitopes[7],[16]" — so the figure is somebody else's
    result restated, not measured here. The record's `note:` says exactly that ("it is a
    restatement; the chapter should attribute it as such"), but the attribution does not
    appear in the claim, which is the only field the chapter can cite. Worth flagging too
    that a sibling source in this block reports a different figure for mouse (PMC5289002
    L65: "a low percentage of cryptic exons (~6%) do not induce nonsense mediated decay ...
    sequence lengths that are multiples of three").
  lines read: PMC10878965 L21; PMC5289002 L65

NEU-164  number wrong
  claim says: "across 66 plasma samples from 43 C9orf72 carriers and 30 disease-control
    samples, plasma ratios tracked matched cerebrospinal-fluid ratios closely overall"
  source says: the 66/43 figures are the plasma assay cohort (L71: "66 plasma samples from
    43 C9orf72 mutation carriers"), but the CSF-plasma correlation was not run on all of
    them. L77: "Fifty-eight C9orf72 mutation carrier plasma samples had previously assayed
    matching CSF samples from the NINDS cohort, and the 30 control plasma samples also had
    previously assayed matching CSF samples. Plasma:diluent signal ratios were highly
    correlated with CSF:diluent signal ratios (r = 0.83 ...)". So the correlation
    denominator is 58 + 30, not 66 + 30. Everything else is confirmed: r = 0.93 in carriers,
    r = 0.19 (P = 0.30) in controls, NPH second-highest concentrations (mean 4.8 ng/ml,
    s.d. 9.5), "These differences were not significant, however" (L76).
  lines read: PMC10878965 L71-L77

NEU-166  note wrong
  claim says: note reads "The mass-spectrometry work in NEU-157's paper shares authors with
    neither this paper nor, necessarily, the work referred to here."
  source says: the work referred to here IS NEU-157's paper. The sentence at L80 ("another
    group was also able to detect the presence of cryptic HDGFL2 in CSF of presymptomatic
    C9orf72 mutation carriers, instead using a targeted mass spectrometry approach[29]")
    carries reference 29, which at L202 is "Seddighi, S. et al. Mis-spliced transcripts
    generate de novo proteins in TDP-43-related ALS/FTD. Preprint at bioRxiv
    10.1101/2023.01.23.525149 (2023)" — the same preprint recorded at NEU-157. The
    authorship half of the note is right (Irwin and Seddighi share no author), but a chapter
    reading NEU-157 and NEU-166 as two separate confirmations would be double-counting one
    paper.
  lines read: PMC10878965 L80, L202

NEU-169  qualifier lost + tier wrong
  claim says: "even though the same exons carry splice sites close in strength to those of
    their annotated neighbours"
  source says: the comparison runs the other way. L114: "Although the canonical splice
    sites were on average stronger than their corresponding cryptic splice site (P < 0.05;
    paired t-test), the majority had scores far greater than those from random sequence,
    suggesting that they are able function as real, albeit weaker, splice sites when TDP-43
    is depleted." The finding is significantly weaker than the neighbours and far above
    random AG/GT sequence — not "close in strength". The clause also sits outside the cited
    line (L106 carries only the PhyloP result), which the note acknowledges.
  also: the tier string "isoform-specific biochemical or binding difference, no organismal
    phenotype" does not describe a PhyloP conservation analysis against two sequence control
    sets; a descriptive tier is what the brief asks for here.
  lines read: PMC5446763 L106-L107, L114-L115

NEU-173  source metadata wrong
  claim says: author string reads "... Nash, L. A.; Juan, I. G. S.; Aronica, E. ..."
  source says: the corpus byline is "Leslie A. Nash; Irune Guerra San Juan; Eleonora
    Aronica". The surname is Guerra San Juan, so the entry should read "Guerra San Juan, I.";
    the reformatting kept only the last word of the surname. The claim itself checks against
    the abstract line in full, including the exon skip escaping degradation, the severely
    reduced conductance, the intrinsic hyperexcitability and the ASO rescue "in induced
    pluripotent stem cell cortical neurons and spinal motor neurons with TDP-43 depletion",
    and the note's shared-author list (Brown, Keuss, Fratta, Prudencio, Petrucelli) is
    correct.
  lines read: PMC12672377 L18; PMC12672377 meta.json

NEU-175  qualifier lost + note wrong
  claim says: "nuclear depletion of FUS by either knockout or a localisation-signal mutation
    produced splicing changes enriched for retained introns that are evolutionarily
    conserved ... including an intron in FUS itself that the authors link to its
    autoregulation"
  source says: the direction is omitted, and it is the opposite of what a reader will assume
    from a TDP-43 chapter. L116: "the direction of change shows these introns to be
    predominantly decreasing in retention upon FUS KO or NLS mutation." L121: "two retained
    introns (introns 6 and 7) in the Fus transcript to be less retained in FUS NLS mutants".
    The class enrichment in L117 is confirmed exactly, as is "cassette exons are not bound by
    FUS beyond random chance", and the autoregulation link is correctly attributed (L51: "We
    propose intron retention to be a mechanism whereby FUS autoregulates"). It is two Fus
    introns, not one.
  also: the note says "Humphrey, Brown, Isaacs, Plagnol and Fratta are authors of this and
    of NEU-158's and NEU-174's papers". Anna-Leigh Brown is not an author of
    PMC5446763 (Humphrey; Emmett; Fratta; Isaacs; Plagnol — five authors). The four shared
    names are Humphrey, Isaacs, Plagnol and Fratta, which still supports the note's
    conclusion that the FUS null and the FUS positive come from one group.
  lines read: PMC7337901 L45, L51, L116-L117, L121-L122; PMC5446763 meta.json

NEU-176  qualifier lost
  claim says: "in ALS motor neurons, especially those with TDP-43 mislocalised out of the
    nucleus, cytoplasmic TARDBP message was increased"
  source says: the cited line is the abstract, which says that; the body of the same paper
    qualifies it twice. L56: "the amount of total TARDBP mRNA did not increase as previously
    reported". L59: "The mean number of TARDBP mRNA spots in neurons from SALS patients
    decreased in the nucleus and increased in the cytoplasm compared to controls; however,
    the differences were not significant ... The mean values of the proportion of cytoplasmic
    TARDBP mRNA in SALS and ALS10 were significantly larger, by 121 and 131%, respectively,
    than those in controls. In contrast, the mean values of the proportion of cytoplasmic
    TARDBP mRNA in ALS1 were similar to those in controls." L58: "This system does not just
    increase the total amount of mRNA, but redistributes the mRNA to the cytoplasm." What is
    significant is the cytoplasmic proportion, in two of three genotype groups; the absolute
    cytoplasmic amount is not. The autoregulation mechanism in the first half of the claim is
    confirmed word for word at L9.
  also: the note says "the cell-level measurement in ALS motor neurons is stated there
    without a cohort size, so no denominator can be given". That is true of the abstract
    line only — this document has full text (L26, L56-L68 carry the post-mortem cohort and
    the per-genotype analysis), so the denominator exists and was not read.
  lines read: PMC4937342 L9, L26, L56, L58-L59, L68

NEU-177  source metadata wrong
  claim says: source block reads year: 2026 with bibkey dinh2025tardbputr
  source says: the corpus record gives pub_year 2025 and pub_date 2025-07-19 for Experimental
    Animals doi 10.1538/expanim.25-0061 (pmid 40691077). The record's year disagrees with the
    corpus and with its own bibkey. A 2026 issue year is possible for an advance-published
    Experimental Animals paper, so I cannot adjudicate which is right from this corpus — but
    one of the two is wrong. Everything in the claim is confirmed at the abstract line,
    including the three deleted element classes, the decreased Tardbp message, embryonic
    lethality after gastrulation, and the aged-heterozygote triad.
  also: as with NEU-176, the note's "no group sizes or effect sizes are available" is true of
    the abstract line only; the paper has full text with the mouse cohorts (L39-L64).
  lines read: PMC12826566 L9, L39-L40, L61, L64; PMC12826566 meta.json

NEU-179  scope too wide + note wrong + source metadata wrong
  claim says: "changes that TDP-43 knockdown and knockout did not produce at all"
  source says: the two nulls are in different systems and only one is neuronal. L41: "Analysis
    of RNA sequencing data of TDP-43 knockdown (KD) in iPSC-derived neurons did not reveal
    aberrant APP splicing (deltaPSI < 0.01, P-values > 0.6) ... Similarly, no APP mis-splicing
    was observed upon complete knockout of TDP-43 in HeLa cells (deltaPSI < 0.01, P-values >
    0.55)". The knockout null is HeLa, a non-neuronal line, and both nulls are reanalyses of
    other groups' datasets (refs 10 and 58), not experiments in this paper. The record states
    neither. The two percentages are exact (L43: 32% decrease in the APP695-specific junction,
    24% increase in the APP751-specific junction, both P < 0.0001, deltaNLS against NES), and
    the record does attribute rather than adjudicate the dispute.
  also: the note says "These authors share no author with the Brown, Ma, Irwin or Wong groups
    recorded here." Two of the four are wrong. Eran Hornstein, the senior author here, is also
    an author of NEU-141 to NEU-151's paper through the NYGC ALS Consortium byline
    (PMC8891020: "... Siddharthan Chandran; Suvankar Pal; Eran Hornstein; Daniel J. MacGowan
    ..."), and he is in the 16-name byline at L2 as well, so that overlap holds for the
    version read. Colin Smith is a second same-name match with Brown, present in the 38-name
    byline only. Prudencio, M. and Dickson, D. W. are shared with NEU-152 to NEU-156's paper
    (PMC8891019), also in the 38-name byline only. The Irwin and Wong clauses do hold: I
    found no shared name with PMC10878965, PMC5289002 or bio_dbc45dfc6dcf.
  also: same corrupted author string as NEU-160, "Morato, J. G." for "Garcia Morato, J."
  lines read: bio_2d481f216c17 L2, L41-L43; PMC8891019 meta.json

## Minor observations, not scored as defects

- NEU-143: the cited line L108 is the figure legend and covers cycloheximide only; the UPF1
  knockdown half of the claim is supported at L110 (and ED Fig. 3h, n = 4), which is NEU-142's
  cited line. The replicate counts in the note (7 for UNC13A and STMN2, 8 for UNC13B) are
  exact. "which has no predicted premature termination codon" is the record's gloss of the
  paper's "which was not predicted to undergo NMD".
- NEU-145: "left the authors unable to say" is a shade stronger than L118's "making it
  difficult to determine".
- NEU-152: "six further minigene reporters carrying every combination" — L39 says "six
  additional minigene reporters, each carrying a different combination of the reference and
  risk alleles (individually, two at a time, or all three)", which is six of the eight
  possible combinations, the two haplotype constructs having been built earlier (L38).
- NEU-159 and NEU-168: the cross-reference to NEU-005 rests on a Crossref byline (Ling,
  Pletnikova, Troncoso, Wong) attached to an abstract-only document (doc 64751354,
  text_access abstract_only, no authors field in the corpus record). "Shares Ling and Wong"
  is therefore a same-name-string match, not something this corpus can confirm.
- NEU-170: the different-position statement is at L3, not the cited L14; the note says so.
- NEU-172: the note's restored-target list (Mical2, Cx3cl1, Synj2bp, Ift81) omits Unc13a,
  which L10 includes in the BaseScope rescue panel and L1 names in the abstract. That
  strengthens rather than weakens the record, but it is the paper's own list.
- Tier strings: NEU-158, NEU-161, NEU-166, NEU-168 and NEU-174 all carry "correlation of
  isoform ratio with a phenotype only" for records in which no phenotype is measured at all —
  pipeline concordance counts, a restated in-frame fraction, cross-species overlap, an FUS
  comparison. These do not overstate, but the brief asks for a descriptive tier in exactly
  this situation. NEU-167 carries the tier-2 string for an immunoassay compared across
  autopsy-defined diagnostic groups, which is the same mismatch as NEU-146 (flagged).
- NEU-141's authors field renders the consortium byline as "Phatnani, H.; NYGC ALS
  Consortium; Phatnani, H."; the corpus byline repeats "Hemali Phatnani" three times with no
  consortium entry. A sensible rendering rather than a corruption, but it is an insertion.

## Author-string check (twelve new bibkeys)

Eleven of the twelve new bibkeys resolve to a single corpus document whose byline I compared
name by name. Two reformatting corruptions, both of multi-word surnames:

- vanzuiden2025gainoffunction (NEU-160, NEU-179): "Morato, J. G." for "Garcia Morato, J."
- joseph2025kcnq2 (NEU-173): "Juan, I. G. S." for "Guerra San Juan, I."

The agent handled three other multi-word surnames correctly: "Peethambaran Mallika, A.",
"Castellanos Otero, P.", "Siqueira Kazu, R.".

seddighi2024crypticpeptides cannot be checked. The document read is the January 2023 bioRxiv
preprint (46 names); the record carries a 51-name Crossref byline for the 2024 Science
Translational Medicine version, in a different order, with five names absent from the
preprint (Mehta, Zanovello, Hallegger, Reich, Dickson) and with "Kargbo-Hill, S. E." where
the preprint has "Sarah E. Hill". All of that is consistent with a journal version, and the
record's note says the author list may differ, so "same name string" is the strongest
statement available; no corruption is visible. The other nine bylines match exactly.

## Preprint flags

Six records carry `preprint: true`: NEU-157 (PMC9900763), NEU-160 and NEU-179
(bio_2d481f216c17), NEU-170, NEU-171 and NEU-172 (bio_dbc45dfc6dcf). All three documents are
preprints in the corpus (meta journal bioRxiv / source biorxiv), and each record's note says
the lines read were a preprint's. Correct, and no record in the block that should carry the
flag lacks it — the other eleven documents are journal articles.

## Laboratory clusters

Three clusters, as reported, confirmed from the bylines:

1. Fratta / Ward (UCL-NIH): brown2022unc13a (NEU-141 to NEU-151), seddighi2024crypticpeptides
   (NEU-157), humphrey2017crypticquant (NEU-158, NEU-168, NEU-169, NEU-174),
   humphrey2020fusintrons (NEU-175), joseph2025kcnq2 (NEU-173). Fratta is on all five;
   Humphrey on both of his own; Brown on four of the five (not humphrey2017crypticquant);
   Ward on brown2022unc13a, seddighi2024crypticpeptides and calliari2024hdgfl2.
2. Wong / Ling (Johns Hopkins): jeong2017celltypecryptic (NEU-159), irwin2024crypticfluid
   (NEU-161 to NEU-166), mallika2026multipletargets (NEU-170 to NEU-172). Jonathan P. Ling
   and Philip C. Wong are on all three. mallika2026multipletargets is byline-identical
   between NEU-171 and NEU-172, so the single-target null and the multi-target rescue are one
   laboratory's internal contrast, as NEU-172's note says.
3. Petrucelli / Gitler (Mayo-Stanford): ma2022unc13a (NEU-152 to NEU-156), calliari2024hdgfl2
   (NEU-167). Petrucelli, Gitler, Prudencio and Dickson are on both; Prudencio, Petrucelli
   and Dickson are also on joseph2025kcnq2, which links cluster 3 to cluster 1.

Genuinely separate: koyama2016tardbpauto (NEU-176, Niigata), dinh2025tardbputr (NEU-177,
RIKEN), ruf2026celltypetdp43 (NEU-178, Ulm) — no shared surname-plus-initial with any other
paper in the block. Ma against Brown is also genuinely independent: I compared Brown's full
99-name byline against Ma's 35 and the only surname match is Miller (Timothy M. Miller in
Brown's consortium list against Georgiana Miller in Ma), so NEU-152's and NEU-153's "Ma and
Brown share no author" holds.

Two qualifications the block's notes do not make.

- vanzuiden2025gainoffunction (NEU-160, NEU-179) is not separate from anything. It shares
  Glass, Seyfried and Prudencio with seddighi2024crypticpeptides, Hornstein and Smith with
  brown2022unc13a, Dickson and Prudencio with ma2022unc13a and calliari2024hdgfl2, and
  Dickson and Prudencio with joseph2025kcnq2.
- cluster 2 is not sealed off from cluster 1 either: irwin2024crypticfluid shares James D.
  Berry and Timothy M. Miller with brown2022unc13a through the NYGC ALS Consortium byline. No
  record claims otherwise, but a chapter sentence pairing NEU-162 against the UNC13A records
  as independent work should know it.

## The personal-communication item

Found and clean. The statement is at bio_dbc45dfc6dcf L14: "Since preventing cryptic splicing
of Unc13a is sufficient to attenuate cognitive decline in mice lacking TDP-43 in brain
neurons (personal communication), but was insufficient to attenuate motor neuron disease ...".
It is no longer carried as a claim: a grep of the whole research file for "personal
communication" and "cognitive decline" returns it only inside NEU-170's note, which states
correctly that it is attributed to a personal communication and is therefore not recorded. No
record in the block asserts the cognitive rescue.
