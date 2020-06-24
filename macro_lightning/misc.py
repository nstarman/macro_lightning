# -*- coding: utf-8 -*-

"""Miscellaneous Functions, TO SORT."""


__all__ = [
    "CMB",
    "nuclear_density",
    "BH",
    "atomic_density",
    "KeplerTop",
    "LMCTop",
]


##############################################################################
# IMPORTS

# BUILT-IN


# THIRD PARTY

import numpy as np

from utilipy.utils.typing import array_like


# PROJECT-SPECIFIC


##############################################################################
# PARAMETERS

PI = np.pi


##############################################################################
# CODE
##############################################################################


def CMB(M: array_like) -> array_like:
    """CMB."""  # TODO document
    return 4.5e-7 * M


# /def


# -------------------------------------------------------------------


def nuclear_density(M: array_like) -> array_like:
    """Nuclear Density."""  # TODO document
    volume = 4.0 / 3.0 * PI * 3.6e14
    out = PI * np.power(M / volume, 2.0 / 3)
    return out


# /def


# -------------------------------------------------------------------


def black_hole(M: array_like) -> array_like:
    """Black Holes."""  # TODO document
    return PI * (3e5) ** 2 * (M / (2e33)) ** 2.


# /def


# -------------------------------------------------------------------


def atomic_density(M: array_like) -> array_like:
    """Atomic Density."""  # TODO document
    volume = 4. / 3. * PI * 1e0
    out = PI * np.power(M / volume, 2.0 / 3.)
    return out


# /def


# -------------------------------------------------------------------


def KeplerTop(M: array_like) -> array_like:
    """Kepler Best Observation."""  # TODO document
    return 1e-6 * M


# /def


# -------------------------------------------------------------------


def LMCTop(M: array_like) -> array_like:
    """LMC Best Observation."""  # TODO document
    return 1e-4 * M


# /def

# -------------------------------------------------------------------


##############################################################################
# END
