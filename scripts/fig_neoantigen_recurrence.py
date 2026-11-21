#!/usr/bin/env python3
"""Recurrent tumour-enriched junctions against recurrent somatic point
mutations, and how much of that survives a wider normal reference.

Original figure. Nothing here is traced from or redrawn after a published
figure. Both panels come from anchored claims in research/06-cancer.yml
(CAN-027 for the counts, CAN-030 for the deflation).

The left panel uses a log axis, which is normally worth avoiding. Here the two
quantities differ by more than three orders of magnitude and the comparison is
the point, so both bars carry their value as a direct label and the axis is
marked in powers of ten. A linear axis would render the mutation bar invisible,
which would overstate rather than clarify.

The right panel is the counterweight and is deliberately the same size. Most of
what a tissue-matched comparison calls cancer-specific is found in other adult
tissue once the reference is widened.

Palette: dataviz reference instance. Left panel: categorical slots 1 and 2, one
per event class. Right panel: slot 1 for the surviving share against the
neutral for the rest, because that is one quantity split, not two categories.

Writes figures/neoantigen-recurrence.svg and -dark.svg.
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parent.parent

# CAN-027: events present in at least 100 of 8,705 TCGA tumours.
RECURRENT = [
    ("tumour-enriched\nsplice junctions", 18000, "about 18,000", 0),
    ("somatic point\nmutations", 13, "13", 1),
]
# CAN-030: share of "cancer-specific" junctions seen in other adult normals.
ELSEWHERE = 80.6

THEME = {
    "light": {"surface": "#fcfcfb", "series": ["#2a78d6", "#eb6834"],
              "neutral": "#c9ced3", "ink": "#1a1a19", "muted": "#5c6670",
              "rule": "#e2e2df"},
    "dark": {"surface": "#1a1a19", "series": ["#3987e5", "#d95926"],
             "neutral": "#4a5158", "ink": "#f4f4f2", "muted": "#a8b0b6",
             "rule": "#333331"},
}


def draw(mode: str) -> pathlib.Path:
    c = THEME[mode]
    fig, (axl, axr) = plt.subplots(1, 2, figsize=(9.2, 3.5),
                                   gridspec_kw={"width_ratios": [1.25, 1]})
    fig.patch.set_facecolor(c["surface"])
    for ax in (axl, axr):
        ax.set_facecolor(c["surface"])
        for s in ax.spines.values():
            s.set_visible(False)
        ax.tick_params(length=0, pad=4)
        ax.set_yticks([])

    # ---- left: recurrence -------------------------------------------------
    for i, (label, n, txt, slot) in enumerate(RECURRENT):
        y = 1 - i
        axl.barh(y, n, left=1, height=0.42, color=c["series"][slot],
                 edgecolor="none", zorder=3)
        axl.text(n * 1.45, y, txt, va="center", ha="left", fontsize=9.4,
                 color=c["ink"])
        axl.text(0.55, y, label, va="center", ha="right", fontsize=8.6,
                 color=c["ink"], linespacing=1.35)
    axl.set_xscale("log")
    axl.set_xlim(1, 200000)
    axl.set_ylim(-1.25, 1.7)
    axl.set_xticks([1, 10, 100, 1000, 10000, 100000])
    axl.set_xticklabels(["1", "10", "100", "1,000", "10,000", "100,000"],
                        fontsize=7.6, color=c["muted"])
    axl.xaxis.grid(True, color=c["rule"], lw=0.7, zorder=0)
    axl.set_axisbelow(True)
    axl.set_title("Events shared by at least 100 of 8,705 tumours",
                  fontsize=9.8, color=c["ink"], loc="left", x=-0.34, pad=10)
    axl.text(1, -0.80, "log scale: the two differ by more than three\n"
                       "orders of magnitude",
             fontsize=7.4, color=c["muted"], style="italic", linespacing=1.4,
             va="center")

    # ---- right: the deflation --------------------------------------------
    axr.barh(0, ELSEWHERE, height=0.42, color=c["series"][0],
             edgecolor="none", zorder=3)
    axr.barh(0, 100 - ELSEWHERE, left=ELSEWHERE + 1.2, height=0.42,
             color=c["neutral"], edgecolor="none", zorder=3)
    axr.text(ELSEWHERE / 2, 0, f"{ELSEWHERE}%", va="center", ha="center",
             fontsize=10.0, color=c["surface"], fontweight="semibold",
             zorder=4)
    axr.text(ELSEWHERE / 2, -0.42, "found in other adult non-cancer tissue",
             va="top", ha="center", fontsize=8.0, color=c["muted"])
    axr.text(100, 0.42, "not found", va="bottom", ha="right", fontsize=8.0,
             color=c["muted"])
    axr.set_xlim(0, 101.5)
    axr.set_ylim(-1.5, 1.2)
    axr.set_xticks([])
    axr.set_title("Junctions called cancer-specific against\n"
                  "tissue-matched normals, re-checked more widely",
                  fontsize=9.8, color=c["ink"], loc="left", x=0.0, pad=10,
                  linespacing=1.4)

    fig.subplots_adjust(left=0.135, right=0.985, top=0.76, bottom=0.14,
                        wspace=0.38)

    out = ROOT / "figures" / (
        "neoantigen-recurrence.svg" if mode == "light"
        else "neoantigen-recurrence-dark.svg")
    out.parent.mkdir(exist_ok=True)
    fig.savefig(out, format="svg", facecolor=c["surface"],
                bbox_inches="tight", pad_inches=0.16)
    plt.close(fig)
    return out


if __name__ == "__main__":
    for m in ("light", "dark"):
        print("wrote", draw(m))
