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
from generator import white
from time import sleep

fs = 44100 #[Hz] sample rate of sound card playback
nloop = 10
nsec = 10 #unique sound length

def main(ntype):
    if ntype.lower() == 'white':
        samps = white(nsec*fs) * 32768/8  #FIXME normalize instead

    pygame.mixer.pre_init(fs, size=-16, channels=1)
    pygame.mixer.init()
    sound = pygame.sndarray.make_sound(samps.astype(np.int16))
    
    sound.play(loops=nloop)
    #print(samps.max())
    #print(samps.size)
    #print(sound.get_volume())
    sleep(sound.get_length()*nloop) #seconds

if __name__ == '__main__':
    main('white')
