# -*- coding: utf-8 -*-

"""Plotting Functions."""

__author__ = ["Nathaniel Starkman", "Jagjit Sidhu", "Inherited Code People"]
__maintainer__ = "Nathaniel Starkman"

# __all__ = [
#     # functions
#     "",
#     # other
#     "",
# ]


##############################################################################
# IMPORTS

# BUILT-IN

from contextlib import contextmanager
import typing as T

# THIRD PARTY

from matplotlib import pyplot

import numpy as np


# PROJECT-SPECIFIC

from .misc import atomic_density, nuclear_density, black_hole, CMB, LMCTop
from . import data

##############################################################################
# PARAMETERS


##############################################################################
# CODE
##############################################################################

#####################################################################
# Reference Densities


def plot_atomic_density_line(mass: T.Sequence):
    """Plot Atomic Density Line.

    Returns
    -------
    `~matplotlib.lines.Line2D`

    """
    line = pyplot.loglog(
        mass,
        atomic_density(mass),
        "k",
        markersize=4,
        color="k",
        lw=1,
        label="Atomic density",
        zorder=0,
    )
    return line[0]


# /def


# -------------------------------------------------------------------


def plot_nuclear_density_line(mass: T.Sequence):
    """Plot Nuclear Density Line.

    Returns
    -------
    `~matplotlib.lines.Line2D`

    """
    line = pyplot.loglog(
        mass,
        nuclear_density(mass),
        "k",
        markersize=4,
        color="g",
        lw=2,
        label="Nuclear density",
        zorder=0,
    )
    return line[0]


# /def


# -------------------------------------------------------------------


def plot_black_hole_line(mass: T.Sequence, ymin: float):
    """Plot Black Hole Density Line and Constraint Region.

    This assumes that a macro cannot be denser than a black hole.

    Returns
    -------
    `~matplotlib.lines.Line2D`
    `~matplotlib.collections.PolyCollection`

    """
    line = pyplot.loglog(
        mass,
        black_hole(mass),
        "k",
        markersize=4,
        color="m",
        lw=3,
        label="Black holes",
        zorder=3,
    )
    fill = pyplot.fill_between(
        mass,
        ymin,
        black_hole(mass),
        where=None,
        color=["1"] * len(mass),
        edgecolor="",
        hatch="+",
        alpha=1,
        zorder=2,
    )
    return line[0], fill


# /def

# -------------------------------------------------------------------


def plot_reference_densities(mass: T.Sequence, ymin: float = 1e-15):
    """Plot Reference Density lines / constraints.

    - atomic density line
    - nuclear density line
    - black hole density line and constraint
        this assumes that macros cannot be denser than a black hole.

    Returns
    -------
    atom_line : `~matplotlib.lines.Line2D`
    nuc_line : `~matplotlib.lines.Line2D`
     bh_line : `~matplotlib.lines.Line2D`
    bh_fill : `~matplotlib.collections.PolyCollection`

    """
    atom_line = plot_atomic_density_line(mass)
    nuc_line = plot_nuclear_density_line(mass)
    bh_line, bh_fill = plot_black_hole_line(mass, ymin)

    return atom_line, nuc_line, bh_line, bh_fill


# /def


#####################################################################


def plot_mica_constraints(points: T.Optional[T.Sequence] = None):
    r"""Plot Constraints from Mica.

    A longstanding constraint comes from examination of a slab of
    ancient mica for tracks that would have been left by the passage of
    a macro moving at the typical speed of dark matter in the Galaxy.
    This was used to rule out macros of $M_x \leq 55\,$g for a wide
    range of cross sections [price]_, [derujula]_, [jacobs]_

    Parameters
    ----------
    points : ndarray, optional
        N x 2 array for a `~matplotlib.Polygon`
        if None (default) will load from :mod:`~src.data`

    Returns
    -------
    `~matplotlib.Polygon`

    References
    ----------
    .. [price] Price, P. (1988). Limits on Contribution of Cosmic Nuclearites
        to Galactic Dark MatterPhysical Review D, 38, 3813-3814.
    .. [derujula] De Rujula, A., & Glashow, S. (1984).
        Nuclearites: A Novel Form of Cosmic RadiationNature, 312, 734-737.
    .. [jacobs] David M. Jacobs, Glenn D. Starkman, & Bryan W. Lynn (2014).
        Macro Dark MatterMNRAS.

    """
    if points is None:
        points = data.load_mica_constraint()

    mica_poly = pyplot.Polygon(
        points,
        closed=None,
        fill=True,
        facecolor="yellow",
        edgecolor="black",
        alpha=0.8,
        hatch="|",
        lw=1,
        zorder=0,
    )
    pyplot.gca().add_line(mica_poly)

    return mica_poly


