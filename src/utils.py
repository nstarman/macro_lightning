# -*- coding: utf-8 -*-

"""Utilities."""

__author__ = "Nathaniel Starkman"


__all__ = [
    "as_quantity",
    "qsquare",
    "qnorm",
]


##############################################################################
# IMPORTS

# THIRD PARTY

from astropy.units import Quantity

import numpy as np
from numpy.linalg import norm


##############################################################################
# PARAMETERS


##############################################################################
# CODE
##############################################################################


def as_quantity(a):
    """Convert argument to a Quantity (or raise NotImplementedError).

    from :mod:`~astropy.utils`.

    """
    try:
        return Quantity(a, copy=False, subok=True)
    except Exception:
        raise NotImplementedError


# /def

# -------------------------------------------------------------------


def qsquare(*args, **kw):
    """Quantity, Squared."""
    return np.square(as_quantity(args), **kw)


# /def

# -------------------------------------------------------------------


def qnorm(*args, **kw):
    """Quantity, Normed."""
    return norm(as_quantity(args), **kw)


# /def


# -------------------------------------------------------------------


##############################################################################
# END
