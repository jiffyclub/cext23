# See Cython docs at http://docs.cython.org/
from . import _cext


def add(x, y):
    """
    Add two integers.

    """
    return _cext.add(x, y)
