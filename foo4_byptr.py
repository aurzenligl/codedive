#!/usr/bin/env python

from ctypes import *

foo = cdll.LoadLibrary('libfoo.so')
x = c_int()
print x.value
foo.bar(byref(x))
print x.value

import ipdb;ipdb.set_trace()
