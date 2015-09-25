# See Cython docs at http://docs.cython.org/

cdef extern from "demo.h":
    # the cpdef thing both declares the function, wraps it for Python,
    # and includes it as part of the module, see
    # http://docs.cython.org/src/tutorial/external.html#external-declarations
    cpdef int scalar_int_add(int a, int b)
