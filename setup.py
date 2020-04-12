from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy
setup(
  ext_modules = cythonize(
    Extension(
    'dameraulevenshtein',
    ['dameraulevenshtein.pyx'],
    include_dirs = [numpy.get_include()]
    )
  ),
  install_requires = "numpy"
)
