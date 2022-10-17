#!/usr/bin/python
# -*- coding: UTF-8 -*-


from Inheritance_Inheritance import GotCat
from fish import Medaka


class Main(GotCat, Medaka):
	def __init__(self):
		super(Main, self).__init__()

cat1 = GotCat('だい', '癒す', 5)
cat1.power()
print(cat1.name, cat1.magic)


fish1 = Medaka('メダカ1号')
print(fish1.name)


class CatCat(GotCat):
	def __init__(self, name, function, magic, change):
		super(CatCat, self).__init__(name, function, magic)
		self.change = change + 'に変身だにゃー'

cat2 = CatCat('こんきち', 'はねる', '2', 'みけねこ')
print(cat2.name, cat2.change)










