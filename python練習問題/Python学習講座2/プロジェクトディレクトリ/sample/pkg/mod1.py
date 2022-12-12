#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
sampleモジュール sampleクラス等の説明文
"""


class SampleClass:
	"""
	sampleクラスの説明文
	"""

	def __init__(self, arg):
		"""
		引数の文字列表現の前後を装飾する

		:param arg: パラメータ
		:return: 結果文字列
		"""
		self.d_str = arg

	def func1(self, arg):
		"""
		引数の文字列表現の前後を装飾する

		:param arg:パラメータ
		:return: 結果文字列
		"""
		result = self.d_str + str(arg) + self.d_str
		return result
