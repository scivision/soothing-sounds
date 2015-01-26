"""
Michael Hirsch
GPL v3
based on python-acoustics noise generator code
"""
from __future__ import division
import numpy as np
import pygame
from generator import white
fs = 44100 #[Hz] sample rate of sound card playback

def main(ntype):
    if ntype.lower() == 'white':
        samps = white(441000) * 32768/4

    pygame.mixer.pre_init(fs, size=-16, channels=1)
    pygame.mixer.init()
    sound = pygame.sndarray.make_sound(samps.astype(np.int16))
    
    sound.play(loops=0)
    print(samps.max())
    print(samps.size)
    print(sound.get_volume())
    print(sound.get_length()) #seconds

if __name__ == '__main__':
    main('white')
