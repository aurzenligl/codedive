#!/usr/bin/env python

from ctypes import *

foo = cdll.LoadLibrary('libfoo.so')
X = c_int.in_dll(foo, "X")
print X.value, foo.foo(2)
X.value = 42
print X.value, foo.foo(2)

import ipdb;ipdb.set_trace()
