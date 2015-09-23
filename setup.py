import sys

from Cython.Build import cythonize
from setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args or '')
        sys.exit(errno)


# see args descriptions at
# https://docs.python.org/3/distutils/apiref.html#distutils.core.Extension
extensions = [
    # this compiles the code for the ctypes example
    Extension(
        name='cext23.ctypes._cext',
        sources=['src/demo.c'],
        include_dirs=['src/']),
    # this compiles the Cython example
    Extension(
        name='cext23.cython._cext',
        sources=['cext23/cython/_cext.pyx', 'src/demo.c'],
        include_dirs=['src/'])]

setup(
    name='cext23',
    version='0.1dev',
    packages=find_packages(),
    ext_modules=cythonize(extensions),
    setup_requires=['cffi >= 1.1'],
    cffi_modules=['cext23/cffi/cextcffi_build.py:ffi'],
    install_requires=['cffi >= 1.1', 'cython >= 0.23'],
    tests_require=['pytest >= 2.7.3'],
    cmdclass={'test': PyTest})
