#!/usr/bin/env python3
"""Coding genes, the proteoforms estimated to exist in one cell, and the
proteoforms one experiment reports.

Original figure. Nothing here is traced from or redrawn after a published
figure. Three quantities recorded in research/12-proteoforms-drugs.yml:
about 20,000 protein-coding genes and an estimate of more than one million
distinct protein forms per cell (DRG-001), against thousands of proteoforms
identified and quantified in a single top-down study from a cell lysate
(DRG-011).

The measured quantity is drawn as a band spanning one decade rather than a
point, because the source says only "thousands" and does not give a figure.
That imprecision is stated on the chart rather than resolved by guessing.

Palette: dataviz reference instance, categorical slot 1 for the two stated
counts and the neutral for the imprecise band. Log axis, because the three
quantities span five orders of magnitude; every value is directly labelled.

Writes figures/proteoform-scale.svg and -dark.svg.
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.ticker  # noqa: E402
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parent.parent

THEME = {
    "light": {"surface": "#fcfcfb", "series": "#2a78d6", "neutral": "#9aa7b1",
              "ink": "#1a1a19", "muted": "#5c6670", "rule": "#d9d9d6"},
    "dark": {"surface": "#1a1a19", "series": "#3987e5", "neutral": "#7d8890",
             "ink": "#f4f4f2", "muted": "#a8b0b6", "rule": "#3a3a38"},
}


def draw(mode: str) -> None:
    c = THEME[mode]
    fig, ax = plt.subplots(figsize=(8.2, 3.5))
    fig.patch.set_facecolor(c["surface"])
    ax.set_facecolor(c["surface"])

    # y=2 top row down to y=0
    rows = [
        (2, "Protein-coding genes", 20_000, "20,000", "point"),
        (1, "Protein forms estimated\nin a single cell", 1_000_000,
         "more than a million", "point"),
        (0, "Protein forms reported by one\ntop-down proteomics study", None,
         "thousands", "band"),
    ]

    for y, label, val, vlabel, kind in rows:
        if kind == "point":
            ax.plot([700, val], [y, y], color=c["series"], lw=2.4, zorder=3,
                    solid_capstyle="butt")
            ax.plot([val], [y], "o", ms=9, color=c["series"], zorder=4)
            ax.text(val * 1.45, y, vlabel, va="center", ha="left",
                    color=c["ink"], fontsize=10, fontweight="medium", zorder=4)
        else:
            ax.add_patch(plt.Rectangle((1_000, y - 0.17), 9_000, 0.34,
                                       facecolor=c["neutral"], alpha=0.55,
                                       edgecolor="none", zorder=3))
            ax.text(10_000 * 1.45, y, vlabel, va="center", ha="left",
                    color=c["ink"], fontsize=10, fontweight="medium", zorder=4)
        ax.text(-0.02, y, label, va="center", ha="right", color=c["ink"],
                fontsize=9.5, linespacing=1.35, zorder=4,
                transform=ax.get_yaxis_transform())

    ax.annotate("", xy=(1_000_000, 0.78), xytext=(10_000, 0.78),
                arrowprops=dict(arrowstyle="<->", color=c["muted"], lw=1.1))
    ax.text(100_000, 0.60, "the gap this chapter is about",
            ha="center", va="top", color=c["muted"], fontsize=8.8,
            style="italic", zorder=4)

    ax.set_xscale("log")
    ax.set_xlim(700, 1.1e7)
    ax.set_ylim(-0.55, 2.5)
    ax.set_yticks([])
    ax.set_xticks([1e3, 1e4, 1e5, 1e6, 1e7])
    ax.set_xticklabels(["1,000", "10,000", "100,000", "1 million", "10 million"],
                       fontsize=8.8, color=c["muted"])
    ax.tick_params(axis="x", which="both", length=0, pad=6)
    ax.xaxis.set_minor_locator(matplotlib.ticker.NullLocator())
    for s in ax.spines.values():
        s.set_visible(False)
    ax.grid(axis="x", color=c["rule"], lw=0.8, zorder=0)
    ax.set_axisbelow(True)

    fig.subplots_adjust(left=0.30, right=0.84, top=0.96, bottom=0.17)
    suffix = "" if mode == "light" else "-dark"
    fig.savefig(ROOT / f"figures/proteoform-scale{suffix}.svg",
                format="svg", facecolor=c["surface"])
    plt.close(fig)


for m in ("light", "dark"):
    draw(m)
print("wrote figures/proteoform-scale.svg and -dark.svg")
