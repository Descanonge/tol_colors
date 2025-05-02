"""Definitions and user functions.

Copyright (c) 2019, Paul Tol, Clément Haëck
All rights reserved.
License:  Standard 3-clause BSD
Colorsets and colormaps designed by PT. Software initially written by PT. Software
expanded, packaged, and maintained by CH.
"""

# ruff: noqa: N815, N816

import functools
import json
import logging
import os
import warnings
from collections import namedtuple
from collections.abc import Sequence
from importlib import resources
from typing import Literal, NamedTuple, overload

import matplotlib
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

__version__ = "2.0.0"

log = logging.getLogger(__name__)

# Load data

with resources.files("tol_colors").joinpath("colors.json").open("r") as fp:
    _colors = json.load(fp)


## Colorsets
# Colorsets are defined statically to provide robust type-checking and auto-completion

Bright = namedtuple("Bright", "blue, red, green, yellow, cyan, purple, grey")
Vibrant = namedtuple("Vibrant", "orange, blue, cyan, magenta, red, teal, grey")
Muted = namedtuple(
    "Muted",
    "rose, indigo, sand, green, cyan, wine, teal, olive, purple, pale_grey",
)

HighContrast = namedtuple("HighContrast", "black, blue, red, yellow, white")
MediumContrast = namedtuple(
    "MediumContrast",
    [
        "white",
        "light_blue",
        "dark_blue",
        "light_yellow",
        "dark_yellow",
        "light_red",
        "dark_red",
        "black",
    ],
)

Pale = namedtuple(
    "Pale",
    "pale_blue, pale_red, pale_green, pale_yellow, pale_cyan, pale_grey",
)
Dark = namedtuple(
    "Dark",
    "dark_blue, dark_red, dark_green, dark_yellow, dark_cyan, dark_grey",
)
Light = namedtuple(
    "Light",
    [
        "light_blue",
        "orange",
        "light_yellow",
        "pink",
        "light_cyan",
        "mint",
        "pear",
        "olive",
        "pale_grey",
    ],
)

LandCover = namedtuple(
    "LandCover",
    [
        "water",  # 0
        "evergreen_needleleaf_forest",  # 1
        "evergreen_broadleaf_forest",  # 2
        "deciduous_needleleaf_forest",  # 3
        "deciduous_broadleaf_forest",  # 4
        "mixed_forest",  # 5
        "woodland",  # 6
        "wooded_grassland",  # 7
        "closed_shrubland",  # 8
        "open_shrubland",  # 9
        "grassland",  # 10
        "cropland",  # 11
        "bare_ground",  # 12
        "urban_and_built_up",  # 13
    ],
)

bright = Bright(**_colors["colorsets"]["bright"])
vibrant = Vibrant(**_colors["colorsets"]["vibrant"])
muted = Muted(**_colors["colorsets"]["muted"])
high_contrast = HighContrast(**_colors["colorsets"]["high_contrast"])
medium_contrast = MediumContrast(**_colors["colorsets"]["medium_contrast"])
pale = Pale(**_colors["colorsets"]["pale"])
dark = Dark(**_colors["colorsets"]["dark"])
light = Light(**_colors["colorsets"]["light"])
land_cover = LandCover(**_colors["colorsets"]["land_cover"])


class ColorsetMapping(dict[str, NamedTuple]):
    """Special mapping replacing hyphens by underscores when retrieving an item."""

    # Some overloading for static type-checking

    @overload
    def __getitem__(self, key: Literal["bright"]) -> Bright: ...

    @overload
    def __getitem__(self, key: Literal["vibrant"]) -> Vibrant: ...

    @overload
    def __getitem__(self, key: Literal["muted"]) -> Muted: ...

    @overload
    def __getitem__(
        self, key: Literal["high_contrast", "high-contrast"]
    ) -> HighContrast: ...

    @overload
    def __getitem__(
        self, key: Literal["medium_contrast", "medium-contrast"]
    ) -> MediumContrast: ...

    @overload
    def __getitem__(self, key: Literal["pale"]) -> Pale: ...

    @overload
    def __getitem__(self, key: Literal["dark"]) -> Dark: ...

    @overload
    def __getitem__(self, key: Literal["light"]) -> Light: ...

    @overload
    def __getitem__(self, key: Literal["land_cover", "land-cover"]) -> LandCover: ...

    @overload
    def __getitem__(self, key: str) -> NamedTuple: ...

    def __getitem__(self, key: str) -> NamedTuple:
        return super().__getitem__(key.replace("-", "_"))


