# Research record contract

Every chapter of this book is written from **claim records**, never from source
prose.

The separation is deliberate: the agent (or person) who reads a paper produces
structured records. A later writing pass turns records into original prose.
Nobody writes book text while looking at source text. That is the single most
effective guard against inadvertent plagiarism, and it also makes every sentence
auditable.

## Sources that are not papers

The corpus holds FDA regulatory documents under `/fda`, clinical trial records
under `/trials` and protein entries under `/proteins`, and a claim may cite any
of them. A regulatory primary is often the *right* source: `CONTRIBUTING.md`
forbids citing a review for a primary finding, and for a drug approval the
primary is the approval package, not a paper about it.

Set `source_type:` to `fda`, `trials` or `proteins` on such a source. Three
things follow from it:

- **No DOI.** A regulatory document has none. It is cited by its issuing body
  in `authors` and its application number in `journal`, as in "FDA BLA 761365
  review documents" or "FDA PMA P230018". `verify_claims.py` requires those two
  instead of a DOI. Record a `url:` only if you have retrieved it and it
  resolves; four constructed `accessdata.fda.gov` links in this project all
  returned 404.
- **`build_bib.py` emits `@techreport`**, not `@article`, so an approval
  package does not render as a peer-reviewed paper.
- **`lines:` are labels, not positions.** Some FDA documents label the first
  line `L0`, so a label is one ahead of the position `paperclip cat --lines`
  addresses. `verify_claims.py` detects each document's first label and
  converts; record the label, matching `grep -n` and the anchor.

## Two optional keys the deepening passes added

`note:` on a claim records a caveat that belongs to the record rather than to
the claim sentence: a species the abstract does not mention, an absent limit of
detection, a unit error in the source's own abstract. Writing passes must read
it, because it is usually the reason a number cannot be stated as simply as it
looks.

`preprint: true` on a source marks a document read as a preprint. Set it
whenever the text read was a preprint, including when `doi` carries the journal
version, which is the case the gates cannot see: `verify_claims.py` checks the
quote against the preprint it came from and `build_bib.py` emits the journal.
`research/ALLOCATION.md` lists every source in the book where those two differ.

`verify_claims.py` ignores both keys.

## File layout

One file per research area: `research/<area>.yml`.

```yaml
area: catalogs
researcher: agent-09-catalogs
date: 2026-11-21
corpus: paperclip 0.8.23

claims:
  - id: CAT-001
    claim: >
      Original one-sentence statement of the finding, in the researcher's own
      words. Must be a claim a reader could check against the cited lines.
    topic: ENCODE4 long-read RNA-seq
    source:
      doc_id: PMC1234567          # paperclip doc id
      title: "..."
      authors: "Lastname, A. B., Lastname, C. D."   # from meta.json
      journal: "..."
      year: 2024
      doi: 10.1038/s41586-024-xxxxx
      bibkey: author2024keyword   # lowercase, DOI-derived; used in references.bib
    evidence:
      text_access: full_text      # full_text | abstract_only
      lines: L120-L128
      anchor: https://paperclip.gxl.ai/citations/papers/PMC1234567#L120-L128
      quote: >
        Verbatim span of at most 25 words, copied exactly.
        AUDIT TRAIL ONLY. Never appears in the book.
    confidence: high              # high | medium
    figure_idea: >
      Optional. What an original figure here should SHOW (the relationship,
      the axes, the comparison). Not a description of the paper's own figure.

leads:
  - note: >
      Something recalled or suspected but NOT found in the corpus. Never cite
      a lead. Listed so a human can chase it.
    why: "why it matters if true"
```

## Hard rules

1. **`claim` is the researcher's own sentence.** If it reads like the paper's
   abstract, rewrite it. Do not lightly reword — restate.
2. **`quote` is audit-only.** It exists so a reviewer can confirm the claim
   against the source. It is never published. Maximum 25 words.
3. **Read the lines you cite.** `lines` and `anchor` must come from text actually
   read with `cat`/`grep`/`scan`. Line numbers reported by `map` or `search`
   summaries are not good enough — open the file and confirm.
4. **Never cite a figure you have not accounted for.** Do not copy figures,
   figure panels, or figure captions out of papers. Published figures are
   copyrighted. Record a `figure_idea` instead; the book draws its own.
5. **Memory is not a source.** Anything you believe but cannot anchor goes in
   `leads`, never in `claims`.
6. **Abstract-only is allowed but must be declared.** Much of the pre-2000
   literature exists in the corpus as abstract-only records (full abstract at
   `L1`). Citing those is fine — set `text_access: abstract_only` so the writing
   pass knows not to assert details the abstract does not contain.
7. **No quantitative claim without a line anchor.** Percentages, counts and
   effect sizes are exactly where secondhand error creeps in.

