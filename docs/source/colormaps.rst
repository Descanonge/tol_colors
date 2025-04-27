
*********
Colormaps
*********

The various colormaps are available:

- in the dictionary :data:`tol_colors.colormaps` (*eg* ``tc.colormaps["sunset"]``)
- as attributes of the :mod:`tol_colors` module (*eg* ``tc.sunset``)
- directly in matplotlib, registered with the prefix "tol."
  (*eg* ``plt.imshow(..., cmap="tol.sunset")``)

Each colormap has a reversed variant directly available with the suffix "_r"
(*eg* ``tc.sunset_r``)

Click somewhere to show viscm visualization. Maybe collapsible section?

Linear colormaps
================

Unless indicated otherwise, the colormaps in this section can be used either
linearly interpolated, or as discrete maps. Discrete variants are available by
adding "_discrete" to their name (*eg* ``tc.sunset_discrete``).

Sunset
------

.. cmap:: sunset
    :alt: Sunset colormap

BuRd
----

.. cmap:: BuRd
    :alt: Blue-Red colormap

PRGn
----

.. cmap:: PRGn
    :alt: Purple-Green colormap

YlOrBr
------

.. cmap:: YlOrBr
    :alt: Yellow-Orange-Brown colormap


With variant WhOrBr that replaces the first color with pure white:

.. cmap:: WhOrBr
    :alt: White-Orange-Brown colormap

Iridescent
----------

This one is *not* available as discrete.

.. cmap:: iridescent
    :alt: iridescent colormap


Linear rainbow
==============

Rainbow colormap. Only used linearly interpolated, for discrete see next
section. For colorblind people should avoid using the whole range. Start at
purple rather than white or/and end at red rather than brown.

.. cmap:: rainbow_WhBr
    :alt: rainbow colormap (white to brown)

text

.. cmap:: rainbow_WhRd
    :alt: rainbow colormap (white to red)

text

.. cmap:: rainbow_PuBr
    :alt: rainbow colormap (purple to brown)


text

.. cmap:: rainbow_PuRd
    :alt: rainbow colormap (purple to red)

Aliases.

Discrete rainbow
================

Discrete rainbow.
Number of colors can be choosen between 1 and 23 (included). Use function to get.

colors are choosen with the following pattern.
plot.

.. image:: /img/cmap_rainbow_discrete.svg
    :alt: discrete rainbow colormap
    :class: img-padding
