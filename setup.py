from Cython.Build import cythonize
from setuptools import setup, find_packages, Extension


# see args descriptions at
# https://docs.python.org/3/distutils/apiref.html#distutils.core.Extension
extensions = [
    # this compiles the code for the ctypes example
    Extension(
        name='cext23.ctypes._cext',
        sources=['src/add.c'],
        include_dirs=['src/']),
    # this compiles the Cython example
    Extension(
        name='cext23.cython._cext',
        sources=['cext23/cython/_cext.pyx', 'src/add.c'],
        include_dirs=['src/'])]

setup(
    name='cext23',
    version='0.1dev',
    packages=find_packages(),
    ext_modules=cythonize(extensions),
    setup_requires=['cffi >= 1.1'],
    cffi_modules=['cext23/cffi/cextcffi_build.py:ffi'],
    install_requires=['cffi >= 1.1'])
