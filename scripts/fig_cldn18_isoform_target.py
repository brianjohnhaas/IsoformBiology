#!/usr/bin/env python3
"""Two first exons of CLDN18, the two proteins they produce, and the antibody
that binds only one of them.

Original figure. Nothing here is traced from or redrawn after a published
figure. It is a schematic of one fact recorded in
research/12-proteoforms-drugs.yml (DRG-020, DRG-022): the stomach and lung
forms of claudin-18 are identical except for the N-terminal cytoplasmic
region, the first transmembrane domain and the first extracellular loop, all of
which derive from isoform-specific first exons; the approved antibody was
designed against the stomach form's loop to avoid binding the lung form.

Exon count, exon sizes and the proportions of the protein bar are illustrative.
The sources give the identity of the differing regions, not their lengths, and
nothing here should be measured.

Palette: dataviz reference instance, categorical slots 1 and 2 for the two
isoforms, neutral for the sequence they share. Both isoforms directly labelled,
so no legend.

Writes figures/cldn18-isoform-target.svg and -dark.svg.
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

ROOT = pathlib.Path(__file__).resolve().parent.parent

THEME = {
    "light": {"surface": "#fcfcfb", "lung": "#2a78d6", "stomach": "#eb6834",
              "neutral": "#c3c9ce", "ink": "#1a1a19", "muted": "#5c6670",
              "rule": "#d9d9d6"},
    "dark": {"surface": "#1a1a19", "lung": "#3987e5", "stomach": "#d95926",
             "neutral": "#55605a", "ink": "#f4f4f2", "muted": "#a8b0b6",
             "rule": "#3a3a38"},
}

E1A = (0, 10)       # lung-specific first exon
E1B = (20, 30)      # stomach-specific first exon
SHARED = [(44, 56), (64, 76), (84, 96)]
H = 0.5


def antibody(ax, x, y, colour):
    """A simple Y below the bar: the two binding arms meet the protein, and
    the stem points away from it."""
    ax.plot([x - 3.6, x], [y - 0.30, y - 0.95], color=colour, lw=2.4, zorder=5,
            solid_capstyle="round")
    ax.plot([x + 3.6, x], [y - 0.30, y - 0.95], color=colour, lw=2.4, zorder=5,
            solid_capstyle="round")
    ax.plot([x, x], [y - 0.95, y - 1.58], color=colour, lw=2.4, zorder=5,
            solid_capstyle="round")


def draw(mode: str) -> None:
    c = THEME[mode]
    fig, (ax, bx) = plt.subplots(
        2, 1, figsize=(8.4, 4.8), gridspec_kw={"height_ratios": [1.0, 1.25]})
    for a in (ax, bx):
        a.set_facecolor(c["surface"])
        a.set_xticks([])
        a.set_yticks([])
        for s in a.spines.values():
            s.set_visible(False)
    fig.patch.set_facecolor(c["surface"])

    # ---- the gene ----------------------------------------------------
    y = 0.0
    ax.plot([E1A[0], SHARED[-1][1]], [y, y], color=c["muted"], lw=1.0, zorder=2)
    for (a0, a1), col, lab in ((E1A, c["lung"], "lung-specific\nfirst exon"),
                               (E1B, c["stomach"], "stomach-specific\nfirst exon")):
        ax.add_patch(plt.Rectangle((a0, y - H / 2), a1 - a0, H, facecolor=col,
                                   edgecolor="none", zorder=3))
        ax.text((a0 + a1) / 2, y - H / 2 - 0.30, lab, ha="center", va="top",
                color=c["ink"], fontsize=8.8, linespacing=1.35)
    for a0, a1 in SHARED:
        ax.add_patch(plt.Rectangle((a0, y - H / 2), a1 - a0, H,
                                   facecolor=c["neutral"], edgecolor="none",
                                   zorder=3))
    ax.text((SHARED[0][0] + SHARED[-1][1]) / 2, y - H / 2 - 0.30,
            "exons shared by both isoforms", ha="center", va="top",
            color=c["muted"], fontsize=8.8)

    # splice arcs: 1a skips 1b; 1b starts its own transcript
    ax.add_patch(FancyArrowPatch((E1A[1], y + H / 2), (SHARED[0][0], y + H / 2),
                                 connectionstyle="arc3,rad=-0.45",
                                 arrowstyle="-", color=c["lung"], lw=1.5,
                                 zorder=4))
    ax.add_patch(FancyArrowPatch((E1B[1], y - H / 2), (SHARED[0][0], y - H / 2),
                                 connectionstyle="arc3,rad=0.42",
                                 arrowstyle="-", color=c["stomach"], lw=1.5,
                                 zorder=4))
    ax.set_xlim(-4, 100)
    ax.set_ylim(-1.9, 1.7)

    # ---- the two proteins --------------------------------------------
    DIFF = 26          # drawn length of the isoform-specific portion
    TOTAL = 86
    rows = [(1.9, c["lung"], "CLDN18.1", "lung"),
            (0.0, c["stomach"], "CLDN18.2", "stomach")]
    for yy, col, name, tissue in rows:
        bx.add_patch(plt.Rectangle((0, yy - H / 2), DIFF, H, facecolor=col,
                                   edgecolor="none", zorder=3))
        bx.add_patch(plt.Rectangle((DIFF + 1.2, yy - H / 2), TOTAL - DIFF - 1.2,
                                   H, facecolor=c["neutral"], edgecolor="none",
                                   zorder=3))
        bx.text(-2.5, yy, name, va="center", ha="right", color=c["ink"],
                fontsize=10.5, fontweight="medium")
        bx.text(-2.5, yy - 0.52, tissue, va="center", ha="right",
                color=c["muted"], fontsize=8.8, style="italic")

    bx.text(DIFF / 2, rows[0][0] + 0.52,
            "N-terminal region, first transmembrane\n"
            "domain and first extracellular loop",
            ha="center", va="bottom", color=c["ink"], fontsize=8.8,
            linespacing=1.35)
    bx.text((DIFF + TOTAL) / 2, rows[0][0] + 0.52, "identical in both",
            ha="center", va="bottom", color=c["muted"], fontsize=8.8)

    antibody(bx, DIFF / 2, rows[1][0], c["stomach"])
    bx.text(DIFF / 2 + 7.5, rows[1][0] - 1.15,
            "the approved antibody binds here,\nso it does not touch CLDN18.1",
            ha="left", va="center", color=c["ink"], fontsize=8.8,
            linespacing=1.35)

    bx.set_xlim(-26, 100)
    bx.set_ylim(-2.3, 3.3)

    fig.subplots_adjust(left=0.02, right=0.99, top=0.97, bottom=0.04, hspace=0.28)
    suffix = "" if mode == "light" else "-dark"
    fig.savefig(ROOT / f"figures/cldn18-isoform-target{suffix}.svg",
                format="svg", facecolor=c["surface"])
    plt.close(fig)


for m in ("light", "dark"):
    draw(m)
print("wrote figures/cldn18-isoform-target.svg and -dark.svg")
