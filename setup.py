#!/usr/bin/env python
install_requires = ['numpy','scipy']
tests_require = ['nose','coveralls']


from setuptools import setup,find_packages

setup(name='soothingsounds',
      packages=find_packages(),
      author='Michael Hirsch, Ph.D',
      url = 'https://github.com/scivision/soothing-sounds',
      install_requires=install_requires,
      extras_require={'pyfftw':['pyfftw'],'tests':tests_require},
      tests_require=tests_require,
      python_requires='>=3.5',
	  )
