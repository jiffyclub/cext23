from cext23.cffi import cextcffi


def test_add():
    assert cextcffi.add(33, 98) == 131
