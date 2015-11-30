#!/usr/bin/env python

from _cffi_foo_py import ffi

lib = ffi.dlopen('libfoo.so')

print lib.foo(3)
lib.X = 10
print lib.foo(3)

for _ in xrange(1000 * 1000):
    lib.foo(4)
