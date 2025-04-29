
********
Overview
********

Here is a quick presentation of the colorsets and colormaps available. For
details on how and when to use them, see the dedicated pages.

Colorsets
---------

.. note::

    More details at :doc:`colorsets`.

These are various sets of colors that can be used for lines, markers,
qualitative maps, etc. All colorsets are given as named tuples. You can then
access the colors by index or by name::

    >>> cset = tc.bright
    >>> cset.blue
    '#4477AA'

Each colorset is available as a module attribute (``tc.bright``).
All colorsets are also stored in the dictionnary :data:`tol_colors.colorsets`.
This is a special mapping that will accepts both hyphen and underscore versions
(``tc.colorsets["high-contrast"]`` and ``tc.colorsets["high_contrast"]`` will
both work).

.. image:: /img/csets_condensed.svg
    :width: 100%

.. note::

    Additional sets *dark* and *pale* (not shown above) are available for text
    and text background, respectively.


Colormaps
---------

.. note::

    More details at :doc:`colormaps`.

Colormaps are available as module attributes (``tc.sunset``), stored in a
dictionnary :data:`tol_colors.colormaps` (``tc.colormaps["sunset"]``), and
registered in Matplotlib with the prefix "tol." (``plt.imshow(...,
cmap="tol.sunset")``). Reversed variants are available by appending "_r" to the
colormap name.

A discrete rainbow colormap is available by specifying the number of colors
between 1 and 23 (``tc.get_colormap("rainbow_discrete", n_colors=14)``).

.. image:: /img/cmaps_condensed.svg
    :width: 100%
