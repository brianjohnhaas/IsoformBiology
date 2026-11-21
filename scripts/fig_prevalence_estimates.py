#!/usr/bin/env python3
"""Published estimates of how many human genes are alternatively spliced,
1999 to 2008, each shown with the method, denominator and threshold that
produced it.

Original figure. Nothing here is traced from or redrawn after a published
figure. Every value is an anchored claim in research/04-technology-arc.yml, and
the right-hand column exists because the numbers are not comparable without it:
they are measured over different denominators, under different abundance
thresholds, and some are extrapolations rather than counts.

The subject of the figure is the spread, not the trend. Reading it as a rising
line would be reading nine different questions as one.

Palette: dataviz reference instance, categorical slots 1-3 by assay family,
validated in both modes under --pairs all. Every point carries a direct value
label, which also satisfies the relief obligation the aqua slot carries on the
light surface.

Writes figures/prevalence-estimates.svg and -dark.svg.
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

ROOT = pathlib.Path(__file__).resolve().parent.parent

FAMILIES = ["EST", "array", "RNA-seq"]

# (year, method, family, low, high, at_least, denominator / threshold, claim)
ROWS = [
    (1999, "spliced alignment of EST contigs", "EST", 35, 35, False,
     "known human genes", "TECH-010"),
    (2000, "EST comparison", "EST", 38, 38, False,
     "7,867 non-redundant mRNAs", "TECH-011"),
    (2001, "mRNA and EST on the draft genome", "EST", 42, 42, True,
     "human genes", "TECH-012"),
    (2002, "EST, minor form above 5% with support", "EST", 17, 28, False,
     "genes examined", "TECH-013"),
    (2003, "junction arrays, 52 tissues", "array", 74, 74, True,
     "multi-exon genes", "TECH-015"),
    (2008, "mRNA-seq combined with EST and cDNA", "RNA-seq", 95, 95, False,
     "multi-exon genes", "TECH-023"),
    (2008, "RNA-seq, sigmoid extrapolation", "RNA-seq", 98, 100, False,
     "multi-exon genes", "TECH-025"),
    (2008, "RNA-seq, minor isoform above 15%", "RNA-seq", 92, 92, False,
     "multi-exon genes", "TECH-026"),
    (2008, "the same, rescaled", "RNA-seq", 86, 86, False,
     "all human genes", "TECH-026"),
]

THEME = {
    "light": {"surface": "#fcfcfb", "series": ["#2a78d6", "#eb6834", "#1baf7a"],
              "ink": "#1a1a19", "muted": "#5c6670", "rule": "#e2e2df"},
    "dark": {"surface": "#1a1a19", "series": ["#3987e5", "#d95926", "#199e70"],
             "ink": "#f4f4f2", "muted": "#a8b0b6", "rule": "#333331"},
}


def draw(mode: str) -> pathlib.Path:
    c = THEME[mode]
    colour = dict(zip(FAMILIES, c["series"]))
    fig, ax = plt.subplots(figsize=(9.1, 4.6))
    fig.patch.set_facecolor(c["surface"])
    ax.set_facecolor(c["surface"])

    ys = list(range(len(ROWS)))[::-1]
    for y, (year, method, fam, lo, hi, at_least, denom, _) in zip(ys, ROWS):
        col = colour[fam]
        ax.plot([0, 104], [y, y], color=c["rule"], lw=0.7, zorder=0)
        if hi > lo:
            ax.plot([lo, hi], [y, y], color=col, lw=2.4, zorder=3,
                    solid_capstyle="round")
            ax.plot([lo, hi], [y, y], "o", color=col, ms=5.2, zorder=4)
            label = f"{lo}–{hi}%"
        else:
            ax.plot([lo], [y], "o", color=col, ms=6.4, zorder=4)
            label = f"{'at least ' if at_least else ''}{lo}%"
        if at_least:
            ax.annotate("", xy=(lo + 5.5, y), xytext=(lo + 1.4, y),
                        arrowprops=dict(arrowstyle="-|>", color=col, lw=1.3,
                                        shrinkA=0, shrinkB=0), zorder=3)
        ax.text(max(hi, lo) + (8.5 if at_least else 2.6), y, label,
                va="center", ha="left", fontsize=8.2, color=c["ink"])
        ax.text(-2.5, y, f"{year}  {method}", va="center", ha="right",
                fontsize=8.4, color=c["ink"])
        ax.text(130, y, denom, va="center", ha="left", fontsize=7.8,
                color=c["muted"], style="italic")

    ax.text(130, len(ROWS) - 0.35, "denominator", va="center", ha="left",
            fontsize=7.8, color=c["ink"], fontweight="semibold")

    ax.set_xlim(0, 104)
    ax.set_ylim(-0.9, len(ROWS) - 0.15)
    ax.set_yticks([])
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xticklabels(["0", "25", "50", "75", "100%"], fontsize=8,
                       color=c["muted"])
    ax.tick_params(length=0, pad=5)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_clip_on(False)

    ax.legend(handles=[Line2D([], [], marker="o", linestyle="none",
                              color=colour[f], markersize=6, label=f)
                       for f in FAMILIES],
              loc="lower left", bbox_to_anchor=(0.0, -0.215), ncol=3,
              frameon=False, fontsize=8.2, labelcolor=c["muted"],
              handletextpad=0.4, columnspacing=1.6)

    ax.set_title("Human genes called alternatively spliced, by study",
                 fontsize=11.4, color=c["ink"], loc="left", pad=14, x=-0.305)
    fig.subplots_adjust(left=0.305, right=0.80, top=0.86, bottom=0.14)

    out = ROOT / "figures" / (
        "prevalence-estimates.svg" if mode == "light"
        else "prevalence-estimates-dark.svg")
    out.parent.mkdir(exist_ok=True)
    fig.savefig(out, format="svg", facecolor=c["surface"],
                bbox_inches="tight", pad_inches=0.18)
    plt.close(fig)
    return out


if __name__ == "__main__":
    for m in ("light", "dark"):
        print("wrote", draw(m))
