"""Build images for documentation."""

import matplotlib.pyplot as plt
import numpy as np
from colorspacious import cspace_convert
from matplotlib.colors import to_rgb
from matplotlib.patches import ConnectionPatch, RegularPolygon

import tol_colors as tc

plt.matplotlib.rcdefaults()
plt.rcParams["font.sans-serif"] = ["Noto Sans"]

savedir = "docs/source/img/"

## Colorsets


def cset_detailed(name: str):
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


def cset_dark():
    cset = tc.dark
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
            fc="w",
            ec="k",
            lw=0.5,
        )
        ax.add_artist(p)

        ax.annotate(
            f"{color}",
            xy=(0.5, 0.5),
            xycoords=p,
            xytext=(0, 2),
            textcoords="offset points",
            ha="center",
            va="bottom",
            color=color,
            size=10,
        )
        ax.annotate(
            f"{col_name}",
            xy=(0.5, 0.35),
            xycoords=p,
            ha="center",
            color=color,
            size=10 + (1 - len(col_name) / 10) * 2.5,
        )

        fig.savefig(savedir + "cset_dark.svg")
        plt.close(fig)


def land_cover():
    cset = tc.land_cover
    n_colors = len(cset)

    h_pad = 0.01
    v_pad = 0.01

    fig, ax = plt.subplots(figsize=(10, 2.2), layout="constrained", dpi=150)
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
            size=9,
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

        fig.savefig(savedir + "cset_land_cover.svg")
        plt.close(fig)


def csets_condensed():
    fig = plt.figure(figsize=(10, 8), dpi=100)
    margin = 0.10
    ax = fig.add_axes((margin, 0, 1 - margin, 1))

    sets = [
        "bright",
        "vibrant",
        "muted",
        "pale",
        "dark",
        "light",
        "high_contrast",
        "medium_contrast",
    ]
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
                lw=0.5 if col_name == "white" else 0.1,
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
                size=18 - len(col_name) * 0.8,
                style="italic",
            )
            if i_col == 0:
                ax.annotate(
                    cset_name,
                    xy=(0, 0.5),
                    xycoords=p,
                    xytext=(-5, 0),
                    textcoords="offset points",
                    ha="right",
                    va="center",
                    size=14,
                    weight="semibold",
                )

    ax.set_axis_off()
    ax.set_aspect("equal")
    ax.set_xlim(0, max_n_colors)
    ax.set_ylim(-n_sets * (1 + border), 0)

    fig.savefig(savedir + "csets_condensed.svg")
    plt.close(fig)


def csets_cvd():
    cvds_names = dict(deuteranomaly="Deuteranopia", protanomaly="Protanopia")

    fig, axes = plt.subplots(1, 2, figsize=(8, 3.5), layout="constrained", dpi=150)

    sets = [
        "bright",
        "vibrant",
        "muted",
        "pale",
        "dark",
        "light",
        "high_contrast",
        "medium_contrast",
    ]
    n_sets = len(sets)

    max_n_colors = max(len(tc.colorsets[name]) for name in sets)
    border = 0.1

    octs = dict(deuteranomaly=[], protanomaly=[])
    for ax, (cvd_type, cvd_name) in zip(axes, cvds_names.items(), strict=False):
        space = dict(name="sRGB1+CVD", cvd_type=cvd_type, severity=100)

        ax.set_axis_off()
        ax.set_aspect("equal")
        ax.set_xlim(0, max_n_colors)
        ax.set_ylim(-n_sets * (1 + border), 0)

        ax.annotate(
            cvd_name,
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
            octs[cvd_type].append([])
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
                    lw=0.5 if col_name == "white" else 0.1,
                )
                octs[cvd_type][-1].append(p)
                ax.add_artist(p)

    # leave space for center annotations
    fig.get_layout_engine().set(wspace=0.15)

    from matplotlib.transforms import ScaledTranslation, blended_transform_factory

    for i_set, cset_name in enumerate(sets):
        y = -i_set * (1 + border) - 0.5
        ann = axes[0].annotate(
            cset_name,
            xy=(0.5, y),
            xycoords=("figure fraction", "data"),
            ha="center",
            va="center_baseline",
            size=11,
        )
        ann.set_in_layout(False)
        if cset_name in ["muted", "medium_contrast"]:
            continue
        left_oct = octs["deuteranomaly"][i_set][-1]
        right_oct = octs["protanomaly"][i_set][0]
        offset = len(cset_name) / 2 * 7 / 72
        line = ConnectionPatch(
            xyA=[left_oct.xy[0] + 0.8, y],
            xyB=[0.5, y],
            coordsA=axes[0].transData,
            coordsB=blended_transform_factory(
                fig.transFigure + ScaledTranslation(-offset, 0, fig.dpi_scale_trans),
                axes[0].transData,
            ),
        )
        fig.add_artist(line)
        line = ConnectionPatch(
            xyA=[right_oct.xy[0] - 0.8, y],
            xyB=[0.5, y],
            coordsA=axes[1].transData,
            coordsB=blended_transform_factory(
                fig.transFigure + ScaledTranslation(offset, 0, fig.dpi_scale_trans),
                axes[1].transData,
            ),
        )
        fig.add_artist(line)

    fig.savefig(savedir + "csets_cvd.svg")
    plt.close(fig)


