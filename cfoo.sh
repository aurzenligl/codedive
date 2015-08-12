#!/bin/bash
g++ -s -O3 -fno-exceptions -fPIC -fvisibility=hidden foo.cpp -shared -o libfoo.so
