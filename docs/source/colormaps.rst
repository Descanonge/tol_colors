
.. currentmodule:: tol_colors

.. role:: rawhtml(raw)
    :format: html

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

.. tip::

    Click on a colormap to show its `viscm <https://pypi.org/project/viscm/>`__
    evaluation in a new tab.

Linear colormaps
================

The colormaps are created by linear interpolation of carefully chosen colors.
Those colors can be used as is for discrete colormaps and are shown below. These
discrete variants are available by adding "_discrete" to the colormap name (*eg*
``tc.sunset_discrete``). However, the *iridescent* and *rainbow* colormaps are
**not** available as discrete colormaps.

To obtain discrete colormaps with a specific number of colors it is possible to
resample a continuous colormap with::

  tc.sunset.resampled(n_colors)

.. important::

    The three diverging schemes (*sunset*, *BuRd* and *PRGn*) look similar in
    color-blind vision, so if more than one is used, do not reverse the
    direction in one of them.

Sunset
------

.. _Color-Brewer: http://colorbrewer2.org

The scheme is related to the `Color-Brewer`_ *RdYlBu* scheme, but with darker
central colors and made more symmetric. Sunset is designed for situations where
bad data have to be shown white.

.. cmap:: sunset
    :alt: Sunset colormap

BuRd
----
This is the reversed and tweaked `Color-Brewer`_ *RdBu* scheme.
Bad data is :rawhtml:`<span style="background-color: #FFEE99; padding: 3pt;">#FFEE99</span>`.

.. cmap:: BuRd
    :alt: Blue-Red colormap

PRGn
----

This is the `Color-Brewer`_ *PRGn* scheme, with green to make it print-friendly.
Bad data is :rawhtml:`<span style="background-color: #FFEE99; padding: 3pt;">#FFEE99</span>`.

.. cmap:: PRGn
    :alt: Purple-Green colormap

YlOrBr
------

This is the `Color-Brewer`_ *YlOrBr* scheme, with orange shifted to make it
print-friendly.
Bad data is :rawhtml:`<span style="background-color: #888888; padding: 3pt;">#888888</span>`.

.. cmap:: YlOrBr
    :alt: Yellow-Orange-Brown colormap

The variant *WhOrBr* replaces the first color (pale yellow) with pure white:

.. cmap:: WhOrBr
    :alt: White-Orange-Brown colormap

Iridescent
----------

A colormap with linearly varying luminance that also works in colourblind
vision.
Bad data is :rawhtml:`<span style="background-color: #999999; padding: 3pt;">#999999</span>`.
*iridescent* is not directly available as a discrete colormap.

.. cmap:: iridescent
    :alt: iridescent colormap


Linear rainbow
==============

There are many pitfalls to using a continuous rainbow colormap for ordered data:

- The spectral order of visible light carries no inherent magnitude message.
  However, a rainbow provides a scheme with many colors, showing subtle effects
  in the data clearer or making it easier to read the value in a map. There are
  also cases where a scheme is preferred that does not have pale colors at the
  low end or middle of the range.
- Most rainbow schemes contain bands of almost constant hue with sharp
  transitions between them, which are perceived as jumps in the data. This can
  be avoided with careful design.
- Colorblind people have difficulty distinguishing some colors of the rainbow.
  This can be taken into account in the design.

.. important::

    The following colormaps should only be used interpolated. For a discrete rainbow
    colormap, see the :ref:`next section <discrete-rainbow>`.

rainbow_WhBr
------------

The full rainbow colormap. It is also available under the alias ``rainbow``.

.. cmap:: rainbow_WhBr
    :alt: rainbow colormap (white to brown)

rainbow_WhRd
------------

Often it is better to use only a limited range of the rainbow colors.
*rainbow_WhRd* avoids the brown/deep reds, which is useful when the highest
values (towards brown) occurs often in the data.

.. cmap:: rainbow_WhRd
    :alt: rainbow colormap (white to red)

rainbow_PuBr
------------

Often it is better to use only a limited range of the rainbow colors.
*rainbow_PuBr* avoids the white/light purple, which is useful when the lowest
values (towards white) occurs often in the data. It is preferable to avoid
mixing light purples and light blues too much for colorblind people.

.. cmap:: rainbow_PuBr
    :alt: rainbow colormap (purple to brown)

rainbow_PuRd
------------

Often it is better to use only a limited range of the rainbow colors.
*rainbow_PuRd* avoids both ends, which is useful when the lowest and hightest
values occurs often in the data.

.. cmap:: rainbow_PuRd
    :alt: rainbow colormap (purple to red)


.. _discrete-rainbow:

Discrete rainbow
================

A function is provided to return a discrete rainbow colormap with a given number
of colors. That number can vary between 1 and 23 (included).
The colors are obtained by selecting among 23 statically defined colors. The
results are displayed below.

Bad data is marked with white by default, except when using 23 colors where it
will be marked with grey :rawhtml:`<span style="background-color: #777777;
padding: 3pt;">#777777</span>`.

.. autofunction:: rainbow_discrete
    :no-index:

.. image:: /img/cmap_rainbow_discrete.svg
    :alt: discrete rainbow colormap
    :class: img-padding
