"""Build images for documentation."""

import matplotlib.pyplot as plt
import numpy as np
from colorspacious import cspace_convert
from matplotlib.colors import to_rgb
from matplotlib.patches import RegularPolygon

import tol_colors as tc

## Colorsets


def detailed_colorset(name: str):
    cset = tc.colorsets[name]
    n_colors = len(cset)

    height = 1.0
    width = 1.0 * (n_colors - 1)

    h_pad = 0.01
    v_pad = h_pad / (n_colors - 2)  # approximately the plot aspect

    fig = plt.figure(figsize=(width, height), dpi=200)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_xlim(0 - h_pad, n_colors + h_pad)
    ax.set_ylim(-0.5 - v_pad, 0.5 + v_pad)
    ax.set_aspect("equal")
    ax.set_axis_off()

    names = cset._fields
    colors = list(cset)
    for i, (col_name, color) in enumerate(zip(names, colors, strict=True)):
        # octogon side
        a = 1.0 / (1 + np.sqrt(2))
        # outer radius
        r = 1.307 * a
        p = RegularPolygon(
            (i + 0.5, 0.0),
            numVertices=8,
            radius=r,
            orientation=np.pi / 360 * 45,
            fc=color,
            ec="k" if col_name == "white" else color,
            lw=0.5 if col_name == "white" else 0.1,
        )
        ax.add_artist(p)

        text_col = "w" if name == "dark" or col_name in ["black", "indigo"] else "k"
        ax.annotate(
            f"{color}\n{col_name}",
            xy=(0.5, 0.5),
            xycoords=p,
            ha="center",
            va="center",
            color=text_col,
            size=10,
        )

        if name.endswith("contrast"):
            r_height = 0.2
            luminance = cspace_convert(to_rgb(color), "sRGB1", "JCh")[0]
            gray_col = f"{luminance/100:f}"
            r = plt.Rectangle(
                (i, -0.5 - r_height),
                1,
                r_height,
                fc=gray_col,
                ec="k" if col_name == "white" else gray_col,
                lw=0.5,
            )
            ax.add_artist(r)
            ax.set_ylim(-0.5 - r_height - v_pad, 0.5 + v_pad)

        fig.savefig(f"docs/source/img/cset_{name}.svg")
        plt.close(fig)


def land_cover():
    cset = tc.land_cover
    n_colors = len(cset)

    h_pad = 0.01
    v_pad = 0.01

    fig, ax = plt.subplots(figsize=(10, 2.1), layout="constrained", dpi=150)
    # ax = fig.add_axes((0, 0, 1, 1))
    ax.set_xlim(0 - h_pad, n_colors + h_pad)
    ax.set_ylim(-0.5 - v_pad, 0.5 + v_pad)
    ax.set_aspect("equal")
    ax.set_axis_off()

    names = cset._fields
    colors = list(cset)
    for i, (col_name, color) in enumerate(zip(names, colors, strict=True)):
        # octogon side
        a = 1.0 / (1 + np.sqrt(2))
        # outer radius
        r = 1.307 * a
        p = RegularPolygon(
            (i + 0.5, 0.0),
            numVertices=8,
            radius=r,
            orientation=np.pi / 360 * 45,
            fc=color,
            ec="k",
            lw=0.5,
        )
        ax.add_artist(p)

        ax.annotate(
            color,
            xy=(0.5, 0.5),
            xycoords=p,
            ha="center",
            va="center",
            size=10,
        )

        ax.annotate(
            col_name,
            xy=(0.5, 0.0),
            xycoords=p,
            xytext=(0, -3),
            textcoords="offset points",
            rotation=45,
            rotation_mode="anchor",
            ha="right",
            va="top",
            clip_on=False,
        )

        fig.savefig(f"docs/source/img/cset_{name}.svg")
        plt.close(fig)


for name in tc.colorsets:
    detailed_colorset(name)

# special plot for land cover
land_cover()

## Colormaps


def detailed_cmap(name: str):
    cmap = tc.colormaps[name]
    has_discrete = f"{name}_discrete" in tc.colormaps

    aspect = 12
    width = 12 / 2.54
    height = width / (aspect / (1 + has_discrete))

    fig = plt.figure(figsize=(width, height), dpi=200)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_axis_off()

    x = np.linspace(0, 1, 256)
    x = np.vstack((x, x))

    if not has_discrete:
        ax.imshow(x, extent=(0, 1, 0, 1), cmap=cmap, transform=ax.transAxes)
    else:
        ax.imshow(x, extent=(0, 1, 0.5, 1), cmap=cmap, transform=ax.transAxes)

        cmap_d = tc.colormaps[f"{name}_discrete"]
        width_rect = 1 / cmap_d.N
        for i, color in enumerate(cmap_d.colors):
            rect = plt.Rectangle(
                (i * width_rect, 0.0),
                width_rect,
                0.5,
                fc=color,
                ec=color,
                lw=0.1,
                transform=ax.transAxes,
            )
            ax.add_artist(rect)

    fig.savefig(f"docs/source/img/cmap_{name}.svg")
    plt.close(fig)


for name in [
    "sunset",
    "BuRd",
    "PRGn",
    "YlOrBr",
    "WhOrBr",
    "iridescent",
    "rainbow_WhBr",
    "rainbow_WhRd",
    "rainbow_PuBr",
    "rainbow_PuRd",
]:
    detailed_cmap(name)
