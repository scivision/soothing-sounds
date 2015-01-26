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
from time import sleep

fs = 44100 #[Hz] sample rate of sound card playback
nloop = 10
nsec = 10 #unique sound length

def main(ntype):
    ntype = ntype.lower()
    samps = noise(nsec*fs, color=ntype) * 32768/8 #TODO arbitary scaling to 16-bit

    pygame.mixer.pre_init(fs, size=-16, channels=1)
    pygame.mixer.init()
    sound = pygame.sndarray.make_sound(samps.astype(np.int16))
    
    sound.play(loops=nloop)
    print('max sample value {:0.0f}'.format(samps.max()))
    #print(samps.size)
    #print(sound.get_volume())
    sleep(sound.get_length()*nloop) #seconds

if __name__ == '__main__':
    from sys import argv
    if len(argv)<2:
       ntype = 'white'
    else:
       ntype = argv[1]
    main(ntype)
