# -*- coding: utf-8 -*-

"""Plotting Functions."""

__author__ = ["Nathaniel Starkman", "Jagjit Sidhu", "Inherited Code People"]
__maintainer__ = "Nathaniel Starkman"

__all__ = [
    # density lines
    "plot_atomic_density_line",
    "plot_nuclear_density_line",
    "plot_black_hole_line",
    "plot_reference_densities",
    # constraints
    "plot_mica_constraints",
    "plot_white_dwarf_constraints",
    "plot_cmb_constraints",
    "plot_superbursts_constraints",
    "plot_humandeath_constraints",
    "plot_dfn_constraints",
    "plot_lensing_constraints",
    "plot_black_hole_constraints",
    # contextmanager
    "constraints_plot",
]


##############################################################################
# IMPORTS

# BUILT-IN

from contextlib import contextmanager
import typing as T

# THIRD PARTY

from matplotlib import pyplot

import numpy as np


# PROJECT-SPECIFIC

from .physics import atomic_density, nuclear_density, black_hole, CMB, LMCTop
from . import data


##############################################################################
# PARAMETERS


##############################################################################
# CODE
##############################################################################

#####################################################################
# Reference Densities


def plot_atomic_density_line(mass: T.Sequence, label=True):
    r"""Plot Atomic Density Line.

    Parameters
    ----------
    mass : Sequence
        used in atomic_density(mass)

    Returns
    -------
    :class:`~matplotlib.lines.Line2D`

    Other Parameters
    ----------------
    label : bool
        Whether to add the label r"$\rho_{atomic}$"

    Notes
    -----
    Plot properties:

        - color : black
        - markersize : 4
        - linewidth : 1

    See Also
    --------
    :func:`~macro_lightning.plot.plot_reference_densities`

    """
    line = pyplot.loglog(
        mass,
        atomic_density(mass),
        "k",
        markersize=4,
        color="k",
        lw=1,
        label=r"$\rho_{atomic}$" if label else None,
        zorder=0,
    )
    return line[0]


# /def


# -------------------------------------------------------------------


def plot_nuclear_density_line(mass: T.Sequence, label=True):
    r"""Plot Nuclear Density Line.

    Parameters
    ----------
    mass : Sequence
        used in atomic_density(mass)

    Returns
    -------
    `~matplotlib.lines.Line2D`

    Other Parameters
    ----------------
    label : bool
        whether to add the label r"$\rho_{nuclear}$"

    Notes
    -----
    Plot properties:

        - color : green
        - markersize : 4
        - linewidth : 2

    See Also
    --------
    :func:`~macro_lightning.plot.plot_reference_densities`

    """
    line = pyplot.loglog(
        mass,
        nuclear_density(mass),
        markersize=4,
        color="g",
        lw=2,
        label=r"$\rho_{nuclear}$" if label else None,
        zorder=0,
    )
    return line[0]


# /def


# -------------------------------------------------------------------


def plot_black_hole_line(mass: T.Sequence, label=True):
    r"""Plot Black Hole Density Line.

    Parameters
    ----------
    mass : Sequence
        used in atomic_density(mass)

    Returns
    -------
    `~matplotlib.lines.Line2D`

    Other Parameters
    ----------------
    label : bool
        whether to add the label r"$\rho_{BH}$"

    Notes
    -----
    Plot properties:

        - color : black
        - markersize : 4
        - linewidth : 3

    See Also
    --------
    :func:`~macro_lightning.plot.plot_reference_densities`

    """
    line = pyplot.loglog(
        mass,
        black_hole(mass),
        markersize=4,
        color="k",
        lw=3,
        label=r"$\rho_{BH}$" if label else None,
        zorder=3,
    )
    return line[0]


# /def

# -------------------------------------------------------------------


def plot_reference_densities(
    mass: T.Sequence, label=True
):
    """Plot Reference Density lines / constraints.

    - atomic density line
    - nuclear density line
    - black hole density line

    Parameters
    ----------
    mass : Sequence
        used in atomic_density(mass)

    Returns
    -------
    atom_line : :class:`~matplotlib.lines.Line2D`
        see `plot_atomic_density_line`
    nuc_line : :class:`~matplotlib.lines.Line2D`
        see `plot_nuclear_density_line`
    bh_line : :class:`~matplotlib.lines.Line2D`
        see `plot_black_hole_line`

    Other Parameters
    ----------------
    label : bool
        whether to add the labels to the lines.

    See Also
    --------
    :func:`~macro_lightning.plot.plot_atomic_density_line`
    :func:`~macro_lightning.plot.plot_nuclear_density_line`
    :func:`~macro_lightning.plot.plot_black_hole_line`

    """
    atom_line = plot_atomic_density_line(mass, label=label)
    nuc_line = plot_nuclear_density_line(mass, label=label)
    bh_line = plot_black_hole_line(mass, label=label)

    return atom_line, nuc_line, bh_line


