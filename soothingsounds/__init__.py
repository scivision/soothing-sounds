from pathlib import Path
import numpy as np
from time import sleep
import importlib
import logging
from time import time
#
from .generator import noise

def computenoise(ntype, fs,nsec,nbitfloat,nbitfile):
    nsamp = int(fs*nsec)
    ramused = nsamp*nbitfloat//8 #bytes, assuming np.float32, does NOT account for copies!
    if ramused>128e6:
        logging.warning('using more than {:d} MB of RAM for samples, this can be too much for Raspberry Pi.'.format(ramused//1e6))

    rawused = ramused//(nbitfloat//nbitfile)
    if rawused>1e9:
        logging.warning('your raw output is {:.1f} GB of data.'.format(rawused/1e9))

    print('sound samples used at least {:.0f} MB of RAM to create.'.format(ramused//1e6))

    ntype = ntype.lower()
    tic = time()
    samps = (noise(nsamp, color=ntype) * 32768/8).astype(np.int16) #TODO arbitary scaling to 16-bit, noise() outputs float64
    print('it took {:.2f} seconds to compute {:.0f} sec. of {:s} noise.'.format(
           time()-tic, nsec,ntype))
    print('max sample value {:.0f}'.format(samps.max()))

    return samps

def liveplay(samps,nhours,fs,nsec,soundmod):
    smod = importlib.import_module(soundmod)

    if soundmod == 'pyaudio':
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
        sleep(sleepsec) #seconds
    elif soundmod=='scikits.audiolab':
        smod.play(samps)
    elif soundmod=='pyglet':
        print('pyglet not yet implemented')
#        """
#        http://www.pyglet.org/doc-current/api/pyglet/media/pyglet.media.AudioFormat.html#pyglet.media.AudioFormat
#        """
#        src = smod.media.StaticMemorySource(samps.tostring(),
#                            smod.media.AudioFormat(channels=1, sample_size=16, sample_rate=fs))
#        src.play()

    else:
        raise ImportError('unknown sound module {}'.format(soundmod))

def savenoise(samps,nhours,ofn,fs,nsec, wavapi):
    if ofn is not None:
        ofn = Path(ofn).expanduser()

        if wavapi == 'raw':
            try: #delete because we're going to append
                ofn.unlink()
            except OSError:
                pass

            with ofn.open('a+b') as f:
                for i in range(int(nhours*3600/nsec)):
                    f.write(samps)
        elif wavapi == 'scipy':
            from scipy.io import wavfile
            wavfile.write(ofn,fs,samps)
        elif wavapi=='skaudio':
            from scikits.audiolab import Format,Sndfile
            fmt = Format('flac')
            f = Sndfile(ofn,'w',fmt, 1, 16000) #too old to work with "with...." syntax
            f.write_frames(samps)
            f.close()
