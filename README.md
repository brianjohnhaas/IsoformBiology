# Isoform Biology

A community reference on why transcript isoforms matter, built as a book from
the primary literature, with every claim traceable to the lines it came from.

**Status: first draft, unreviewed.** All thirteen chapters are drafted from
verified claim records. No chapter has yet been read by a subject expert, which
is the project's largest gap. See
[how to contribute](https://brianjohnhaas.github.io/IsoformBiology/contributing.html).

## Why this exists

A gene is not a transcript. Most human genes produce several, and the
differences between them are frequently the biology: which domain is present,
which cell type uses which form, whether a transcript is translated at all.
Most transcriptomic analysis still collapses that to one number per gene.

Plenty of excellent material already covers *tools* for isoform analysis and
*how to run* the pipelines. Nothing covers the biological case end to end:
landmark examples across the tree of life, the technology arc that made them
visible, the disease biology that depends on isoform resolution, and the
current efforts to catalog the isoform universe. That is the gap this fills.
It is a biology book rather than a tool catalogue, see
[the resources appendix](chapters/99-glossary.qmd) for where the tool
catalogues and training material live.

## How it is built

Research and writing are deliberately separate passes:

```
read the literature  ->  research/*.yml       ->  chapters/*.qmd
                         claim records            original prose
                         (+ audit quotes)         (written from records)
```

Nobody writes book prose while looking at source prose. Every claim carries the
exact source lines it came from, and `scripts/verify_claims.py` re-reads those
lines and asserts the stored quote matches byte-for-byte. Published figures are
never reproduced; figures are generated, drawn, or openly licensed with
attribution recorded.

See [CONTRIBUTING.md](CONTRIBUTING.md) and
[research/SCHEMA.md](research/SCHEMA.md) for the full contract.

## Building locally

```bash
quarto render          # -> _book/index.html
python3 scripts/verify_claims.py    # check claim records against sources
python3 scripts/check_overlap.py    # check prose against recorded quotes
```

Needs [Quarto](https://quarto.org/) 1.11+ and `matplotlib`, `jupyter`, `pyyaml`
for figures. Note the conda-forge `quarto` package is currently broken (ships
without its bundled deno) — use the official release.

## License

Prose and original figures: [CC BY 4.0](LICENSE).
Code and scripts: [MIT](LICENSE-CODE).