colorsets = ColorsetMapping(
    bright=bright,
    vibrant=vibrant,
    muted=muted,
    high_contrast=high_contrast,
    medium_contrast=medium_contrast,
    pale=pale,
    dark=dark,
    light=light,
    land_cover=land_cover,
)
"""Mapping of colorsets."""


def set_default_colors(
    cset: str = "bright", fname: str | None = None, dry: bool = False
):
    """Modify matplotlibrc to set default colors to those of one of the colorsets.

    This will modify the colors used autmotically by matplotlib.
    This function will add a new line in a matplotlibrc file or stylesheet for the
    property "axes.prop_cycle". If a line setting a color cycler already exist in the
    file, it will be overwritten.

    This function can run without modifying the file and simply show the line to add
    by setting the *dry* parameter to True.

    Parameters
    ----------
    cset
        Name of the colorset to set as new default. Default is "bright".
    fname
        Name of the file to modify. It can be a matplotlibrc or stylesheet file (see the
        matplotlib documentation on `Customizing Matplotlib
        <https://matplotlib.org/stable/users/explain/customizing.html>`__).
        If left to None, it will default to:

        - ``$MPLCONFIGDIR`` if set, else
        - On Unix/Linux: ``$XDG_CONFIG_HOME/matplotlib/matplotlibrc`` if set, else
          ``$HOME/.config/matplotlib/matplotlibrc``
        - On other platforms ``$HOME/.matplotlib/matplotlibrc``

        It will create the file and leading directories if necessary.
    dry
        If set to True, the function will only print the new configuration line to
        stdout and will not modify any file. You can then copy-paste the line manually.
    """
    colors = [f"'{c[1:]}'" for c in colorsets[cset]]
    newline = f"axes.prop_cycle : cycler('color', [{', '.join(colors)}])\n"
    print(f"New config line: {newline}", end="")

    if dry:
        return

    if fname is None:
        fname = os.path.join(matplotlib.get_configdir(), "matplotlibrc")
    print(f"Injecting line in file '{fname}'")

    base_dir = os.path.dirname(fname)
    if not os.path.exists(base_dir):
        os.makedirs(base_dir, exist_ok=True)

    if os.path.exists(fname):
        # check if cycler for color already exists in file
        with open(fname) as fp:
            lines = fp.readlines()

        has_line = False
        line_idx = 0
        for i, line in enumerate(lines):
            if line.startswith("axes.prop") and (
                "cycler('color')" or 'cycler("color")' in line
            ):
                has_line = True
                line_idx = i
                break

        if has_line:
            lines[line_idx] = newline
        else:
            lines.append(newline)
    else:
        lines = [newline]

    with open(fname, "w") as fp:
        fp.writelines(lines)


## Colormaps


def _make_linear_cmap(
    name: str, colors: Sequence[str], bad: str
) -> LinearSegmentedColormap:
    cmap = LinearSegmentedColormap.from_list(name, colors)
    cmap.set_bad(bad)
    return cmap


def _make_discrete_cmap(name: str, colors: Sequence[str], bad: str) -> ListedColormap:
    cmap = ListedColormap(colors, name=name)
    cmap.set_bad(bad)
    return cmap


class ColormapMapping(dict[str, LinearSegmentedColormap | ListedColormap]):
    """Mapping type to have better type checking."""

    @overload
    def __getitem__(
        self,
        key: Literal[
            "sunset", "sunset_r", "BuRd", "BuRd_r", "PRGn", "PRGn_r",
            "YlOrBr", "YlOrBr_r", "WhOrBr", "WhOrBr_r",
            "iridescent", "iridescent_r",
            "rainbow_WhBr", "rainbow_WhBr_r", "rainbow", "rainbow_r",
            "rainbow_WhRd", "rainbow_WhRd_r",
            "rainbow_PuRd", "rainbow_PuRd_r",
            "rainbow_PuBr", "rainbow_PuBr_r",
        ],
    ) -> LinearSegmentedColormap:  # fmt: skip
        ...

    @overload
    def __getitem__(
        self,
        key: Literal[
            "sunset_discrete", "sunset_discrete_r",
            "BuRd_discrete", "BuRd_discrete_r",
            "PRGn_discrete", "PRGn_discrete_r",
            "YlOrBr_discrete", "YlOrBr_discrete_r",
            "WhOrBr_discrete", "WhOrBr_discrete_r",
        ],
    ) -> ListedColormap:  # fmt: skip
        ...

    @overload
    def __getitem__(self, key: str) -> LinearSegmentedColormap | ListedColormap: ...

    def __getitem__(self, key: str) -> LinearSegmentedColormap | ListedColormap:
        return super().__getitem__(key)


