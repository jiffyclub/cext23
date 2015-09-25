# See Cython docs at http://docs.cython.org/
from . import _cext


def scalar_int_add(x, y):
    """
    Add two integers.

    """
    return _cext.scalar_int_add(x, y)


def np_int32_add(x, y):
    """
    Add two integer NumPy arrays elementwise.

    """
    return _cext.np_int32_add_wrap(x, y)
