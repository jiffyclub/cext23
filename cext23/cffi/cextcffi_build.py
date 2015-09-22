from cffi import FFI


ffi = FFI()

ffi.set_source(
    'cext23.cffi._cextcffi',
    '#include "add.h"',
    include_dirs=['src/'],
    sources=['src/add.c'])
ffi.cdef('int add(int a, int b);')
