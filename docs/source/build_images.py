"""Build images for documentation."""

import matplotlib.pyplot as plt
import numpy as np
from colorspacious import cspace_convert
from matplotlib.colors import to_rgb
from matplotlib.patches import RegularPolygon

import tol_colors as tc

savedir = "docs/source/img/"

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

        text_col = (
            "w"
            if name == "dark" or col_name in ["black", "indigo", "blue", "dark_blue"]
            else "k"
        )
        ax.annotate(
            f"{color}",
            xy=(0.5, 0.5),
            xycoords=p,
            xytext=(0, 2),
            textcoords="offset points",
            ha="center",
            va="bottom",
            color=text_col,
            size=10,
        )
        ax.annotate(
            f"{col_name}",
            xy=(0.5, 0.35),
            xycoords=p,
            ha="center",
            color=text_col,
            size=10 + (1 - len(col_name) / 10) * 2.5,
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

        fig.savefig(savedir + f"cset_{name}.svg")
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

        fig.savefig(savedir + f"cset_{name}.svg")
        plt.close(fig)


def condensed_csets():
    fig = plt.figure(figsize=(6, 3.75), dpi=150)
    margin = 0.1
    ax = fig.add_axes((margin, 0, 1 - margin, 1))

    sets = ["bright", "vibrant", "muted", "light", "high_contrast", "medium_contrast"]
    n_sets = len(sets)

    max_n_colors = max(len(tc.colorsets[name]) for name in sets)
    border = 0.1

    for i_set, cset_name in enumerate(sets):
        cset = tc.colorsets[cset_name]
        x_left = (max_n_colors / 2) - len(cset) / 2
        for i_col, (col_name, color) in enumerate(
            zip(cset._fields, cset, strict=False)
        ):
            p = RegularPolygon(
                (x_left + i_col + 0.5, -i_set * (1 + border) - 0.5),
                numVertices=8,
                radius=1.307 / (1 + np.sqrt(2)),
                orientation=np.pi / 360 * 45,
                fc=color,
                ec="k" if col_name == "white" else color,
                lw=0.1,
            )
            ax.add_artist(p)
            text_col = (
                "w"
                if cset_name == "dark"
                or col_name in ["black", "indigo", "blue", "dark_blue"]
                else "k"
            )
            ax.annotate(
                col_name,
                xy=(0.5, 0.5),
                xycoords=p,
                ha="center",
                va="center",
                color=text_col,
                size=7 + (1 - len(col_name) / 10) * 2.5,
            )
            if i_col == 0:
                ax.annotate(
                    cset_name,
                    xy=(0, 0.5),
                    xycoords=p,
                    xytext=(-3, 0),
                    textcoords="offset points",
                    ha="right",
                    va="center",
                    size=9,
                )

    ax.set_axis_off()
    ax.set_aspect("equal")
    ax.set_xlim(0, max_n_colors)
    ax.set_ylim(-n_sets * (1 + border), 0)

    fig.savefig(savedir + "cset_condensed.svg")
    plt.close(fig)


def colorsets_cvd():
    spaces = ["deuteranomaly", "protanomaly"]

    fig, axes = plt.subplots(1, 2, figsize=(8, 2.7), layout="constrained", dpi=150)

    sets = ["bright", "vibrant", "muted", "light", "high_contrast", "medium_contrast"]
    n_sets = len(sets)

    max_n_colors = max(len(tc.colorsets[name]) for name in sets)
    border = 0.1

    for i_ax, (ax, space_name) in enumerate(zip(axes, spaces, strict=False)):
        space = dict(name="sRGB1+CVD", cvd_type=space_name, severity=100)

        ax.set_axis_off()
        ax.set_aspect("equal")
        ax.set_xlim(0, max_n_colors)
        ax.set_ylim(-n_sets * (1 + border), 0)

        ax.annotate(
            space_name.capitalize(),
            xy=(0.5, 1),
            xycoords="axes fraction",
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
            size=12,
        )

        for i_set, cset_name in enumerate(sets):
            cset = tc.colorsets[cset_name]
            x_left = (max_n_colors / 2) - len(cset) / 2
            for i_col, (col_name, color) in enumerate(
                zip(cset._fields, cset, strict=False)
            ):
                rgb = to_rgb(color)
                rgb = cspace_convert(rgb, space, "sRGB1")
                rgb = np.clip(rgb, 0, 1)
                p = RegularPolygon(
                    (x_left + i_col + 0.5, -i_set * (1 + border) - 0.5),
                    numVertices=8,
                    radius=1.307 / (1 + np.sqrt(2)),
                    orientation=np.pi / 360 * 45,
                    fc=rgb,
                    ec="k" if col_name == "white" else rgb,
                    lw=0.1,
                )
                ax.add_artist(p)

    # leave space for center annotations
    fig.get_layout_engine().set(wspace=0.15)

    for i_set, cset_name in enumerate(sets):
        ann = axes[0].annotate(
            cset_name,
            xy=(0.5, -i_set * (1 + border) - 0.5),
            xycoords=("figure fraction", "data"),
            ha="center",
            va="center",
            size=11,
        )
        ann.set_in_layout(False)

    fig.savefig(savedir + "cset_cvd.svg")
    plt.close(fig)


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

    fig.savefig(savedir + f"cmap_{name}.svg")
    plt.close(fig)


## discrete rainbow


def rainbow_discrete():
    fig = plt.figure(figsize=(6.1, 6), dpi=150)
    ax = fig.add_axes((0, 0, 1, 1))

    for n_col in range(1, 24):
        cmap = tc.rainbow_discrete(n_col)

        for i_col, color in enumerate(cmap.colors):
            h = RegularPolygon(
                (i_col - n_col / 2, -n_col),
                numVertices=6,
                radius=np.sqrt(3) / 3,
                fc=color,
                ec=color,
                lw=0.1,
            )
            ax.add_artist(h)

            if i_col == 0:
                ax.annotate(
                    str(n_col),
                    xy=(0, 0.5),
                    xycoords=h,
                    xytext=(-5, 0),
                    textcoords="offset points",
                    ha="right",
                    va="center",
                    size=9,
                )

    ax.set_axis_off()
    ax.set_aspect("equal")
    ax.set_xlim(-13.5, 11.2)
    ax.set_ylim(-24, -0.2)

    fig.savefig(savedir + "cmap_rainbow_discrete.svg")
    plt.close(fig)


if __name__ == "__main__":
    for name in tc.colorsets:
        detailed_colorset(name)

    # special plot for land cover
    land_cover()

    condensed_csets()
    colorsets_cvd()

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

    rainbow_discrete()