# /def

# -------------------------------------------------------------------


def plot_white_dwarf_constraints(points: T.Optional[T.Sequence] = None):
    r"""Plot Constraints from White Dwarfs.

    Parameters
    ----------
    points : ndarray, optional
        N x 2 array for a `~matplotlib.Polygon`
        if None (default) will load from :mod:`~src.data`

    Returns
    -------
    `~matplotlib.Polygon`

    """
    if points is None:
        points = data.WD  # TODO as function

    wd_poly = pyplot.Polygon(
        points,
        closed=None,
        fill=True,
        facecolor="blue",
        edgecolor="black",
        alpha=0.6,
        hatch="",
        lw=1,
        zorder=2,
    )
    pyplot.gca().add_line(wd_poly)

    return wd_poly


# /def


# -------------------------------------------------------------------


def plot_cmb_constraints(m_arr: T.Sequence, ymax: float):
    r"""Plot Constraints from the CMB.

    Parameters
    ----------
    m_arr : ndarray
    ymax : float

    Returns
    -------
    `~matplotlib.collections.PolyCollection`

    """
    cmb_fill = pyplot.fill_between(
        m_arr,
        CMB(m_arr),
        ymax,
        where=None,
        color="grey",
        edgecolor="black",
        hatch="",
        alpha=0.7,
        zorder=1,
    )

    return cmb_fill


# /def

# -------------------------------------------------------------------


def plot_superbursts_constraints(
    points1: T.Optional[T.Sequence] = None,
    points2: T.Optional[T.Sequence] = None,
):
    r"""Plot Constraints from Superbursts.

    Parameters
    ----------
    points1 : ndarray, optional
        N x 2 array for a `~matplotlib.Polygon`
        if None (default) will load from :mod:`~src.data`
    points2 : ndarray, optional
        N x 2 array for a `~matplotlib.Polygon`
        if None (default) will load from :mod:`~src.data`

    Returns
    -------
    superbursts1_poly : `~matplotlib.Polygon`
    superbursts2_poly : `~matplotlib.Polygon`

    """
    if points1 is None:
        points1 = data.load_superbursts_polygon()

    superbursts1_poly = pyplot.Polygon(
        points1,
        closed=None,
        fill=True,
        facecolor="purple",
        edgecolor="black",
        alpha=0.6,
        hatch="",
        lw=1,
        zorder=5,
    )
    pyplot.gca().add_line(superbursts1_poly)

    if points2 is None:
        points2 = data.load_superbursts1_polygon()

    superbursts2_poly = pyplot.Polygon(
        points2,
        closed=None,
        fill=True,
        facecolor="purple",
        edgecolor="black",
        alpha=0.6,
        hatch="//",
        lw=1,
        zorder=5,
    )
    pyplot.gca().add_line(superbursts2_poly)

    return superbursts1_poly, superbursts2_poly


# /def


# -------------------------------------------------------------------


def plot_humandeath_constraints(
    human_mass: T.Optional[T.Sequence] = None,
    human_xsec: T.Optional[T.Sequence] = None,
    human_upper: T.Optional[T.Sequence] = None,
):
    r"""Plot Constraints from dark matter caused human deaths.

    Parameters
    ----------
    human_mass : ndarray, optional
        N x 1 array for a `~fill_between`
        if None (default) will load from :mod:`~src.data`
    human_xsec : ndarray, optional
        N x 1 array for a `~fill_between`
        if None (default) will load from :mod:`~src.data`
    human_upper : ndarray, optional
        N x 1 array for a `~fill_between`
        if None (default) will load from :mod:`~src.data`

    Returns
    -------
    `~matplotlib.collections.PolyCollection`

    """
    if human_mass is None:
        human_mass = data.humanmass
    if human_xsec is None:
        human_xsec = data.humancross
    if human_upper is None:
        human_upper = data.humanupper

    human_fill = pyplot.fill_between(
        human_mass,
        human_xsec,
        human_upper,
        where=None,
        facecolor="red",
        edgecolor="black",
        hatch="",
        alpha=1.0,
        zorder=10,
    )

    # leghumans = pyplot.Rectangle(
    #     (0, 0), 1, 1, fc="purple", edgecolor="black", hatch="", alpha=0.6
    # )

    return human_fill


# /def


# -------------------------------------------------------------------


