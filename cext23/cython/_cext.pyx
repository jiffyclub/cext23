# See Cython docs at http://docs.cython.org/

from libc.stdint cimport int32_t

import numpy as np
cimport numpy as np

cdef extern from "demo.h":
    # the cpdef thing both declares the function, wraps it for Python,
    # and includes it as part of the module, see
    # http://docs.cython.org/src/tutorial/external.html#external-declarations
    cpdef int scalar_int_add(int a, int b)
    cdef int np_int32_add(int32_t* a, int32_t* b, int32_t* out, int size)


def np_int32_add_wrap(np.ndarray x, np.ndarray y):
    # x.data is a pointer to the array data in memory
    cdef int32_t* x_ptr = <int32_t*> x.data
    cdef int32_t* y_ptr = <int32_t*> y.data
    cdef np.ndarray out = np.empty_like(x)
    cdef int32_t* out_ptr = <int32_t*> out.data

    np_int32_add(x_ptr, y_ptr, out_ptr, x.size)

    return out
