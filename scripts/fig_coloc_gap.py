#!/usr/bin/env python3
"""How often a GWAS signal is explained by a molecular QTL, from two angles.

Original figure. Nothing here is traced from or redrawn after a published
figure. Both panels come from anchored claims in research/10-variants-qtl.yml.

Left: GTEx v8 colocalization over 5,385 GWAS associations in 1,167 independent
LD blocks from 87 complex traits (VAR-004). The two bars are drawn side by side
rather than nested because the published numbers do not give their overlap, and
stacking them would assert an overlap nobody reported.

Right: the colocalization audit (VAR-001, VAR-002). Genes nominated as causal
on non-expression grounds, then how many have an eQTL in a trait-relevant
tissue, then how many actually colocalize. The collapse is at the last step.
The middle bar is drawn hatched because its value is reported as "more than
nine in ten" rather than as a count.

Palette: dataviz reference instance, categorical slots 1 and 2. The two panels
use the same two hues for the same two meanings: an expression explanation and
a splicing one on the left, and on the right a single slot-1 series, since
every bar there counts the same kind of thing.

Writes figures/coloc-gap.svg and figures/coloc-gap-dark.svg.
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = pathlib.Path(__file__).resolve().parent.parent

GTEX = [("colocalizes with\na cis-eQTL", 43, 0), ("colocalizes with\na cis-sQTL", 23, 1)]
FUNNEL = [
    ("genes nominated as causal\non non-expression grounds", 220, False),
    ("with an eQTL in at least one\ntrait-relevant tissue", 200, True),
    ("whose GWAS and eQTL\nsignals colocalize", 18, False),
]

THEME = {
    "light": {"surface": "#fcfcfb", "series": ["#2a78d6", "#eb6834"],
              "ink": "#1a1a19", "muted": "#5c6670", "rule": "#e2e2df"},
    "dark": {"surface": "#1a1a19", "series": ["#3987e5", "#d95926"],
             "ink": "#f4f4f2", "muted": "#a8b0b6", "rule": "#333331"},
}


def draw(mode: str) -> pathlib.Path:
    c = THEME[mode]
    fig, (axl, axr) = plt.subplots(1, 2, figsize=(9.0, 3.9),
                                   gridspec_kw={"width_ratios": [1, 1.35]})
    fig.patch.set_facecolor(c["surface"])

    for ax in (axl, axr):
        ax.set_facecolor(c["surface"])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)
        ax.tick_params(length=0, pad=4)

    # ---- left: GTEx v8 ----------------------------------------------------
    for i, (label, pct, slot) in enumerate(GTEX):
        y = 1 - i
        ax = axl
        ax.add_patch(plt.Rectangle((0, y - 0.20), pct, 0.40,
                                   facecolor=c["series"][slot],
                                   edgecolor="none", zorder=3))
        ax.text(pct + 2, y, f"{pct}%", va="center", ha="left", fontsize=9.6,
                color=c["ink"])
        ax.text(-2.5, y, label, va="center", ha="right", fontsize=8.4,
                color=c["ink"], linespacing=1.35)
    axl.set_xlim(0, 100)
    axl.set_ylim(-0.95, 1.75)
    axl.set_xticks([0, 50, 100])
    axl.set_xticklabels(["0", "50", "100%"], fontsize=8, color=c["muted"])
    axl.xaxis.grid(True, color=c["rule"], lw=0.7, zorder=0)
    axl.set_axisbelow(True)
    axl.set_title("GTEx v8, 5,385 GWAS associations", fontsize=9.8,
                  color=c["ink"], loc="left", x=-0.56, pad=10)
    axl.text(0, -0.78, "the overlap between the two was not reported,\n"
                       "so the bars are not stacked",
             fontsize=7.4, color=c["muted"], style="italic", linespacing=1.4,
             va="center")

    # ---- right: the funnel ------------------------------------------------
    for i, (label, n, approx) in enumerate(FUNNEL):
        y = 2 - i
        kw = dict(facecolor=c["series"][0], edgecolor="none", zorder=3)
        if approx:
            kw = dict(facecolor="none", edgecolor=c["series"][0], lw=1.3,
                      hatch="////", zorder=3)
        axr.add_patch(plt.Rectangle((0, y - 0.20), n, 0.40, **kw))
        if approx:
            # Inside the bar: the value is a bound, not a count, and putting it
            # on the axis beside the others would read as one.
            axr.text(n / 2, y, "more than nine in ten", va="center",
                     ha="center", fontsize=8.2, color=c["muted"],
                     bbox=dict(facecolor=c["surface"], edgecolor="none",
                               boxstyle="square,pad=0.30"), zorder=4)
        else:
            axr.text(n + 5, y, str(n), va="center", ha="left", fontsize=9.0,
                     color=c["ink"])
        axr.text(-6, y, label, va="center", ha="right", fontsize=8.4,
                 color=c["ink"], linespacing=1.35)
    axr.set_xlim(0, 240)
    axr.set_ylim(-0.95, 2.75)
    axr.set_xticks([0, 100, 200])
    axr.set_xticklabels(["0", "100", "200 genes"], fontsize=8, color=c["muted"])
    axr.xaxis.grid(True, color=c["rule"], lw=0.7, zorder=0)
    axr.set_axisbelow(True)
    axr.set_title("Genes nominated as causal, tested for an eQTL explanation",
                  fontsize=9.8, color=c["ink"], loc="left", x=-0.42, pad=10)
    axr.text(0, -0.78, "18 of 220 is 8.2%, which those authors note is not\n"
                       "clearly better than chance",
             fontsize=7.4, color=c["muted"], style="italic", linespacing=1.4,
             va="center")

    fig.subplots_adjust(left=0.175, right=0.985, top=0.80, bottom=0.14,
                        wspace=0.80)

    out = ROOT / "figures" / (
        "coloc-gap.svg" if mode == "light" else "coloc-gap-dark.svg")
    out.parent.mkdir(exist_ok=True)
    fig.savefig(out, format="svg", facecolor=c["surface"],
                bbox_inches="tight", pad_inches=0.16)
    plt.close(fig)
    return out


if __name__ == "__main__":
    for m in ("light", "dark"):
        print("wrote", draw(m))
