#!/usr/bin/env python3
"""
Michael Hirsch
GPL v3
based on python-acoustics noise generator code
generates soothing sounds, e.g. for sleep enhancement

future: add GPIO input for Raspberry Pi, Beaglebone, Edison, etc.
"""
from __future__ import division
import numpy as np
import pygame
from generator import noise
from time import sleep, time

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
    print('it took {:0.0f}'.format(time()-tic) + ' seconds to compute {:0.0f}'.format(nsec) + ' sec. of white noise.')

    pygame.mixer.pre_init(fs, size=-16, channels=1)
    pygame.mixer.init()
    sound = pygame.sndarray.make_sound(samps)

    nloop = int(nhours*3600/nsec)
    sound.play(loops=nloop)

    sleepsec = sound.get_length()*nloop

    print('max sample value {:0.0f}'.format(samps.max()))
    print('pygame volume level: ' + str(sound.get_volume()))
    print('sound playing for {:0.0f}'.format(sleepsec) + ' seconds')
    
 
    sleep(sleepsec) #seconds

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description="noise generation program for Raspberry Pi or any Python-capable computer")
    p.add_argument('-m','--nmode',help='what type of white noise [white, pink, brown...]',type=str,default='white')
    p.add_argument('-n','--hours',help='how many hours do you want sound generated for [default=8 hours]',type=float,default=8)	
    a = p.parse_args()

    main(a.nmode, a.hours)
