import glob
import os.path
from ctypes import cdll



lib = glob.glob(os.path.join(os.path.dirname(__file__), '_cext*.so'))[0]
cext = cdll.LoadLibrary(lib)


def add(x, y):
    """
    Add two integers.

    """
    return cext.add(x, y)
