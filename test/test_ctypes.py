from cext23.ctypes import cextctypes


def test_scalar_int_add():
    assert cextctypes.scalar_int_add(33, 98) == 131