## Public vs. internal citation

- **In the book:** standard numbered references via `references.bib`, resolved to
  DOIs. That is what readers see and what makes the book citable.
- **In `research/*.yml`:** paperclip anchors and audit quotes. Internal provenance,
  so any claim can be traced back to the lines it came from.

---

## Verified operational notes for the paperclip corpus

Learned the hard way on 2026-11-21. Trust these over your instincts; each one
cost a pilot agent real time.

- **`-s` is required** on `search`: `paperclip search -s papers "query" -n 8`.
- **`lookup doi` and `lookup pmid` silently fail** on papers that ARE in the
  corpus. **`lookup title "<exact title>"` works** and is the fastest way to
  resolve a paper you can name. Otherwise use `search`.
- **Pre-2000 classics are abstract-only** records with numeric doc_ids. The full
  abstract is at `L1`; `meta.json` carries doi/pmid/pmcid. Find them with
  `search -s abstracts`. Declare `text_access: abstract_only`.
- **`--lines N` (single number) returns a section index on some documents, not
  the line.** Always request a range, even degenerate: `--lines 54-54`.
- **`cat .../meta.json` appends a timing line** like `[23ms]`, so piping it into
  `json.load` fails. `grep` the fields you need instead.
- **`scan` can emit 50KB+** and blow your context. Use `grep -nE` with a tight
  pattern; it returns whole lines, which is what you want anyway.
- **Figure and table captions are interleaved with body text** in
  `content.lines` with no structural marker. When a caption sits inside the span
  you want, cite a comma list (`L22,L24`) rather than a range.
- **Do NOT use `paperclip git` / repo commands.** The active repo is global
  shared state and agents run concurrently.
- No shell loops, `xargs`, `curl`, or `rm` in the paperclip sandbox; `/.gxl/` is
  the only writable path there.

## Two editorial rules that came out of the pilot

1. **Preprint vs. journal version.** Several major papers exist in the corpus
   only as preprints (ENCODE4 LR-RNA-seq, the GTEx long-read paper) even when
   `meta.json` lists a journal DOI. Cite the lines you actually read, but record
   the journal DOI in `source.doi` when one exists, and add a `leads` entry
   saying the figure should be re-checked against the published version.
2. **When sources conflict, record the conflict.** GENCODE's own 2025 count of
   human protein-coding transcripts and CHESS 3's count for the *same* release
   differ by ~57,000 because the projects use different inclusion rules. Do not
   pick a winner and do not average. Record both, attributed, plus a claim or
   lead stating that the definitions differ. Any table in the book that puts
   counts from different projects side by side must state each project's
   inclusion rule or it will read as an error.

## Before you finish

Run the central verifier on your file:

```
python3 scripts/verify_claims.py research/<your-file>.yml
```

It re-reads every cited line range and asserts your quote is a byte-exact
substring. Zero problems is the bar. A claim that fails is either mis-anchored
or was written from memory; both are disqualifying — fix it or drop it.

---

## Bibliographic metadata is never written from memory

Abstract-only records carry title, DOI, PMID and year, but **no author list and
no journal name**. `sql` cannot reach them either, since that table covers only
PMC and the preprint servers.

Supplying those fields from memory produces a byline that looks authoritative,
cites a real DOI, and may credit the wrong people. That is worse than a blank
field, because nothing downstream can detect it.

So: if `meta.json` does not carry it, do not write it. Put the literal string
`RESOLVE_FROM_DOI` in `authors` and `journal`, make the bibkey title-derived
rather than author-derived, and move on. The orchestrator fills them
authoritatively with:

```
python3 scripts/resolve_metadata.py --check    # report
python3 scripts/resolve_metadata.py --write    # apply
```

which asks Crossref, writes back the real author list, journal and year, and
reports any case where a recorded first author disagrees with the DOI record.

The same rule applies inside `claim` text. Do not write "Smith and colleagues
showed..." unless you read the name in `meta.json`. If a name is wrong there,
the prose inherits it and the citation looks correct while the attribution is
not.

Read `meta.json` values to the closing quote. A `grep -oE '"doi"[^,]*'` pattern
truncates journal names at the first comma, and a loop that pulls only
`pub_year` and `journal` leaves the DOI unverified, since the verifier only
checks that the field is non-empty.

Note the key is `pub_year`, not `year`.

## Quotes: slice, never retype

Build the audit quote by re-reading the cited line and slicing between two ASCII
anchors in it. Retyping loses `∼`, `–`, `Δ`, `ρ`, curly apostrophes and prime
characters, and the verifier is byte-exact by design, so a retyped quote fails.

## Rate limit

`paperclip search` allows roughly 25 starts per 60 seconds and the quota appears
to be shared across concurrent agents. `grep` and `cat` are unaffected, so
prefer them once you know which document you want.
