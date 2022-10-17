#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Cat(object):
	def __init__(self, name):
		self.name = name

class SuperCat(Cat):
	def __init__(self, name, function):
		super(SuperCat, self).__init__(name)
		self.function = function

class GotCat(SuperCat):
	def __init__(self, name, function, magic):
		super(GotCat, self).__init__(name, function)
		self.magic = magic

	def power(self):
		self.magic = "マジックパワー！！" + self.function * self.magic
