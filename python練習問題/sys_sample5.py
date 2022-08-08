#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

try:
    print(sys.argv[3])
except IndexError:
    print('引数が足りていません')
