#!/usr/bin/env python3
"""What differential gene expression, transcript usage and transcript
expression each see, laid out over one two-isoform gene.

Original figure. Nothing here is traced from or redrawn after a published
figure. The distinction it draws is anchored in research/01-foundations.yml
(FND-028, with FND-029 on exon-level testing); the abundances in the bars are
illustrative round numbers chosen to make each case unambiguous, not
measurements, and the chapter does not cite them as data.

Palette: dataviz reference instance, categorical slots 1 and 2 in fixed order,
a subset of the validated slots 1-3 used by the Dscam figure. Validated with
scripts/validate_palette.js in both modes under --pairs all.

Writes figures/dge-dtu-dte.svg (light) and figures/dge-dtu-dte-dark.svg.
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

ROOT = pathlib.Path(__file__).resolve().parent.parent

BASE = (60, 40)   # isoform 1, isoform 2 in the reference condition

# (row, col): the treated condition, and which tests call the gene changed.
CASES = {
    (0, 0): ((60, 40), []),
    (0, 1): ((25, 75), ["DTU", "DTE"]),
    (1, 0): ((120, 80), ["DGE", "DTE"]),
    (1, 1): ((50, 150), ["DGE", "DTU", "DTE"]),
}
ROW_LABELS = ["total output\nunchanged", "total output\ndoubled"]
COL_LABELS = ["proportions unchanged", "proportions shifted"]
ALL_TESTS = ["DGE", "DTU", "DTE"]

THEME = {
    "light": {
        "surface": "#fcfcfb",
        "series": ["#2a78d6", "#eb6834"],
        "ink": "#1a1a19",
        "muted": "#5c6670",
        "rule": "#d9d9d6",
        "off": "#c3c9ce",
    },
    "dark": {
        "surface": "#1a1a19",
        "series": ["#3987e5", "#d95926"],
        "ink": "#f4f4f2",
        "muted": "#a8b0b6",
        "rule": "#3a3a38",
        "off": "#55605a",
    },
}

YMAX = 215
GAP = 4.0        # surface gap between stacked segments, in data units


def stack(ax, x, width, parts, c):
    """One stacked bar, with a surface-coloured gap between segments."""
    bottom = 0.0
    for i, v in enumerate(parts):
        y = bottom + (GAP if i else 0.0)
        h = v - (GAP if i else 0.0)
        ax.add_patch(plt.Rectangle(
            (x - width / 2, y), width, h,
            facecolor=c["series"][i], edgecolor="none", zorder=3))
        bottom += v


def draw(mode: str) -> pathlib.Path:
    c = THEME[mode]
    fig, axes = plt.subplots(2, 2, figsize=(8.2, 5.4))
    fig.patch.set_facecolor(c["surface"])

    for (r, col), ax in zip(
            [(0, 0), (0, 1), (1, 0), (1, 1)],
            [axes[0][0], axes[0][1], axes[1][0], axes[1][1]]):
        treated, fires = CASES[(r, col)]
        ax.set_facecolor(c["surface"])
        ax.set_xlim(-0.55, 2.55)
        ax.set_ylim(0, YMAX)
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)

        ax.plot([-0.42, 1.42], [0, 0], color=c["rule"], lw=1.1, zorder=1)

        stack(ax, 0.1, 0.46, BASE, c)
        stack(ax, 1.0, 0.46, treated, c)
        for x, label in ((0.1, "reference"), (1.0, "treated")):
            ax.text(x, -11, label, ha="center", va="top",
                    fontsize=7.8, color=c["muted"])

        # Which tests call this gene changed. Greyed when the test is blind.
        for i, name in enumerate(ALL_TESTS):
            on = name in fires
            y = YMAX - 22 - i * 26
            ax.text(1.70, y, name, ha="left", va="center", fontsize=9.0,
                    color=c["ink"] if on else c["off"],
                    fontweight="semibold" if on else "normal")
            ax.text(2.52, y, "calls it" if on else "blind",
                    ha="right", va="center", fontsize=7.4,
                    color=c["muted"] if on else c["off"])

    for col, label in enumerate(COL_LABELS):
        axes[0][col].set_title(label, fontsize=9.6, color=c["ink"], pad=9)
    for r, label in enumerate(ROW_LABELS):
        axes[r][0].text(-0.62, YMAX / 2, label, rotation=90, ha="right",
                        va="center", fontsize=9.2, color=c["ink"],
                        linespacing=1.4)

    fig.legend(
        handles=[Patch(facecolor=c["series"][i], edgecolor="none",
                       label=f"isoform {i + 1}") for i in range(2)],
        loc="lower center", ncol=2, frameon=False, fontsize=8.6,
        labelcolor=c["muted"], bbox_to_anchor=(0.5, 0.004),
        handlelength=1.1, handleheight=1.1, columnspacing=1.8)

    fig.suptitle("Which test sees which change", fontsize=11.6,
                 color=c["ink"], y=0.972, x=0.055, ha="left")
    fig.subplots_adjust(left=0.115, right=0.995, top=0.845, bottom=0.095,
                        hspace=0.34, wspace=0.09)

    out = ROOT / "figures" / (
        "dge-dtu-dte.svg" if mode == "light" else "dge-dtu-dte-dark.svg")
    out.parent.mkdir(exist_ok=True)
    fig.savefig(out, format="svg", facecolor=c["surface"])
    plt.close(fig)
    return out


if __name__ == "__main__":
    for m in ("light", "dark"):
        print("wrote", draw(m))
