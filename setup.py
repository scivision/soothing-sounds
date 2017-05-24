#!/usr/bin/env python
req = ['nose','numpy','scipy']

import pip
try:
    import conda.cli
    conda.cli.main('install',*req)
except ImportError:    
    pip.main(['install'] + req)
# %%
from setuptools import setup

setup(name='soothingsounds',
      packages=['soothingsounds'],
      author='Michael Hirsch, Ph.D',
      url = 'https://github.com/scivision/soothing-sounds',
      install_requires=req,
      extras_require={'pyfftw':['pyfftw']},
	  )