def plot_dfn_constraints(
    DFN_mass: T.Optional[T.Sequence] = None,
    DFN_xsec: T.Optional[T.Sequence] = None,
    DFN_upper: T.Optional[T.Sequence] = None,
):
    r"""Plot Constraints from Desert Fireball Network.

    Parameters
    ----------
    DFNmass : ndarray, optional
        N x 1 array for a `~fill_between`
        if None (default) will load from :mod:`~src.data`
    DFN_xsec : ndarray, optional
        N x 1 array for a `~fill_between`
        if None (default) will load from :mod:`~src.data`
    DFN_upper : ndarray, optional
        N x 1 array for a `~fill_between`
        if None (default) will load from :mod:`~src.data`

    Returns
    -------
    `~matplotlib.collections.PolyCollection`

    """
    if DFN_mass is None:
        DFN_mass = data.DFNmass
    if DFN_xsec is None:
        DFN_xsec = data.DFNcrosssection
    if DFN_upper is None:
        DFN_upper = data.DFNupper

    dfn_fill = pyplot.fill_between(
        DFN_mass,
        DFN_xsec,
        DFN_upper,
        where=None,
        facecolor="green",
        edgecolor="black",
        hatch="",
        alpha=1.0,
        zorder=6,
    )

    return dfn_fill


# /def


# -------------------------------------------------------------------


def plot_lensing_constraints(Mmicro: T.Optional[T.Sequence] = None,):
    r"""Plot Constraints from microlensing of the LMC.

    Parameters
    ----------
    Mmicro : ndarray, optional
        N x 1 array for a `~fill_between`
        if None (default) will ``np.logspace(23.0, 28.0)``

    Returns
    -------
    `~matplotlib.collections.PolyCollection`

    """
    if Mmicro is None:
        Mmicro = np.logspace(23.0, 28.0)

    micro_fill = pyplot.fill_between(
        Mmicro,
        black_hole(Mmicro),
        LMCTop(Mmicro),
        where=None,
        facecolor="brown",
        edgecolor="black",
        hatch="/",
        alpha=1,
        zorder=2,
    )

    return micro_fill


# /def

# -------------------------------------------------------------------


def plot_black_hole_constraints(m_arr: T.Sequence, ymin: float):
    r"""Plot Constraints from Black Holes.

    Parameters
    ----------
    m_arr : ndarray, optional
        N x 1 array for a `~fill_between`

    Returns
    -------
    `~matplotlib.collections.PolyCollection`

    """
    bh_fill = pyplot.fill_between(
        m_arr,
        ymin,
        black_hole(m_arr),
        where=None,
        color="1",
        edgecolor="",
        hatch="+",
        alpha=1,
        zorder=2,
    )

    return bh_fill


# /def


#####################################################################


@contextmanager
def constraint_plot(
    m_arr: T.Sequence,
    ymin: float = 1e-15,
    ymax: float = 1e25,
    *,
    mica_constr: bool = False,
    WD_constr: bool = False,
    CMB_constr: bool = False,
    superbursts_constr: bool = False,
    humandeath_constr: bool = False,
    dfn_constr: bool = False,
    lensing_constr: bool = False,
    bh_constr: bool = False,
):
    """Make standard constraint plot, with custom constraints in context.

    Custom constraints are created in the `with` statement

    Parameters
    ----------
    m_arr
    ymin : float
    ymax : float

    Examples
    --------
    In this example we make an empty constraint plot.
        >>> M = np.logspace(1, 25)
        >>> with constraint_plot(M, ymin=1e-15):
        ...     pass

    """
    # Code to acquire resource, e.g.:
    fig, ax = pyplot.subplots(figsize=(6, 4))

    ax.grid(True)

    ax.set_xlabel(r"$M_{X}$ [g]", fontsize=18)
    ax.set_xlim([m_arr.min(), m_arr.max()])

    ax.set_ylim(ymin, ymax)  # min/max of nuclear_density(M1)
    ax.set_ylabel(r"$\sigma_{X}$ [cm$^{2}$]", fontsize=18)

    plot_reference_densities(m_arr)

    # previous constraints

    if mica_constr:
        plot_mica_constraints()
    if WD_constr:
        plot_white_dwarf_constraints()
    if CMB_constr:
        plot_cmb_constraints(m_arr, ymax=ymax)
    if superbursts_constr:
        plot_superbursts_constraints()
    if humandeath_constr:
        plot_humandeath_constraints()
    if dfn_constr:
        plot_dfn_constraints()
    if lensing_constr:
        plot_lensing_constraints(Mmicro=None)
    if bh_constr:
        plot_black_hole_constraints(m_arr, ymin=ymin)

    try:
        yield ax, m_arr, ymin, ymax

    finally:

        ax.legend(loc="upper left", shadow=True)
        pyplot.tight_layout()


# /def


##############################################################################
# END
