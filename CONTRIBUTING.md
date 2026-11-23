# Contributing

## The one rule that matters most

**Nobody writes book prose while looking at source prose.**

Research and writing are separate passes, with a structured artifact in between:

```
read the literature  →  research/<area>.yml   →  chapters/<n>-<name>.qmd
   (claim records)        (own-words claims        (original prose, written
                           + audit quotes)          from the records)
```

A contributor reading a paper produces **claim records** (see
[`research/SCHEMA.md`](research/SCHEMA.md)): a one-sentence claim in their own
words, the bibliographic source, the exact lines read, and a short verbatim quote
kept **only** as an audit trail. The writing pass then works from records, not
from papers. This makes close paraphrase structurally unlikely rather than a
matter of individual discipline, and it means every sentence in the book can be
traced to the lines it came from.

## How deep a section goes

**Depth is set by the subject, and the book is sized like a book.** A specialist
scientific book of this kind runs 70,000 to 85,000 words. This one stands at
about 49,000, so the chapters that have not had a deepening pass are still
expected to grow several times over rather than be polished at their current
length.

Count words with `scripts/wordcount.py chapters/*.qmd`, which is the project's
only definition of a word count and exists because three different hand counts
of the same chapter disagreed by several hundred words. It excludes front
matter, code, table rows, div fences and captions, and counts headings.

Working targets, not gates:

| Unit | Now | Target |
|---|---|---|
| Whole book | about 49,000 words | 70,000 to 85,000 |
| Chapter, not yet deepened | 1,150 to 2,350 words | 5,500 to 6,500 |
| Section | 150 to 350 words | 600 to 750 |
| Claim records | 906 | roughly 1,500 |

Four chapters are now at target or past it: 12 at 5,315 words, 5 at 6,634, 2 at
7,539 and 3 at 11,861. Chapters 2 and 3 are a deliberate exception to the
per-chapter target. "Across the tree of life" is the part of the book most worth growing, so
depth there is limited by the evidence rather than by a word count, and the
selection criterion is how well a case is evidenced rather than how many cases
are covered.

At the current rate of about one claim record per fifty words of prose, a
chapter at target needs on the order of 120 records rather than 35.

### There was a cap, and it was an accident

Ten of the twelve research files hold between 34 and 38 claims. That is a quota,
not a property of the literature, and it was never an editorial decision: it was
a working budget inside each research pass that became the book's shape because
nobody wrote it down. Four files record the consequence in their own leads,
naming findings that were "cut at the 36-claim cap", "trimmed at the 35-claim
cap" and "dropped for the claim cap", each with a document id and line numbers
and each marked reusable without re-reading.

The two files that ignored the cap are the two best chapters. Chapter 11 ran to
55 records and is the deepest in the book; chapter 9 ran to 44.

So there is no cap. A section stops when the subject is covered, and a chapter
that needs 150 records gets 150.

### Running a deepening pass with research agents

Three procedural rules, each learned by breaking it.

**Wait for the agent's report, not for its file.** A research file that exists
and parses is not a finished one. On the chapter 5 pass all three agents had
written their files before any of them reported, and two then ran correction
passes. The merge taken from those files carried a truncated author list, a
claim anchored on a discussion line rather than the measured one, a claim mixing
two denominators, and one record missing entirely.

**Give each agent its own scratch directory.** Two agents on that pass wrote
same-named working files into one shared directory and clobbered each other's.
No research was lost, because every quote was re-verified from the written file,
but only because of that.

**Write prose from the records, not from the agent's report.** A report
summarises and sometimes carries numbers from a record's `note:` field rather
than its claim. Two sentences written that way reached a draft of chapter 5: one
cited a record that a correction pass had removed, and one used a figure that
appears only in a note. `check_citations.py` caught both, which is luck rather
than process, since it only checks digits.

### Depth without synthesis makes the book worse

304 of the book's 358 cited paragraphs cite exactly one source. The shape is
topic sentence, one study, bracket, moral, and it is the clearest remaining sign
that the prose was assembled from records rather than written by someone who had
read the field.

Adding records at that rhythm multiplies the defect. A deepening pass has to
hold two or three sources against each other inside a paragraph, say where they
agree, and say what differs between them. A section that triples in length and
keeps one source per paragraph has got longer without getting better.

## Writing

Read [STYLE.md](STYLE.md) before drafting. It covers the voice the book aims
for, the AI writing patterns to avoid, and the rule that keeps the main text
readable: explain plainly, trust the reader, and put the patient explanation in
a collapsible aside or a `walkthroughs/` document rather than in the chapter.

## Citations

- Every non-obvious factual claim carries a citation. Every number carries one.
- Public citations are DOIs, via `references.bib`, rendered in Nature style.
- Keys are `lastname<year><keyword>`, lowercase, derived from the DOI record.
- Direct quotation is allowed but should be rare: short, in quotation marks,
  attributed in the sentence itself ("as Sharp and colleagues put it, ..."),
  and cited. If a passage needs more than ~25 quoted words, restate it instead.
- Reviews may be cited as reviews ("reviewed in [N]"). Do not cite a review for a
  primary finding — go to the primary paper and read it.

## Figures

