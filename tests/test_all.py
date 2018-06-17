#!/usr/bin/env python
import pytest
from soothingsounds import computenoise

nsec = 1
nbitfile = 16
nbitfloat = 32  # from generator.py

def test_noise():
    samps = computenoise('pink', 16000, nsec, nbitfloat, nbitfile)
    assert samps.itemsize == 2
    assert samps.shape == (16000,)
    
    
    
if __name__ == '__main__':
    pytest.main()
