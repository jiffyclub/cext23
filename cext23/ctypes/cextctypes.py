# See the ctypes documentation at
# https://docs.python.org/3/library/ctypes.html
import glob
import os.path
import sys
from ctypes import cdll


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
cext = cdll.LoadLibrary(lib)


def add(x, y):
    """
    Add two integers.

    """
    return cext.add(x, y)
