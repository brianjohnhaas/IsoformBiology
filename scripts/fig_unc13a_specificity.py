#!/usr/bin/env python3
"""Detection of the UNC13A cryptic exon by diagnostic group.

Original figure. Nothing here is traced from or redrawn after a published
figure. The rates are the anchored claim in research/07-neuro-mendelian.yml
(NEU-011), measured across 1,349 post-mortem brain and spinal cord tissues from
377 individuals.

The zeroes are the message, so the groups with no detections are drawn as
labelled zero rows rather than left out. A chart showing only the two positive
bars would say the marker is present in TDP-43 proteinopathy; this one says it
is present there and nowhere else tested.

Palette: dataviz reference instance. Slot 1 for the TDP-43 proteinopathies and
the neutral for every group without the pathology, because the split is one
condition present or absent rather than a set of categories. Both bands are
labelled directly, so there is no legend box.

Writes figures/unc13a-specificity.svg and -dark.svg.
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parent.parent

# (group, per cent of individuals with the cryptic exon, TDP-43 pathology)
GROUPS = [
    ("FTLD-TDP", 89, True),
    ("ALS-TDP", 38, True),
    ("ALS with SOD1 mutation", 0, False),
    ("ALS with FUS mutation", 0, False),
    ("FTLD-TAU", 0, False),
    ("FTLD-FUS", 0, False),
    ("controls", 0, False),
]

THEME = {
    "light": {"surface": "#fcfcfb", "series": "#2a78d6", "neutral": "#b9c0c6",
              "ink": "#1a1a19", "muted": "#5c6670", "rule": "#e2e2df"},
    "dark": {"surface": "#1a1a19", "series": "#3987e5", "neutral": "#5a6268",
             "ink": "#f4f4f2", "muted": "#a8b0b6", "rule": "#333331"},
}


def draw(mode: str) -> pathlib.Path:
    c = THEME[mode]
    fig, ax = plt.subplots(figsize=(7.8, 3.9))
    fig.patch.set_facecolor(c["surface"])
    ax.set_facecolor(c["surface"])

    ys = list(range(len(GROUPS)))[::-1]
    for y, (name, pct, tdp) in zip(ys, GROUPS):
        colour = c["series"] if tdp else c["neutral"]
        if pct:
            ax.add_patch(plt.Rectangle((0, y - 0.21), pct, 0.42,
                                       facecolor=colour, edgecolor="none",
                                       zorder=3))
            ax.text(pct + 1.6, y, f"{pct}%", va="center", ha="left",
                    fontsize=9.4, color=c["ink"])
        else:
            # A visible zero, so an absent bar cannot be read as missing data.
            ax.plot([0, 0.9], [y, y], color=colour, lw=3.2, zorder=3,
                    solid_capstyle="butt")
            ax.text(2.4, y, "0", va="center", ha="left", fontsize=9.0,
                    color=c["muted"])
        ax.text(-1.8, y, name, va="center", ha="right", fontsize=8.8,
                color=c["ink"])

    ax.text(-1.8, ys[0] + 0.78, "TDP-43 proteinopathy", ha="right",
            va="center", fontsize=7.8, color=c["series"], style="italic")
    # On the right, where the zero rows leave the panel empty; on the left it
    # collided with the first group name.
    ax.text(99, ys[2] + 0.22, "no TDP-43 pathology", ha="right",
            va="center", fontsize=7.8, color=c["muted"], style="italic")
    ax.plot([-1.3, 100], [ys[2] + 0.52, ys[2] + 0.52], color=c["rule"],
            lw=0.9, zorder=1)

    ax.set_xlim(0, 100)
    ax.set_ylim(-1.25, len(GROUPS) - 0.05)
    ax.set_yticks([])
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xticklabels(["0", "25", "50", "75", "100%"], fontsize=8,
                       color=c["muted"])
    ax.tick_params(length=0, pad=5)
    ax.xaxis.grid(True, color=c["rule"], lw=0.7, zorder=0)
    ax.set_axisbelow(True)
    for s in ax.spines.values():
        s.set_visible(False)

    ax.set_title("Individuals carrying the UNC13A cryptic exon",
                 fontsize=11.2, color=c["ink"], loc="left", pad=12, x=-0.30)
    ax.text(0, -0.92, "1,349 post-mortem brain and spinal cord tissues from "
                      "377 individuals",
            fontsize=7.6, color=c["muted"], style="italic", va="center")
    fig.subplots_adjust(left=0.30, right=0.98, top=0.84, bottom=0.14)

    out = ROOT / "figures" / (
        "unc13a-specificity.svg" if mode == "light"
        else "unc13a-specificity-dark.svg")
    out.parent.mkdir(exist_ok=True)
    fig.savefig(out, format="svg", facecolor=c["surface"])
    plt.close(fig)
    return out


if __name__ == "__main__":
    for m in ("light", "dark"):
        print("wrote", draw(m))
