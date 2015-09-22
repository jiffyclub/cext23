from ._cextcffi import lib


def add(x, y):
    """
    Add two integers.

    """
    return lib.add(x, y)
