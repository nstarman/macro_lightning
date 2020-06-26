##############################################
Constraining Dark Matter Models with Lightning
##############################################

Welcome to ``macro_lightning``, the code-base for a paper on constraining macroscopic dark matter models with observations of lightning on Earth and Jupiter. If you are looking for the paper, `click here <www.google.com>`_ (TODO add link). 

Macroscopic dark matter (macros) is a broad class of alternative candidates to particle dark matter. These candidates would transfer energy to matter primarily through elastic scattering. A sufficiently large macro passing through the atmosphere would produce a straight channel of ionized plasma. If the cross-section of the macro is :math:`\sigma_x \gtrapprox 6\times10^{-9} \rm{cm}^2`, then under atmospheric conditions conducive to lightning (eg. a thunderstorm) the plasma channel would be sufficient to seed a lightning strike with a single leader.

This is entirely unlike ordinary bolt lightning in which a long sequence of hundreds or thousands of few-meter-long leaders are strung together. This macro-induced lightning would be extremely straight, and thus highly distinctive. Neither wind shear nor magnetohydrodynamic instabilities would markedly spoil its straightness. The only photographically documented case of a straight lightning bolt is probably not straight enough to have been macro-induced.

For the mathematical derivation of these properties, as well as the phase-space constraints on macro models from non-observation of straight lightning on Earth and Jupiter, see the paper. This is documentation for the code used in the paper.

All code and data is available on a `public repository on GitHub <https://github.com/nstarman/macro_lightning>`_, so if you have any trouble, `open an issue <https://github.com/nstarman/macro_lightning/issues>`_ there.

.. container::

   |DOI| |PyPI| |Build Status| |Coveralls| |astropy|


*************
Documentation
*************

.. toctree::
   :maxdepth: 1

   macro_lightning/index
   documentation/installation
   documentation/testing
   whatsnew/1.0


***********
Subpackages
***********

THough the code base is quite light it has been split into its natural components: utility functions, plotting functions, and the physics functions.

.. toctree::
   :maxdepth: 1

   macro_lightning/plot
   macro_lightning/utils
   macro_lightning/physics
   macro_lightning/parameters


********
Examples
********

.. toctree::
   :maxdepth: 1

   examples/plotting_constraints.ipynb


*****************
How to contribute
*****************

|Milestones| |Open Issues| |Last Commit|

We welcome contributions from anyone via pull requests on `GitHub
<https://github.com/nstarman/macro_lightning>`_. If you don't feel comfortable modifying or
adding functionality, we also welcome feature requests and bug reports as
`GitHub issues <https://github.com/nstarman/macro_lightning/issues>`_.

The development process follows that of the `astropy-package-template <https://docs.astropy.org/en/latest/development/astropy-package-template.html>`_ from Astropy's `release procedure <https://docs.astropy.org/en/latest/development/releasing.html#release-procedure>`_.


***********
Attribution
***********

|DOI| |License|

Copyright 2018- Nathaniel Starkman and contributors.

``macro_lightning`` is free software made available under the BSD-3 License. For details see the `LICENSE <https://github.com/nstarman/macro_lightning/blob/master/LICENSE>`_ file.

If you make use of this code, please consider citing the Zenodo DOI as a software citation::

   @software{macro_lightning:zenodo,
     author       = {nstarman},
     title        = {macro_lightning},
     publisher    = {Zenodo},
     doi          = {10.5281/zenodo.3491011},
     url          = {https://doi.org/10.5281/zenodo.3491011}
   }



***************
Project details
***************

.. toctree::
   :maxdepth: 1

   credits
   whatsnew/index
   documentation/code_quality


.. |astropy| image:: http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat
   :target: http://www.astropy.org/

.. |Build Status| image:: https://travis-ci.com/nstarman/macro_lightning.svg?branch=master
    :target: https://travis-ci.com/nstarman/macro_lightning

.. |Documentation Status| image:: https://readthedocs.org/projects/macro_lightning/badge/?version=latest
   :target: https://macro_lightning.readthedocs.io/en/latest/?badge=latest

.. |DOI| image:: https://zenodo.org/badge/192425953.svg
   :target: https://zenodo.org/badge/latestdoi/192425953

.. |License| image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
   :target: https://opensource.org/licenses/BSD-3-Clause

.. |PyPI| image:: https://badge.fury.io/py/macro_lightning.svg
   :target: https://badge.fury.io/py/macro_lightning

.. |Milestones| image:: https://img.shields.io/github/milestones/open/nstarman/macro_lightning?style=flat
   :alt: GitHub milestones

.. |Open Issues| image:: https://img.shields.io/github/issues-raw/nstarman/macro_lightning?style=flat
   :alt: GitHub issues

.. |Last Commit| image:: https://img.shields.io/github/last-commit/nstarman/macro_lightning/master?style=flat
   :alt: GitHub last commit (branch)

.. |Coveralls| image:: https://coveralls.io/repos/github/nstarman/macro_lightning/badge.svg?branch=master
   :target: https://coveralls.io/github/nstarman/macro_lightning?branch=master
