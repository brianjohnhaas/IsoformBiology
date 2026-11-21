#!/usr/bin/env python3
"""Three populations of cells that give the same bulk isoform ratio.

Original figure. Nothing here is traced from or redrawn after a published
figure, and the three distributions are illustrative rather than measured. They
exist to show what a bulk measurement cannot distinguish, which is the question
the single-cell isoform literature is still arguing about
(research/08-singlecell-spatial.yml: SCS-009 through SCS-014).

Every panel has a population mean isoform fraction of 0.5, so every panel
produces the same number in a bulk experiment. The chapter cites measurements
for which of these actually occurs; the figure only establishes that the
question is real.

Palette: dataviz reference instance, categorical slot 1 for the distributions
and the neutral for the shared bulk line, which is a reference rather than a
series. One series per panel, so no legend; each panel is titled with what it
claims.

Writes figures/within-cell-isoform.svg and -dark.svg.
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parent.parent

BINS = np.linspace(0, 1, 21)
CENTRES = (BINS[:-1] + BINS[1:]) / 2


def densities():
    """Three illustrative shapes, each with mean 0.5."""
    x = CENTRES
    mixed = np.exp(-((x - 0.5) ** 2) / (2 * 0.085 ** 2))
    exclusive = (np.exp(-(x ** 2) / (2 * 0.055 ** 2))
                 + np.exp(-((x - 1) ** 2) / (2 * 0.055 ** 2)))
    graded = np.ones_like(x)
    return [
        ("every cell uses both", "about half of each cell's molecules", mixed),
        ("each cell uses one", "and the cells split evenly", exclusive),
        ("cells differ continuously", "with no preferred ratio", graded),
    ]


THEME = {
    "light": {"surface": "#fcfcfb", "series": "#2a78d6", "neutral": "#9aa7b1",
              "ink": "#1a1a19", "muted": "#5c6670", "rule": "#e2e2df"},
    "dark": {"surface": "#1a1a19", "series": "#3987e5", "neutral": "#7d8890",
             "ink": "#f4f4f2", "muted": "#a8b0b6", "rule": "#333331"},
}


def draw(mode: str) -> pathlib.Path:
    c = THEME[mode]
    panels = densities()
    fig, axes = plt.subplots(1, 3, figsize=(9.0, 3.1), sharey=True)
    fig.patch.set_facecolor(c["surface"])

    for ax, (title, sub, d) in zip(axes, panels):
        d = d / d.max()
        ax.set_facecolor(c["surface"])
        ax.bar(CENTRES, d, width=(BINS[1] - BINS[0]) * 0.82,
               color=c["series"], edgecolor="none", zorder=3)
        ax.axvline(0.5, color=c["neutral"], lw=1.2, ls=(0, (4, 3)), zorder=4)
        ax.set_xlim(-0.04, 1.04)
        ax.set_ylim(0, 1.12)
        ax.set_yticks([])
        ax.set_xticks([0, 0.5, 1])
        ax.set_xticklabels(["0", "0.5", "1"], fontsize=7.8, color=c["muted"])
        ax.tick_params(length=0, pad=4)
        for s in ax.spines.values():
            s.set_visible(False)
        ax.set_title(f"{title}\n{sub}", fontsize=9.4, color=c["ink"],
                     pad=10, linespacing=1.6)

    axes[0].set_ylabel("cells", fontsize=8.6, color=c["muted"], labelpad=8)
    fig.suptitle("Three cell populations, one bulk measurement",
                 fontsize=11.4, color=c["ink"], x=0.012, ha="left", y=0.975)
    fig.text(0.5, 0.155, "fraction of the gene's molecules in a cell that "
                         "use isoform A",
             fontsize=8.2, color=c["muted"], ha="center")
    fig.text(0.012, 0.045,
             "The dashed line is the population mean. It is 0.5 in all three "
             "panels, so a bulk assay returns the same value for each.",
             fontsize=7.6, color=c["muted"], style="italic")
    fig.subplots_adjust(left=0.065, right=0.985, top=0.73, bottom=0.27,
                        wspace=0.22)

    out = ROOT / "figures" / (
        "within-cell-isoform.svg" if mode == "light"
        else "within-cell-isoform-dark.svg")
    out.parent.mkdir(exist_ok=True)
    fig.savefig(out, format="svg", facecolor=c["surface"])
    plt.close(fig)
    return out


if __name__ == "__main__":
    for m in ("light", "dark"):
        print("wrote", draw(m))
