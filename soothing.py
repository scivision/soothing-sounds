#!/usr/bin/env python3
"""
Michael Hirsch
GPL v3
based on python-acoustics noise generator code
generates soothing sounds, e.g. for sleep enhancement

future: add GPIO input for Raspberry Pi, Beaglebone, Edison, etc.
"""
from __future__ import division
import sys
import importlib
import numpy as np
#
from generator import noise
from time import sleep, time

soundmod = 'pygame'#'pyglet'#'pyaudio' #'pygame'
smod = importlib.import_module(soundmod)

fs = 44100 #[Hz] sample rate of sound card playback
nsec = 60 #unique sound length -- 600 sec was too much for 512MB Rpi in certain noise modes that do advanced computations

def main(ntype,nhours):
    ramused = fs*nsec*64//8 #bytes
    if ramused>128e6:
        exit('*** using more than 128MB of RAM for samples, this can be too much for Raspberry Pi, exiting')
    print('sound samples used at least {:0d}'.format(ramused) + ' bytes of RAM to create')
    ntype = ntype.lower()
    tic = time()
    samps = (noise(nsec*fs, color=ntype) * 32768/8).astype(np.int16) #TODO arbitary scaling to 16-bit, noise() outputs float64
    print('it took {:0.1f}'.format(time()-tic) + ' seconds to compute {:0.0f}'.format(nsec) + ' sec. of ' + ntype + ' noise.')
    print('max sample value {:0.0f}'.format(samps.max()))

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
        print('sound playing for {:0.2f}'.format(sleepsec/3600) + ' hours')
        sleep(sleepsec) #seconds
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

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description="noise generation program for Raspberry Pi or any Python-capable computer")
    p.add_argument('nmode',help='what type of white noise [white, pink, brown...]',type=str,nargs='?',default='pink')
    p.add_argument('hours',help='how many hours do you want sound generated for [default=8 hours]',type=float,nargs='?',default=8)
    a = p.parse_args()

    main(a.nmode, a.hours)
