REM echo off
(
  echo;from setuptools import setup, Extension
  echo;from Cython.Build import cythonize
  echo;import numpy
  echo;setup(
  echo;  ext_modules = cythonize(
  echo;    Extension(
  echo;    '%~n1',
  echo;    ['%1'],
  echo;    include_dirs = [numpy.get_include(^)]
  echo;    ^)
  echo;  ^),
  echo;  install_requires = "numpy"
  echo;^)
) > "setup.py"

call "D:\Soft\anaconda3\Scripts\activate.bat" "D:\Soft\anaconda3\envs\levenshtein"
python setup.py build_ext --inplace
