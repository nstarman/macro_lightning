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
# __version__ = "0.0.0"
__maintainer__ = "Nathaniel Starkman"
# __email__ = ""
# __status__ = "Production"


__all__ = [
    # modules
    "data",
    "utils",
    "misc",
]


##############################################################################
# IMPORTS

# keep this content at the top. (sets the __version__)
from ._astropy_init import *  # noqa
from ._astropy_init import __version__  # noqa


# PROJECT-SPECIFIC

from . import data, utils, misc


##############################################################################
# END
