
.. currentmodule:: tol_colors

*********
Colorsets
*********

These are various sets of colors that can be used for lines, markers,
qualitative maps, etc. Below is succinctly described how they are used and
when to use each of them.

Each colorset is accessible in the dictionnary :data:`tol_colors.colorsets`.
This is a special mapping that will accepts both hyphen and underscore versions
(``tc.colorsets["high-contrast"]`` and ``tc.colorsets["high_contrast"]`` will
both work).

Each colorset is also available as a module attribute: ``tc.bright`` for
instance.

Except for the *high* and *medium-constrast* colorsets that can be sorted by
luminance, the colors can be used in any order. In this package, they are given
in the order suggested by the technical notes.

Sets
====

Bright
------

.. image:: /img/cset_bright.svg
    :alt: Bright colorset
    :class: img-padding

Vibrant
-------

.. image:: /img/cset_vibrant.svg
    :alt: Vibrant colorset
    :class: img-padding

Muted
-----

.. image:: /img/cset_muted.svg
    :alt: Muted colorset
    :class: img-padding

High-contrast
-------------

.. image:: /img/cset_high_contrast.svg
    :alt: High-contrast colorset
    :class: img-padding

Medium-contrast
---------------

.. image:: /img/cset_medium_contrast.svg
    :alt: Medium-contrast colorset
    :class: img-padding

Pale
----

.. image:: /img/cset_pale.svg
    :alt: Pale colorset
    :class: img-padding

Light
-----

.. image:: /img/cset_light.svg
    :alt: Light colorset
    :class: img-padding

Dark
----

.. image:: /img/cset_dark.svg
    :alt: Dark colorset
    :class: img-padding

Land-cover
----------

.. image:: /img/cset_land_cover.svg
    :alt: Land-cover colorset
    :class: img-padding


Matplotlib default colors
=========================

The package provides a function to easily set the default colors used by
Matplotlib.

.. autofunction:: tol_colors.set_default_colors

CVD Simulation
==============

Below is a simulation of all the colorsets for total deuteranomaly and
protanomaly.

.. image:: /img/cset_cvd.svg
    :width: 100%
