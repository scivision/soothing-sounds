from pathlib import Path
import numpy as np
from time import sleep
import importlib
import logging
from time import time
from typing import Any
#
from .generator import noise


def computenoise(ntype: str, fs: int, nsec: int, nbitfloat: int, nbitfile: int) -> np.ndarray:
    nsamp = int(fs*nsec)
    ramused = nsamp*nbitfloat//8  # bytes, assuming np.float32, does NOT account for copies!
    if ramused > 128e6:
        logging.warning('using more than {:d} MB of RAM for samples, this can be too much for Raspi.'.format(ramused//1e6))

    rawused = ramused // (nbitfloat // nbitfile)
    if rawused > 1e9:
        logging.warning('your raw output is {:.1f} GB of data.'.format(rawused/1e9))

    print('sound samples used at least {:.0f} MB of RAM to create.'.format(ramused//1e6))

    ntype = ntype.lower()
    tic = time()
    # TODO arbitary scaling to 16-bit, noise() outputs float64
    samps = (noise(nsamp, color=ntype) * 32768 / 8).astype(np.int16)

    print('it took {:.2f} seconds to compute {:.0f} sec. of {:s} noise.'.format(
        time()-tic, nsec, ntype))
    print('max sample value {:.0f}'.format(samps.max()))

    return samps


def liveplay(samps: np.ndarray, nhours: int, fs: int, nsec: int, soundmod: str='sounddevice'):
    smod: Any = importlib.import_module(soundmod)

    if soundmod == 'sounddevice':
        smod.play(samps, fs)  # releases GIL
    elif soundmod == 'pyaudio':
        p = smod.PyAudio()
        stream = p.open(rate=fs, format=smod.paInt16, channels=1, output=True)
        for i in range(int(nhours*3600/nsec)):
            stream.write(samps.tostring())
    elif soundmod == 'pygame':
        smod.mixer.pre_init(fs, size=-16, channels=1)
        smod.mixer.init()
        sound = smod.sndarray.make_sound(samps)
        nloop = int(nhours*3600/nsec)
        sound.play(loops=nloop)
        sleepsec = sound.get_length()*nloop
        print('pygame volume level: ' + str(sound.get_volume()))
        print('sound playing for {:.2f} hours.'.format(sleepsec/3600))
        sleep(sleepsec)  # seconds
    elif soundmod == 'scikit.audiolab':
        smod.play(samps)
    elif soundmod == 'pyglet':
        print('pyglet not yet implemented')
#        """
#        http://www.pyglet.org/doc-current/api/pyglet/media/pyglet.media.AudioFormat.html#pyglet.media.AudioFormat
#        """
#        src = smod.media.StaticMemorySource(samps.tostring(),
#                            smod.media.AudioFormat(channels=1, sample_size=16, sample_rate=fs))
#        src.play()

    else:
        raise ImportError('unknown sound module {}'.format(soundmod))


def savenoise(samps: np.ndarray, nhours: int, ofn: Path, fs: int, nsec: int, wavapi: str):
    if ofn is not None:
        ofn = Path(ofn).expanduser()

        f: Any

        if wavapi == 'raw':
            try:  # delete because we're going to append
                ofn.unlink()
            except OSError:
                pass

            with ofn.open('a+b') as f:
                for i in range(int(nhours*3600/nsec)):
                    f.write(samps)
        elif wavapi == 'scipy':
            from scipy.io import wavfile
            wavfile.write(ofn, fs, samps)
        elif wavapi == 'skaudio':
            from scikits.audiolab import Format, Sndfile
            fmt = Format('flac')
            f = Sndfile(ofn, 'w', fmt, 1, 16000)  # scikit-audio does not have context manager
            f.write_frames(samps)
            f.close()
