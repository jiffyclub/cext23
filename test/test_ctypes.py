from cext23.ctypes import cextctypes


def test_add():
    assert cextctypes.add(33, 98) == 131