csets_cvd()

## Colormaps


def plot_linear(ax, cmap, vext, cspace=None):
    x = np.linspace(0, 1, 256)
    x = np.vstack((x, x))
    rgb = cmap(x)[..., :3]
    if cspace is not None:
        rgb = cspace_convert(rgb, cspace, "sRGB1")
        rgb = np.clip(rgb, 0, 1)
    ax.imshow(rgb, extent=(0, 1, *vext), transform=ax.transAxes)


def plot_discrete(ax, cmap, vext, cspace=None):
    width_rect = 1 / cmap.N
    for i, color in enumerate(cmap.colors):
        rgb = to_rgb(color)[:3]
        if cspace is not None:
            rgb = cspace_convert(rgb, cspace, "sRGB1")
            rgb = np.clip(rgb, 0, 1)
        rect = plt.Rectangle(
            (i * width_rect, vext[0]),
            width_rect,
            vext[1] - vext[0],
            fc=rgb,
            ec=rgb,
            lw=0.1,
            transform=ax.transAxes,
        )
        ax.add_artist(rect)


def cmap_detailed(name: str):
    cmap = tc.colormaps[name]
    has_discrete = f"{name}_discrete" in tc.colormaps

    aspect = 12
    width = 12 / 2.54
    height = width / (aspect / (1 + has_discrete))

    fig = plt.figure(figsize=(width, height), dpi=200)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_axis_off()

    if not has_discrete:
        plot_linear(ax, cmap, (0, 1))
    else:
        plot_linear(ax, cmap, (0.5, 1))
        plot_discrete(ax, tc.colormaps[f"{name}_discrete"], (0, 0.505))

    fig.savefig(savedir + f"cmap_{name}.svg")
    plt.close(fig)


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


def cmaps_condensed():
    cmaps_names = [
        ("sunset",),
        ("nightfall",),
        ("BuRd",),
        ("PRGn",),
        ("YlOrBr",),
        ("iridescent",),
        ("incandescent",),
        ("rainbow_WhBr", "rainbow_WhRd", "rainbow_PuRd", "rainbow_PuBr"),
        ("rainbow_discrete",),
    ]
    fig = plt.figure(figsize=(10, 11), dpi=100)
    fig.subplots_adjust(left=0.20, bottom=0.01, top=0.99, right=0.99)
    gs = plt.GridSpec(
        len(cmaps_names), 1, figure=fig, height_ratios=[2, 2, 2, 2, 2, 1, 1, 4, 1]
    )

    ann_kw = dict(
        xycoords="axes fraction",
        xytext=(-3, 0),
        textcoords="offset points",
        ha="right",
        va="center",
        family="monospace",
        size=12,
    )

    for i, cmap_names_gs in enumerate(cmaps_names):
        if len(cmap_names_gs) > 1:
            axes = gs[i].subgridspec(len(cmap_names_gs), 1, hspace=0.08).subplots()
        else:
            axes = [fig.add_subplot(gs[i])]

        for cmap_name, ax in zip(cmap_names_gs, axes, strict=False):
            ax.set_axis_off()

            if cmap_name == "rainbow_discrete":
                plot_discrete(ax, tc.rainbow_discrete(22), (0, 1))
                ax.annotate(cmap_name, (0, 0.5), **ann_kw)
                continue

            cmap = tc.colormaps[cmap_name]
            if (cmap_d_name := f"{cmap_name}_discrete") in tc.colormaps:
                cmap_d = tc.colormaps[cmap_d_name]
                plot_linear(ax, cmap, (0.5, 1))
                plot_discrete(ax, cmap_d, (0, 0.505))
                ax.annotate(cmap_name, (0, 0.75), **ann_kw)
                ax.annotate(cmap_d_name, (0, 0.25), **ann_kw)
            else:
                plot_linear(ax, cmap, (0, 1))
                ax.annotate(cmap_name, (0, 0.5), **ann_kw)

    fig.savefig(savedir + "cmaps_condensed.svg")
    plt.close(fig)


