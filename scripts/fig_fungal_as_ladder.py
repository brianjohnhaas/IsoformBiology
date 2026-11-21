#!/usr/bin/env python3
"""Per-gene alternative splicing rate across fungal groups of increasing
structural complexity.

Original figure. Nothing here is traced from or redrawn after a published
figure. The four rates are the sampling-depth-corrected per-gene rates recorded
in research/03-plants-fungi-other.yml (PFO-021), all from one comparative study
using one method, which is the only reason they can be put on a shared axis at
all. The chapter says so, and PFO-031 is the reason it has to.

Palette: dataviz reference instance, a single categorical hue (slot 1) because
this is one series. Sequential shading is deliberately avoided; the groups are
ordered but the rate is the magnitude, and shading it twice would encode the
same thing in two channels. No legend, per the single-series rule; the title
names the measure and every bar is directly labelled.

Writes figures/fungal-as-ladder.svg and figures/fungal-as-ladder-dark.svg.
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parent.parent

# PFO-021. Ordered as the study orders them, by structural complexity.
GROUPS = [
    ("Saccharomycotina and\nTaphrinomycotina", "mostly single-celled", 0.26),
    ("Mucoromycotina", "", 2.3),
    ("Pezizomycotina", "filamentous", 7.2),
    ("Basidiomycota", "fruiting bodies", 8.6),
]

THEME = {
    "light": {"surface": "#fcfcfb", "series": "#2a78d6", "ink": "#1a1a19",
              "muted": "#5c6670", "rule": "#d9d9d6"},
    "dark": {"surface": "#1a1a19", "series": "#3987e5", "ink": "#f4f4f2",
             "muted": "#a8b0b6", "rule": "#3a3a38"},
}


def draw(mode: str) -> pathlib.Path:
    c = THEME[mode]
    fig, ax = plt.subplots(figsize=(7.6, 3.5))
    fig.patch.set_facecolor(c["surface"])
    ax.set_facecolor(c["surface"])

    ys = list(range(len(GROUPS)))[::-1]
    for y, (name, habit, rate) in zip(ys, GROUPS):
        ax.add_patch(plt.Rectangle((0, y - 0.22), rate, 0.44,
                                   facecolor=c["series"], edgecolor="none",
                                   zorder=3))
        ax.text(rate + 0.18, y, f"{rate}%", va="center", ha="left",
                fontsize=9.4, color=c["ink"], zorder=4)
        ax.text(-0.35, y + 0.10, name, va="center", ha="right",
                fontsize=9.0, color=c["ink"], linespacing=1.3)
        if habit:
            ax.text(-0.35, y - 0.30, habit, va="center", ha="right",
                    fontsize=7.8, color=c["muted"], style="italic")

    ax.set_xlim(0, 10.6)
    ax.set_ylim(-0.75, len(GROUPS) - 0.25)
    ax.set_yticks([])
    ax.set_xticks([0, 2, 4, 6, 8, 10])
    ax.set_xticklabels(["0", "2", "4", "6", "8", "10%"], fontsize=8,
                       color=c["muted"])
    ax.tick_params(length=0, pad=5)
    ax.xaxis.grid(True, color=c["rule"], lw=0.7, zorder=0)
    ax.set_axisbelow(True)
    for s in ax.spines.values():
        s.set_visible(False)

    ax.set_title("Genes alternatively spliced, per fungal group",
                 fontsize=11.2, color=c["ink"], loc="left", pad=12,
                 x=-0.335)
    fig.subplots_adjust(left=0.335, right=0.985, top=0.83, bottom=0.14)

    out = ROOT / "figures" / (
        "fungal-as-ladder.svg" if mode == "light"
        else "fungal-as-ladder-dark.svg")
    out.parent.mkdir(exist_ok=True)
    fig.savefig(out, format="svg", facecolor=c["surface"])
    plt.close(fig)
    return out


if __name__ == "__main__":
    for m in ("light", "dark"):
        print("wrote", draw(m))
