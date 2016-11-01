#!/usr/bin/env python
from setuptools import setup
import subprocess

try: #Anaconda Python
    subprocess.check_call(['conda','install','--file','requirements.txt'])
except Exception:
    pass

setup(name='soothingsounds',
      install_requires=['pathlib2'],
      packages=['soothingsounds']
	  )