colormaps = ColormapMapping()
"""Mapping of colormaps."""

# Standard colormaps
for name, data in _colors["colormaps"].items():
    colormaps[name] = _make_linear_cmap(name, data["colors"], data["bad"])
    if data["discrete"]:
        dname = f"{name}_discrete"
        colormaps[dname] = _make_discrete_cmap(dname, data["colors"], data["bad"])

# Linear rainbow colormaps
_rainbow_lin = _colors["rainbow_linear"]
colormaps["rainbow_WhBr"] = _make_linear_cmap(
    "rainbow", _rainbow_lin["colors"], _rainbow_lin["bad_Wh"]
)
colormaps["rainbow_WhRd"] = _make_linear_cmap(
    "rainbow_WhRd",
    _rainbow_lin["colors"][: _rainbow_lin["Rd_index"]],
    _rainbow_lin["bad_Wh"],
)
colormaps["rainbow_PuBr"] = _make_linear_cmap(
    "rainbow_PuBr",
    _rainbow_lin["colors"][_rainbow_lin["Pu_index"] :],
    _rainbow_lin["bad_Pu"],
)
colormaps["rainbow_PuRd"] = _make_linear_cmap(
    "rainbow_PuRd",
    _rainbow_lin["colors"][_rainbow_lin["Pu_index"] : _rainbow_lin["Rd_index"]],
    _rainbow_lin["bad_Pu"],
)

# Reverse colormaps
colormaps.update({f"{name}_r": cmap.reversed() for name, cmap in colormaps.items()})

# Aliases
colormaps["rainbow"] = colormaps["rainbow_WhBr"]
colormaps["rainbow_r"] = colormaps["rainbow_WhBr_r"]

# Register all colormaps in matplotlib
for name, cmap in colormaps.items():
    matplotlib.colormaps.register(cmap, name=f"tol.{name}")


def rainbow_discrete(n_colors: int = 22) -> ListedColormap:
    """Discrete rainbow colormaps.

    The number of colors can vary between 1 and 23 (included).
    """
    max_n_colors = 23
    if n_colors < 1:
        raise ValueError("Number of colors must be at least greater than one.")
    if n_colors > max_n_colors:
        raise ValueError("Number of colors cannot be greater than 23.")

    data = _colors["rainbow_discrete"]
    colors = data["colors"]
    indexes = data["indexes"]

    bad = data["bad_max"] if n_colors == max_n_colors else data["bad"]

    cmap = _make_discrete_cmap(
        "rainbow_discrete", [colors[i] for i in indexes[n_colors - 1]], bad
    )
    return cmap


# Add colormaps as module attributes
locals().update(colormaps)


def __dir__():
    # only show colorsets and colormaps in auto-completion
    attrs = []
    attrs += list(colorsets.keys())
    attrs += list(colormaps.keys())
    attrs.append("rainbow_discrete")
    attrs.append("set_default_colors")
    attrs.sort()
    return attrs


# Static type-checking
sunset: LinearSegmentedColormap
sunset_r: LinearSegmentedColormap
sunset_discrete: ListedColormap
sunset_discrete_r: ListedColormap

BuRd: LinearSegmentedColormap
BuRd_r: LinearSegmentedColormap
BuRd_discrete: ListedColormap
BuRd_discrete_r: ListedColormap

PRGn: LinearSegmentedColormap
PRGn_r: LinearSegmentedColormap
PRGn_discrete: ListedColormap
PRGn_discrete_r: ListedColormap

YlOrBr: LinearSegmentedColormap
YlOrBr_r: LinearSegmentedColormap
YlOrBr_discrete: ListedColormap
YlOrBr_discrete_r: ListedColormap

