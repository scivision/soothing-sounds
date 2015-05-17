from soothing import computenoise

samps = computenoise('pink', 16000)
assert samps.itemsize == 2
assert samps.shape == (960000,)
