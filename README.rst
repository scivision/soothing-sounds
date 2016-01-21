.. image:: https://codeclimate.com/github/scienceopen/soothing-sounds/badges/gpa.svg
 :target: https://codeclimate.com/github/scienceopen/soothing-sounds
 :alt: Code Climate

.. image:: https://travis-ci.org/scienceopen/soothing-sounds.svg
 :target: https://travis-ci.org/scienceopen/soothing-sounds
 :alt: Travis CI
 
.. image:: https://coveralls.io/repos/scienceopen/soothing-sounds/badge.svg
 :target: https://coveralls.io/r/scienceopen/soothing-sounds
 :alt: Coveralls.io

=================
soothing-sounds
=================

An acoustically pleasing Python code, targeted initially for Raspberry Pi, but should run almost anywhere

Note: the core noise generation code is almost entirely from 
`Python Acoustics <https://github.com/python-acoustics/python-acoustics>`_ 
why didn't I merely have people install that package first? Because it requires Numpy >=1.8 and several other new versions including SciPy, and Raspberry Pi currently comes with Numpy 1.6.2 and it takes a long time to install Numpy, SciPy, etc. via pip on Raspberry Pi due to slow CPU.


Usage examples:
===============
::

 python main.py <color>
 
where <color> is one of

 white  pink blue violet brown

Prereqs:
========
::

 pip install -r requirements.txt


optional high performance Python FFTW install:
==============================================
::

 sudo apt-get install libfftw3-dev
 pip install -r optional-requirements.txt


optional Audio library install:
----------------------
If you want live playback instead of saving to disk,

Pick one of the following:

Pygame
------
if you don't have pygame installed already, try::

 sudo apt-get install python-pygame

or::

 sudo apt-get install mercurial libflac-dev libmad0-dev libmikmod2-dev libogg-dev libportmidi-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libvorbis-dev libwebp-dev libwebpdemux1 sharutils 

 pip install hg+http://bitbucket.org/pygame/pygame

or more manually::

 sudo apt-get install mercurial libflac-dev libmad0-dev libmikmod2-dev libogg-dev libportmidi-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libvorbis-dev libwebp-dev libwebpdemux1 sharutils 

 cd /tmp
 
 git clone http://bitbucket.org/pygame/pygame
 
 cd /tmp/pygame
 
 python setup.py build
 
 python setup.py install

Note, there is a bug noted on some Linux installs of anaconda where the solution is to rename the symbolic links
https://groups.google.com/a/continuum.io/forum/#!topic/anaconda/-DLG2ZdTkw0
e.g. if you can't import pygame due to an error like

ImportError: /home/username/anaconda3/bin/../lib/libm.so.6: version `GLIBC_2.15' not found (required by /usr/lib/x86_64-linux-gnu/libpulse.so.0)

so in my ~/anaconda3/lib I renamed libm.so and libm.so.6 to libm.so.bak and libm.so.6.bak and then pygame worked.

PyAudio:
--------
::
 
 sudo apt-get install portaudio19-dev libjack-dev libjack0
 
 pip install pyaudio --allow-external pyaudio --allow-unverified pyaudio

which on my Ubuntu system removed the packages libasound2-plugins:i386 libjack-jackd2-0 libjack-jackd2-0:i386
(for reference in case someday you want them back)
