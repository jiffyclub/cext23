from cext23.cython import cextcython


def test_scalar_int_add():
    assert cextcython.scalar_int_add(33, 98) == 131
