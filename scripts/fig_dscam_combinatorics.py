#!/usr/bin/env python3
"""Dscam1 combinatorial isoform diversity: the gene, the arithmetic, the usage.

Original figure. Nothing here is traced from or redrawn after a published
figure; it is generated from the anchored numbers in research/02-animals.yml.

Palette: dataviz reference instance, categorical slots 1-3 in fixed order, plus
a neutral for the transmembrane exon (a binary choice, not a variable cluster,
so it is deliberately not given a categorical hue). Validated with
scripts/validate_palette.js in both modes: all six checks pass. Aqua carries a
relief obligation on the light surface, satisfied by direct labels on every mark.

Writes figures/dscam-combinatorics.svg (light) and
figures/dscam-combinatorics-dark.svg.
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Anchored in research/02-animals.yml (ANM-001, ANM-005, ANM-007).
CLUSTERS = [("exon 4", 12), ("exon 6", 48), ("exon 9", 33)]
TM_EXON = ("exon 17", 2)
ECTODOMAIN = 12 * 48 * 33          # 19,008
TOTAL = ECTODOMAIN * 2            # 38,016
PER_NEURON = (10, 50)             # isoforms used by a single neuron

THEME = {
    "light": {
        "surface": "#fcfcfb",
        "series": ["#2a78d6", "#eb6834", "#1baf7a"],
        "neutral": "#9aa7b1",
        "ink": "#1a1a19",
        "muted": "#5c6670",
        "rule": "#d9d9d6",
    },
    "dark": {
        "surface": "#1a1a19",
        "series": ["#3987e5", "#d95926", "#199e70"],
        "neutral": "#7d8890",
        "ink": "#f4f4f2",
        "muted": "#a8b0b6",
        "rule": "#3a3a38",
    },
}


def draw(mode: str) -> pathlib.Path:
    c = THEME[mode]
    fig, (ax_gene, ax_math) = plt.subplots(
        2, 1, figsize=(8.4, 4.9), height_ratios=[1.35, 1],
        gridspec_kw={"hspace": 0.12},
    )
    for ax in (ax_gene, ax_math):
        ax.set_facecolor(c["surface"])
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)
    fig.patch.set_facecolor(c["surface"])

    # ---- panel 1: the gene, with one cluster drawn out as stacked variants ----
    ax_gene.set_xlim(0, 100)
    ax_gene.set_ylim(-1.6, 3.4)
    ax_gene.plot([2, 98], [0, 0], color=c["rule"], lw=2, zorder=1,
                 solid_capstyle="round")

    spans = [(10, 16), (34, 20), (62, 16), (86, 7)]
    items = CLUSTERS + [TM_EXON]
    for i, ((label, n), (x0, w)) in enumerate(zip(items, spans)):
        col = c["series"][i] if i < 3 else c["neutral"]
        # stacked variant exons, suggesting the cluster's depth
        for k, dy in enumerate((0.95, 0.62, 0.29)):
            ax_gene.add_patch(FancyBboxPatch(
                (x0 + k * 1.1, dy), w - 2.2, 0.26,
                boxstyle="round,pad=0.015,rounding_size=0.09",
                facecolor=col, edgecolor=c["surface"], lw=1.4,
                alpha=1.0 - 0.18 * k, zorder=3 - k * 0.1,
            ))
        ax_gene.text(x0 + w / 2 - 1, 1.62, f"{label}\n{n} variants",
                     ha="center", va="bottom", fontsize=9.5,
                     color=c["ink"], linespacing=1.35,
                     fontweight="semibold" if i < 3 else "normal")
        ax_gene.text(x0 + w / 2 - 1, -0.62,
                     "mutually exclusive\n(one chosen)" if i < 3
                     else "alternative\n(one of two)",
                     ha="center", va="top", fontsize=7.8, color=c["muted"],
                     linespacing=1.3)

    # constant exons between the clusters
    for cx in (28, 56, 80, 95):
        ax_gene.add_patch(Rectangle((cx, 0.47), 2.6, 0.3,
                                    facecolor=c["rule"], edgecolor="none",
                                    zorder=2))
    ax_gene.set_title(
        "Dscam1 builds tens of thousands of isoforms by combination",
        fontsize=11.5, color=c["ink"], pad=12, loc="left", fontweight="semibold",
    )

    # ---- panel 2: the arithmetic, and how little of it one neuron uses ----
    ax_math.set_xlim(0, 100)
    ax_math.set_ylim(0, 10)
    terms = " × ".join(str(n) for _, n in CLUSTERS)
    ax_math.text(2, 8.1, f"{terms}", fontsize=15, color=c["ink"],
                 va="center", fontweight="semibold")
    ax_math.text(2, 5.4, f"= {ECTODOMAIN:,} distinct ectodomains",
                 fontsize=11.5, color=c["ink"], va="center")
    ax_math.text(2, 2.4,
                 f"× 2 transmembrane forms\n= {TOTAL:,} isoforms in total",
                 fontsize=10, color=c["muted"], va="center", linespacing=1.6)

    # the contrast that matters biologically
    ax_math.plot([52, 52], [0.8, 9.2], color=c["rule"], lw=1.4)
    ax_math.text(56, 8.1, "What one neuron actually uses",
                 fontsize=10.5, color=c["ink"], va="center",
                 fontweight="semibold")
    ax_math.text(56, 5.4,
                 f"roughly {PER_NEURON[0]} to {PER_NEURON[1]} isoforms,\n"
                 "drawn probabilistically",
                 fontsize=10.5, color=c["ink"], va="center", linespacing=1.6)
    frac = f"1 in {ECTODOMAIN // PER_NEURON[1]:,} to 1 in {ECTODOMAIN // PER_NEURON[0]:,}"
    ax_math.text(56, 2.4, f"of the repertoire,\nabout {frac}",
                 fontsize=9, color=c["muted"], va="center", linespacing=1.6)

    out = ROOT / "figures" / (
        "dscam-combinatorics.svg" if mode == "light"
        else "dscam-combinatorics-dark.svg"
    )
    fig.savefig(out, format="svg", bbox_inches="tight",
                facecolor=c["surface"])
    plt.close(fig)
    return out


if __name__ == "__main__":
    for m in ("light", "dark"):
        print("wrote", draw(m))
    assert ECTODOMAIN == 19008, ECTODOMAIN
    assert TOTAL == 38016, TOTAL
    print(f"arithmetic checks: {ECTODOMAIN:,} ectodomains, {TOTAL:,} total")
