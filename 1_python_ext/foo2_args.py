#!/usr/bin/env python

from ctypes import *

libc = cdll.LoadLibrary('libc.so.6')
libc.strchr.argtypes = [c_char_p, c_char]
libc.strchr.restype = c_char_p
print libc.strchr('abcdef', 'd')

import ipdb;ipdb.set_trace()
