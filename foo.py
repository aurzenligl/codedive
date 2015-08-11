#!/usr/bin/env python

from ctypes import *
import _ctypes

foo = CDLL('libfoo.so')
print foo.foo(42)
print foo.calls()
print foo.calls()
_ctypes.dlclose(foo._handle)

foo = CDLL('libfoo.so')
print foo.calls()

libc = CDLL('libc.so.6')
libc.printf('abcd %d %f\n', 42, c_double(412.6))

class In():
    def __init__(self, x):
        self.x = x

    @property
    def _as_parameter_(self):
        return self.x

    def from_param(self):
        return self._as_parameter_

class Out():
    def __init__(self, x):
        self.x = x

libc.strchr.restype = Out
out = libc.strchr(' ', 32)

import ipdb;ipdb.set_trace()