**Do not reproduce figures from papers.** Published figures are copyrighted, and
"it's educational" is not a licence. Three acceptable routes:

1. **Generate it.** A script in `scripts/` that produces an SVG/PNG into
   `figures/`, from real data where possible. Reproducible and unambiguously ours.
2. **Draw it.** An original schematic as hand-authored SVG. If the *concept*
   comes from a specific paper, the caption says so: "Schematic after [N]."
   An original drawing of someone else's idea, credited, is fine; a redraw that
   reproduces their specific layout and labelling is not.
3. **Reuse an openly licensed figure.** Permitted, and sometimes the honest
   choice when a published figure is the canonical depiction of a result. It
   carries the most obligations, so work through the checklist below before
   committing one.

### Checklist for reusing a published figure

Do all of these, in order. If any step is unclear, pick route 1 or 2 instead;
redrawing is usually faster than resolving a licence question.

1. **Find the licence on the article itself**, not on the journal's general
   policy page and not on a PDF aggregator. Look for an explicit CC BY, CC BY-SA,
   CC0 or public-domain statement attached to that article.
2. **Check the figure's own caption and credit line.** Open-access articles
   routinely contain panels reproduced from earlier, non-open papers under a
   one-time permission that does not transfer. A figure captioned "adapted from
   [x]" or "reproduced with permission" is off limits no matter what licence the
   host article carries.
3. **Reject the non-commercial and no-derivatives variants.** CC BY-NC and
   CC BY-ND are incompatible with this book's CC BY 4.0 licence, because they
   restrict what downstream readers may do with the whole work.
4. **Check the publisher, not just the repository.** A PMC copy does not
   establish a licence; PMC hosts articles under many terms, including ones that
   permit reading but not redistribution.
5. **Attribute in the caption itself**, not only in the manifest: author, year,
   source, licence name, and a link to the licence text. The attribution has to
   travel with the image.
6. **Record it in `figures/MANIFEST.yml`** with `route: reused`, the licence, the
   licence URL, the source DOI, and the date checked.
7. **Do not crop, recolour or relabel** a reused figure beyond scaling. Editing
   it can exceed the licence and will usually misrepresent the original. If the
   figure needs changing to make your point, you want route 2.

When in doubt, redraw. An original schematic crediting the source concept is
always safe, and it usually serves the argument better, since a figure drawn for
a paper was composed to make that paper's point rather than this chapter's.

Load the `dataviz` guidance before writing any chart code, so figures across
chapters read as one system.

## Before a chapter is marked done

- [ ] Every claim traces to a record in `research/`
- [ ] Every number has a line-anchored citation
- [ ] All seven checks below pass
- [ ] All figures accounted for under one of the three routes above
- [ ] `quarto render` clean, no unresolved cross-references
- [ ] Read by someone who did not write it, for the things no check can see

### The seven checks

Six run in CI on every push. The seventh needs the paperclip corpus, which the
build machine does not have, so run it locally before a research file is
committed and after any edit to a quote or an anchor.

| Script | What it proves | Where |
|---|---|---|
| `verify_claims.py` | Every stored quote is still a byte-exact substring of the lines it cites, and bibkeys and DOIs agree across files | local only |
| `check_overlap.py` | No chapter reuses 8+ consecutive words from a recorded source quote | CI |
| `check_citations.py` | Every number in a section appears in a claim for a source that section cites | CI |
| `build_bib.py --check` | `references.bib` is exactly what the claim records generate, one work has one bibkey, and author strings parse | CI |
| `check_style.py` | Sentence length upper and lower bounds, first person, banned constructions, em dashes, metronomic runs | CI |
| `check_figures.py` | Every figure has a manifest entry with its provenance, and every entry names files that exist | CI |
| `check_accounting.py` | Every row of the accounting tables carries a figure recorded against the source that row names | CI |

### What the checks cannot see

They compare digits and wording. They do not read meaning, and three failures
have come from that gap:

- **A sentence extended past its claim.** The record says three quarters were
  chargeable to one compartment; the prose added what the other quarter was.
  Nothing in the chapter is wrong by any mechanical test.
- **A number from one context reused in another.** "The third approved SMA
  therapy" became "three approved splicing-directed drugs".
- **Arithmetic over a range.** Two estimates were called four-fold apart when
  one of them was a range and the other was "nearly every gene".

Most of these appeared while rewriting a sentence to satisfy `check_style.py`.
When you split a long sentence, re-read the result against the claim record,
not against the sentence you started with.

### Overlap check

`scripts/check_overlap.py` compares chapter prose against the audit quotes
stored in `research/*.yml` and flags any shared span of 8+ consecutive words. It
is a smoke alarm, not a plagiarism detector: it only sees text we recorded. A
hit means go back and restate, or make it an explicit attributed quotation.

## Licensing

Prose and original figures: **CC BY 4.0**. Code and scripts: **MIT**. By
contributing you agree your contribution ships under those terms. Reused
openly-licensed material keeps its own licence, recorded in the manifest.

## Scope

This book is about **biology** — what isoforms do, why they matter, and how we
came to see them. It is not a tools catalogue and not a pipeline tutorial; those
exist elsewhere and are linked from the resources appendix. Methods appear where
they shaped what was discoverable.
