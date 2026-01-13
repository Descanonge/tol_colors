
.. currentmodule:: tol_colors

***
API
***


Colorsets
=========

.. autodata:: colorsets
    :no-value:

    .. autoclass:: ColorsetMapping
        :show-inheritance:

.. autofunction:: set_default_colors

.. py:data:: bright
    :type: Bright

    .. autoclass:: Bright

.. py:data:: vibrant
    :type: Vibrant

    .. autoclass:: Vibrant

.. py:data:: muted
    :type: Muted

    .. autoclass:: Muted

.. py:data:: high_contrast
    :type: HighContrast

    .. autoclass:: HighContrast

.. py:data:: medium_contrast
    :type: MediumContrast

    .. autoclass:: MediumContrast

.. py:data:: pale
    :type: Pale

    .. autoclass:: Pale

.. py:data:: dark
    :type: Dark

    .. autoclass:: Dark

.. py:data:: light
    :type: Light

    .. autoclass:: Light

.. py:data:: land_cover
    :type: LandCover

    .. autoclass:: LandCover


Colormaps
=========

.. autodata:: colormaps
    :no-value:

Sunset
------

.. py:data:: sunset
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: sunset_r
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: sunset_discrete
    :type: ~matplotlib.colors.ListedColormap

.. py:data:: sunset_discrete_r
    :type: ~matplotlib.colors.ListedColormap

Nightfall
---------

.. py:data:: nightfall
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: nightfall_r
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: nightfall_discrete
    :type: ~matplotlib.colors.ListedColormap

.. py:data:: nightfall_discrete_r
    :type: ~matplotlib.colors.ListedColormap

BuRd
----

.. py:data:: BuRd
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: BuRd_r
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: BuRd_discrete
    :type: ~matplotlib.colors.ListedColormap

.. py:data:: BuRd_discrete_r
    :type: ~matplotlib.colors.ListedColormap

PRGn
----

.. py:data:: PRGn
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: PRGn_r
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: PRGn_discrete
    :type: ~matplotlib.colors.ListedColormap

.. py:data:: PRGn_discrete_r
    :type: ~matplotlib.colors.ListedColormap

YlOrBr
------

.. py:data:: YlOrBr
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: YlOrBr_r
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: YlOrBr_discrete
    :type: ~matplotlib.colors.ListedColormap

.. py:data:: YlOrBr_discrete_r
    :type: ~matplotlib.colors.ListedColormap

WhOrBr
------

.. py:data:: WhOrBr
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: WhOrBr_r
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: WhOrBr_discrete
    :type: ~matplotlib.colors.ListedColormap

.. py:data:: WhOrBr_discrete_r
    :type: ~matplotlib.colors.ListedColormap

Iridescent
----------

.. py:data:: iridescent
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: iridescent_r
    :type: ~matplotlib.colors.LinearSegmentedColormap

Incandescent
------------

.. py:data:: incandescent
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: incandescent_r
    :type: ~matplotlib.colors.LinearSegmentedColormap

Rainbow
-------

.. autofunction:: rainbow_discrete

.. rubric:: Full rainbow
.. py:data:: rainbow_WhBr
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: rainbow_WhBr_r
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: rainbow

    Alias for :data:`rainbow_WhBr`.

.. py:data:: rainbow_r

    Alias for :data:`rainbow_WhBr_r`.

.. rubric:: White to red
.. py:data:: rainbow_WhRd
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: rainbow_WhRd_r
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. rubric:: Purple to brown
.. py:data:: rainbow_PuBr
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: rainbow_PuBr_r
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. rubric:: Purple to red
.. py:data:: rainbow_PuRd
    :type: ~matplotlib.colors.LinearSegmentedColormap

.. py:data:: rainbow_PuRd_r
    :type: ~matplotlib.colors.LinearSegmentedColormap


Legacy API
==========

Present for backward compatibility, but should be replaced by alternatives
above.

.. autofunction:: get_colorset

.. autofunction:: tol_cset

.. autofunction:: get_colormap

.. autofunction:: tol_cmap
