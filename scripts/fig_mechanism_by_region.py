#!/usr/bin/env python3
"""Which regulatory mechanism accounts for variation in which part of a protein.

Original figure. Nothing here is traced from or redrawn after a published
figure. It plots four percentages recorded in
research/11-transcript-to-protein.yml (PRO-001, PRO-003, PRO-004) from a
pairwise comparison of 35,082 annotated human protein isoform pairs: 70 per
cent of variable N-termini are attributable to alternative transcription start
sites and 9 per cent to splicing in the 5' UTR; 17 per cent of internal changes
are single residues produced by codons split across junctions; 72 per cent of
variable C-termini involve a reading frameshift.

The denominators differ by row and are named on the axis label rather than
assumed away. No residual or "other" category is drawn, because the source does
not state one and inventing it would imply the categories are exhaustive.

Palette: dataviz reference instance, categorical slot 1 only. One measure, so
no legend; every bar carries its value as a direct label.

Writes figures/mechanism-by-region.svg and figures/mechanism-by-region-dark.svg.
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parent.parent

# (region, mechanism, per cent of that region's variation)
ROWS = [
    ("C-terminus", "reading frameshift", 72),
    ("Internal", "single residue from a split codon", 17),
    ("N-terminus", "splicing within the 5' UTR", 9),
    ("N-terminus", "alternative transcription start site", 70),
]

THEME = {
    "light": {"surface": "#fcfcfb", "series": "#2a78d6", "ink": "#1a1a19",
              "muted": "#5c6670", "rule": "#d9d9d6"},
    "dark": {"surface": "#1a1a19", "series": "#3987e5", "ink": "#f4f4f2",
             "muted": "#a8b0b6", "rule": "#3a3a38"},
}


def draw(mode: str) -> None:
    c = THEME[mode]
    fig, ax = plt.subplots(figsize=(8.4, 4.1))
    fig.patch.set_facecolor(c["surface"])
    ax.set_facecolor(c["surface"])

    ys = range(len(ROWS))
    for y, (region, mech, pct) in zip(ys, ROWS):
        ax.barh(y, pct, height=0.52, color=c["series"], edgecolor=c["surface"],
                linewidth=2, zorder=3)
        ax.text(pct + 1.6, y, f"{pct}%", va="center", ha="left",
                color=c["ink"], fontsize=10.5, fontweight="medium", zorder=4)
        # Region and mechanism on one line: the region is the denominator, so
        # it has to travel with the bar rather than sit in a separate column.
        ax.text(-0.02, y, mech, va="center", ha="right", color=c["ink"],
                fontsize=9.4, zorder=4, transform=ax.get_yaxis_transform())
        ax.text(-0.02, y + 0.33, region, va="center", ha="right",
                color=c["muted"], fontsize=8.6, style="italic", zorder=4,
                transform=ax.get_yaxis_transform())

    ax.set_xlim(0, 86)
    ax.set_ylim(-0.7, len(ROWS) - 0.3)
    ax.set_yticks([])
    ax.set_xticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xlabel("per cent of the variation observed in that region of the protein",
                  color=c["muted"], fontsize=9.4, labelpad=10)

    fig.subplots_adjust(left=0.37, right=0.97, top=0.96, bottom=0.15)
    suffix = "" if mode == "light" else "-dark"
    fig.savefig(ROOT / f"figures/mechanism-by-region{suffix}.svg",
                format="svg", facecolor=c["surface"])
    plt.close(fig)


for m in ("light", "dark"):
    draw(m)
print("wrote figures/mechanism-by-region.svg and -dark.svg")
