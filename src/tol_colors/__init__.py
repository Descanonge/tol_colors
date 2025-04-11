"""Definitions and user functions.

Definition of colour schemes for lines and maps that also work for colour-blind
people. See https://personal.sron.nl/~pault/ for background information and
best usage of the schemes.

Copyright (c) 2019, Paul Tol
All rights reserved.

License:  Standard 3-clause BSD
"""

import logging
from collections import namedtuple
from collections.abc import Sequence
from typing import Any, Literal, NamedTuple, overload

import numpy as np
from matplotlib.colors import LinearSegmentedColormap, to_rgba_array

__version__ = "1.4.0"


log = logging.getLogger(__name__)


class ColorsetDefinitions:
    """Definitions of the colorsets.

    Each colorset has a class method to its name which return a corresponding
    named-tuple. The named-tuple class is defined as a class attribute.

    NamedTuples are defined as class attributes. Corresponding class methods return
    an instance with colors set as literal arguments. We avoid any mutability issue.

    Named tuples are given in the order suggested by the technical notes.
    For high-contrast, black and white are put first and last, respectively. That should
    make an easy conversion to grayscale.
    """

    colorset_names = [
        "bright",
        "muted",
        "vibrant",
        "high_contrast",
        "medium_contrast",
        "pale",
        "light",
        "dark",
        "land_cover",
    ]
    """List of available colorset. Must correspond to method names."""

    Bright = namedtuple("Bright", "blue, red, green, yellow, cyan, purple, grey")

    @classmethod
    def bright(cls) -> Bright:
        """Define "bright", the main scheme for lines and their labels."""
        return cls.Bright(
            blue="#4477AA",
            red="#EE6677",
            green="#228833",
            yellow="#CCBB44",
            cyan="#66CCEE",
            purple="#AA3377",
            grey="#BBBBBB",
        )

    Muted = namedtuple(
        "Muted",
        "rose, indigo, sand, green, cyan, wine, teal, olive, purple, pale_grey",
    )

    @classmethod
    def muted(cls) -> Muted:
        """Define the "muted" qualitative colour scheme.

        It is equally colour-blind safe with more colours, but lacking a clear red or
        medium blue. Pale grey is meant for bad data in maps.
        """
        return cls.Muted(
            rose="#CC6677",
            indigo="#332288",
            sand="#DDCC77",
            green="#117733",
            cyan="#88CCEE",
            wine="#882255",
            teal="#44AA99",
            olive="#999933",
            purple="#AA4499",
            pale_grey="#DDDDDD",
        )

    Vibrant = namedtuple("Vibrant", "orange, blue, cyan, magenta, red, teal, grey")

    @classmethod
    def vibrant(cls) -> Vibrant:
        """Define the "vibrant" qualitative colour scheme.

        It is equally colour-blind safe. It has been designed for data visualization
        framework TensorBoard, built around their signature orange ``FF7043``. That
        colour has been replaced here to make it print-friendly.
        """
        return cls.Vibrant(
            orange="#EE7733",
            blue="#0077BB",
            cyan="#33BBEE",
            magenta="#EE3377",
            red="#CC3311",
            teal="#009988",
            grey="#BBBBBB",
        )

    HighContrast = namedtuple("HighContrast", "black, blue, yellow, red, white")

    @classmethod
    def high_contrast(cls) -> HighContrast:
        """Define the "high-contrast" qualitative colour scheme.

        It is colour-blind safe and optimized for contrast. This scheme also works well
        for people with monochrome vision and in a monochrome printout.
        """
        return cls.HighContrast(
            black="#000000",
            blue="#004488",
            yellow="#DDAA33",
            red="#BB5566",
            white="#FFFFFF",
        )

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

    @classmethod
    def medium_contrast(cls) -> MediumContrast:
        """Define the "medium-contrast" qualitative colour scheme.

        It is colour-blind safe with more colours. It is also optimized for contrast to
        work in a monochrome printout, but the differences are inevitably smaller. It is
        designed for situations needing colour pairs
        """
        return cls.MediumContrast(
            light_blue="#6699CC",
            dark_blue="#004488",
            light_yellow="#EECC66",
            dark_yellow="#997700",
            light_red="#EE99AA",
            dark_red="#994455",
            white="#FFFFFF",
            black="#000000",
        )

    Pale = namedtuple(
        "Pale",
        "pale_blue, pale_red, pale_green, pale_yellow, pale_cyan, pale_grey",
    )

    @classmethod
    def pale(cls) -> Pale:
        """Define the "pale" qualitative colour scheme.

        The colours are not very distinct in either normal or colour-blind vision; they
        are not meant for lines or maps, but for marking text. Use the pale colours for
        the background of black text, for example to highlight cells in a table. One of
        the dark colours can be chosen for text itself on a white background, for
        example when a large block of text has to be marked. In both cases, the text
        remains easily readable.
        """
        return cls.Pale(
            pale_blue="#BBCCEE",
            pale_red="#FFCCCC",
            pale_green="#CCDDAA",
            pale_yellow="#EEEEBB",
            pale_cyan="#CCEEFF",
            pale_grey="#DDDDDD",
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

    @classmethod
    def light(cls) -> Light:
        """Define the "light" qualitative colour scheme.

        It was designed to fill labelled cells with more and lighter colours than
        contained in the bright scheme, using more distinct colours than that in the
        pale scheme, but keeping black labels clearly readable. However, it can also be
        used for general qualitative maps.
        """
        return cls.Light(
            light_blue="#77AADD",
            orange="#EE8866",
            light_yellow="#EEDD88",
            pink="#FFAABB",
            light_cyan="#99DDFF",
            mint="#44BB99",
            pear="#BBCC33",
            olive="#AAAA00",
            pale_grey="#DDDDDD",
        )

    Dark = namedtuple(
        "Dark",
        "dark_blue, dark_red, dark_green, dark_yellow, dark_cyan, dark_grey",
    )

    @classmethod
    def dark(cls) -> Dark:
        """Define the "dark" qualitative colour scheme.

        The colours are not very distinct in either normal or colour-blind vision; they
        are not meant for lines or maps, but for marking text. Use the pale colours for
        the background of black text, for example to highlight cells in a table. One of
        the dark colours can be chosen for text itself on a white background, for
        example when a large block of text has to be marked. In both cases, the text
        remains easily readable.
        """
        return cls.Dark(
            dark_blue="#222255",
            dark_red="#663333",
            dark_green="#225522",
            dark_yellow="#666633",
            dark_cyan="#225555",
            dark_grey="#555555",
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

    @classmethod
    def land_cover(cls) -> LandCover:
        """Define the "land-cover" qualitative color-scheme.

        For the global land cover classification, as generated by the University of
        Maryland Department of Geography from AVHRR data acquired between 1981 and 1994.
        There is a recommended colour scheme, but the colours are not distinct, some not
        even in normal vision. This gives a more subtle and logical scheme where all
        colours are distinct in all visions.
        """
        return cls.LandCover(
            water="#5566AA",
            evergreen_needleleaf_forest="#117733",
            deciduous_needleleaf_forest="#44AA66",
            mixed_forest="#55AA22",
            evergreen_broadleaf_forest="#668822",
            deciduous_broadleaf_forest="#99BB55",
            woodland="#558877",
            wooded_grassland="#88BBAA",
            grassland="#AADDCC",
            cropland="#44AA88",
            closed_shrubland="#DDCC66",
            open_shrubland="#FFDD44",
            bare_ground="#FFEE88",
            urban_and_built_up="#BB0011",
        )

    @classmethod
    def build_colorset(cls, name: str) -> tuple[Any]:
        """Return one of the colorset named-tuple."""
        name = name.replace("-", "_")
        if name not in cls.colorset_names:
            raise KeyError(
                f"Unknown colorset '{name}', the "
                f"defined colorsets are {cls.colorset_names}"
            )
        return getattr(cls, name)()


@overload
def get_colorset(name: Literal["bright"]) -> ColorsetDefinitions.Bright: ...


@overload
def get_colorset(name: Literal["muted"]) -> ColorsetDefinitions.Muted: ...


@overload
def get_colorset(name: Literal["vibrant"]) -> ColorsetDefinitions.Vibrant: ...


@overload
def get_colorset(
    name: Literal["high_contrast", "high-contrast"],
) -> ColorsetDefinitions.HighContrast: ...


@overload
def get_colorset(
    name: Literal["medium_contrast", "medium-contrast"],
) -> ColorsetDefinitions.MediumContrast: ...


@overload
def get_colorset(name: Literal["pale"]) -> ColorsetDefinitions.Pale: ...


@overload
def get_colorset(name: Literal["dark"]) -> ColorsetDefinitions.Dark: ...


@overload
def get_colorset(name: Literal["light"]) -> ColorsetDefinitions.Light: ...


@overload
def get_colorset(name: str) -> NamedTuple: ...


def get_colorset(
    name: str = "bright",
) -> (
    tuple[Any]
    | ColorsetDefinitions.Bright
    | ColorsetDefinitions.Muted
    | ColorsetDefinitions.Vibrant
    | ColorsetDefinitions.HighContrast
    | ColorsetDefinitions.MediumContrast
    | ColorsetDefinitions.Pale
    | ColorsetDefinitions.Dark
    | ColorsetDefinitions.Light
):
    """Return discrete colorsets for qualitative data.

    The colorset is returned as a named-tuple instance containing the colors in hex
    format.

    - cset.red and cset[1] give the same color (in default 'bright' colorset)
    - cset._fields gives a tuple with all color names
    - list(cset) gives a list with all colors

    Parameters
    ----------
    name
        Name of the color set. It must be one of "bright", "muted", "vibrant",
        "high_contrast", "medium_contrast", "pale", "dark", or "light". Hyphens are
        automatically replaced, so "hight-contrast" works as well.
    """
    return ColorsetDefinitions.build_colorset(name)


def tol_cset(colorset=None):
    """Discrete color sets for qualitative data.

    Define a namedtuple instance with the colors.
    Examples for: cset = tol_cset("<scheme>")
      - cset.red and cset[1] give the same color (in default 'bright' colorset)
      - cset._fields gives a tuple with all color names
      - list(cset) gives a list with all colors

    Parameters
    ----------
    colorset: str
        Name of the color set. If None return the list of possible sets.
        If not in defined sets, will default to 'bright'.
    """
    namelist = ColorsetDefinitions.colorset_names
    if colorset is None:
        return namelist
    if colorset not in namelist:
        colorset = "bright"
        logging.warning(
            "Requested colorset not defined, using '%s'. " "Known colorsets are %s.",
            colorset,
            namelist,
        )
    return get_colorset(colorset)


def _discretemap(colormap: str, hex_colors: Sequence[str]) -> LinearSegmentedColormap:
    """Produce a colormap from a list of discrete colors without interpolation."""
    colors = to_rgba_array(hex_colors)
    colors = np.vstack([colors[0], colors, colors[-1]])
    cdict = {}
    for ki, key in enumerate(("red", "green", "blue")):
        cdict[key] = [
            (i / (len(colors) - 2.0), colors[i, ki], colors[i + 1, ki])
            for i in range(len(colors) - 1)
        ]
    return LinearSegmentedColormap(colormap, cdict)  # type: ignore[arg-type]


class ColormapDefinitions:
    """Class TOLcmaps definition."""

    colormap_names: list[str] = [
        "sunset",
        "sunset_discrete",
        "BuRd",
        "BuRd_discrete",
        "PRGn",
        "PRGn_discrete",
        "YlOrBr",
        "YlOrBr_discrete",
        "WhOrBr",
        "iridescent",
        "rainbow_PuRd",
        "rainbow_PuBr",
        "rainbow_WhRd",
        "rainbow_WhBr",
        "rainbow_discrete",
    ]
    """List of available colormaps."""

    @classmethod
    def _sunset_colors(cls) -> list[str]:
        """Define "sunset" colors."""
        colors = [
            "#364B9A",
            "#4A7BB7",
            "#6EA6CD",
            "#98CAE1",
            "#C2E4EF",
            "#EAECCC",
            "#FEDA8B",
            "#FDB366",
            "#F67E4B",
            "#DD3D2D",
            "#A50026",
        ]
        return colors

    @classmethod
    def sunset(cls) -> LinearSegmentedColormap:
        """Define colormap 'sunset'."""
        cmap = LinearSegmentedColormap.from_list("sunset", cls._sunset_colors())
        cmap.set_bad("#FFFFFF")
        return cmap

    @classmethod
    def sunset_discrete(cls) -> LinearSegmentedColormap:
        """Define colormap 'sunset_discrete'."""
        cmap = _discretemap("sunset_discrete", cls._sunset_colors())
        cmap.set_bad("#FFFFFF")
        return cmap

    @classmethod
    def _BuRd_colors(cls) -> list[str]:
        """Define "BuRd" colors."""
        colors = [
            "#2166AC",
            "#4393C3",
            "#92C5DE",
            "#D1E5F0",
            "#F7F7F7",
            "#FDDBC7",
            "#F4A582",
            "#D6604D",
            "#B2182B",
        ]
        return colors

    @classmethod
    def BuRd(cls) -> LinearSegmentedColormap:
        """Define colormap 'BuRd'."""
        cmap = LinearSegmentedColormap.from_list("BuRd", cls._BuRd_colors())
        cmap.set_bad("#FFEE99")
        return cmap

    @classmethod
    def BuRd_discrete(cls) -> LinearSegmentedColormap:
        """Define colormap 'BuRd_discrete'."""
        cmap = _discretemap("BuRd_discrete", cls._BuRd_colors())
        cmap.set_bad("#FFEE99")
        return cmap

    @classmethod
    def _PRGn_colors(cls) -> list[str]:
        """Define "PRGn" colors."""
        colors = [
            "#762A83",
            "#9970AB",
            "#C2A5CF",
            "#E7D4E8",
            "#F7F7F7",
            "#D9F0D3",
            "#ACD39E",
            "#5AAE61",
            "#1B7837",
        ]
        return colors

    @classmethod
    def PRGn(cls) -> LinearSegmentedColormap:
        """Define colormap 'PRGn'."""
        cmap = LinearSegmentedColormap.from_list("PRGn", cls._PRGn_colors())
        cmap.set_bad("#FFEE99")
        return cmap

    @classmethod
    def PRGn_discrete(cls) -> LinearSegmentedColormap:
        """Define colormap 'PRGn_discrete'."""
        cmap = _discretemap("PRGn_discrete", cls._PRGn_colors())
        cmap.set_bad("#FFEE99")
        return cmap

    @classmethod
    def _YlOrBr_colors(cls) -> list[str]:
        colors = [
            "#FFFFE5",
            "#FFF7BC",
            "#FEE391",
            "#FEC44F",
            "#FB9A29",
            "#EC7014",
            "#CC4C02",
            "#993404",
            "#662506",
        ]
        return colors

    @classmethod
    def YlOrBr(cls) -> LinearSegmentedColormap:
        """Define colormap 'YlOrBr'."""
        cmap = LinearSegmentedColormap.from_list("YlOrBr", cls._YlOrBr_colors())
        cmap.set_bad("#888888")
        return cmap

    @classmethod
    def YlOrBr_discrete(cls) -> LinearSegmentedColormap:
        """Define colormap 'YlOrBr_discrete'."""
        cmap = _discretemap("YlOrBr_discrete", cls._YlOrBr_colors())
        cmap.set_bad("#888888")
        return cmap

    @classmethod
    def WhOrBr(cls) -> LinearSegmentedColormap:
        """Define colormap 'WhOrBr'."""
        colors = [
            "#FFFFFF",
            "#FFF7BC",
            "#FEE391",
            "#FEC44F",
            "#FB9A29",
            "#EC7014",
            "#CC4C02",
            "#993404",
            "#662506",
        ]
        cmap = LinearSegmentedColormap.from_list("WhOrBr", colors)
        cmap.set_bad("#888888")
        return cmap

    @classmethod
    def iridescent(cls) -> LinearSegmentedColormap:
        """Define colormap 'iridescent'."""
        colors = [
            "#FEFBE9", "#FCF7D5", "#F5F3C1", "#EAF0B5", "#DDECBF", "#D0E7CA",
            "#C2E3D2", "#B5DDD8", "#A8D8DC", "#9BD2E1", "#8DCBE4", "#81C4E7",
            "#7BBCE7", "#7EB2E4", "#88A5DD", "#9398D2", "#9B8AC4", "#9D7DB2",
            "#9A709E", "#906388", "#805770", "#684957", "#46353A"
        ]  # fmt: skip
        cmap = LinearSegmentedColormap.from_list("iridescent", colors)
        cmap.set_bad("#999999")
        return cmap

    @classmethod
    def rainbow_PuRd(cls) -> LinearSegmentedColormap:
        """Define colormap 'rainbow_PuRd'."""
        colors = [
            "#6F4C9B", "#6059A9", "#5568B8", "#4E79C5", "#4D8AC6", "#4E96BC",
            "#549EB3", "#59A5A9", "#60AB9E", "#69B190", "#77B77D", "#8CBC68",
            "#A6BE54", "#BEBC48", "#D1B541", "#DDAA3C", "#E49C39", "#E78C35",
            "#E67932", "#E4632D", "#DF4828", "#DA2222"
        ]  # fmt: skip
        cmap = LinearSegmentedColormap.from_list("rainbow_PuRd", colors)
        cmap.set_bad("#FFFFFF")
        return cmap

    @classmethod
    def rainbow_PuBr(cls) -> LinearSegmentedColormap:
        """Define colormap 'rainbow_PuBr'."""
        colors = [
            "#6F4C9B", "#6059A9", "#5568B8", "#4E79C5", "#4D8AC6", "#4E96BC",
            "#549EB3", "#59A5A9", "#60AB9E", "#69B190", "#77B77D", "#8CBC68",
            "#A6BE54", "#BEBC48", "#D1B541", "#DDAA3C", "#E49C39", "#E78C35",
            "#E67932", "#E4632D", "#DF4828", "#DA2222", "#B8221E", "#95211B",
            "#721E17", "#521A13"
        ]  # fmt: skip
        cmap = LinearSegmentedColormap.from_list("rainbow_PuBr", colors)
        cmap.set_bad("#FFFFFF")
        return cmap

    @classmethod
    def rainbow_WhRd(cls) -> LinearSegmentedColormap:
        """Define colormap 'rainbow_WhRd'."""
        colors = [
            "#E8ECFB", "#DDD8EF", "#D1C1E1", "#C3A8D1", "#B58FC2", "#A778B4",
            "#9B62A7", "#8C4E99", "#6F4C9B", "#6059A9", "#5568B8", "#4E79C5",
            "#4D8AC6", "#4E96BC", "#549EB3", "#59A5A9", "#60AB9E", "#69B190",
            "#77B77D", "#8CBC68", "#A6BE54", "#BEBC48", "#D1B541", "#DDAA3C",
            "#E49C39", "#E78C35", "#E67932", "#E4632D", "#DF4828", "#DA2222"
        ]  # fmt: skip
        cmap = LinearSegmentedColormap.from_list("rainbow_WhRd", colors)
        cmap.set_bad("#666666")
        return cmap

    @classmethod
    def rainbow_WhBr(cls) -> LinearSegmentedColormap:
        """Define colormap 'rainbow_WhBr'."""
        colors = [
            "#E8ECFB", "#DDD8EF", "#D1C1E1", "#C3A8D1", "#B58FC2", "#A778B4",
            "#9B62A7", "#8C4E99", "#6F4C9B", "#6059A9", "#5568B8", "#4E79C5",
            "#4D8AC6", "#4E96BC", "#549EB3", "#59A5A9", "#60AB9E", "#69B190",
            "#77B77D", "#8CBC68", "#A6BE54", "#BEBC48", "#D1B541", "#DDAA3C",
            "#E49C39", "#E78C35", "#E67932", "#E4632D", "#DF4828", "#DA2222",
            "#B8221E", "#95211B", "#721E17", "#521A13"
        ]  # fmt: skip
        cmap = LinearSegmentedColormap.from_list("rainbow_WhBr", colors)
        cmap.set_bad("#666666")
        return cmap

    @classmethod
    def rainbow_discrete(cls, n_colors: int | None = None) -> LinearSegmentedColormap:
        """Define colormap 'rainbow_discrete'."""
        colors = [
            "#E8ECFB", "#D9CCE3", "#D1BBD7", "#CAACCB", "#BA8DB4", "#AE76A3",
            "#AA6F9E", "#994F88", "#882E72", "#1965B0", "#437DBF", "#5289C7",
            "#6195CF", "#7BAFDE", "#4EB265", "#90C987", "#CAE0AB", "#F7F056",
            "#F7CB45", "#F6C141", "#F4A736", "#F1932D", "#EE8026", "#E8601C",
            "#E65518", "#DC050C", "#A5170E", "#72190E", "#42150A"
        ]  # fmt: skip
        indexes = [
            [9],
            [9, 25],
            [9, 17, 25],
            [9, 14, 17, 25],
            [9, 13, 14, 17, 25],
            [9, 13, 14, 16, 17, 25],
            [8, 9, 13, 14, 16, 17, 25],
            [8, 9, 13, 14, 16, 17, 22, 25],
            [8, 9, 13, 14, 16, 17, 22, 25, 27],
            [8, 9, 13, 14, 16, 17, 20, 23, 25, 27],
            [8, 9, 11, 13, 14, 16, 17, 20, 23, 25, 27],
            [2, 5, 8, 9, 11, 13, 14, 16, 17, 20, 23, 25],
            [2, 5, 8, 9, 11, 13, 14, 15, 16, 17, 20, 23, 25],
            [2, 5, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25],
            [2, 5, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 27],
            [2, 4, 6, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 27],
            [2, 4, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 27],
            [2, 4, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 26, 27],
            [1, 3, 4, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 26, 27],
            [1, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 19, 21, 23, 25, 26, 27],
            [1, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 26,
                27],
            [1, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 26,
                27, 28],
            [0, 1, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 26,
                27, 28],
        ]  # fmt: skip
        max_n_colors = 23
        default_n_colors = 22

        if n_colors is None:
            n_colors = default_n_colors
        if n_colors < 1:
            log.warning("Number of colors must be at least greater than one.")
            n_colors = default_n_colors
        if n_colors > max_n_colors:
            log.warning("Number of colors cannot be greater than 23.")
            n_colors = default_n_colors

        cmap = _discretemap(
            "rainbow_discrete", [colors[i] for i in indexes[n_colors - 1]]
        )

        if n_colors == max_n_colors:
            cmap.set_bad("#777777")
        else:
            cmap.set_bad("#FFFFFF")

        return cmap

    @classmethod
    def build_colormap(
        cls, name="rainbow_PuRd", n_colors: int | None = None
    ) -> LinearSegmentedColormap:
        """Return requested colormap, default is 'rainbow_PuRd'."""
        name = name.replace("-", "_")
        if name not in cls.colormap_names:
            raise KeyError(
                f"Unknown colormap '{name}', the "
                f"defined colormaps are {cls.colormap_names}"
            )

        if name == "rainbow_discrete":
            return cls.rainbow_discrete(n_colors)
        return getattr(cls, name)()


def get_colormap(name: str, n_colors: int | None = None) -> LinearSegmentedColormap:
    """Continuous and discrete color sets for ordered data.

    Return one of the colormap/scheme as a matplotlib colormap.

    The name of the colormap must be in "sunset", "sunset_discrete", "BuRd",
    "BuRd_discrete", "PRGn", "PRGn_discrete", "YlOrBr", "YlOrBr_discrete", "WhOrBr",
    "iridescent", "rainbow_PuRd", "rainbow_PuBr", "rainbow_WhRd", "rainbow_WhBr", or
    "rainbow_discrete",

    Hyphens will automatically be replaced by underscores, so "sunset-discrete" works
    as well for instance.

    Parameters
    ----------
    name
        Name of the colormap.
    n_colors
        Only used for "rainbow_discrete". This parameter specifies the number of
        discrete colors to keep. It can vary from 1 to 23 (included). If unspecified or
        outside the valid range, it will default to 22. See the documentation for more
        details or run ``python -m tol_colors`` to see the effect of this parameter.
    """
    return ColormapDefinitions.build_colormap(name, n_colors)


def tol_cmap(
    colormap: str | None = None, lut: int | None = None
) -> LinearSegmentedColormap | list[str]:
    """Continuous and discrete color sets for ordered data.

    Return a matplotlib colormap.
    Parameter lut is ignored for all colormaps except 'rainbow_discrete'.
    """
    colormaps = list(ColormapDefinitions.colormap_names)
    if colormap is None:
        return colormaps
    if colormap not in colormaps:
        colormap = "rainbow_PuRd"
        logging.warning(
            "Requested colormap not defined, using '%s'. " "Known colormaps are %s.",
            colormap,
            colormaps,
        )
    return ColormapDefinitions.build_colormap(colormap, lut)
