[![image](https://travis-ci.org/scivision/soothing-sounds.svg)](https://travis-ci.org/scivision/soothing-sounds)
[![image](https://coveralls.io/repos/scivision/soothing-sounds/badge.svg)](https://coveralls.io/r/scivision/soothing-sounds)
[![Build status](https://ci.appveyor.com/api/projects/status/bg0wym66ousyk657?svg=true)](https://ci.appveyor.com/project/scivision/soothing-sounds)
[![pypi versions](https://img.shields.io/pypi/pyversions/soothingsounds.svg)](https://pypi.python.org/pypi/soothingsounds)
[![pypi format](https://img.shields.io/pypi/format/soothingsounds.svg)](https://pypi.python.org/pypi/soothingsounds)
[![PyPi Download stats](http://pepy.tech/badge/soothingsounds)](http://pepy.tech/project/soothingsounds)

# Soothing Sounds Generator


An acoustically pleasing Python code, targeted initially for Raspberry Pi, but should run almost anywhere. 
Uses lightweight, pure Python
[SoundDevice](https://pypi.org/project/sounddevice/)
to generate sounds.
Optionally, other sound playback Python packages can be used.

I have used the outputs of this program written to SD cards, played on media players in multiple locations for a few years.

## Install

    pip install -e .

## Usage

The noise `color` option is one of

> white pink blue violet brown

the examples will use pink noise.

### Play sound from speakers

    python soothing.py pink

### save sound to disk


1. generate raw sound file: `python soothing.py pink -o pink.raw`
2. convert raw to lossless FLAC (playable in almost all media players, computer, phone etc.)
   ```bash
   ffmpeg -f s16le -ar 16000 -ac 1 -i pink.raw pink.fla
   ``` 


## Notes

The core noise generation code is almost entirely from 
[Python Acoustics](https://github.com/python-acoustics/python-acoustics)

### optional high performance Python FFTW install:

    sudo apt-get install libfftw3-dev
    
### Optional PyAudio

* Linux: `apt install portaudio19-dev libjack-dev libjack0`
* Mac: ` brew install portaudio`

and then:

    pip install pyaudio


### Optional Pygame

Pick one of the following methods to install pygame

#### pip

simplest way for PCs, but may require compiling for ARM CPU:

    pip install pygame

#### Linux distro
For ARM CPU, this is the best choice generally for PyGame.

    apt install python-pygame

#### compile Pygame via pip
Usually you don't want to bother with this

    apt install mercurial libflac-dev libmad0-dev libmikmod2-dev libogg-dev libportmidi-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libvorbis-dev libwebp-dev libwebpdemux1 sharutils libswscale-dev libavformat-dev

    pip install hg+http://bitbucket.org/pygame/pygame


    cd /tmp

    hg clone http://bitbucket.org/pygame/pygame

    cd /tmp/pygame

    python setup.py build

    python setup.py install
