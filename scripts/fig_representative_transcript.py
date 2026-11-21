#!/usr/bin/env python3
"""How often each way of picking one transcript per gene agrees with the
isoform proteomics actually finds dominant.

Original figure. Nothing here is traced from or redrawn after a published
figure. The four rates and the random-choice reference are the anchored claim
in research/09-catalogs.yml (CAT-023).

The note about different gene subsets is on the figure rather than only in the
caption, because without it the chart invites a precision it does not have: the
four rates were computed over different sets of genes and the gaps between
neighbouring bars should not be read as exact differences.

Palette: dataviz reference instance. Slot 1 for the curated resources and the
neutral for the two convenience heuristics, because the comparison is curation
against shortcut rather than four unrelated categories. Both groups are
labelled directly, so there is no legend box.

Writes figures/representative-transcript.svg and -dark.svg.
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parent.parent

# (strategy, agreement per cent, curated)
STRATEGIES = [
    ("APPRIS core principal", 96.1, True),
    ("MANE Select", 94.6, True),
    ("the longest isoform", 86.4, False),
    ("the most-expressed transcript", 70.1, False),
]
RANDOM = 30.0

THEME = {
    "light": {"surface": "#fcfcfb", "series": "#2a78d6", "neutral": "#aab2b9",
              "ink": "#1a1a19", "muted": "#5c6670", "rule": "#e2e2df"},
    "dark": {"surface": "#1a1a19", "series": "#3987e5", "neutral": "#616a71",
             "ink": "#f4f4f2", "muted": "#a8b0b6", "rule": "#333331"},
}


def draw(mode: str) -> pathlib.Path:
    c = THEME[mode]
    fig, ax = plt.subplots(figsize=(7.9, 3.4))
    fig.patch.set_facecolor(c["surface"])
    ax.set_facecolor(c["surface"])

    ys = list(range(len(STRATEGIES)))[::-1]
    for y, (name, pct, curated) in zip(ys, STRATEGIES):
        colour = c["series"] if curated else c["neutral"]
        ax.add_patch(plt.Rectangle((0, y - 0.21), pct, 0.42,
                                   facecolor=colour, edgecolor="none",
                                   zorder=3))
        ax.text(pct + 1.4, y, f"{pct}%", va="center", ha="left",
                fontsize=9.4, color=c["ink"])
        ax.text(-1.6, y, name, va="center", ha="right", fontsize=9.0,
                color=c["ink"])

    ax.axvline(RANDOM, color=c["ink"], lw=1.1, ls=(0, (4, 3)), zorder=4,
               alpha=0.55)
    ax.text(RANDOM + 1.2, -0.72, "a randomly chosen isoform agrees "
                                 f"about {int(RANDOM)}% of the time",
            fontsize=7.8, color=c["muted"], va="center")

    # Inside the panel on the left, where the rows leave a gap; on the right
    # these collided with the value labels.
    ax.text(1.5, ys[0] + 0.50, "curated", ha="left", va="center",
            fontsize=7.8, color=c["series"], style="italic")
    ax.text(1.5, ys[2] + 0.50, "heuristic", ha="left", va="center",
            fontsize=7.8, color=c["muted"], style="italic")

    ax.set_xlim(0, 112)
    ax.set_ylim(-1.15, len(STRATEGIES) - 0.25)
    ax.set_yticks([])
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xticklabels(["0", "25", "50", "75", "100%"], fontsize=8,
                       color=c["muted"])
    ax.tick_params(length=0, pad=5)
    ax.xaxis.grid(True, color=c["rule"], lw=0.7, zorder=0)
    ax.set_axisbelow(True)
    for s in ax.spines.values():
        s.set_visible(False)

    ax.set_title("Agreement with the proteomics-dominant isoform",
                 fontsize=11.2, color=c["ink"], loc="left", pad=22, x=-0.285)
    ax.text(-0.285, 1.055, "the four rates are computed over different gene "
                           "subsets, so neighbouring bars are not exactly "
                           "comparable",
            transform=ax.transAxes, fontsize=7.6, color=c["muted"],
            style="italic", va="center")
    fig.subplots_adjust(left=0.285, right=0.985, top=0.80, bottom=0.17)

    out = ROOT / "figures" / (
        "representative-transcript.svg" if mode == "light"
        else "representative-transcript-dark.svg")
    out.parent.mkdir(exist_ok=True)
    fig.savefig(out, format="svg", facecolor=c["surface"])
    plt.close(fig)
    return out


if __name__ == "__main__":
    for m in ("light", "dark"):
        print("wrote", draw(m))
