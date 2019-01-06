from matplotlib.pyplot import figure, specgram, gci, psd
import numpy as np

NFFT = 512


def time(data: np.ndarray, fs: int, nmode: str):
    t = np.arange(0, data.size/fs, 1/fs)

    ax = figure().gca()

    ax.plot(t, data)
    ax.set_ylabel('sample value (16-bit)')
    ax.set_xlabel('time [sec]')


def plotpsd(data: np.ndarray, fs: int, nmode: str):
    ax = figure().gca()

    Pxx, f = psd(data, NFFT=NFFT, Fs=fs,
                 label='measured')
    ax.set_xscale('log')
    ax.set_xlim((100, None))

    f2 = f[-2]
    a2 = 10*np.log10(Pxx[-2])

    f1 = 100

    octaves = np.log2(f2/f1)

    if nmode == 'white':
        ax.axhline(a2, linestyle='--', color='black', label='theoretical')
    elif nmode == 'pink':
        ax.plot([f1, f2], [3*octaves+a2, a2], linestyle='--', color='black', label='theoretical')
    elif nmode == 'blue':
        ax.plot([f1, f2], [-3*octaves+a2, a2], linestyle='--', color='black', label='theoretical')
    elif nmode == 'brown':
        ax.plot([f1, f2], [6*octaves+a2, a2], linestyle='--', color='black', label='theoretical')
    elif nmode == 'violet':
        ax.plot([f1, f2], [-6*octaves+a2, a2], linestyle='--', color='black', label='theoretical')

    ax.set_title(f'{nmode} noise')
    ax.legend(loc='best')


def plotspectrogram(data: np.ndarray, fs: int, nmode: str):
    fg = figure()
    ax = fg.gca()

    Pxx, freqs, bins, im = specgram(data, NFFT=NFFT, Fs=fs, noverlap=500)

    fg.colorbar(gci(), ax=ax)

    ax.set_title(f'{nmode} noise')
    ax.set_xlabel('time (sec.)')
    ax.set_ylabel('frequency (Hz)')
