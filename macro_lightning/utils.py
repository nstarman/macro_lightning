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


def as_quantity(arg):
    """Convert argument to a Quantity (or raise NotImplementedError).

    from :mod:`~astropy.utils`.

    Returns
    -------
    Quantity
        not copied, quantity subclasses passed through.

    Raises
    ------
    NotImplementedError
        if Quantity() fails

    """
    try:
        return Quantity(arg, copy=False, subok=True)
    except Exception:
        raise NotImplementedError


# /def

# -------------------------------------------------------------------


def qsquare(*args, **kw):
    """Quantity, Squared.

    Parameters
    ----------
    *args : Quantity
        passed, as tuple, to :func:`~as_quantity`
    **kw
        arguments into :func:`~numpy.square`

    Returns
    -------
    Quantity
        not copied, quantity subclasses passed through.

    Raises
    ------
    NotImplementedError
        if :func:`~as_quantity` fails

    """
    return np.square(as_quantity(args), **kw)


# /def

# -------------------------------------------------------------------


def qnorm(*args, **kw):
    """Quantity, Normed.

    Parameters
    ----------
    *args : Quantity
        passed, as tuple, to :func:`~as_quantity`
    **kw
        arguments into :func:`~numpy.linalg.norm`

    Returns
    -------
    Quantity
        not copied, quantity subclasses passed through.

    Raises
    ------
    NotImplementedError
        if :func:`~as_quantity` fails

    """
    return norm(as_quantity(args), **kw)


# /def


# -------------------------------------------------------------------


##############################################################################
# END