# /def


#####################################################################


def plot_mica_constraints(points: T.Optional[T.Sequence] = None, label=False):
    r"""Plot Constraints from Mica.

    A longstanding constraint comes from examination of a slab of
    ancient mica for tracks that would have been left by the passage of
    a macro moving at the typical speed of dark matter in the Galaxy.
    This was used to rule out macros of :math:`M_x \leq 55\,` g for a wide
    range of cross sections [1]_, [2]_, [3]_

    Parameters
    ----------
    points : ndarray, optional
        N x 2 array for a `~matplotlib.Polygon`
        if None (default) will load from :mod:`~macro_lightning.data`

    Returns
    -------
    :class:`~matplotlib.patches.Polygon`

    Other Parameters
    ----------------
    label : bool
        whether to add the label 'Mica'

    Notes
    -----
    plot properties:

        - facecolor: yellow
        - edgecolor: black
        - hatched: |
        - linewidth: 1
        -  alpha: 0.8

    References
    ----------
    .. [1] Price, P. (1988). Limits on Contribution of Cosmic Nuclearites
        to Galactic Dark MatterPhysical Review D, 38, 3813-3814.
    .. [2] De Rujula, A., & Glashow, S. (1984).
        Nuclearites: A Novel Form of Cosmic RadiationNature, 312, 734-737.
    .. [3] David M. Jacobs, Glenn D. Starkman, & Bryan W. Lynn (2014).
        Macro Dark MatterMNRAS.

    See Also
    --------
    :func:`~macro_lightning.plot.constraints_plot`

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
        label="Mica" if label else None,
    )
    pyplot.gca().add_patch(mica_poly)

    return mica_poly


# /def


# -------------------------------------------------------------------


def plot_white_dwarf_constraints(
    points: T.Optional[T.Sequence] = None, label=False
):
    r"""Plot Constraints from the existence of massive White Dwarfs.

    For sufficiently large cross-sections, the linear energy deposition could
    produce observable signals if a macro were to pass through compact objects
    such as white dwarfs in the form of thermonuclear runaway leading to a
    type IA supernova. These are weaker than previously inferred [2]_ in
    important respects because of more careful treatment of the passage of a
    macro through the white dwarf and greater conservatism regarding the size
    of the region that must be heated to initiate runaway. On the other hand,
    more stringent constraints are placed on macros at low cross-section,
    using new data from the Montreal White Dwarf Database [1]_.

    Parameters
    ----------
    points : ndarray, optional
        N x 2 array for a `~matplotlib.Polygon`
        if None (default) will load from :mod:`~macro_lightning.data`

    Returns
    -------
    :class:`~matplotlib.patches.Polygon`

    Other Parameters
    ----------------
    label : bool
        whether to add the label 'WD'

    Notes
    -----
    plot properties:

        - facecolor: blue
        - edgecolor: black
        - linewidth: 1
        - alpha: 0.6

    References
    ----------
    .. [1] J. S. Sidhu and G. D. Starkman, Physical Review D 101 (2020),
        0.1103/physrevd.101.083503.
    .. [2] P. Graham, R. Janish, V. Narayan, S. Rajendran, and P. Riggins,
       Physical Review D 98, 115027 (2018).

    See Also
    --------
    :func:`~macro_lightning.plot.constraints_plot`

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
        label="WD" if label else None,
    )
    pyplot.gca().add_patch(wd_poly)

    return wd_poly


# /def


# -------------------------------------------------------------------


