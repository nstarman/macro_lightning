# -*- coding: utf-8 -*-

"""Physics Functions."""


__all__ = [
    "CMB",
    "nuclear_density",
    "black_hole",
    "atomic_density",
    "KeplerTop",
    "LMCTop",
]


##############################################################################
# IMPORTS

# BUILT-IN

import itertools
import functools
import typing as T

# THIRD PARTY

import astropy.units as u

import numpy as np

from utilipy.utils.typing import array_like

from tqdm import tqdm


# PROJECT-SPECIFIC

from .utils import as_quantity, qnorm


##############################################################################
# PARAMETERS

_KMS = u.km / u.s


##############################################################################
# CODE
##############################################################################


def CMB(M):
    """CMB."""  # TODO document
    return M * 4.5e-7


# /def


# -------------------------------------------------------------------


def nuclear_density(M: array_like) -> array_like:
    """Nuclear Density."""  # TODO document
    volume = 4.0 / 3.0 * np.pi * 3.6e14
    out = np.pi * np.power(M / volume, 2.0 / 3)
    return out


# /def


# -------------------------------------------------------------------


def black_hole(M: array_like) -> array_like:
    """Black Holes."""  # TODO document
    return np.pi * (3e5) ** 2 * (M / (2e33)) ** 2.0


# /def


# -------------------------------------------------------------------


def atomic_density(M: array_like) -> array_like:
    """Atomic Density."""  # TODO document
    volume = 4.0 / 3.0 * np.pi * 1e0
    out = np.pi * np.power(M / volume, 2.0 / 3.0)
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
     J.  S.  Sidhu  and  G.  Starkman,  Physical  Review  D
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


def multibody_esc_v(
    *vescs,
    vo: T.Union[None, T.Sequence[u.Quantity]] = None,
    accumulate: bool = False,
) -> u.Quantity:
    r"""Multi-body escape velocity.

    *Note:* all the orbits are assumed circular. This might be changed
    in the future

    Parameters
    ----------
    *vels: Quantity
        velocities, ordered from 1st to last body.

    vo : list of Quantity or None, optional
        The orbital velocity of object vescs[i+1] around object vescs[i].
        if list of quantities, must match `vescs` in length
        if None (default) then orbits are assumed circular.

    Returns
    -------
    :class:`itertools.accumulate`
        The compound escape velocity

    Examples
    --------
    For a Galactic macro falling into the potential well of the Earth,
    the minimum observed velocity

        >>> v_sun_at_earth = 42.1 * u.km / u.s
        >>> v_esc_earth = 11.186 * u.km / u.s
        >>> multibody_esc_v(v_sun_at_earth, v_esc_earth)
        <Quantity 42.22729171 km / s>

    Notes
    -----
    From `Wikipedia <https://en.wikipedia.org/wiki/Escape_velocity>`_:

    When escaping a compound system, such as a moon orbiting a planet or a
    planet orbiting a sun, a rocket that leaves at escape velocity (ve1) for
    the first (orbiting) body, (e.g. Earth) will not travel to an infinite
    distance because it needs an even higher speed to escape gravity of the
    second body (e.g. the Sun). Near the Earth, the rocket's trajectory will
    appear parabolic, but it will still be gravitationally bound to the second
    body and will enter an elliptical orbit around that body, with an orbital
    speed similar to the first body.

    To escape the gravity of the second body once it has escaped the first
    body the rocket will need to be travelling at the escape velocity for the
    second body (ve2) (at the orbital distance of the first body). However,
    when the rocket escapes the first body it will still have the same orbital
    speed around the second body that the first body has (vo). So its excess
    velocity as it escapes the first body will need to be the difference
    between the orbital velocity and the escape velocity. With a circular
    orbit, escape velocity is √2 times the orbital speed. Thus the total
    escape velocity vte when leaving one body orbiting a second and seeking to
    escape them both is, under simplified assumptions:

    .. math::

        v_{te}=\sqrt{(v_{e2} - v_o)^2 + v_{e1}^2}
        = \sqrt{\left(k v_{e2}\right)^2 + v_{e1}^2}

    where :math:`k=1−1/2 \sim 0.2929` for circular orbits.

    """
    vs: u.Quantity = as_quantity(vescs)

    if vo is None:
        vs[1:] = vs[1:] * (1 - 1 / np.sqrt(2))
    else:
        vs[1:] = vs[1:] - vo

    if accumulate:
        return itertools.accumulate(vs, _norm_v1_v2)
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
            # mx <<= m_unit

            Mxs[i] = mx

            # update variable
            Vhold = vrel

    # /for

    Mxs = Mxs[Mxs > 0 * m_unit]

    return Mxs, vbar, Vhold


# /def

# -------------------------------------------------------------------


def calculate_Sx(vels, vesc, vhold, vcirc, vmin, sigmax, sig_unit=u.cm ** 2):
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
    sigmax : Quantity

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
    sigma_factor = 1e4 * (u.m * u.cm / u.s) ** 2

    Sxs = np.zeros(len(vels) ** 3) * sig_unit
    iterator = itertools.product(vels, vels, vels)

    for i, (vx, vy, vz) in tqdm(enumerate(iterator), total=len(Sxs)):
        if qnorm(vx, vy, vz) <= vesc:
            vrel = qnorm(vmin, vx, vy - vcirc, vz)
            if vrel > vhold:
                vrel = vhold
            vhold = vrel  # update vhold   # problem? never reset vhold

            sx = sigma_factor / vrel ** 2
            if sx < sigmax:
                sx = sigmax
            # sx <<= sig_unit

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
    sigmax=6e-8 * u.cm ** 2,
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
    sigmax : Quantity

    Returns
    -------
    Mxs, Sxs : Sequence
    vbar : Quantity
    vhold : Quantity

    Other Parameters
    ----------------
    sigmax : Quantity
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
        sigmax=sigmax,
        sig_unit=sig_unit,
    )

    return Mxs, Sxs, vbar, Vhold


# /def


##############################################################################
# END
