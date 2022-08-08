#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

print('変換前')
print(type(sys.argv[1]))
print(type(sys.argv[2]))
print('変換後')
print(type(int(sys.argv[1])))
print(type(bool(sys.argv[2])))