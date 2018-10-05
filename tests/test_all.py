#!/usr/bin/env python
import pytest
import soothingsounds as ss
import tempfile
import os
from pathlib import Path

nsec = 1
nbitfile = 16
nbitfloat = 32  # from generator.py

Noises = ['white', 'pink', 'blue', 'brown', 'violet']

APPVEYOR = 'APPVEYOR' in os.environ and os.environ['APPVEYOR']


@pytest.fixture
def noise():

    for noise in Noises:
        samps = ss.computenoise(noise, 16000, nsec, nbitfloat, nbitfile)
        assert samps.itemsize == 2
        assert samps.shape == (16000,)

    return samps


@pytest.mark.xfail(APPVEYOR, reason="AppVeyor strict permissions even in same directory")
def test_write(noise):
    # specifying same directory is for CI, which may not give permission to write in temp dir.
    with tempfile.NamedTemporaryFile(suffix='.raw') as f:
        ofn = Path(f.name)
        ss.savenoise(noise, nhours=0.01, ofn=ofn, fs=44100, nsec=nsec, wavapi='raw')

        assert ofn.is_file()


if __name__ == '__main__':
    pytest.main([__file__])
