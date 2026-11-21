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
3. **Reuse an openly licensed figure.** Only CC-BY / CC0 / public-domain, with
   the licence and full attribution in the caption. Record it in
   `figures/MANIFEST.yml` with the licence and a link to the licence terms.
   Check the *figure's* licence, not the journal's general policy — open-access
   articles sometimes contain all-rights-reserved panels reused from elsewhere.

Load the `dataviz` guidance before writing any chart code, so figures across
chapters read as one system.

## Before a chapter is marked done

- [ ] Every claim traces to a record in `research/`
- [ ] Every number has a line-anchored citation
- [ ] `scripts/check_overlap.py` run, no flagged spans (see below)
- [ ] All figures accounted for under one of the three routes above
- [ ] `quarto render` clean, no unresolved cross-references
- [ ] Reviewed by someone who did not write it

### Overlap check

`scripts/check_overlap.py` compares chapter prose against the audit quotes stored
in `research/*.yml` and flags any shared span of 8+ consecutive words. It is a
smoke alarm, not a plagiarism detector: it only sees text we recorded. A hit means
go back and restate, or make it an explicit attributed quotation.

## Licensing

Prose and original figures: **CC BY 4.0**. Code and scripts: **MIT**. By
contributing you agree your contribution ships under those terms. Reused
openly-licensed material keeps its own licence, recorded in the manifest.

## Scope

This book is about **biology** — what isoforms do, why they matter, and how we
came to see them. It is not a tools catalogue and not a pipeline tutorial; those
exist elsewhere and are linked from the resources appendix. Methods appear where
they shaped what was discoverable.
