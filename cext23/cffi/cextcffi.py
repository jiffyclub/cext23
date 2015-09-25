import numpy as np

# See CFFI docs at https://cffi.readthedocs.org/en/latest/
from ._cextcffi import ffi, lib


def scalar_int_add(x, y):
    """
    Add two integers.

    """
    return lib.scalar_int_add(x, y)


def np_int32_add(x, y):
    """
    Add two integer NumPy arrays elementwise.

    """
    # info on the ndarray.ctypes attribute is at
    # http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.ctypes.html
    # I learned about this via this SO question:
    # http://stackoverflow.com/questions/16276268/how-to-pass-a-numpy-array-into-a-cffi-function-and-how-to-get-one-back-out
    x_ptr = ffi.cast('int32_t *', x.ctypes.data)
    y_ptr = ffi.cast('int32_t *', y.ctypes.data)
    out = np.empty_like(x)
    out_ptr = ffi.cast('int32_t *', out.ctypes.data)

    lib.np_int32_add(x_ptr, y_ptr, out_ptr, x.size)

    return out
