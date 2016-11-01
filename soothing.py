#!/usr/bin/env python
"""
Michael Hirsch
based on python-acoustics noise generator code
generates soothing sounds, e.g. for sleep enhancement

SUGGESTED USE:
write file to SD card, use it in speaker/phone capable of playing FLAC
Example (assuming fs=16000):
python soothing.py pink 8 -o test.raw   # 931MB file, 8 hours of pink noise
ffmpeg -f s16le -ar 16000 -ac 1 -i test.raw test.flac #760.4MB file  (or just .wav, gives same size file as .raw)


--nsec:  600 sec was too much for 512MB Rpi 1 in certain noise modes that do advanced computations

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
from soothingsounds import computenoise,liveplay, savenoise
from soothingsounds.plots import plotspectrogram
from matplotlib.pyplot import show

soundmod = 'pygame'#'pyglet'#'pyaudio' #'pygame' #'scikits.audiolab'
wavapi = 'raw' #'skaudio' #'scipy'

nbitfile = 16
nbitfloat = 32 #from generator.py

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description="noise generation program for Raspberry Pi or any Python-capable computer")
    p.add_argument('nmode',help='what type of white noise [white, pink, brown...]',nargs='?',default='pink')
    p.add_argument('hours',help='how many hours do you want sound generated for [default=8 hours]',type=float,nargs='?',default=8)
    p.add_argument('--fs',help='sampling freq e.g. 16000 or 44100',type=int,default=16000)
    p.add_argument('-o','--ofn',help='output .wav filename')
    p.add_argument('--nsec',help='length of unique noise sequence [seconds]',type=float,default=60)
    p = p.parse_args()

    samps = computenoise(p.nmode, p.fs, p.nsec,nbitfloat,nbitfile)
    if p.ofn is None:
        try:
            liveplay(samps, p.hours, p.fs, p.nsec, soundmod)
        except Exception as e:
            raise RuntimeError('could not play live sound. Consider just saving to disk and using an SD card. {}'.format(e))
    else:
        savenoise(samps, p.hours, p.ofn, p.fs, p.nsec, wavapi)
        plotspectrogram(samps,p.fs, p.nmode)

        show()
