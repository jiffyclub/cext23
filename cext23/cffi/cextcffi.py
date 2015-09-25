# See CFFI docs at https://cffi.readthedocs.org/en/latest/
from ._cextcffi import lib


def scalar_int_add(x, y):
    """
    Add two integers.

    """
    return lib.scalar_int_add(x, y)
