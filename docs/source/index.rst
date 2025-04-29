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
his work so that it can be easily installed using pip. His work and details on
how to use those schemes can be found on his `website
<https://personal.sron.nl/~pault/>`__, in the khroma R package `documentation
<https://cran.r-project.org/web/packages/khroma/vignettes/tol.html>`__. This
package and documentation is built using the technical notes issue 3.2 (2021)
that can be found in this project `repository
<https://github.com/Descanonge/tol_colors/blob/master/docs/colourschemes.pdf>`__.

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
