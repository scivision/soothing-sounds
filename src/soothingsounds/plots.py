from matplotlib.pyplot import figure, specgram, gci, psd
import numpy as np

NFFT = 512


def time(data, fs: int) -> None:
    t = np.arange(0, data.size / fs, 1 / fs)

    ax = figure().gca()

    ax.plot(t, data)
    ax.set_ylabel("sample value (16-bit)")
    ax.set_xlabel("time [sec]")


def plotpsd(data, fs: int, nmode: str) -> None:
    ax = figure().gca()

    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.psd.html
    pxx_out = psd(data, NFFT=NFFT, Fs=fs, label="measured")
    Pxx, f = pxx_out[0], pxx_out[1]
    ax.set_xscale("log")
    ax.set_xlim(100, None)

    f2 = f[-2]
    a2 = 10 * np.log10(Pxx[-2])

    f1 = 100

    octaves = np.log2(f2 / f1)

    match nmode:
        case "white":
            ax.axhline(a2, linestyle="--", color="black", label="theoretical")
        case "pink":
            ax.plot(
                [f1, f2],
                [3 * octaves + a2, a2],
                linestyle="--",
                color="black",
                label="theoretical",
            )
        case "blue":
            ax.plot(
                [f1, f2],
                [-3 * octaves + a2, a2],
                linestyle="--",
                color="black",
                label="theoretical",
            )
        case "brown":
            ax.plot(
                [f1, f2],
                [6 * octaves + a2, a2],
                linestyle="--",
                color="black",
                label="theoretical",
            )
        case "violet":
            ax.plot(
                [f1, f2],
                [-6 * octaves + a2, a2],
                linestyle="--",
                color="black",
                label="theoretical",
            )

    ax.set_title(f"{nmode} noise")
    ax.legend(loc="best")


def plotspectrogram(data, fs: int, nmode: str) -> None:
    fg = figure()
    ax = fg.gca()

    specgram(data, NFFT=NFFT, Fs=fs, noverlap=500)

    g = gci()
    if g is not None:
        fg.colorbar(g, ax=ax)

    ax.set_title(f"{nmode} noise")
    ax.set_xlabel("time (sec.)")
    ax.set_ylabel("frequency (Hz)")
