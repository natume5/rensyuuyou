#!/usr/bin/python
# -*- coding: UTF-8 -*-

# runner.py
import unittest
import test.test_mod1
import test.test_mod2


class TestRunner(unittest.TestCase):
	def test_runner(self):
		test_suite = unittest.TestSuite()

		# testクラスを見つけ出す
		tests = unittest.defaultTestLoader.discover("test", pattern="test_*.py")

		# 見つけたestクラスを追加する
		test_suite.addTest(tests)
		unittest.TextTestRunner().run(test_suite)

test_suite.addTest(unittest.makeSuite(test.test_mod1.TestMod1))

test_suite.addTest(unittest.makeSuite(test.test_mod2.TestMod2))
unittest.TextTestRunner().run(test_suite)
