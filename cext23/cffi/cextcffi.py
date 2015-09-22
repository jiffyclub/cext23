# See CFFI docs at https://cffi.readthedocs.org/en/latest/
from ._cextcffi import lib


def add(x, y):
    """
    Add two integers.

    """
    return lib.add(x, y)
