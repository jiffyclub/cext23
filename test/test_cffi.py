import numpy as np
import numpy.testing as npt

from cext23.cffi import cextcffi


def test_scalar_int_add():
    assert cextcffi.scalar_int_add(33, 98) == 131


def test_np_int32_add_1d():
    x = np.arange(10, dtype='int32')
    y = np.arange(20, 30, dtype='int32')

    result = cextcffi.np_int32_add(x, y)

    npt.assert_array_equal(result, x + y)


def test_np_int32_add_2d():
    x = np.arange(10, dtype='int32').reshape((5, 2))
    y = np.arange(20, 30, dtype='int32').reshape((5, 2))

    result = cextcffi.np_int32_add(x, y)

    npt.assert_array_equal(result, x + y)
