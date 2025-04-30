
# Tol_colors

<div align="left">

[![PyPI](https://img.shields.io/pypi/v/tol-colors)](https://pypi.org/project/tol-colors)
[![GitHub release](https://img.shields.io/github/v/release/Descanonge/tol_colors)](https://github.com/Descanonge/tol_colors/releases)

</div>

<img alt="icon" src="/docs/source/_static/icon.svg" width="128" align="left">

Those color schemes were designed by Paul Tol. This repository is packaging his work so that it can be easily installed using pip.
This packages and its documentation follow the technical notes of the color schemes (issue 3.2, 2021), which are archived in this [repository](/docs/technical_notes.pdf). Details and implementations for other lanugages can be found on Paul Tols's [website](https://personal.sron.nl/~pault/).

A more user-friendly documentation is available at <https://tol-colors.readthedocs.io>, detailing how and when to use the various colorsets and colormaps.

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

All colorsets are given as named tuples. You can then access the colors by index or by name:
``` python
>>> cset = tc.bright
>>> cset.blue
'#4477AA'
```

Each colorset is available as a module attribute (`tc.bright`) and stored in the dictionary `tol_colors.colorsets`. This is a special mapping that will accepts both hyphen and underscore versions
(`tc.colorsets["high-contrast"]` and `tc.colorsets["high_contrast"]` will
both work).

![colorsets](/docs/source/img/csets_condensed.svg)

This package also provides a function to easily set the default colors used by Matplotlib to one of the colorsets. This will change your matplotlibrc file or a stylesheet file.

## Colormaps

The following colormaps were created by linear interpolation of carefully chosen
colors. Those colors can be used as is for discrete colormaps. These discrete
variants are available by adding "_discrete" to the colormap name (*eg*
`tc.sunset_discrete`). Note the *iridescent* does not have a readily available
discrete version, and one should use the a dedicated function to obtain a
discrete rainbow.

Colormaps are available as module attributes (`tc.sunset`), stored in a
dictionnary `tol_colors.colormaps` (`tc.colormaps["sunset"]`), and registered in
Matplotlib with the prefix "tol." (`plt.imshow(..., cmap="tol.sunset")`).
Reversed variants are available by appending "_r" to the colormap name.

Rather than resampling the interpolated colormaps, discrete rainbow colormap is
available by specifying the number of colors between 1 and 23
(`tc.get_colormap("rainbow_discrete", n_colors=14)`).

![colorsmaps](/docs/source/img/cmaps_condensed.svg)

## See also

Other packages already implement these colorschemes and might better suit your needs:
 - [color_tol](https://github.com/lazarillo/color_tol)
 - [pyplot-themes](https://github.com/raybuhr/pyplot-themes)
 - [khroma](https://cran.r-project.org/web/packages/khroma): R package that includes those schemes 

