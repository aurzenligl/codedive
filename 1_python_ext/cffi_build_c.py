#!/usr/bin/env python

from cffi import FFI
ffi = FFI()

ffi.set_source("_cffi_foo_c",
    """ // passed to the real C compiler
        #include "foo.hpp"
    """,
    libraries=['foo'],
    library_dirs=['.'])

ffi.cdef("""
    int calls();
    extern int X;
    int foo(int x);
    void bar(int* y);

    typedef struct IntVec IntVec;
    typedef bool (*Comp)(int a, int b);
    struct IntVec* IntVec_create(long size);
    void IntVec_delete(struct IntVec* v);
    int* IntVec_begin(struct IntVec* v);
    size_t IntVec_size(struct IntVec* v);
    void IntVec_push_back(struct IntVec* v, int x);
    void IntVec_resize(struct IntVec* v, long size);
    void IntVec_sort(struct IntVec* v, Comp comp);
""")

if __name__ == "__main__":
    ffi.compile()
