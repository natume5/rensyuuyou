#!/usr/bin/python
# -*- coding: UTF-8 -*-


from pkg1 import mod1


def func1():
	print('sample1.py: ' + __name__)
	mod1.func1()

if __name__ == '__main__':
	func1()
