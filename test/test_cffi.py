from cext23.cffi import cextcffi


def test_scalar_int_add():
    assert cextcffi.scalar_int_add(33, 98) == 131
