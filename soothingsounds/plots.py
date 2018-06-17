from matplotlib.pyplot import figure, specgram, gci

NFFT = 512


def plotspectrogram(data, fs: int, nmode: str):
    fg = figure()
    ax = fg.gca()

    Pxx, freqs, bins, im = specgram(data, NFFT=NFFT, Fs=fs, noverlap=500)

    fg.colorbar(gci(), ax=ax)

    ax.set_title('{} noise'.format(nmode))
    ax.set_xlabel('time (sec.)')
    ax.set_ylabel('frequency (Hz)')
