
# Tol_colors

> Colormaps and qualitative colorsets that are colorblind-safe

<div align="left">

[![PyPI](https://img.shields.io/pypi/v/tol-colors)](https://pypi.org/project/tol-colors)
[![GitHub release](https://img.shields.io/github/v/release/Descanonge/tol_colors)](https://github.com/Descanonge/tol_colors/releases)
[![Tests](https://github.com/Descanonge/tol_colors/actions/workflows/tests.yml/badge.svg)](https://github.com/Descanonge/tol_colors/actions/workflows/tests.yml)
[![Documentation](https://readthedocs.org/projects/tol-colors/badge/?version=latest)](https://tol-colors.readthedocs.io/en/latest/)

</div>

<img alt="icon" src="https://raw.githubusercontent.com/Descanonge/tol_colors/refs/heads/master/docs/source/_static/icon.svg" width="128" align="left">

Those color schemes were designed by Paul Tol. This repository is packaging his work so that it can be easily installed using pip.
This package and its documentation follow his technical notes<sup id="a1">[1](#f1)</sup>, which are archived in this [repository](https://github.com/Descanonge/tol_colors/blob/master/docs/technical_notes.pdf). Details and implementations for other languages can be found on Paul Tols's [website](https://sronpersonalpages.nl/~pault/).

A more user-friendly documentation is available at <https://tol-colors.readthedocs.io>, detailing how and when to use the various colorsets and colormaps in this package.

## Install

Using pip:
``` sh
pip install tol-colors
```

From source:
``` sh
git clone https://github.com/Descanonge/tol_colors.git
cd tol_colors
pip install .
```

Show the available colorsets, colormaps, and the discrete rainbow colormap:
``` shell
python -m tol_colors
```

## Requirements

- numpy
- matplotlib

## Discrete/qualitative schemes

Sets of colors that can be used for lines, markers, qualitative maps, etc.
All colorsets are given as named tuples. You can then access the colors by index or by name:
``` python
>>> import tol_colors as tc
>>> cset = tc.bright
>>> cset.blue
'#4477AA'
```

Each colorset is available as a module attribute (`tc.bright`) or in the
dictionary `tol_colors.colorsets`. This is a special mapping that will accept
both hyphen and underscore versions (`tc.colorsets["high-contrast"]` and
`tc.colorsets["high_contrast"]` will both work).

![colorsets](https://raw.githubusercontent.com/Descanonge/tol_colors/refs/heads/master/docs/source/img/csets_condensed.svg)

This package also provides a function to easily set the default colors used by Matplotlib to one of the colorsets. This will change your matplotlibrc file or a given stylesheet file.

## Colormaps

The following colormaps were created by linear interpolation of carefully chosen
colors. Those colors can be used as is for discrete colormaps. Discrete variants
are available by adding "_discrete" to the colormap name (*eg*
`tc.sunset_discrete`).

The `iridescent` colormap is meant to be used interpolated; you can still use
`tc.iridescent.resampled(N)` to obtain a discrete version. To obtain a discrete
rainbow colormap, use `tc.rainbow_discrete(n_colors=14)` with a number between 1
and 23.

Colormaps are available either:

- as module attributes (`tc.sunset`),
- stored in a dictionary (`tc.colormaps["sunset"]`) which returns copies,
- registered in matplotlib with the prefix "tol." (`plt.imshow(..., cmap="tol.sunset")`).

Reversed variants are available by appending "_r" to the colormap name.

![colorsmaps](https://raw.githubusercontent.com/Descanonge/tol_colors/refs/heads/master/docs/source/img/cmaps_condensed.svg)

## See also

Other packages already implement these colorschemes and might better suit your needs:
 - [color_tol](https://github.com/lazarillo/color_tol)
 - [pyplot-themes](https://github.com/raybuhr/pyplot-themes)
 - [khroma](https://cran.r-project.org/web/packages/khroma): R package that includes those schemes 
 
 ---

<b id="f1">1</b>: *Colour Schemes*, Paul Tol, SRON/EPS/TN/09-002, issue 3.2, 18 August 2021 [↩](#a1)
