#!/usr/bin/python
# -*- coding: UTF-8 -*-


# sample2.py
from pkg1 import mod1

def func1():
	print('sample2.py: ' + __name__)
	mod1.func1()

if __name__ == '__main__':
	func1()
