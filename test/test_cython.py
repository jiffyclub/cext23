from cext23.cython import cextcython


def test_add():
    assert cextcython.add(33, 98) == 131
