# See the ctypes documentation at
# https://docs.python.org/3/library/ctypes.html
import ctypes as ct
import glob
import os.path
import sys

import numpy as np


dirname = os.path.dirname(__file__)

# have to jump through some hoops here because on Python 3.5(+) the
# compiled .so file has a fancy name, see
# https://docs.python.org/3/whatsnew/3.5.html#build-and-c-api-changes
#
# this is probably not how this should be done in practice,
# and I'm not sure about the best way to compile your C code and make it
# available to your Python file
#
# for this reason ctypes is probably best used with already installed
# C libraries
if os.path.exists(os.path.join(dirname, '_cext.so')):
    libfile = '_cext.so'
else:
    major = sys.version_info.major
    minor = sys.version_info.minor
    libfile = glob.glob(
        os.path.join(dirname, '_cext.*{}{}*.so'.format(major, minor)))[0]

lib = os.path.join(dirname, libfile)
cext = ct.cdll.LoadLibrary(lib)


def scalar_int_add(x, y):
    """
    Add two integers.

    """
    return cext.scalar_int_add(x, y)


def np_int32_add(x, y):
    """
    Add two integer NumPy arrays elementwise.

    """
    # info on the ndarray.ctypes attribute is at
    # http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.ctypes.html
    out = np.empty_like(x)
    cext.np_int32_add(
        x.ctypes.data_as(ct.POINTER(ct.c_int32)),
        y.ctypes.data_as(ct.POINTER(ct.c_int32)),
        out.ctypes.data_as(ct.POINTER(ct.c_int32)),
        x.size)
    return out
