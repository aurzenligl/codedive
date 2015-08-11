#!/bin/bash
gcc -fPIC -fvisibility=hidden foo.cpp -shared -o libfoo.so
