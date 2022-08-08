#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

if len(sys.argv) - 1 >= 3:
    print(sys.argv[3])
else:
    print('引数が足りていません')