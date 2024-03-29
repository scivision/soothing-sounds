"""
# Generator

The generator module provides signal generators.

The following functions calculate `N` samples and return an array containing the samples.

For indefinitely long iteration over the samples, consider using the output of these functions in `itertools.cycle`.

## Noise

In general, noise with spectrum S(f) is generated by taking uniform white noise
and filtering with filter response H(f) to get the desired noise spectrum.

Color  | Power/octave | Power density/octave
-------|-------|--------------
White  | +3 dB | 0 dB
Pink   |  0 dB | -3 dB
Blue   | +6 dB | +3 dB
Brown  | -3 dB | -6 dB
Violet | +9 dB | +6 dB
-------|-------|--------------

"""
import numpy as np

try:
    from pyfftw.interfaces.numpy_fft import (
        rfft,
        irfft,
    )  # Performs much better than numpy's fftpack

    print("using high-performance FFTW")
except ImportError:
    from numpy.fft import rfft, irfft

from .signal_acoustics import normalise


def noise(N: int, color: str = "white") -> np.ndarray:
    """Noise generator.

    * N: Amount of samples.
    * color: Color of noise.

    https://github.com/python-acoustics
    """
    noise_generators = {
        "white": white,
        "pink": pink,
        "blue": blue,
        "brown": brown,
        "violet": violet,
    }

    return noise_generators[color](N)


def white(N: int) -> np.ndarray:
    """
    White noise.

    * N: Amount of samples.

    White noise has a constant power density.
    Its narrowband spectrum is therefore flat.
    The power in white noise will increase by a factor of two for each octave band,
    and therefore increases with 3 dB per octave.

    https://github.com/python-acoustics
    """
    return np.random.randn(N).astype(np.float32)


def pink(N: int) -> np.ndarray:
    """
    Pink noise.

    * N: Amount of samples.

    Pink noise has equal power in bands that are proportionally wide.
    Power density decreases with 3 dB per octave.

    https://github.com/python-acoustics
    """

    # This method uses the filter with the following coefficients.
    # b = np.array([0.049922035, -0.095993537, 0.050612699, -0.004408786])
    # a = np.array([1, -2.494956002, 2.017265875, -0.522189400])
    # return lfilter(B, A, np.random.randn(N))

    # Another way would be using the FFT
    x = white(N)
    X = rfft(x) / N
    S = np.sqrt(np.arange(X.size) + 1.0)  # +1 to avoid divide by zero
    y = irfft(X / S).real[:N]

    return normalise(y)  # extremely tiny value 1e-9 without normalization


def blue(N: int) -> np.ndarray:
    """
    Blue noise.

    * N: Amount of samples.

    Power increases with 6 dB per octave.
    Power density increases with 3 dB per octave.

    https://github.com/python-acoustics
    """
    x = white(N)
    X = rfft(x) / N
    S = np.sqrt(np.arange(X.size))  # Filter
    y = irfft(X * S).real[:N]

    return normalise(y)


def brown(N: int) -> np.ndarray:
    """
    Violet noise.

    * N: Amount of samples.

    Power decreases with -3 dB per octave.
    Power density decreases with 6 dB per octave.

    https://github.com/python-acoustics
    """
    x = white(N)
    X = rfft(x) / N
    S = np.arange(X.size) + 1  # Filter
    y = irfft(X / S).real[:N]

    return normalise(y)


def violet(N: int) -> np.ndarray:
    """
    Violet noise. Power increases with 6 dB per octave.

    * N: Amount of samples.

    Power increases with +9 dB per octave.
    Power density increases with +6 dB per octave.

    https://github.com/python-acoustics
    """
    x = white(N)
    X = rfft(x) / N
    S = np.arange(X.size)  # Filter
    y = irfft(X * S).real[0:N]

    return normalise(y)
