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

# PROJECT-SPECIFIC


##############################################################################
# PARAMETERS

PI = np.pi


##############################################################################
# CODE
##############################################################################


def CMB(M):
    """CMB."""  # TODO document
    return 4.5e-7 * M


# /def


# -------------------------------------------------------------------


def nuclear_density(M):
    """Nuclear Density."""  # TODO document
    f = PI * (3 / (4 * PI * 3.6e14)) ** (2.0 / 3) * np.power(M, 2.0 / 3.0)
    return f


# /def


# -------------------------------------------------------------------


def black_hole(M):
    """Black Holes."""  # TODO document
    f = PI * (3e5) ** 2 * (M / (2e33)) ** 2
    return f


# /def


# -------------------------------------------------------------------


def atomic_density(M):
    """Atomic Density."""  # TODO document
    f = PI * (3 / (4 * PI * 1e0)) ** (2.0 / 3) * pow(M, 2.0 / 3)
    return f


# /def


# -------------------------------------------------------------------


def KeplerTop(M):
    """Kepler Best Observation."""  # TODO document
    f = 1e-6 * M
    return f


# /def


# -------------------------------------------------------------------


def LMCTop(M):
    """LMC Best Observation."""  # TODO document
    f = 1e-4 * M
    return f


# /def

# -------------------------------------------------------------------


##############################################################################
# END
