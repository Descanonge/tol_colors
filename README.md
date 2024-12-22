
# Tol_colors

> Color schemes for lines and maps, color-blind safe

<div align="left">

[![PyPI](https://img.shields.io/pypi/v/tol-colors)](https://pypi.org/project/tol-colors)
[![GitHub release](https://img.shields.io/github/v/release/Descanonge/tol_colors)](https://github.com/Descanonge/tol_colors/releases)

</div>

Those color schemes were designed by Paul Tol. This repository is only packaging his work so that it can be easily installed using pip.
His work and details on how to use those schemes can be found on his [website](https://personal.sron.nl/~pault/) and in the [docs](./docs) directory.

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

## Get started

Get a colorset:
``` python
cset = tc.get_colorset('bright')
```

Get a colormap:
``` python
cmap = tc.get_colormap('sunset')
```

Show the available colorsets, colormaps, and the discrete rainbow colormap:
``` shell
python -m tol_colors
```

See each function docstring for details.

To change the default matplotlib colorset or colormap:
``` python
import matplotlib.pyplot as plt
plt.rc('axes', prop_cycle=plt.cycler('color', list(tc.get_colorset('bright'))))

plt.cm.register_cmap('rainbow_PuRd', tc.get_colormap('rainbow_PuRd'))
plt.rc('image', cmap='rainbow_PuRd')
```

## Requirements

- numpy
- matplotlib

## See also

Other packages already implement these colorschemes and might better suit your needs:
 - [color_tol](https://github.com/lazarillo/color_tol)
 - [pyplot-themes](https://github.com/raybuhr/pyplot-themes)

