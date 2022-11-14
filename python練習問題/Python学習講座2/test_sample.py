#!/usr/bin/python
# -*- coding: UTF-8 -*-


# test_sample.py テストする側のコード
import unittest
import sample4


class TestStringMethods(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('*** 全体前処理 ***')

	@classmethod
	def tearDownClass(cls):
		print('*** 全体後処理 ***')

	def setUp(self):
		print('+ テスト前処理')

	def tearDown(self):
		print('+ テスト後処理')

	def test_add_num(self):
		"""
		add_numの単体テスト
		"""
		print('test_add_num開始')
		self.assertEqual(7, sample4.add_num(3, 4))
		print('test_add_num終了')

	@unittest.skip("モジュール修正中のためスキップ")
	def test_is_positive(self):
		"""
		is_numの単体テスト
		"""
		print('test_is_positive開始')
		self.assertTrue(sample4.is_positive(3))
		self.assertFalse(sample4.is_positive(0))
		self.assertFalse(sample4.is_positive(-1))
		print('test_is_positive終了')
