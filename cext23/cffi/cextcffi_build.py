# See CFFI docs at https://cffi.readthedocs.org/en/latest/
from cffi import FFI


ffi = FFI()

# set_source is where you specify all the include statements necessary
# for your code to work and also where you specify additional code you
# want compiled up with your extension, e.g. custom C code you've written
#
# set_source takes mostly the same arguments as distutils' Extension, see:
# https://cffi.readthedocs.org/en/latest/cdef.html#ffi-set-source-preparing-out-of-line-modules
# https://docs.python.org/3/distutils/apiref.html#distutils.core.Extension
ffi.set_source(
    'cext23.cffi._cextcffi',
    '#include "demo.h"',
    include_dirs=['src/'],
    sources=['src/demo.c'])

# declare the functions, variables, etc. from the stuff in set_source
# that you want to access from your C extension:
# https://cffi.readthedocs.org/en/latest/cdef.html#ffi-cdef-declaring-types-and-functions
ffi.cdef('int scalar_int_add(int a, int b);')
