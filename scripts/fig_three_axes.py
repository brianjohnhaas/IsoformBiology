#!/usr/bin/env python3
"""One splice chain, the ends annotation gives it, and the ends long reads
attach to it.

Original figure. Nothing here is traced from or redrawn after a published
figure. It is a schematic of the asymmetry recorded in
research/05-long-reads.yml (LR-021, LR-022): a multi-exon splice chain carries
at most three annotated start or end sites in GENCODE v40, and exactly one
start site in 99.7 per cent of cases and one end site in 99.4 per cent, while
the long-read annotation attaches substantially more distinct ends to the same
chain. The exon structure drawn here is illustrative and is not a real locus.

Palette: dataviz reference instance. The annotated band uses the neutral,
because it is a baseline rather than a category; the observed band uses
categorical slot 1. Two bands, each directly labelled, so no legend box.

Writes figures/three-axes.svg and figures/three-axes-dark.svg.
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Illustrative models. The internal exons are identical in every row, which is
# the whole point: one intron chain, many first and last exons.
INTERNAL = [(40, 46), (54, 60), (68, 74)]
FIRST_DONOR = 34       # every first exon ends here
LAST_ACCEPTOR = 80     # every last exon begins here

ANNOTATED = (26, 90)                       # the single annotated model
OBSERVED = [(16, 86), (22, 92), (26, 98), (31, 104), (35, 110)]

THEME = {
    "light": {"surface": "#fcfcfb", "series": "#2a78d6", "neutral": "#9aa7b1",
              "ink": "#1a1a19", "muted": "#5c6670", "rule": "#e2e2df",
              "band": "#eef2f6"},
    "dark": {"surface": "#1a1a19", "series": "#3987e5", "neutral": "#7d8890",
             "ink": "#f4f4f2", "muted": "#a8b0b6", "rule": "#333331",
             "band": "#232527"},
}

H = 1.15         # exon height, well under ROW_GAP so rows stay apart
ROW_GAP = 3.0    # vertical distance between transcript models


def model(ax, y, start, end, colour):
    """One transcript: variable first exon, fixed internal chain, variable last."""
    exons = [(start, FIRST_DONOR)] + INTERNAL + [(LAST_ACCEPTOR, end)]
    ax.plot([start, end], [y, y], color=colour, lw=1.0, zorder=2)
    for a, b in exons:
        ax.add_patch(plt.Rectangle((a, y - H / 2), b - a, H,
                                   facecolor=colour, edgecolor="none",
                                   zorder=3))


def draw(mode: str) -> pathlib.Path:
    c = THEME[mode]
    fig, ax = plt.subplots(figsize=(8.6, 4.2))
    fig.patch.set_facecolor(c["surface"])
    ax.set_facecolor(c["surface"])

    rows = len(OBSERVED)
    ys = [i * ROW_GAP for i in range(rows)][::-1]
    y_annot = max(ys) + ROW_GAP * 1.5

    # The shared region, shaded once behind everything.
    ax.add_patch(plt.Rectangle(
        (FIRST_DONOR, -1.9), LAST_ACCEPTOR - FIRST_DONOR, y_annot + 3.2,
        facecolor=c["band"], edgecolor="none", zorder=0))
    ax.text((FIRST_DONOR + LAST_ACCEPTOR) / 2, -2.4,
            "identical intron chain", ha="center", va="top", fontsize=8.0,
            color=c["muted"], style="italic")

    model(ax, y_annot, *ANNOTATED, c["neutral"])
    ax.text(12, y_annot, "annotated", ha="right", va="center", fontsize=9.4,
            color=c["ink"])

    ax.plot([8, 114], [y_annot - ROW_GAP * 0.62, y_annot - ROW_GAP * 0.62], color=c["rule"],
            lw=0.9, zorder=1)

    for y, (s, e) in zip(ys, OBSERVED):
        model(ax, y, s, e, c["series"])
    ax.text(12, (max(ys) + min(ys)) / 2, "observed", ha="right", va="center",
            fontsize=9.4, color=c["ink"])

    ax.text(8, y_annot + 3.4,
            "GENCODE v40 gives a multi-exon splice chain exactly one start "
            "site in 99.7% of cases,\nand one end site in 99.4%. Long reads "
            "attach many more ends to the same chain.",
            ha="left", va="center", fontsize=8.5, color=c["muted"],
            linespacing=1.55)

    ax.set_xlim(-2, 116)
    ax.set_ylim(-4.6, y_annot + 5.4)
    ax.axis("off")
    ax.set_title("One splice chain is not one transcript",
                 fontsize=11.4, color=c["ink"], loc="left", x=0.0, pad=2)
    fig.subplots_adjust(left=0.015, right=0.99, top=0.90, bottom=0.02)

    out = ROOT / "figures" / (
        "three-axes.svg" if mode == "light" else "three-axes-dark.svg")
    out.parent.mkdir(exist_ok=True)
    fig.savefig(out, format="svg", facecolor=c["surface"])
    plt.close(fig)
    return out


if __name__ == "__main__":
    for m in ("light", "dark"):
        print("wrote", draw(m))
