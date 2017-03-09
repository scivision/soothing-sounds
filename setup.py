#!/usr/bin/env python
from setuptools import setup

req = ['numpy','scipy','pyfftw']

setup(name='soothingsounds',
      packages=['soothingsounds'],
      author='Michael Hirsch, Ph.D',
      url = 'https://github.com/scivision/soothing-sounds',
      install_requires=req,
	  )
