#!/usr/bin/env python
import pytest
import soothingsounds as ss
import tempfile
import os

nsec = 1
nbitfile = 16
nbitfloat = 32  # from generator.py

Noises = ['white', 'pink', 'blue', 'brown', 'violet']

APPVEYOR = 'APPVEYOR' in os.environ and os.environ['APPVEYOR']


@pytest.fixture
def test_noise():

    for noise in Noises:
        samps = ss.computenoise(noise, 16000, nsec, nbitfloat, nbitfile)
        assert samps.itemsize == 2
        assert samps.shape == (16000,)

    return samps


@pytest.mark.xfail(APPVEYOR, reason="AppVeyor strict permissions even in same directory")
def test_write():
    # specifying same directory is for CI, which may not give permission to write in temp dir.
    with tempfile.NamedTemporaryFile(suffix='.raw') as f:
        ss.savenoise(test_noise(), nhours=0.01, ofn=f.name, fs=44100, nsec=nsec, wavapi='raw')


if __name__ == '__main__':
    pytest.main()
