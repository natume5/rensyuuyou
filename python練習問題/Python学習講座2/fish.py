#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Fish:
	def __init__(self, name, build='ほね', eyelids=False):
		self.name = name
		self.build = build
		self.eyelids = eyelids

	def swim(self):
		print("こちらの魚は泳ぎます")

	def swim_back(self):
		print('こちらの魚は後ろ向きにも泳ぎます')

class Medaka(Fish):
	pass

class Kingyo(Fish):
	def __init__(self, name, build='ほね', eyelids=False):
		self.name = '金魚ちゃん' + name + 'だよ'
		self.build = build + ' かな'
		self.eyelids = eyelids




