# -*- coding: utf-8 -*-

"""test utilities."""


__all__ = [
    "test_as_quantity",
    "test_qsquare",
    "test_qnorm",
]


##############################################################################
# IMPORTS

# BUILT-IN

# THIRD PARTY

import astropy.units as u
import pytest


# PROJECT-SPECIFIC

from .. import utils

##############################################################################
# PARAMETERS


##############################################################################
# CODE
##############################################################################


def test_as_quantity():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    # ------------------
    # Quantities Unchanged

    # single number
    x = 1 * u.m
    y = utils.as_quantity(x)
    assert y == x

    # array
    x = [1, 2] * u.m
    y = utils.as_quantity(x)
    assert all(y == x)

    # ------------------
    # Change Copies

    # array
    x = [1, 2, 3] * u.m
    y = utils.as_quantity(x)
    assert all(y == x)

    # changed
    x[0] = 0 * u.m
    assert all(y == x)

    # ------------------
    # Recast arrays

    # array
    x = [1 * u.m, 2 * u.m, 3 * u.m]
    y = utils.as_quantity(x)
    assert all(y == [1, 2, 3] * u.m)

    # array, with conversion
    x = [1 * u.m, 200 * u.cm, 3 * u.m]
    y = utils.as_quantity(x)
    assert all(y == [1, 2, 3] * u.m)

    # ------------------
    # Failure Tests

    with pytest.raises(NotImplementedError):
        utils.as_quantity("arg")


# /def


# -------------------------------------------------------------------


def test_qsquare():
    """Test :func:`~macro_lightning.utils.qsquare`.

    Most tests are covered by `test_as_quantity`
    and numpy's internal testing for :func:`~numpy.square`

    """
    x = 2 * u.m
    y = utils.qsquare(x)
    assert y == x ** 2


# /def


# -------------------------------------------------------------------


def test_qnorm():
    """Test :func:`~macro_lightning.utils.qnorm`.

    Most tests are covered by `test_as_quantity`
    and numpy's internal testing for :func:`~numpy.square`

    """
    # norm a scalar
    x = -2 * u.m
    y = utils.qnorm(x)
    assert y == -x

    # norm an array
    x = [3, 4] * u.m
    y = utils.qnorm(x)
    assert y == 5 * u.m


# /def


##############################################################################
# END
