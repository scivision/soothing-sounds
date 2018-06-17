#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = ['numpy', 'sounddevice']
tests_require = ['pytest', 'coveralls', 'flake8', 'mypy']


setup(name='soothingsounds',
      packages=find_packages(),
      description='Generate a variety of white/brown/pink noises good for relaxation',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      author='Michael Hirsch, Ph.D',
      version='0.6.0',
      url='https://github.com/scivision/soothing-sounds',
      install_requires=install_requires,
      extras_require={'io': [ 'scipy', 'pyfftw'],
                      'play': ['sounddevice'], 
                      'tests': tests_require},
      tests_require=tests_require,
      python_requires='>=3.5',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7', ]
      )
