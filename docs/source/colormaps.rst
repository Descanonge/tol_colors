
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

.. image:: /img/cmap_sunset.svg
    :alt: Sunset colormap
    :class: img-padding

BuRd
----

.. image:: /img/cmap_BuRd.svg
    :alt: Blue-Red colormap
    :class: img-padding

PRGn
----

.. image:: /img/cmap_PRGn.svg
    :alt: Purple-Green colormap
    :class: img-padding

YlOrBr
------

.. image:: /img/cmap_YlOrBr.svg
    :alt: Yellow-Orange-Brown colormap
    :class: img-padding


With variant WhOrBr that replaces the first color with pure white:

.. image:: /img/cmap_WhOrBr.svg
    :alt: White-Orange-Brown colormap
    :class: img-padding

Iridescent
----------

This one is *not* available as discrete.

.. image:: /img/cmap_iridescent.svg
    :alt: iridescent colormap
    :class: img-padding

Linear rainbow
==============

Rainbow colormap. Only used linearly interpolated, for discrete see next
section. For colorblind people should avoid using the whole range. Start at
purple rather than white or/and end at red rather than brown.

.. image:: /img/cmap_rainbow_WhBr.svg
    :alt: rainbow colormap (white to brown)
    :class: img-padding

text

.. image:: /img/cmap_rainbow_WhRd.svg
    :alt: rainbow colormap (white to red)
    :class: img-padding


text

.. image:: /img/cmap_rainbow_PuBr.svg
    :alt: rainbow colormap (purple to brown)
    :class: img-padding


text

.. image:: /img/cmap_rainbow_PuRd.svg
    :alt: rainbow colormap (purple to red)
    :class: img-padding

Aliases.

Discrete rainbow
================

Discrete rainbow.
Number of colors can be choosen between 1 and 23 (included). Use function to get.

colors are choosen with the following pattern.
plot.
