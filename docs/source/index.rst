.. Tol-colors documentation master file, created by
   sphinx-quickstart on Fri Apr 25 17:53:23 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

########################
Tol-colors documentation
########################

.. highlights::

   Color schemes for lines and maps, color-blind safe

Those color schemes were designed by Paul Tol. This repository is only packaging
his work so that it can be easily installed using pip. This packages and its
documentation follow the technical notes of the color schemes [#tech]_, which
are archived in this project `repository
<https://github.com/Descanonge/tol_colors/blob/master/docs/technical_notes.pdf>`__.
More details and implementations for other languages can be found on Paul Tols's
`website <https://sronpersonalpages.nl/~pault/>`__.

Have a quick look at all available colorsets and colormaps at :doc:`overview`,
or see in more details how and when to use the :doc:`colorsets` and
:doc:`colormaps` in the dedicated pages.


Install
=======

Using pip::

   pip install tol-colors

From source::

   git clone https://github.com/Descanonge/tol_colors.git
   cd tol_colors
   pip install .

Show the available colorsets and colormaps::

   python -m tol_colors


Contents
========

.. toctree::
   :maxdepth: 2

   overview

   colorsets

   colormaps

   api

.. [#tech] *Colour Schemes*, Paul Tol, SRON/EPS/TN/09-002, issue 3.2, 18 August 2021
