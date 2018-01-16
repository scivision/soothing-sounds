.. image:: https://travis-ci.org/scivision/soothing-sounds.svg
 :target: https://travis-ci.org/scivision/soothing-sounds
 :alt: Travis CI

.. image:: https://coveralls.io/repos/scivision/soothing-sounds/badge.svg
 :target: https://coveralls.io/r/scivision/soothing-sounds
 :alt: Coveralls.io

=================
soothing-sounds
=================

An acoustically pleasing Python code, targeted initially for Raspberry Pi, but should run almost anywhere.  Typically uses Pygame or PyAudio to generate sounds.

.. contents::

Install
=======
::

    pip install -e .


Usage examples:
===============
::

    python soothing.py <color>

where <color> is one of

    white pink blue violet brown


optional high performance Python FFTW install:
----------------------------------------------
::

 sudo apt-get install libfftw3-dev


For live playback of Python audio (optional)
============================================

pick one of the following:

Pygame installation or compile Pygame
-------------------------------------
Pick one of the following methods to install pygame

pip
~~~
simplest way::

    pip install pygame

Linux distro
~~~~~~~~~~~~
::

    sudo apt install python-pygame

compile Pygame via pip
~~~~~~~~~~~~~~~~~~~~~~
::

    sudo apt-get install mercurial libflac-dev libmad0-dev libmikmod2-dev libogg-dev libportmidi-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libvorbis-dev libwebp-dev libwebpdemux1 sharutils libswscale-dev libavformat-dev

    pip install hg+http://bitbucket.org/pygame/pygame

manually compile and install Pygame
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    cd /tmp

    hg clone http://bitbucket.org/pygame/pygame

    cd /tmp/pygame

    python setup.py build

    python setup.py install


PyAudio:
--------
::

    pip install pyaudio

Linux PyAudio prereq
~~~~~~~~~~~~~~~~~~~~
::

    sudo apt-get install portaudio19-dev libjack-dev libjack0

Mac PyAudio prereq
~~~~~~~~~~~~~~~~~~~
::

    brew install portaudio


Reference
=========
the core noise generation code is almost entirely from `Python Acoustics <https://github.com/python-acoustics/python-acoustics>`_
