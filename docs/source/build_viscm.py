"""Build viscm visualizations of colormaps."""

import matplotlib
import matplotlib.pyplot as plt
from viscm import gui

import tol_colors

matplotlib.rcdefaults()


def make_viz(cmap: str, cmap_type: str):
    fig = plt.figure(figsize=(18, 11))
    cm = gui.Colormap(cmap_type, "CatmulClark", "CAM02-UCS")
    cm.load(f"tol.{cmap}")
    gui.viscm(cm.cmap, name=cm.name, figure=fig, uniform_space=cm.uniform_space)
    fig.savefig(f"docs/source/img/cmap_viscm_{cmap}.svg", dpi=50)


make_viz("sunset", "diverging")
make_viz("nightfall", "diverging")
make_viz("BuRd", "diverging")
make_viz("PRGn", "diverging")
make_viz("YlOrBr", "linear")
make_viz("WhOrBr", "linear")
make_viz("iridescent", "linear")
make_viz("incandescent", "linear")
make_viz("rainbow_WhBr", "linear")
make_viz("rainbow_WhRd", "linear")
make_viz("rainbow_PuBr", "linear")
make_viz("rainbow_PuRd", "linear")
