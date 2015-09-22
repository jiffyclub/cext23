# See Cython docs at http://docs.cython.org/

cdef extern from "add.h":
    cpdef int add(int a, int b)
