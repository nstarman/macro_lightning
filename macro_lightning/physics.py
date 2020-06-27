# -*- coding: utf-8 -*-

"""Physics Functions."""


__all__ = [
    "CMB",
    "nuclear_density",
    "black_hole",
    "atomic_density",
    "KeplerTop",
    "LMCTop",
    "twobody_vesc",
    "multibody_vesc",
    "calculate_Mx",
    "calculate_Sx",
    "calculate_Mx_and_Sx",
]


##############################################################################
# IMPORTS

# BUILT-IN

import itertools
import functools
import typing as T

# THIRD PARTY

import astropy.units as u
from astropy.utils.decorators import format_doc

import numpy as np

from tqdm import tqdm


# PROJECT-SPECIFIC

from .utils import as_quantity, qnorm


##############################################################################
# PARAMETERS

_KMS = u.km / u.s

_sqrt2 = np.sqrt(2)


##############################################################################
# CODE
##############################################################################


def CMB(M: T.Sequence) -> T.Sequence:
    """CMB."""  # TODO document
    return M * 4.5e-7


# /def


# -------------------------------------------------------------------


def nuclear_density(M: T.Sequence) -> T.Sequence:
    """Nuclear Density."""  # TODO document
    volume = 4.0 / 3.0 * np.pi * 3.6e14
    out = np.pi * np.power(M / volume, 2.0 / 3)
    return out


# /def


# -------------------------------------------------------------------


def black_hole(M: T.Sequence) -> T.Sequence:
    """Black Holes."""  # TODO document
    return np.pi * (3e5) ** 2 * (M / (2e33)) ** 2.0


# /def


# -------------------------------------------------------------------


def atomic_density(M: T.Sequence) -> T.Sequence:
    """Atomic Density."""  # TODO document
    volume = 4.0 / 3.0 * np.pi * 1e0
    out = np.pi * np.power(M / volume, 2.0 / 3.0)
    return out


# /def


# -------------------------------------------------------------------


def KeplerTop(M: T.Sequence) -> T.Sequence:
    """Kepler Best Observation."""  # TODO document
    return 1e-6 * M


# /def


# -------------------------------------------------------------------


def LMCTop(M: T.Sequence) -> T.Sequence:
    """LMC Best Observation."""  # TODO document
    return 1e-4 * M


# /def

# -------------------------------------------------------------------


@u.quantity_input(vx="speed", vbin="speed", vvir="speed")
def f_BM_bin(vx, vbin, vvir):
    """Equation 3 of [1]_, binned.

    Parameters
    ----------
    vx : Quantity
        With physical type "speed"
    vvir : Quantity
        The virial velocity
        With physical type "speed"

    Returns
    -------
    Quantity

    References
    ----------
    .. [1] J.  S.  Sidhu  and  G.  Starkman,  Physical  Review  D
         100(2019), 10.1103/physrevd.100.123008.

    """
    norm = (vbin / vvir) ** 3 / np.power(np.pi, 3.0 / 2.0)
    exp = np.exp(-np.square(vx / vvir))

    return norm * exp


# /def

# -------------------------------------------------------------------


def _norm_v1_v2(v1: T.Sequence, v2: T.Sequence) -> T.Sequence:
    return np.sqrt(v1 ** 2.0 + v2 ** 2.0)


# /def


_multibody_escape_wikipedia = r"""
    When escaping a compound system, such as a moon orbiting a planet or a
    planet orbiting a sun, a rocket that leaves at escape velocity (ve1) for
    the first (orbiting) body, (e.g. Earth) will not travel to an infinite
    distance because it needs an even higher speed to escape gravity of the
    second body (e.g. the Sun). Near the Earth, the rocket's trajectory will
    appear parabolic, but it will still be gravitationally bound to the second
    body and will enter an elliptical orbit around that body, with an orbital
    speed similar to the first body.

    To escape the gravity of the second body once it has escaped the first
    body the rocket will need to be traveling at the escape velocity for the
    second body (ve2) (at the orbital distance of the first body). However,
    when the rocket escapes the first body it will still have the same orbital
    speed around the second body that the first body has (vo). So its excess
    velocity as it escapes the first body will need to be the difference
    between the orbital velocity and the escape velocity. With a circular
    orbit, escape velocity is sqrt(2) times the orbital speed. Thus the total
    escape velocity vte when leaving one body orbiting a second and seeking to
    escape them both is, under simplified assumptions:

    .. math::

        v_{te}=\sqrt{(v_{e2} - v_o)^2 + v_{e1}^2}
        = \sqrt{\left(k v_{e2}\right)^2 + v_{e1}^2}

    where :math:`k=1−1/\sqrt{2} \sim 0.2929` for circular orbits.
"""  # TODO instead indent by function


