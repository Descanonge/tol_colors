import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import RegularPolygon

from tol_colors import ColorsetDefinitions, get_colorset, tol_cmap


def main():
    # Show colorsets get_colorset(<scheme>).
    cset_names = ColorsetDefinitions.colorset_names
    fig, axes = plt.subplots(
        ncols=len(cset_names), figsize=(11, 3.5), layout="constrained", sharey=True
    )
    max_ncolors = max(len(get_colorset(n)) for n in cset_names)
    for ax, cset_name in zip(axes, cset_names, strict=False):
        cset = get_colorset(cset_name)
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
                orientation=45 / np.sqrt(2),
                ec=None,
                fc=color,
            )
            ax.add_artist(p)
            ax.annotate(name, xy=(1.1, 0.5), xycoords=p, ha="left", va="center")
        ax.set_xlim(-r, r)
        ax.set_ylim(0, max_ncolors + 1)
        ax.set_aspect("equal")
        ax.set_axis_off()
        ax.set_title(cset_name, weight="bold")
    plt.show()

    # Show colormaps tol_cmap(<scheme>).
    schemes = tol_cmap()
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    fig, axes = plt.subplots(nrows=len(schemes))
    fig.subplots_adjust(top=0.98, bottom=0.02, left=0.2, right=0.99)
    for ax, scheme in zip(axes, schemes, strict=False):
        pos = list(ax.get_position().bounds)
        ax.set_axis_off()
        ax.imshow(gradient, aspect=4, cmap=tol_cmap(scheme))
        fig.text(
            pos[0] - 0.01,
            pos[1] + pos[3] / 2.0,
            scheme,
            va="center",
            ha="right",
            fontsize=10,
        )
    plt.show()

    # Show colormaps tol_cmap('rainbow_discrete', <lut>).
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    fig, axes = plt.subplots(nrows=23)
    fig.subplots_adjust(top=0.98, bottom=0.02, left=0.25, right=0.99)
    for lut, ax in enumerate(axes, start=1):
        pos = list(ax.get_position().bounds)
        ax.set_axis_off()
        ax.imshow(gradient, aspect=4, cmap=tol_cmap("rainbow_discrete", lut))
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
