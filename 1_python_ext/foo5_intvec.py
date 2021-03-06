#!/usr/bin/env python

from ctypes import *

foo = cdll.LoadLibrary('libfoo.so')

def types(fun, ret, args):
    fun.restype = ret
    fun.argtypes = args

Comp = CFUNCTYPE(c_bool, c_int, c_int)

types(foo.IntVec_create, c_void_p, [c_size_t])
types(foo.IntVec_delete, None, [c_void_p])
types(foo.IntVec_begin, POINTER(c_int), [c_void_p])
types(foo.IntVec_size, c_size_t, [c_void_p])
types(foo.IntVec_resize, None, [c_void_p, c_size_t])
types(foo.IntVec_push_back, None, [c_void_p, c_int])
types(foo.IntVec_sort, None, [c_void_p, Comp])

class IntVec(object):
    def __init__(self, size):
        self.v = foo.IntVec_create(size)

    def __del__(self):
        foo.IntVec_delete(self.v)

    def push_back(self, value):
        foo.IntVec_push_back(self.v, value)

    def size(self):
        return foo.IntVec_size(self.v)

    def resize(self, size):
        return foo.IntVec_resize(self.v, size)

    def sort(self, comp):
        foo.IntVec_sort(self.v, Comp(comp))

    def _begin(self):
        return foo.IntVec_begin(self.v)

    def __repr__(self):
        return str([x for x in self])

    def __setitem__(self, index, value):
        self._begin()[index] = value

    def __iter__(self):
        class IntVecIter(object):
            def __init__(self, ptr, size):
                self.ptr = ptr
                self.size = size
                self.current = 0
            def next(self):
                if self.current == self.size:
                    raise StopIteration
                else:
                    self.current += 1
                    return self.ptr[self.current - 1]
        return IntVecIter(self._begin(), self.size())

print "\n--- Let's create and delete immediately."
foo.IntVec_delete(foo.IntVec_create(10))

print "\n--- Let's create named IntVec..."
v = IntVec(1)
print "--- ...again... (note deallocation of previous IntVec)"
v = IntVec(2)
print "--- ...and delete second one explicitly."
del v

print "\n--- Let's fill elements..."
v = IntVec(3)
v[0] = 42
v[1] = 666
v[2] = 65536
print v
print "--- ...push_back a couple more..."
v.push_back(7)
v.push_back(8)
v.push_back(9)
print v
print "--- ...sort them..."
v.sort(lambda x,y: x<y)
print v
v.sort(lambda x,y: x>y)
print v
print "--- ...and resize down and up."
v.resize(2)
print v
v.resize(20)
print v

import ipdb;ipdb.set_trace()
