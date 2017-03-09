#!/usr/bin/env python
from soothingsounds import computenoise

nsec=1
nbitfile = 16
nbitfloat = 32 #from generator.py

samps = computenoise('pink', 16000,nsec,nbitfloat,nbitfile)
assert samps.itemsize == 2
assert samps.shape == (16000,)