@format_doc(None, wikipedia=_multibody_escape_wikipedia)
def twobody_vesc(
    ve1, ve2, vo: T.Union[None, T.Sequence] = None,
):
    r"""Two-body escape velocity.

    Parameters
    ----------
    ve1, ve2: :class:`~astropy.units.Quantity`
        Escape velocities.
    vo : Quantity or None, optional
        The orbital velocity of object 1 around object 2.

    Returns
    -------
    vesc : :class:`~astropy.units.Quantity`
        The compound escape velocity.

    Examples
    --------
    For a Galactic macro falling into the potential well of the Earth,
    the minimum observed velocity

        >>> vesc_earth = 11.186 * u.km / u.s
        >>> vesc_sun_at_earth = 42.1 * u.km / u.s
        >>> twobody_vesc(vesc_earth, vesc_sun_at_earth)
        <Quantity 16.6485836 km / s>

    Notes
    -----
    From `Wikipedia <https://en.wikipedia.org/wiki/Escape_velocity>`_ [1]_:

    {wikipedia}

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Escape_velocity

    See Also
    --------
    :func:`~macro_lightning.physics.multibody_vesc`

    """
    vo = vo or ve2 / _sqrt2  # None -> circular

    return np.sqrt(ve1 ** 2 + (ve2 - vo) ** 2)


# /def


@format_doc(None, wikipedia=_multibody_escape_wikipedia)
def multibody_vesc(
    *vescs, vo: T.Union[None, T.Sequence] = None, accumulate: bool = False,
):
    """Multi-body escape velocity.

    Parameters
    ----------
    *vescs: Quantity
        velocities, ordered from 1st to last body.

    vo : list of Quantity or None, optional
        The orbital velocity of object vescs[i+1] around object vescs[i].
        if list of quantities, must match vescs in length
        if None (default) then orbits are assumed circular.

    accumulate : bool
        whether to return the accumulative escape velocity for each larger
        system (True), or just the total escape velocity (False, default).

    Returns
    -------
    :class:`~astropy.units.Quantity`
        The compound escape velocity
        if `accumulate` False (default) then scalar, else accumulated vector.

    Examples
    --------
    For a Galactic macro falling into the potential well of the Earth,
    the minimum observed velocity

        >>> vesc_earth = 11.186 * u.km / u.s
        >>> vesc_sun_at_earth = 42.1 * u.km / u.s
        >>> vesc_gal_at_sun = 550 * u.km / u.s
        >>> multibody_vesc(vesc_earth, vesc_sun_at_earth, vesc_gal_at_sun)
        <Quantity 161.94929058 km / s>

    Notes
    -----
    From `Wikipedia <https://en.wikipedia.org/wiki/Escape_velocity>`_ [1]_:

    {wikipedia}

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Escape_velocity

    See Also
    --------
    :func:`~macro_lightning.physics.twobody_vesc`

    """
    vs: u.Quantity = as_quantity(vescs)

    if vo is None:
        vs[1:] = vs[1:] * (1 - 1 / np.sqrt(2))
    else:
        vs[1:] = vs[1:] - vo

    if accumulate:
        return as_quantity(itertools.accumulate(vs, _norm_v1_v2))
    else:
        return functools.reduce(_norm_v1_v2, vs)


# /def


# -------------------------------------------------------------------