def plot_superbursts_constraints(
    points1: T.Optional[T.Sequence] = None,
    points2: T.Optional[T.Sequence] = None,
    label=False,
):
    r"""Plot Constraints from Superbursts in Neutron Stars.

    For sufficiently large cross-sections, the linear energy deposition could
    produce observable signals if a macro were to pass through compact objects
    such as neutron stars in the form of thermonuclear runaway, leading to a
    superburst. New constraints are inferred from the low mass X-ray
    binary 4U 1820-30, in which more than a decade passed between successive
    superbursts [1]_.

    Parameters
    ----------
    points1 : ndarray, optional
        N x 2 array for a `~matplotlib.Polygon`
        if None (default) will load from :mod:`~macro_lightning.data`
    points2 : ndarray, optional
        N x 2 array for a `~matplotlib.Polygon`
        if None (default) will load from :mod:`~macro_lightning.data`

    Returns
    -------
    superbursts1_poly : :class:`~matplotlib.patches.Polygon`
    superbursts2_poly : :class:`~matplotlib.patches.Polygon`

    Other Parameters
    ----------------
    label : bool
        whether to add the label 'superbursts'

    Notes
    -----
    plot properties:

        - facecolor: purple
        - edgecolor: black
        - alpha: 0.6

    References
    ----------
    .. [1] J. S. Sidhu and G. D. Starkman, Physical Review D 101 (2020),
        0.1103/physrevd.101.083503.

    See Also
    --------
    :func:`~macro_lightning.plot.constraints_plot`

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
        label="superbursts" if label else None,
    )
    pyplot.gca().add_patch(superbursts1_poly)

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
    pyplot.gca().add_patch(superbursts2_poly)

    return superbursts1_poly, superbursts2_poly


# /def


# -------------------------------------------------------------------


def plot_cmb_constraints(m_arr: T.Sequence, sigmax: float, label=False):
    r"""Plot Constraints from the CMB.

    Wilkinson et al. [1] utilized the full Boltzmann formalism to
    obtain constraints from macro-photon elastic scattering using the first
    year release of Planck data.

    Parameters
    ----------
    m_arr : ndarray
    sigmax : float
        maximum plotted sigma

    Returns
    -------
    :class:`~matplotlib.collections.PolyCollection`

    Other Parameters
    ----------------
    label : bool
        whether to add the label 'CMB'

    Notes
    -----
    plot properties:

        - facecolor: grey
        - edgecolor: black
        - alpha: 0.7

    References
    ----------
    .. [1] R. J. Wilkinson, J. Lesgourgues, and C. Bœhm,
        Journal of Cosmology and Astroparticle Physics 2014, 026 (2014)

    See Also
    --------
    :func:`~macro_lightning.plot.constraints_plot`

    """
    cmb_fill = pyplot.fill_between(
        m_arr,
        CMB(m_arr),
        sigmax,
        where=None,
        color="grey",
        edgecolor="black",
        hatch="",
        alpha=0.7,
        zorder=1,
        label="CMB" if label else None,
    )

    return cmb_fill


# /def


# -------------------------------------------------------------------


def plot_humandeath_constraints(
    human_mass: T.Optional[T.Sequence] = None,
    human_xsec: T.Optional[T.Sequence] = None,
    human_upper: T.Optional[T.Sequence] = None,
    label=False,
):
    r"""Plot Constraints from dark matter caused human deaths.

    Macroscopic dark matter (macros) refers to a class of dark matter
    candidates that scatter elastically off of ordinary matter with a large
    geometric cross-section. A wide range of macro masses :math:`M_X` and
    cross-sections :math:`\sigma_X` remain unprobed. Over a wide region within
    the unexplored parameter space, collisions of a macro with a human body
    would result in serious injury or death. The absence of such unexplained
    impacts with a well-monitored subset of the human population to exclude a
    region bounded by :math:`\sigma_X > 10^{−8} − 10^{−7}` cm2 and :math:`M_X
    < 50` kg [1].

    Parameters
    ----------
    human_mass : ndarray, optional
        N x 1 array for a :class:`~matplotlib.pyplot.fill_between`
        if None (default) will load from :mod:`~macro_lightning.data`
    human_xsec : ndarray, optional
        N x 1 array for a `~fill_between`
        if None (default) will load from :mod:`~macro_lightning.data`
    human_upper : ndarray, optional
        N x 1 array for a `~fill_between`
        if None (default) will load from :mod:`~macro_lightning.data`

    Returns
    -------
    :class:`~matplotlib.collections.PolyCollection`

    Other Parameters
    ----------------
    label : bool
        whether to add the label 'death'

    References
    ----------
    .. [1] J. S. Sidhu, R. Scherrer, and G. Starkman,
        Physics Let- ters B 803, 135300 (2020).

    See Also
    --------
    :func:`~macro_lightning.plot.constraints_plot`

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
        zorder=9,
        label="death" if label else None,
    )

    return human_fill


# /def


# -------------------------------------------------------------------


