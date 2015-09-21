from setuptools import setup, find_packages, Extension


setup(
    name='cext23',
    version='0.1dev',
    packages=find_packages(),
    ext_modules=[
        Extension(
            'cext23._cext', ['src/add.c'], ['src/'])],
    setup_requires=['cffi >= 1.1'],
    cffi_modules=['cext23/cextcffi_build.py:ffi'],
    install_requires=['cffi >= 1.1'])
