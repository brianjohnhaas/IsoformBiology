#!/usr/bin/env python3
"""RPS24's three microexons at true relative scale, and the protein ends its
isoforms are reported to produce.

Original figure. Nothing here is traced from or redrawn after a published
figure. Two facts are drawn, from research/11-transcript-to-protein.yml:
RPS24 carries microexons of 3, 18 and 22 base pairs between two constitutive
exons (PRO-040, PRO-041), and the published protein isoform names record ends
of two lysines, three lysines, or proline-lysine-glutamate (PRO-052).

Two things are deliberately NOT drawn. The constitutive exons are shown broken,
because their lengths were not read and are not the point. And no line connects
an exon combination to a protein end, because the sources label these molecules
in mutually inconsistent schemes and the published reconciliation is itself
inconsistent (see the chapter). The microexons are placed in the order the
source lists them.

The one thing worth seeing is scale: at the same scale as its neighbours, a
3 bp exon is a single codon.

Palette: dataviz reference instance. Categorical slot 1 for the microexons,
neutral for the constitutive exons, because those are context rather than a
second category. Every element directly labelled, so no legend.

Writes figures/rps24-microexons.svg and -dark.svg.
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parent.parent

# x positions in base pairs of drawing space. Microexon widths are the real
# 3, 18 and 22 bp; the constitutive exons are drawn broken at a nominal width.
CONST_W = 46
GAP = 17
X4 = 0
M3 = X4 + CONST_W + GAP
M18 = M3 + 3 + GAP
M22 = M18 + 18 + GAP
X6 = M22 + 22 + GAP

MICRO = [(M3, 3, "3 bp"), (M18, 18, "18 bp"), (M22, 22, "22 bp")]
# The published names state the terminal residues; they do not state how the
# three whole proteins compare in length, and one source reports a length
# relationship that cannot be assigned to these names from what was read. So the
# terminal residues are spelled out and NO bar length is drawn.
TERMINI = [("S24-3K", "K-K-K"),
           ("S24-2K", "K-K"),
           ("S24-PKE", "P-K-E")]

THEME = {
    "light": {"surface": "#fcfcfb", "series": "#2a78d6", "neutral": "#c3c9ce",
              "ink": "#1a1a19", "muted": "#5c6670", "rule": "#d9d9d6"},
    "dark": {"surface": "#1a1a19", "series": "#3987e5", "neutral": "#55605a",
             "ink": "#f4f4f2", "muted": "#a8b0b6", "rule": "#3a3a38"},
}

H = 0.46


def draw(mode: str) -> None:
    c = THEME[mode]
    fig, (ax, bx) = plt.subplots(
        2, 1, figsize=(8.4, 4.4), gridspec_kw={"height_ratios": [1.5, 1.0]})
    for a in (ax, bx):
        a.set_facecolor(c["surface"])
        a.set_xticks([])
        a.set_yticks([])
        for s in a.spines.values():
            s.set_visible(False)
    fig.patch.set_facecolor(c["surface"])

    # ---- locus -------------------------------------------------------
    y = 0.0
    ax.plot([X4, X6 + CONST_W], [y, y], color=c["muted"], lw=1.1, zorder=2)

    for x0, label in ((X4, "exon 4"), (X6, "exon 6")):
        ax.add_patch(plt.Rectangle((x0, y - H / 2), CONST_W, H,
                                   facecolor=c["neutral"], edgecolor="none",
                                   zorder=3))
        ax.text(x0 + CONST_W / 2, y - H / 2 - 0.22, label, ha="center",
                va="top", color=c["muted"], fontsize=9)
    # Break marks: these exons continue beyond the drawing.
    for xb in (X4 + 3, X6 + CONST_W - 3):
        ax.plot([xb - 2.5, xb + 2.5], [y + H / 2 + 0.05, y + H / 2 - 0.05],
                color=c["surface"], lw=2.4, zorder=4)
        ax.plot([xb - 2.5, xb + 2.5], [y - H / 2 + 0.05, y - H / 2 - 0.05],
                color=c["surface"], lw=2.4, zorder=4)

    for x0, w, label in MICRO:
        ax.add_patch(plt.Rectangle((x0, y - H / 2), w, H,
                                   facecolor=c["series"], edgecolor="none",
                                   zorder=3))
        ax.annotate(label, xy=(x0 + w / 2, y + H / 2),
                    xytext=(x0 + w / 2, y + 0.92), ha="center", va="bottom",
                    color=c["ink"], fontsize=9.4,
                    arrowprops=dict(arrowstyle="-", color=c["rule"], lw=0.9))

    ax.text((M3 + M22 + 22) / 2, y - 1.05,
            "three microexons, drawn at the same scale as each other",
            ha="center", va="top", color=c["muted"], fontsize=9, style="italic")
    ax.set_xlim(X4 - 6, X6 + CONST_W + 6)
    ax.set_ylim(-1.5, 1.5)

    # ---- protein ends ------------------------------------------------
    for i, (name, residues) in enumerate(TERMINI):
        yy = len(TERMINI) - 1 - i
        bx.text(0.30, yy, name, va="center", ha="right", color=c["ink"],
                fontsize=10.5, fontweight="medium")
        bx.text(0.36, yy, "\u2026", va="center", ha="left", color=c["muted"],
                fontsize=11)
        for j, r in enumerate(residues.split("-")):
            bx.add_patch(plt.Rectangle((0.41 + j * 0.055, yy - 0.22), 0.045,
                                       0.44, facecolor=c["series"],
                                       edgecolor="none", zorder=3))
            bx.text(0.41 + j * 0.055 + 0.0225, yy, r, va="center",
                    ha="center", color=c["surface"], fontsize=9.5,
                    fontweight="bold", zorder=4)
    bx.text(0.06, -0.92,
            "Which exon combination yields which end is labelled differently by "
            "each study; the chapter explains why.\n"
            "Nothing here is drawn to indicate how the three whole proteins "
            "compare in length.",
            ha="left", va="center", color=c["muted"], fontsize=8.6,
            style="italic", linespacing=1.4)
    bx.text(0.06, 2.85, "the three reported protein ends", ha="left",
            va="center", color=c["muted"], fontsize=9, style="italic")
    bx.set_xlim(0, 1.18)
    bx.set_ylim(-1.6, 3.2)

    fig.subplots_adjust(left=0.02, right=0.99, top=0.97, bottom=0.03, hspace=0.1)
    suffix = "" if mode == "light" else "-dark"
    fig.savefig(ROOT / f"figures/rps24-microexons{suffix}.svg",
                format="svg", facecolor=c["surface"])
    plt.close(fig)


for m in ("light", "dark"):
    draw(m)
print("wrote figures/rps24-microexons.svg and -dark.svg")
