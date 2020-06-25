# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
#
# AUTHOR  : Nathaniel Starkman, Harrison Winch, Jagjit Sidhu, Glenn Starkman
# PROJECT : macro_lightning
#
# ----------------------------------------------------------------------------

"""Macro-induced Lightning."""

__author__ = [
    "Jagjit Sidhu",
    "Nathaniel Starkman",
    "Harrison Winch",
    "Glenn Starkman",
]
__copyright__ = "Copyright 2020, "
__license__ = "BSD-3"
__maintainer__ = "Nathaniel Starkman"


__all__ = [
    # modules
    "data",
    "utils",
    "physics",
    "plot",
    # functions
    "constraints_plot",
]


##############################################################################
# IMPORTS

# keep this content at the top. (sets the __version__)
from ._astropy_init import *  # noqa
from ._astropy_init import __version__  # noqa


# PROJECT-SPECIFIC

from . import data, utils, physics, plot

from .plot import constraints_plot


##############################################################################
# END
