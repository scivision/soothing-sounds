#!/usr/bin/env python
import pytest
import soothingsounds as ss

nsec = 1
nbitfile = 16
nbitfloat = 32  # from generator.py

Noises = ["white", "pink", "blue", "brown", "violet"]


def noise():

    for noise in Noises:
        samps = ss.computenoise(noise, 16000, nsec, nbitfloat, nbitfile)
        assert samps.itemsize == 2
        assert samps.shape == (16000,)

    return samps


def test_write(tmp_path):
    ofn = tmp_path / "blah.raw"
    ss.savenoise(noise(), nhours=0.01, ofn=ofn, fs=44100, nsec=nsec, wavapi="raw")

    assert ofn.is_file()


if __name__ == "__main__":
    pytest.main([__file__])