def cmaps_cvd():
    cmaps_names = [
        ("sunset",),
        ("nightfall",),
        ("BuRd",),
        ("PRGn",),
        ("YlOrBr",),
        ("iridescent",),
        ("incandescent",),
        ("rainbow_WhBr", "rainbow_WhRd", "rainbow_PuRd", "rainbow_PuBr"),
        ("rainbow_discrete",),
    ]
    fig = plt.figure(figsize=(8, 8), dpi=100)
    fig.subplots_adjust(left=0.01, bottom=0.01, top=0.95, right=0.99)
    gs = plt.GridSpec(
        len(cmaps_names),
        2,
        figure=fig,
        height_ratios=[2, 2, 2, 2, 2, 1, 1, 4, 1],
        wspace=0.31,
    )

    cvds_names = dict(deuteranomaly="Deuteranopia", protanomaly="Protanopia")
    cspaces = [
        dict(name="sRGB1+CVD", cvd_type=name, severity=100) for name in cvds_names
    ]

    ann_kw = dict(
        xycoords=("figure fraction", "axes fraction"), ha="center", va="center"
    )

    for i, cmap_names_gs in enumerate(cmaps_names):
        for lr, cspace in enumerate(cspaces):
            if len(cmap_names_gs) > 1:
                axes = (
                    gs[i, lr].subgridspec(len(cmap_names_gs), 1, hspace=0.08).subplots()
                )
            else:
                axes = [fig.add_subplot(gs[i, lr])]

            if i == 0:
                axes[0].set_title(cvds_names[cspace["cvd_type"]])

            for cmap_name, ax in zip(cmap_names_gs, axes, strict=False):
                ax.set_axis_off()

                if lr == 0:
                    ax.annotate(
                        cmap_name.removesuffix("_discrete"), (0.5, 0.5), **ann_kw
                    )

                if cmap_name == "rainbow_discrete":
                    plot_discrete(ax, tc.rainbow_discrete(22), (0, 1), cspace=cspace)
                    continue

                cmap = tc.colormaps[cmap_name]
                if (cmap_d_name := f"{cmap_name}_discrete") in tc.colormaps:
                    cmap_d = tc.colormaps[cmap_d_name]
                    plot_linear(ax, cmap, (0.5, 1), cspace=cspace)
                    plot_discrete(ax, cmap_d, (0, 0.505), cspace=cspace)

                else:
                    plot_linear(ax, cmap, (0, 1), cspace=cspace)

    fig.savefig(savedir + "cmaps_cvd.svg")
    plt.close(fig)


def icon():
    d = 1 / 3
    t = d / np.sqrt(3)

    def draw_oct(xy, color):
        p = RegularPolygon(
            xy,
            numVertices=6,
            radius=t,
            orientation=np.pi / 2,
            fc=color,
            ec=color,
            lw=0.1,
            transform=ax.transAxes,
        )
        ax.add_artist(p)
        return p

    fig = plt.figure(figsize=(0.64, 0.64), dpi=100)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_axis_off()
    ax.set_aspect("equal")
    cset = tc.bright

    draw_oct((0.5, 0.5), cset.grey)
    draw_oct((0.5, 5 / 6), cset.green)
    draw_oct((0.5, 1 / 6), cset.purple)
    draw_oct((0.5 + 3 * t / 2, 1 / 3), cset.red)
    draw_oct((0.5 - 3 * t / 2, 1 / 3), cset.blue)
    draw_oct((0.5 + 3 * t / 2, 2 / 3), cset.yellow)
    draw_oct((0.5 - 3 * t / 2, 2 / 3), cset.cyan)

    fig.savefig(savedir + "icon.svg", transparent=True)
    plt.close(fig)


if __name__ == "__main__":
    for name in tc.colorsets:
        cset_detailed(name)

    # special plot for dark
    cset_dark()
    # special plot for land cover
    land_cover()

    csets_condensed()
    csets_cvd()

    for name in [
        "sunset",
        "nightfall",
        "BuRd",
        "PRGn",
        "YlOrBr",
        "WhOrBr",
        "iridescent",
        "incandescent",
        "rainbow_WhBr",
        "rainbow_WhRd",
        "rainbow_PuBr",
        "rainbow_PuRd",
    ]:
        cmap_detailed(name)

    rainbow_discrete()
    cmaps_condensed()
    cmaps_cvd()
