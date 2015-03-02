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
sudo python setup.py install
```
Note, for the last command, if you're using anaconda or a virtualenv, you will have to manually type the full path to python.
