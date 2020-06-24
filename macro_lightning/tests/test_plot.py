# -*- coding: utf-8 -*-

"""test plot functions.

It's hard to test the exact plots, so we only test whether the plot function
successfully creates a plot.

"""


# __all__ = [
#     # functions
#     "",
#     # other
#     "",
# ]


##############################################################################
# IMPORTS

# BUILT-IN

# THIRD PARTY

# import astropy.units as u

import matplotlib.pyplot as plt

import numpy as np

import pytest


# PROJECT-SPECIFIC

from .. import plot


##############################################################################
# PARAMETERS

m_arr = np.logspace(1, 25)
ymin: float = 1e-15
ymax: float = 1e25

Mmicro = np.logspace(23.0, 28.0)

##############################################################################
# CODE
##############################################################################


@pytest.mark.mpl_image_compare
def test_plot_atomic_density_line():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(1, 1)
    plot.plot_atomic_density_line(m_arr)

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_nuclear_density_line():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(1, 1)
    plot.plot_nuclear_density_line(m_arr)

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_black_hole_line():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(1, 1)
    plot.plot_plot_black_hole_line(m_arr, ymin=ymin)

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_reference_densities():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(1, 1)
    plot.plot_reference_densities(m_arr, ymin=ymin)

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_mica_constraints():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(1, 1)
    plot.plot_mica_constraints()

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_white_dwarf_constraints():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(1, 1)
    plot.plot_white_dwarf_constraints()

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_cmb_constraints():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(1, 1)
    plot.plot_cmb_constraints(m_arr, ymax=ymax)

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_superbursts_constraints():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(1, 1)
    plot.plot_superbursts_constraints()

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_humandeath_constraints():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(1, 1)
    plot.plot_humandeath_constraints(m_arr)

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_dfn_constraints():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(1, 1)
    plot.plot_dfn_constraints(m_arr)

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_lensing_constraints():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(1, 1)
    plot.plot_lensing_constraints(Mmicro=Mmicro)

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_plot_black_hole_constraints():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(1, 1)
    plot.plot_black_hole_constraints(m_arr, ymin=ymin)

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_empty_constraint_plot():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(1, 1)

    with plot.constraint_plot(m_arr, ymin=ymin, ymax=ymax):
        pass

    # /with

    return fig


# /def


# -------------------------------------------------------------------


@pytest.mark.mpl_image_compare
def test_full_constraint_plot():
    """Test :func:`~macro_lightning.utils.as_quantity`."""
    fig, ax = plt.subplots(1, 1)

    with plot.constraint_plot(
        m_arr,
        ymin=ymin,
        ymax=ymax,
        # constraints
        mica_constr=True,
        WD_constr=True,
        CMB_constr=True,
        superbursts_constr=True,
        humandeath_constr=True,
        dfn_constr=True,
        lensing_constr=True,
        bh_constr=True,
    ):
        pass
    # /with

    return fig


# /def


# -------------------------------------------------------------------


##############################################################################
# END
