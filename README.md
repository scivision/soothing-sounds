# Soothing Sounds Generator

[![DOI](https://zenodo.org/badge/48785075.svg)](https://zenodo.org/badge/latestdoi/48785075)
[![PyPi Download stats](http://pepy.tech/badge/soothingsounds)](http://pepy.tech/project/soothingsounds)

An acoustically pleasing Python code, targeted initially for Raspberry Pi, but should run almost anywhere.
Uses lightweight, pure Python
[SoundDevice](https://pypi.org/project/sounddevice/)
to generate sounds.
Optionally, other sound playback Python packages can be used.

I have used the outputs of this program written to SD cards, played on media players in multiple locations for a few years.

```sh
pip install -e .
```

## Usage

The noise `color` option is one of

> white pink blue violet brown

the examples will use pink noise.

### Play sound from speakers

```sh
python soothing.py pink
```

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

```sh
apt install libfftw3-dev
```
