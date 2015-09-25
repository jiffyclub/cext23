# See Cython docs at http://docs.cython.org/
from . import _cext


def scalar_int_add(x, y):
    """
    Add two integers.

    """
    return _cext.scalar_int_add(x, y)
