# soothing-sounds
An acoustically pleasing Python code, targeted initially for Raspberry Pi, but should run almost anywhere

Note: the core noise generation code is almost entirely from 
https://github.com/python-acoustics/python-acoustics
why didn't I merely have people install that package first? Because it requires Numpy >=1.8 and several other new versions including SciPy, and Raspberry Pi currently comes with Numpy 1.6.2 and it takes a long time to install Numpy, SciPy, etc. via pip on Raspberry Pi due to slow CPU.


