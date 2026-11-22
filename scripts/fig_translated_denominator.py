#!/usr/bin/env python3
"""How often an alternative splice junction is seen in protein, and against
which denominator.

Original figure. Nothing here is traced from or redrawn after a published
figure. It plots two percentages recorded in
research/11-transcript-to-protein.yml (PRO-035, PRO-036) from one deep-proteome
experiment: across everything compared against RNA, about 20 per cent of the
exon-exon junctions expected from splicing were detected in protein; restricted
to the genes expressed highly enough to be read end to end, that rose to about
64 per cent.

The figure exists because the same measurement is quoted both ways. Only two
values are drawn, because only two are stated; no curve is interpolated between
them, since the source gives no intermediate points.

Palette: dataviz reference instance, categorical slot 1 only. One measure, so
no legend; both bars carry direct labels.

Writes figures/translated-denominator.svg and -dark.svg.
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parent.parent

BARS = [
    ("All genes compared\nagainst RNA", 20),
    ("Only genes covered\nend to end", 64),
]
NOTE = ("Here, alternative junctions\n"
        "were detected about as often\n"
        "as constitutive ones.")

THEME = {
    "light": {"surface": "#fcfcfb", "series": "#2a78d6", "ink": "#1a1a19",
              "muted": "#5c6670", "rule": "#d9d9d6"},
    "dark": {"surface": "#1a1a19", "series": "#3987e5", "ink": "#f4f4f2",
             "muted": "#a8b0b6", "rule": "#3a3a38"},
}


def draw(mode: str) -> None:
    c = THEME[mode]
    fig, ax = plt.subplots(figsize=(7.6, 4.0))
    fig.patch.set_facecolor(c["surface"])
    ax.set_facecolor(c["surface"])

    xs = [0, 1]
    for x, (label, pct) in zip(xs, BARS):
        ax.bar(x, pct, width=0.42, color=c["series"], edgecolor=c["surface"],
               linewidth=2, zorder=3)
        ax.text(x, pct + 2.2, f"{pct}%", ha="center", va="bottom",
                color=c["ink"], fontsize=13, fontweight="medium", zorder=4)
        ax.text(x, -4.5, label, ha="center", va="top", color=c["ink"],
                fontsize=9.6, linespacing=1.35, zorder=4)

    # The second bar's meaning depends on this, so it is annotated in place.
    ax.text(1.30, 55, NOTE, ha="left", va="center", color=c["muted"],
            fontsize=8.8, linespacing=1.4, style="italic", zorder=4)
    ax.plot([1.22, 1.27], [64, 55], color=c["rule"], lw=1.1, zorder=2)

    ax.set_xlim(-0.55, 2.95)
    ax.set_ylim(0, 78)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_ylabel("per cent of expected splice junctions\ndetected in the proteome",
                  color=c["muted"], fontsize=9.4, linespacing=1.4)

    fig.subplots_adjust(left=0.17, right=0.995, top=0.97, bottom=0.21)
    suffix = "" if mode == "light" else "-dark"
    fig.savefig(ROOT / f"figures/translated-denominator{suffix}.svg",
                format="svg", facecolor=c["surface"])
    plt.close(fig)


for m in ("light", "dark"):
    draw(m)
print("wrote figures/translated-denominator.svg and -dark.svg")