WhOrBr: LinearSegmentedColormap
WhOrBr_r: LinearSegmentedColormap
WhOrBr_discrete: ListedColormap
WhOrBr_discrete_r: ListedColormap

iridescent: LinearSegmentedColormap
iridescent_r: LinearSegmentedColormap

rainbow_WhBr: LinearSegmentedColormap
rainbow_WhBr_r: LinearSegmentedColormap
rainbow_WhRd: LinearSegmentedColormap
rainbow_WhRd_r: LinearSegmentedColormap
rainbow_PuRd: LinearSegmentedColormap
rainbow_PuRd_r: LinearSegmentedColormap
rainbow_PuBr: LinearSegmentedColormap
rainbow_PuBr_r: LinearSegmentedColormap
rainbow: LinearSegmentedColormap
rainbow_r: LinearSegmentedColormap


## Legacy API


def deprecated(replacements: list[str], version: str):  # noqa: D103
    replacements_ = ", ".join([f"tol_colors.{r}" for r in replacements])

    def decorator(func):
        name = func.__name__

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            warnings.warn(
                f"{name} is soft-deprecated since {version}, "
                f"please use {replacements_} instead",
                DeprecationWarning,
                stacklevel=2,
            )
            return func(*args, **kwargs)

        return wrapped

    return decorator


@deprecated(["colorsets"], "2.0")
def get_colorset(name: str = "bright"):
    """Return discrete colorsets for qualitative data.

    ..  deprecated:: 2.0
        This function is soft-deprecated, please use :data:`colorsets` instead.

    Parameters
    ----------
    name
        Name of the color set. Hyphens are automatically replaced, so "hight-contrast"
        works as well.
    """
    return colorsets[name]


@deprecated(["colorsets"], "2.0")
def tol_cset(colorset=None):
    """Return discrete color sets for qualitative data.

    ..  deprecated:: 2.0
        This function is soft-deprecated, please use :data:`colorsets` instead.

    Parameters
    ----------
    colorset: str
        Name of the color set. Hyphens are automatically replaced. If None return the
        list of possible sets. If not in defined sets, will default to 'bright'.
    """
    namelist = list(colorsets.keys())
    if colorset is None:
        return namelist
    if colorset not in namelist:
        colorset = "bright"
        log.warning(
            "Requested colorset not defined, using '%s'. " "Known colorsets are %s.",
            colorset,
            namelist,
        )
    return get_colorset(colorset)


@deprecated(["colormaps", "rainbow_discrete"], "2.0")
def get_colormap(
    name: str, n_colors: int = 22
) -> LinearSegmentedColormap | ListedColormap:
    """Return continuous and discrete colormaps for ordered data.

    .. deprecated:: 2.0
       This function is soft-deprecated, please use :data:`colorsets` or
       :func:`rainbow_discrete` instead.

    Parameters
    ----------
    name
        Name of the colormap. Hyphens are automatically replaced.
    n_colors
        Only used for "rainbow_discrete": number of discrete colors to use.
    """
    if name.replace("-", "_") == "rainbow_discrete":
        if n_colors < 1 or n_colors > 23:
            log.warning(
                "Number of colors should be between 1 and 23, using default (22)."
            )
            n_colors = 22
        return rainbow_discrete(n_colors)
    return colormaps[name]


@deprecated(["colormaps", "rainbow_discrete"], "2.0")
def tol_cmap(
    colormap: str | None = None, lut: int = 22
) -> LinearSegmentedColormap | ListedColormap | list[str]:
    """Return continuous and discrete colormaps for ordered data.

    .. deprecated:: 2.0
       This function is soft-deprecated, please use :data:`colorsets` or
       :func:`rainbow_discrete` instead.

    Parameters
    ----------
    name
        Name of the colormap. Hyphens are automatically replaced. If None return a list
        available colormaps. If not in defined maps, will default to 'rainbow_PuRd'.
    lut
        Only used for "rainbow_discrete": number of discrete colors to use.
    """
    cmaps_name = list(colormaps.keys()) + ["rainbow_discrete"]
    if colormap is None:
        return cmaps_name
    if colormap not in cmaps_name:
        colormap = "rainbow_PuRd"
        log.warning(
            "Requested colormap not defined, using '%s'. " "Known colormaps are %s.",
            colormap,
            cmaps_name,
        )
    return get_colormap(colormap, lut)