@u.quantity_input(
    vels="speed",
    vvir="speed",
    vesc="speed",
    vstep="speed",
    vmin="speed",
    vcirc="speed",
)
def calculate_Mx(vels, vvir, vesc, vcirc, vmin, Arho, m_unit=u.g):
    """Calculate Mx.

    Parameters
    ----------
    vels : Sequence
        an array of velocities, treated as along one Cartesian component.
        must be evenly spaced
    vvir : Quantity
        virial velocity
    vesc : Quantity
        Galactocentric escape velocity
    vcirc : Quantity
        Galactocentric circular velocity
    vmin : Quantity
        infall velocity of a macro to the Earth.

    Returns
    -------
    Mxs : Sequence
    vbar : Quantity
    Vhold : Quantity

    Other Parameters
    ----------------
    m_unit : :class:`~astropy.units.Unit`

    Notes
    -----
    this is not a particularly efficient calculation method.

    """
    vbar = 0.0 * u.km / u.s
    Vhold = 800.0 * u.km / u.s

    steps = np.diff(vels)
    if not np.allclose(steps[:-1], steps[1:]):  # check all close
        raise ValueError("vels steps unequal in size.")
    else:
        vstep = np.abs(steps[0])  # positive

    Mxs = np.zeros(len(vels) ** 3) * m_unit
    iterator = itertools.product(vels, vels, vels)

    for i, (vx, vy, vz) in tqdm(enumerate(iterator), total=len(Mxs)):
        if qnorm(vx, vy, vz) <= vesc:
            maxwellian = f_BM_bin(qnorm(vx, vy, vz), vbin=vstep, vvir=vvir)
            vrel = qnorm(vmin, vx, vy - vcirc, vz)

            vbar = vbar + vrel * maxwellian  # cumulative

            mx = Arho * vbar

            Mxs[i] = mx

    # update variable
    Vhold = vrel

    # /for

    Mxs = Mxs[Mxs > 0 * m_unit]

    return Mxs, vbar, Vhold


# /def

# -------------------------------------------------------------------


def calculate_Sx(
    vels, vesc, vhold, vcirc, vmin, minsigma, sigma_factor, sig_unit=u.cm ** 2,
):
    """Calculate Sx.

    Parameters
    ----------
    vels : Sequence
        an array of velocities, treated as along one Cartesian component.
        must be evenly spaced
    vesc : Quantity
        Galactocentric escape velocity
    vhold : Quantity
    vcirc : Quantity
        Galactocentric circular velocity
    vmin : Quantity
        infall velocity of a macro to the Earth.
    minsigma : Quantity

    Returns
    -------
    Sxs : Sequence
    vhold : Quantity

    Other Parameters
    ----------------
    sig_unit : :class:`~astropy.units.Unit`

    Notes
    -----
    this is not a particularly efficient calculation method.

    """
    Sxs = np.zeros(len(vels) ** 3) * sig_unit
    iterator = itertools.product(vels, vels, vels)

    for i, (vx, vy, vz) in tqdm(enumerate(iterator), total=len(Sxs)):
        if qnorm(vx, vy, vz) <= vesc:
            vrel = qnorm(vmin, vx, vy - vcirc, vz)
            if vrel > vhold:
                vrel = vhold
            vhold = vrel  # update vhold   # problem? never reset vhold

            sx = sigma_factor / vrel ** 2
            if sx < minsigma:
                sx = minsigma

            Sxs[i] = sx
    # /for

    Sxs = Sxs[Sxs > 0]

    return Sxs, vhold


# /def


# -------------------------------------------------------------------


def calculate_Mx_and_Sx(
    vels,
    vvir=250 * _KMS,
    vesc=550 * _KMS,
    vcirc=220 * _KMS,
    vmin=42.1 * _KMS,
    Arho=3 * u.g * u.s / u.m,  # A_{det}*\rho_{DM},
    *,
    minsigma=6e-8 * u.cm ** 2,
    sigma_factor=None,
    m_unit=u.g,
    sig_unit=u.cm ** 2,
):
    """Calculate Mx and Sx.

    Parameters
    ----------
    vels : Sequence
        an array of velocities, treated as along one Cartesian component.
        must be evenly spaced
    vvir : Quantity
        virial velocity
    vesc : Quantity
        Galactocentric escape velocity
    vcirc : Quantity
        Galactocentric circular velocity
    vmin : Quantity
        infall velocity of a macro to the Earth.
    minsigma : Quantity

    Returns
    -------
    Mxs, Sxs : Sequence
    vbar : Quantity
    vhold : Quantity

    Other Parameters
    ----------------
    minsigma : Quantity
    m_unit : :class:`~astropy.units.Unit`
    sig_unit : :class:`~astropy.units.Unit`

    Notes
    -----
    this is not a particularly efficient calculation method.

    """
    Mxs, vbar, Vhold = calculate_Mx(
        vels,
        vvir=vvir,
        vesc=vesc,
        vcirc=vcirc,
        vmin=vmin,
        Arho=Arho,
        m_unit=m_unit,
    )

    Sxs, Vhold = calculate_Sx(
        vels,
        vesc=vesc,
        vhold=Vhold,
        vmin=vmin,
        vcirc=vcirc,
        minsigma=minsigma,
        sig_unit=sig_unit,
        sigma_factor=sigma_factor,
    )

    return Mxs, Sxs, vbar, Vhold


# /def


##############################################################################
# END