def plot_dfn_constraints(
    DFN_mass: T.Optional[T.Sequence] = None,
    DFN_xsec: T.Optional[T.Sequence] = None,
    DFN_upper: T.Optional[T.Sequence] = None,
    label=False,
):
    r"""Plot Constraints from Desert Fireball Network (DFN).

    Constraints for low mass macros from the null observation of bright
    meteors formed by a passing macro, across two extensive networks of
    cameras built originally to observe meteorites. The parameter space that
    could be probed with planned upgrades to the existing array of cameras in
    one of these networks still currently in use, the Desert Fireball Network
    in Australia, is estimated [1]_.

    Parameters
    ----------
    DFNmass : ndarray, optional
        N x 1 array for a :class:`~matplotlib.pyplot.fill_between`
        if None (default) will load from :mod:`~macro_lightning.data`
    DFN_xsec : ndarray, optional
        N x 1 array for a `~fill_between`
        if None (default) will load from :mod:`~macro_lightning.data`
    DFN_upper : ndarray, optional
        N x 1 array for a `~fill_between`
        if None (default) will load from :mod:`~macro_lightning.data`

    Returns
    -------
    :class:`~matplotlib.collections.PolyCollection`

    Other Parameters
    ----------------
    label : bool
        whether to add the label 'DFN'

    References
    ----------
    .. [1] J. S. Sidhu and G. Starkman, Physical Review D 100 (2019),
        10.1103/physrevd.100.123008.

    See Also
    --------
    :func:`~macro_lightning.plot.constraints_plot`

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
        label="DFN" if label else None,
    )

    return dfn_fill


# /def


# -------------------------------------------------------------------


def plot_lensing_constraints(
    Mmicro: T.Optional[T.Sequence] = None, label=False
):
    r"""Plot Constraints from microlensing of the LMC.

    Parameters
    ----------
    Mmicro : ndarray, optional
        N x 1 array for a :class:`~matplotlib.pyplot.fill_between`
        if None (default) will ``np.logspace(23.0, 28.0)``

    Returns
    -------
    :class:`~matplotlib.collections.PolyCollection`

    Other Parameters
    ----------------
    label : bool
        whether to add the label "$\mu$-lense"

    References
    ----------
    .. [1] C. Alcock et al., The Astrophysical Journal 550, L169 (2001).
    .. [2] K. Griest, A. M. Cieplak, and M. J. Lehner, Physical
        Review Letters 111, 181302 (2013).
    .. [3] P. Tisserand et al., Astronomy & Astrophysics 469, 387 (2007).
    .. [4] B. J. Carr, K. Kohri, Y. Sendouda, and J. Yokoyama,
        Physical Review D 81, 104019 (2010).
    .. [5] H. Niikura et al., Nature Astronomy 3, 524 (2019)


    See Also
    --------
    :func:`~macro_lightning.plot.constraints_plot`

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
        label=r"$\mu$-lense" if label else None,
    )

    return micro_fill


# /def

# -------------------------------------------------------------------


def plot_black_hole_constraints(m_arr: T.Sequence, sigmin: float, label=False):
    r"""Plot Constraints from Black Holes.

    Parameters
    ----------
    m_arr : ndarray, optional
        N x 1 array for a :class:`~matplotlib.pyplot.fill_between`
    sigmin : float
        minimum plotted sigma

    Returns
    -------
    :class:`~matplotlib.collections.PolyCollection`

    Other Parameters
    ----------------
    label : bool
        whether to add the label "BH"

    See Also
    --------
    :func:`~macro_lightning.plot.constraints_plot`

    """
    bh_fill = pyplot.fill_between(
        m_arr,
        sigmin,
        black_hole(m_arr),
        where=None,
        color="gray",
        edgecolor="",
        hatch="+",
        alpha=0.5,
        zorder=2,
        label="BH" if label else None,
    )

    return bh_fill


# /def


#####################################################################


