
# Tol_colors

> Color schemes for lines and maps, color-blind safe

<div align="left">

[![PyPI version](https://badge.fury.io/py/tol-colors.svg)](https://badge.fury.io/py/tol-colors)
[![Release status](https://img.shields.io/github/v/release/Descanonge/tol_colors)](https://github.com/Descanonge/tol_colors/releases)

</div>

Thoses color schemes were designed by Paul Tol. This repository is only packaging his work so that it can be easily installed using pip.
His work and details on how to use thoses schemes can be found on his [website](https://personal.sron.nl/~pault/) and in the [docs](./docs) directory.

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

Show the available colorsets, colormaps, and discrete rainbow colormap:
``` python
import tol_colors as tc
tc.main()
```

Get a colorset:
``` python
cset = tc.tol_cset('bright')
```

Get a colormap:
``` python
cmap = tc.tol_cmap('sunset')
```

See the functions docstrings for details.

To change default colorset (for lines) and colormap:
``` python
import matplotlib.pyplot as plt
plt.rc('axes', prop_cycle=plt.cycler('color', list(tc.tol_cset('bright'))))

plt.cm.register_cmap('rainbow_PuRd', tc.tol_cmap('rainbow_PuRd'))
plt.rc('image', cmap='rainbow_PuRd')
```

## Requirements

- numpy
- matplotlib

## See also

Other packages already implement these colorschemes and might better suit your needs:
 - [color_tol](https://github.com/lazarillo/color_tol)
 - [pyplot-themes](https://github.com/raybuhr/pyplot-themes)

