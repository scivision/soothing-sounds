#!/usr/bin/env python
import pytest
import soothingsounds as ss
import tempfile

nsec = 1
nbitfile = 16
nbitfloat = 32  # from generator.py

Noises = ['white', 'pink', 'blue', 'brown', 'violet']

@pytest.fixture
def test_noise():

    for noise in Noises:
        samps = ss.computenoise(noise, 16000, nsec, nbitfloat, nbitfile)
        assert samps.itemsize == 2
        assert samps.shape == (16000,)
        
    return samps
    
    
def test_write():
  
    with tempfile.NamedTemporaryFile(suffix='.raw') as f:
        ss.savenoise(test_noise(), nhours=0.01, ofn=f.name, fs=44100, nsec=nsec, wavapi='raw')


if __name__ == '__main__':
    pytest.main()
