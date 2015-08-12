#!/usr/bin/env python

from ctypes import *

foo = cdll.LoadLibrary('libfoo.so')

foo.IntVec_create.restype = c_void_p
foo.IntVec_create.argtypes = [c_size_t]
foo.IntVec_delete.restype = None
foo.IntVec_delete.argtypes = [c_void_p]

print "Let's create and delete immediately."
foo.IntVec_delete(foo.IntVec_create(10))

class IntVec(object):
    def __init__(self, size):
        self.v = foo.IntVec_create(size)

    def __del__(self):
        foo.IntVec_delete(self.v)

print "Let's create named IntVec..."
v = IntVec(1)
print "...again... (note deallocation of previous IntVec)"
v = IntVec(2)
print "...and delete second one explicitly."
del v

import ipdb;ipdb.set_trace()
