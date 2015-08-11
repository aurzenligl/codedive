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

class Dupa():
    def __init__(self, x):
        self.x = x

    @property
    def _as_parameter_(self):
        return self.x

    def from_param(self):
        print 'kolanko!'
        return self._as_parameter_

import pdb;pdb.set_trace()
