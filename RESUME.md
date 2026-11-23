# Where this is up to, and what to do next

Paused 2026-11-23 at the user's request, part-way through chapter 7's writing
pass. Everything below is on disk and committed; nothing needs to be rebuilt
from a session transcript.

## State

| chapter | records | reviewed against sources | corrections applied | prose |
|---|---|---|---|---|
| 1 foundations | 268 | yes | yes | 19,088 words |
| 2 animals | 125 | yes | yes | 7,728 words |
| 3 plants, fungi, other | 261 | yes | yes | 13,380 words |
| 4 technology arc | 231 | yes | yes | 9,919 words |
| 5 long reads | 128 | yes | yes | 6,827 words |
| 6 cancer | 163 | yes | yes | 10,599 words |
| **7 neuro, Mendelian** | **312** | **yes, 6 blocks** | **yes** | **2 of 11 sections drafted** |
| **8 single-cell, spatial** | **226** | **yes, 3 blocks** | **no** | 1,742 words (old) |
| 9 catalogues | 318 | no | no | 1,968 words (old) |
| 10 variants, QTL | 355 | no | no | 2,072 words (old) |
| 11 transcript to protein | 316 | no | no | 2,669 words (old) |
| 12 proteoforms, drugs | 108 | yes | yes | 5,839 words |
| 13 accounting | — | — | — | 1,279 words (old) |

All seven CI gates pass. `verify_claims.py` passes on chapter 7: 312 claims, 0
problems, after this pass widened sixteen records' `evidence.lines`.

## The next five things, in order

### 1. Finish chapter 7's prose (8 writer agents, no corpus access needed)

The inputs are built and committed. `research/drafts/ch07/` holds the digest,
the eleven sections routed into eight writer files `W1.md` to `W8.md`, the
writer brief, the key checker, and the router that produced the split.

Two sections are drafted and banked:

- `research/drafts/ch07/sec-mendelian-fraction.md` (1,780 words, from W4)
- `research/drafts/ch07/sec-nof1.md` (1,035 words, from W7)

Six remain: W1 brain and tau, W2 TDP-43, W3 SMA and DMD, W5 RNA-seq diagnosis,
W6 prediction and retina, W8 the SCN1A poison exon programme. Dispatch one
agent per file with `research/drafts/ch07/WRITER-BRIEF.md` as its contract. The
per-section word targets and the chapter-specific traps each writer must be
warned about are in this session's dispatch prompts; the traps are all
recoverable from the records' own notes, which now carry them, and from
`research/reviews/ch07/`.

Three section identifiers are linked from other chapters and must survive
verbatim: `#sec-mapt` (chapter 13), `#sec-sma` (chapter 12),
`#sec-rnaseq-diagnosis` (the glossary).

Then assemble, run a copy editor over the whole chapter with a content guard
proving every citation bracket and numeric token survives, and run the gates.
Budget about 11,000 words; at 35 words per record that is the whole file.

### 2. Apply chapter 8's corrections, then write it

`research/reviews/ch08/{A,B,C}.md` hold all 226 records checked. Not yet
applied. The three findings each reviewer called most load-bearing:

- **A cross-species claim runs the wrong way.** One record says splicing
  programmes are conserved well enough to transfer between mouse and human;
  the cited line supports mouse to human only, and tested the other way about
  57 per cent of human cell-type-specific exons are constitutively included in
  mouse, which those authors read as human exons a mouse cannot model.
- **An inverted author list hid a four-record laboratory overlap.** One
  document's ten authors are all recorded given-name-as-surname, so a group
  that appears four times in the file, and whose own data another record
  reanalyses, looks like four independent sources.
- **Two records state 144 cells where the analysis used 107**, on a line they
  cite, and everything downstream rests on 107.
- `SCS-207`'s 42.3 per cent has an arithmetically impossible denominator: the
  source gives the percentage with no denominator and the record supplied one
  that cannot be right.
- The whole `SCS-001` to `SCS-035` block has no `note` field, so no tier. Same
  defect chapter 7's oldest block had.

### 3. Review chapters 9, 10 and 11, then write them

989 merged records, none reviewed. Five chapter 9 reviewers were dispatched and
stopped at the pause, having produced nothing; re-dispatch from scratch. Use
five or six at a time, not twenty: the corpus rate limit is about 25 calls a
minute shared across every agent running.

Suggested blocks: chapter 9 as CAT-001..053 plus 101..150, 161..219, 221..279,
281..337, 341..390. Chapters 10 and 11 split similarly.

`research/reviews/notes-ch{09,10,11}.md` hold the research pass's own findings,
including several that overturn live chapter text. Do not take them on trust;
each needs checking against the documents. The ones to check first:

- Chapter 9's closing argument may have its direction wrong. `CAT-047` turns
  "may instead hinder" into "degrades"; `CAT-351` has 50 per cent surplus
  models costing about 1 per cent of correlation against 10 per cent for
  omission; three studies find the larger annotation *more* accurate; and no
  measurement in the corpus varies catalogue size and shows an isoform-level
  cost.
- Chapter 10's reclassification figure points the wrong way: the chapter
  carries a projection where every observed series runs opposite, on
  denominators that must not be lined up.
- Chapter 10 calls a cleared assay an "intrinsic-subtype" test. That phrase is
  in neither clearance, and the labelling explicitly excludes therapy
  selection. "CE marked" has nothing behind it and cannot get it from this
  corpus.
- Chapter 11's "two independent directions" cites a statement whose two named
  authors are both authors of the citing paper.

### 4. Chapter 13 last

It restates the home chapters' figures, adds no new source and computes no
totals, so it cannot be written until 7 to 11 are final.

### 5. The fable review, last of all

`Agent` with `model: "fable"` and a fresh subagent type, **not** `fork`, which
ignores the model override. Read-only. Give it the chapters and the record
files, not a list of findings, and ask for cross-chapter contradictions where
one quantity carries two values, chapter 13 against its home chapters, and
claims about the evidence. Have it write to a file. One agent over 120,000
words will thin out, so consider one per part. Verify every finding against the
records before applying anything.

## Two things the user should decide

- **Chapter 2 is the book's centre by the user's own instruction, and it is
  currently its shortest deepened chapter at 7,728 words.** Chapter 1 at 19,088
  nearly equals chapters 2 and 3 combined. Nothing here is wrong, but the
  proportions now cut against "the tree of life section deserves much more
  content and attention than other parts of the book".
- **The word-count target will be overshot.** At the measured 41 words of prose
  per record, chapters 7, 9, 10 and 11 land near 13,000 each and the book near
  135,000, against the 105,000 to 115,000 in `CONTRIBUTING.md`. Either select
  records rather than exhausting them, or raise the target.

## Three longstanding items

- Three glossary terms rest on no source and await the user's sign-off.
- Four chapter 1 figures are specified but not drawn, in this session's
  scratchpad `ch01/FIGURES-TODO.md`, each needing a light and a dark variant
  and a manifest entry.
- `scripts/check_claim_digits.py` is written but its matching is unsound: it
  matches by substring, so "27" passes on "127", and it ignores a corpus read's
  return code, so a throttled read comes back empty and reports every number
  missing. Fix both before trusting it, and cache lines per document.