@contextmanager
def constraints_plot(
    m_arr: T.Sequence,
    sigmin: float = 1e-15,
    sigmax: float = 1e25,
    *,
    constr_labels=False,
    mica_constr: bool = False,
    CMB_constr: bool = False,
    WD_constr: bool = False,
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
    m_arr : Sequence
        mass array
    sigmin : float
        minimum plotted sigma
    sigmax : float
        maximum plotted sigma
    constr_labels : bool
        whether to add labels to all the `Other Parameters`

    Yields
    ------
    fig : :class:`~matplotlib.Figure`
    ax : :class:`~matplotlib.Axes`
    m_arr : Sequence
        mass array
    sigmin : float
        minimum plotted sigma
    sigmax : float
        maximum plotted sigma

    Other Parameters
    ----------------
    mica_constr: bool
        Whether to label the mica constraints (default False)
        References : [1]_, [2]_, [3]_
        See :func:`~macro_lightning.plot.plot_mica_constraints`
    CMB_constr: bool
        Whether to label the CMB constraints (default False).
        References : [5]_
        See :func:`~macro_lightning.plot.plot_cmb_constraints`
    WD_constr: bool
        Whether to label the White Dwarf constraints (default False).
        References : [4]_
        See :func:`~macro_lightning.plot.plot_white_dwarf_constraints`
    superbursts_constr: bool
        Whether to label the superbursts constraints (default False).
        References : [4]_
        See :func:`~macro_lightning.plot.plot_superbursts_constraints`
    humandeath_constr: bool
        Whether to label the human-death constraints (default False).
        References : [6]_
        See :func:`~macro_lightning.plot.plot_humandeath_constraints`
    dfn_constr: bool
        Whether to label the Desert Fireball Network constraints (default False).
        References : [7]_
        See :func:`~macro_lightning.plot.plot_dfn_constraints`
    lensing_constr: bool
        Whether to label the micro-lensing constraints (default False).
        References : [8]_, [9]_, [10]_, [11]_, [12]_
        See :func:`~macro_lightning.plot.plot_lensing_constraints`
    bh_constr: bool
        Whether to label the black hole constraints (default False).
        See :func:`~macro_lightning.plot.plot_black_hole_constraints`

    Examples
    --------
    In this example we make an empty constraint plot.
        >>> M = np.logspace(1, 25)
        >>> with constraints_plot(M, sigmin=1e-15):
        ...     pass

    References
    ----------
    .. [1] Price, P. (1988). Limits on Contribution of Cosmic Nuclearites
        to Galactic Dark MatterPhysical Review D, 38, 3813-3814.
    .. [2] De Rujula, A., & Glashow, S. (1984).
        Nuclearites: A Novel Form of Cosmic RadiationNature, 312, 734-737.
    .. [3] David M. Jacobs, Glenn D. Starkman, & Bryan W. Lynn (2014).
        Macro Dark MatterMNRAS.
    .. [4] R. J. Wilkinson, J. Lesgourgues, and C. Bœhm,
        Journal of Cosmology and Astroparticle Physics 2014, 026 (2014)
    .. [5] J. S. Sidhu and G. D. Starkman, Physical Review D 101 (2020),
        0.1103/physrevd.101.083503.
    .. [6] J. S. Sidhu, R. Scherrer, and G. Starkman,
        Physics Letters B 803, 135300 (2020).
    .. [7] J. S. Sidhu and G. Starkman, Physical Review D 100 (2019),
        10.1103/physrevd.100.123008.
    .. [8] C. Alcock et al., The Astrophysical Journal 550, L169 (2001).
    .. [9] K. Griest, A. M. Cieplak, and M. J. Lehner, Physical
        Review Letters 111, 181302 (2013).
    .. [10] P. Tisserand et al., Astronomy & Astrophysics 469, 387 (2007).
    .. [11] B. J. Carr, K. Kohri, Y. Sendouda, and J. Yokoyama,
        Physical Review D 81, 104019 (2010).
    .. [12] H. Niikura et al., Nature Astronomy 3, 524 (2019)

    """
    fig, ax = pyplot.subplots(figsize=(6, 4))
    ax.grid(True)

    ax.set_xlabel(r"$M_{X}$ [g]", fontsize=18)
    ax.set_xlim([m_arr.min(), m_arr.max()])

    ax.set_ylim(sigmin, sigmax)  # min/max of nuclear_density(M1)
    ax.set_ylabel(r"$\sigma_{X}$ [cm$^{2}$]", fontsize=18)

    plot_reference_densities(m_arr)

    # previous constraints

    if mica_constr:
        plot_mica_constraints(label=constr_labels)
    if WD_constr:
        plot_white_dwarf_constraints(label=constr_labels)
    if CMB_constr:
        plot_cmb_constraints(m_arr, sigmax=sigmax, label=constr_labels)
    if superbursts_constr:
        plot_superbursts_constraints(label=constr_labels)
    if humandeath_constr:
        plot_humandeath_constraints(label=constr_labels)
    if dfn_constr:
        plot_dfn_constraints(label=constr_labels)
    if lensing_constr:
        plot_lensing_constraints(Mmicro=None, label=constr_labels)
    if bh_constr:
        plot_black_hole_constraints(m_arr, sigmin=sigmin, label=constr_labels)

    try:
        yield fig, ax, m_arr, sigmin, sigmax

    finally:

        ax.legend(loc="upper left", shadow=True, zorder=100)
        pyplot.tight_layout()


# /def


##############################################################################
# END
