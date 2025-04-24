"""Definitions and user functions.

Definition of colour schemes for lines and maps that also work for colour-blind
people. See https://personal.sron.nl/~pault/ for background information and
best usage of the schemes.

Copyright (c) 2019, Paul Tol
All rights reserved.

License:  Standard 3-clause BSD
"""

from __future__ import annotations

import json
import logging
from collections import namedtuple
from collections.abc import Sequence
from importlib import resources
from typing import NamedTuple

import matplotlib
from matplotlib.colors import Colormap, LinearSegmentedColormap, ListedColormap

__version__ = "1.4.0"

log = logging.getLogger(__name__)

# Load data
with resources.open_text("tol_colors", "colors.json") as fp:
    _colors = json.load(fp)


## Colorsets
# I also define statically the colorsets to preserve type-checking and auto-completion
# on the attributes of named tuples

colorsets: dict[str, NamedTuple] = {}
"""Mapping of colorsets."""

Bright = namedtuple("Bright", "blue, red, green, yellow, cyan, purple, grey")
bright = Bright(**_colors["colorsets"]["bright"])
colorsets["bright"] = bright

Vibrant = namedtuple("Vibrant", "orange, blue, cyan, magenta, red, teal, grey")
vibrant = Vibrant(**_colors["colorsets"]["vibrant"])
colorsets["vibrant"] = vibrant

Muted = namedtuple(
    "Muted",
    "rose, indigo, sand, green, cyan, wine, teal, olive, purple, pale_grey",
)
muted = Muted(**_colors["colorsets"]["muted"])
colorsets["muted"] = muted

HighContrast = namedtuple("HighContrast", "black, blue, yellow, red, white")
high_contrast = HighContrast(**_colors["colorsets"]["high_contrast"])
colorsets["high_contrast"] = high_contrast

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
medium_contrast = MediumContrast(**_colors["colorsets"]["medium_contrast"])
colorsets["medium_contrast"] = medium_contrast

Pale = namedtuple(
    "Pale",
    "pale_blue, pale_red, pale_green, pale_yellow, pale_cyan, pale_grey",
)
pale = Pale(**_colors["colorsets"]["pale"])
colorsets["pale"] = pale

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
light = Light(**_colors["colorsets"]["light"])
colorsets["light"] = light

Dark = namedtuple(
    "Dark",
    "dark_blue, dark_red, dark_green, dark_yellow, dark_cyan, dark_grey",
)
dark = Dark(**_colors["colorsets"]["dark"])
colorsets["dark"] = dark

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
land_cover = LandCover(**_colors["colorsets"]["land_cover"])
colorsets["land_cover"] = land_cover

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


colormaps: dict[str, Colormap] = {}
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


def __getattr__(key: str):
    # Add colormaps as module attributes
    if key in colormaps:
        return colormaps[key]

    # normal lookup
    raise AttributeError


def __dir__():
    # only show colorsets and colormaps in auto-completion
    attrs = []
    attrs += list(colorsets.keys())
    attrs += list(colormaps.keys())
    attrs.append("rainbow_discrete")
    attrs.sort()
    return attrs
