"""Showcase color sets and maps."""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import RegularPolygon

from tol_colors import colormaps, colorsets, rainbow_discrete


def main():
    """Create three plots to showcase colorsets, colormaps, and rainbow_discrete."""
    # Show colorsets get_colorset(<scheme>).
    fig, axes = plt.subplots(
        ncols=len(colorsets), figsize=(13, 5), layout="constrained", sharey=True
    )
    max_ncolors = max(len(cset) for cset in colorsets.values())
    for ax, (cset_name, cset) in zip(axes, colorsets.items(), strict=False):
        names = cset._fields
        colors = list(cset)
        for i, (name, color) in enumerate(zip(names, colors, strict=False)):
            # octogon side
            a = 1.0 / (1 + np.sqrt(2))
            # and outer radius
            r = 1.307 * a
            p = RegularPolygon(
                xy=(0.0, max_ncolors - i + 0.5),
                numVertices=8,
                radius=r,
                orientation=np.pi / 360 * 45,
                ec=None,
                fc=color,
            )
            ax.add_artist(p)
            ax.annotate(name, xy=(1.1, 0.5), xycoords=p, ha="left", va="center")
        ax.set_xlim(-r, r)
        ax.set_ylim(0, max_ncolors + 1)
        ax.set_aspect("equal")
        ax.set_axis_off()
        ax.set_title(cset_name, loc="left", weight="bold")
    plt.show()
    return

    # Show colormaps
    cmaps_names = [
        n for n in colormaps if not (n.endswith("_r") or n.startswith("rainbow"))
    ]
    cmaps_names += ["rainbow_WhBr", "rainbow_WhRd", "rainbow_PuBr", "rainbow_PuRd"]
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    fig, axes = plt.subplots(nrows=len(cmaps_names))
    fig.subplots_adjust(top=0.98, bottom=0.02, left=0.2, right=0.99)
    for ax, cmap_name in zip(axes, cmaps_names, strict=False):
        pos = list(ax.get_position().bounds)
        ax.set_axis_off()
        ax.imshow(gradient, aspect=4, cmap=colormaps[cmap_name])
        fig.text(
            pos[0] - 0.01,
            pos[1] + pos[3] / 2.0,
            cmap_name,
            va="center",
            ha="right",
            fontsize=10,
        )
    # plt.show()

    # Show discrete rainbow.
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    fig, axes = plt.subplots(nrows=23)
    fig.subplots_adjust(top=0.98, bottom=0.02, left=0.25, right=0.99)
    for lut, ax in enumerate(axes, start=1):
        pos = list(ax.get_position().bounds)
        ax.set_axis_off()
        ax.imshow(gradient, aspect=4, cmap=rainbow_discrete(lut))
        fig.text(
            pos[0] - 0.01,
            pos[1] + pos[3] / 2.0,
            "rainbow_discrete, " + str(lut),
            va="center",
            ha="right",
            fontsize=10,
        )
    plt.show()


if __name__ == "__main__":
    main()
