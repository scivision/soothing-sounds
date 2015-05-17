#!/usr/bin/env python3
"""
Michael Hirsch
GPL v3
based on python-acoustics noise generator code
generates soothing sounds, e.g. for sleep enhancement

SUGGESTED USE:
write file to SD card, use it in speaker/phone capable of playing FLAC
Example (assuming fs=16000):
python soothing.py pink 8 -o test.raw   # 931MB file, 8 hours of pink noise
ffmpeg -f s16le -ar 16000 -ac 1 -i test.raw test.flac #760.4MB file  (or just .wav, gives same size file as .raw)


future: add GPIO input for Raspberry Pi, Beaglebone, Edison, etc.

I demonstrate using a few different packages.
The simplest way to use this program is by writing a file to disk without playing audio,
you can write a WAV file with
scipy (widely available)
or
scikits.audiolab (a little trickier to install)

saving as RAW requires using an external program like FFMPEG or Goldwave to convert
to a more common format. The huge advantage of RAW is that you can iteratively
write several hours of random noise without consuming all your RAM.

"""
from __future__ import division
import sys
import importlib
import numpy as np
import os
#
from generator import noise
from time import sleep, time

soundmod = 'pygame'#'pyglet'#'pyaudio' #'pygame' #'scikits.audiolab'
wavapi = 'raw' #'skaudio' #'scipy'

nsec = 60 #unique sound length -- 600 sec was too much for 512MB Rpi in certain noise modes that do advanced computations
nbitfile = 16
nbitfloat = 32 #from generator.py

def computenoise(ntype, fs):
    nsamp = fs*nsec
    ramused = nsamp*nbitfloat//8 #bytes, assuming np.float32, does NOT account for copies!
    if ramused>128e6:
        print('*** using more than {:d} MB of RAM for samples, this can be too much for Raspberry Pi.'.format(ramused//1e6))

    rawused = ramused//(nbitfloat//nbitfile)
    if rawused>1e9:
        print('** caution, your raw output is {:.1f} GB of data.'.format(rawused/1e9))

    print('sound samples used at least {:.0f} MB of RAM to create.'.format(ramused//1e6))
    ntype = ntype.lower()
    tic = time()
    samps = (noise(nsamp, color=ntype) * 32768/8).astype(np.int16) #TODO arbitary scaling to 16-bit, noise() outputs float64
    print('it took {:.2f} seconds to compute {:.0f} sec. of {:s} noise.'.format(
           time()-tic, nsec,ntype))
    print('max sample value {:.0f}'.format(samps.max()))
    return samps

def liveplay(samps,nhours,fs ):
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
        print('unknown sound module' + str(soundmod))
        sys.exit(1)

def savenoise(samps,nhours,ofn,fs):
    if ofn is not None:
        if wavapi == 'raw':
            try: #delete because we're going to append
                os.remove(ofn)
            except OSError:
                pass

            with open(ofn,'a+b') as f:
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

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description="noise generation program for Raspberry Pi or any Python-capable computer")
    p.add_argument('nmode',help='what type of white noise [white, pink, brown...]',type=str,nargs='?',default='pink')
    p.add_argument('hours',help='how many hours do you want sound generated for [default=8 hours]',type=float,nargs='?',default=8)
    p.add_argument('--fs',help='sampling freq e.g. 16000 or 44100',type=int,default=16000)
    p.add_argument('-o','--ofn',help='output .wav filename',type=str,default=None)
    p = p.parse_args()

    samps = computenoise(p.nmode, p.fs)
    if p.ofn is None:
        try:
            liveplay(samps, p.hours, p.fs)
        except Exception as e:
            print('*** couldnt play live sound. Consider just saving to disk and using an SD card. ' + str(e))
    else:
        savenoise(samps, p.hours, p.ofn, p.fs)
