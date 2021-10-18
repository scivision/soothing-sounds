"""
forked from github.com/python-acoustics
GPLv3
"""
from __future__ import annotations
import numpy as np


def ms(x: np.ndarray) -> np.ndarray:
    """Mean Square value of signal `x`.

    input
    -----

    * x: signal vector

    output
    ------

    * Mean square of `x`.
    """

    return (abs(x) ** 2).mean()


def rms(x: np.ndarray) -> np.ndarray:
    """Root Mean Square value of signal `x`.

    input
    -----

    * x: signal vector
    """

    return np.sqrt(ms(x))


def normalise(y: np.ndarray, x: float | np.ndarray = 1.0) -> np.ndarray:
    """Normalise power in y to a (standard normal) white noise signal.

    Optionally normalise to power in signal `x`.

    The mean power of a Gaussian with `mu=0` and `sigma=1` is 1.
    """

    return y * np.sqrt(ms(np.atleast_1d(x)) / ms(y))
