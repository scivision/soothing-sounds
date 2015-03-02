# soothing-sounds
An acoustically pleasing Python code, targeted initially for Raspberry Pi, but should run almost anywhere

Note: the core noise generation code is almost entirely from 
https://github.com/python-acoustics/python-acoustics
why didn't I merely have people install that package first? Because it requires Numpy >=1.8 and several other new versions including SciPy, and Raspberry Pi currently comes with Numpy 1.6.2 and it takes a long time to install Numpy, SciPy, etc. via pip on Raspberry Pi due to slow CPU.


Usage examples:

```python main.py <color> ```
where ```<color>``` is one of

white  pink blue violet brown

if you don't have pygame installed already, try
```
sudo apt-get install python-pygame
```
or
```
pip install hg+http://bitbucket.org/pygame/pygame
```
or more manually
```
sudo apt-get install libflac-dev libmad0-dev libmikmod2-dev libogg-dev libportmidi-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libvorbis-dev libwebp-dev libwebpdemux1 sharutils 
cd /tmp
git clone http://bitbucket.org/pygame/pygame
cd /tmp/pygame
python setup.py build
python setup.py install
```
Note, there is a bug noted on some Linux installs of anaconda where the solution is to rename the symbolic links
https://groups.google.com/a/continuum.io/forum/#!topic/anaconda/-DLG2ZdTkw0
e.g. if you can't import pygame due to an error like

ImportError: /home/username/anaconda3/bin/../lib/libm.so.6: version `GLIBC_2.15' not found (required by /usr/lib/x86_64-linux-gnu/libpulse.so.0)

so in my ~/anaconda3/lib I renamed libm.so and libm.so.6 to libm.so.bak and libm.so.6.bak and then pygame worked.
