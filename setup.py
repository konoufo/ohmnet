from distutils.core import setup
import os

from Cython.Build import cythonize
import numpy


setup(
    ext_modules=cythonize(os.path.join('ohmnet', 'gensimmod', 'model', 'word2vec_inner.pyx')),
    include_dirs=[numpy.get_include()]
)
