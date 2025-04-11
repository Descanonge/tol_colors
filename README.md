
# Tol_colors

> Color schemes for lines and maps, color-blind safe

<div align="left">

[![PyPI](https://img.shields.io/pypi/v/tol-colors)](https://pypi.org/project/tol-colors)
[![GitHub release](https://img.shields.io/github/v/release/Descanonge/tol_colors)](https://github.com/Descanonge/tol_colors/releases)

</div>

Those color schemes were designed by Paul Tol. This repository is only packaging his work so that it can be easily installed using pip.
His work and details on how to use those schemes can be found on his [website](https://personal.sron.nl/~pault/) and in the [technical note](./docs/colorschemes.pdf).

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

To change the default matplotlib colorset or colormap:
``` python
import matplotlib.pyplot as plt
plt.rc('axes', prop_cycle=plt.cycler('color', list(tc.get_colorset('bright'))))
plt.colormaps.register(name='rainbow_PuRd', cmap=tc.get_colormap('rainbow_PuRd'))
plt.rc('image', cmap='rainbow_PuRd')
```

## Requirements

- numpy
- matplotlib

## Discrete/qualitative schemes

These schemes are discrete sets of colors meant to be used for the color of lines, text, cell background, etc. Each set can be obtained as a named tuple via:
``` python
cset = tc.get_colorset('bright')
```
Each color can set be accessed by name (`cset.blue` for instance).

The default scheme is **"bright"**:

![bright](/docs/img/bright.svg)

An equally colorblind-safe alternative is the **"vibrant"** scheme:

![vibrant](/docs/img/vibrant.svg)

When fewer colors are enough is the **"high-contrast"** scheme, which also works when
converted to greyscale:

![high-contrast](/docs/img/high-contrast.svg)

The **"muted"** scheme has more colors but lacks a clear red or medium blue:

![muted](/docs/img/muted.svg)

The **"medium-contrast"** scheme has three color pairs that can work in greyscale, but not as well as the high-contrast scheme:

![medium-contrast](/docs/img/medium-contrast.svg)

The bright, high-contrast, vibrant, muted and medium-contrast schemes work well for plot lines and map regions, but the colors are too strong to use for backgrounds to mark (black) text, typically in a table. The **"pale"** scheme is designed for that purpose.
The colors are inherently not very distinct from each other, but they are clear in a white area. The **"dark"** scheme is meant for text itself on a white background.

![pale-dark](/docs/img/pale-dark.svg)

The **"light"** scheme is between the bright and pale schemes. It can be used for example for backgrounds in a table where more colors are needed than available in the pale scheme
and where the colored areas are small.

![light](/docs/img/light.svg)

Lastly, the scheme **"land-cover"** provides an alternative to the recommended colors for land cover data with distinct colors:

![land-cover](/docs/img/land-cover.svg)

## Colormaps

These schemes are meant to be used as colormaps. They can be obtained by name via:
``` python
cmap = tc.get_colormap('sunset')
```
The colormaps are linearly interpolated (smoothed), but the *sunset*, *BuRd*, *PRGn*, *YlOrBr* and *rainbow* schemes can be kept discrete/segmented by adding `_discrete` to the scheme name (*ie* tc.get_colormap('sunset_discrete')).
The circled color is meant for bad data.

There are three diverging schemes. **"sunset"** is related to the ColorBrewer RdYlBu scheme, but with darker central colours and made more symmetric:

![sunset](/docs/img/sunset.svg)

**"BuRd"** is the reversed ColorBrewer RdBu scheme:

![BuRd](/docs/img/BuRd.svg)

**"PRGn"** is the ColorBrewer PRGn scheme, with green shifted to make it print-friendly:

![PRGn](/docs/img/PRGn.svg)

There are three sequential schemes. **"YlOrBr"** is the ColorBrewer *YlOrBr* scheme, with orange shifted to make it print-friendly. Pale yellow can be set to completely white, for example in density histograms.

![YlOrBr](/docs/img/YlOrBr.svg)

**"iridescent"** has a linearly varying luminance that also works in colour-blind vision. The colours should be linearly interpolated, optionally extended towards white and black.

![iridescent](/docs/img/iridescent.svg)

Finally, there is a smoothed **"rainbow"** scheme. It is often better to use a limited range of these colors.
If the lowest data value occurs often, start at off-white instead of purple. If the highest data value occurs often, end at red instead of brown.
For color-blind people, the light purples and light blues should not be mixed much.

![rainbow](/docs/img/rainbow.svg)

There is a discrete alternative named **"rainbow_discrete"** where the number of colors can be picked between 1 and 23 (`tc.get_colormap("rainbow_discrete", n_colors=14)`). See the technical note for details.

## Simulations

Here are the color schemes with approximations of red-blind and green-blind vision:

![simulations](/docs/img/simulations.svg)



## See also

Other packages already implement these colorschemes and might better suit your needs:
 - [color_tol](https://github.com/lazarillo/color_tol)
 - [pyplot-themes](https://github.com/raybuhr/pyplot-themes)

