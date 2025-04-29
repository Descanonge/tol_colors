
.. currentmodule:: tol_colors

*********
Colorsets
*********

These are various sets of colors that can be used for lines, markers,
qualitative maps, etc. Below is succinctly described how they are used and
when to use each of them.

All colorsets are given as named tuples. You can then access the colors by index or by name::

    >>> cset = tc.bright
    >>> cset.blue
    '#4477AA'

Each colorset is available as a module attribute: ``tc.bright`` for instance.
All colorsets are also stored in the dictionnary :data:`tol_colors.colorsets`.
This is a special mapping that will accepts both hyphen and underscore versions
(``tc.colorsets["high-contrast"]`` and ``tc.colorsets["high_contrast"]`` will
both work).

Except for the *high* and *medium-constrast* colorsets that can be sorted by
luminance, the colors can be used in any order. In this package, they are given
in the order suggested by the technical notes.


Sets
====

.. admonition:: Design considerations
    :collapsible: closed

    - Red-blind and green-blind vision were simulated by the method described in
      Section 5 of the technical notes.
    - The distance between colors was computed by using the CIEDE2000 color
      difference :math:`\Delta E_{00}`
    - Colors with the same product of saturation S and value V in the HSV color
      system (same ‘vividness’) were considered to match well together.
    - "Print-friendly" colors were chosen from the intersection between the sRGB
      color-space and a generic CMYK color-space that should work with most printers.
    - To reduce the number of calculations, only websmart colors were
      considered, meaning the hexadecimal RGB coordinates are only 00, 11, ..., FF.

Bright
------

The default colorset of this package. Main scheme for lines and labels.

.. image:: /img/cset_bright.svg
    :alt: Bright colorset
    :width: 100%
    :class: img-padding

Vibrant
-------

An alternative to *bright*, equally colorblind-safe. It is designed for the data
visualization framework TensorBoard, built around its signature orange (tweaked
to be print-friendly).

.. image:: /img/cset_vibrant.svg
    :alt: Vibrant colorset
    :class: img-padding
    :width: 100%

Muted
-----

An other alternative to *bright*, equally colorblind-safe. It has more colors,
but lacks a clear red or medium blue. Pale grey is meant for bad data in maps.

.. image:: /img/cset_muted.svg
    :alt: Muted colorset
    :class: img-padding
    :width: 100%

High-contrast
-------------

A colorset optimized for contrast. The rectangles underneath colors are shades
of grey with the same luminance L*.
This set works great for people with monochrome vision, and in a monochrome
printout.

.. image:: /img/cset_high_contrast.svg
    :alt: High-contrast colorset
    :class: img-padding
    :width: 60%

Medium-contrast
---------------

An alternative to *high-contrast*, also colorblind-safe and designed for
situations needing color pairs. It is also optimized for contrast to work in a
monochrome printout, but the differences are inevitably smaller.

.. image:: /img/cset_medium_contrast.svg
    :alt: Medium-contrast colorset
    :class: img-padding
    :width: 100%

Pale
----

The colors of this set are not very distinct in either normal or colorblind
vision; they are not meant for lines or maps, but for marking text. Use the pale
colors for the background of black text, for example to highlight cells in a
table. The text remains readable.

.. image:: /img/cset_pale.svg
    :alt: Pale colorset
    :class: img-padding
    :width: 100%

Dark
----

The colors of this set are not very distinct in either normal or colorblind
vision; they are not meant for lines or maps, but for marking text. Use the dark
colors for text on a white background. The text remains readable.

.. image:: /img/cset_dark.svg
    :alt: Dark colorset
    :class: img-padding
    :width: 100%

Light
-----

An alternative to the *pale* colorset, designed to fill labelled cells with more
and lighter colors than in *bright*, and with more distinct colors than *pale*,
while keeping black text readable.
As the colors are reasonably distinct in normal and colorblind vision, it can
also be used for general qualitative data.

.. image:: /img/cset_light.svg
    :alt: Light colorset
    :class: img-padding
    :width: 100%


Land-cover
----------

A specialized colorset for the global land classification of AVHRR data. An
alternative to the recommended scheme given by the Department of Geography at
the University of Maryland, with more subtle colors distinct in all visions.

.. image:: /img/cset_land_cover.svg
    :alt: Land-cover colorset
    :class: img-padding
    :width: 100%


Matplotlib default colors
=========================

This package provides a function to easily set the default colors used by
Matplotlib to one of the colorsets.

.. autofunction:: tol_colors.set_default_colors
    :no-index:

CVD Simulations
===============

Below are simulations of all the colorsets for total deuteranomaly and
protanomaly.
Note that it was simulated using a different method than that of the technical
notes. Here we relied on the `colorspacious
<https://pypi.org/project/colorspacious/>`__ package, using the model from
Machado, Oliveira and Fernandes (`DOI: 10.1109/TVCG.2009.113
<https://doi.org/10.1109/TVCG.2009.113>`__).

.. image:: /img/csets_cvd.svg
     :width: 100%
