#!/usr/bin/env python

from ctypes import *

foo = cdll.LoadLibrary('libfoo.so')
print foo.calls()
print foo.calls()
cdll.LoadLibrary('libdl.so').dlclose(foo._handle)

foo = cdll.LoadLibrary('libfoo.so')
print foo.calls()

import ipdb; ipdb.set_trace()
