#include "demo.h"
#include <stdint.h>

int scalar_int_add(int a, int b) {
    int c;
    c = a + b;
    return c;
}


int np_int32_add(int32_t* a, int32_t* b, int32_t* out, int size) {
    for (int i = 0; i < size; ++i) {
        out[i] = a[i] + b[i];
    }

    return 0;
}
