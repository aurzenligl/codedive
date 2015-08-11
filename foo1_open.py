#!/usr/bin/env python

from ctypes import *
from _ctypes import dlclose

foo = cdll.LoadLibrary('libfoo.so')
print foo.calls()
print foo.calls()
dlclose(foo._handle)

foo = cdll.LoadLibrary('libfoo.so')
print foo.calls()

