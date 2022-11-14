#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- unittest 単体テスト入門 その1 基本的な使い方 ---")


print("--- 基本的な使い方 ---")


"""
unittestモジュールはpythonの組込みモジュールとして
提供されている単体テストフレームワークです。
Javaの単体テストフレームワークであるJUnitに触発されたものであるため、
使い方もJUnitとほぼ同様です。
まずは簡単なサンプルを通じて使い方を見てみましょう。
まずはテストされる側のモジュールを準備します。
足し算をする関数と、数値が正かどうかを判定する関数が記述されています。

# sample4.py テスト対象モジュール

def add_num(num1, num2):
    return num1 + num2 

def is_positive(num):
    return num > 0


次にテストをする側のコードです。
ファイル名は、test_テスト対象モジュール.pyとします。
また、テストクラスはテスト対象クラス名にTestをつけた名前を使用し、
unittest.TestCaseを継承します。
また各テストケースに該当するテストメソッドは、
テスト対象関数・メソッド名の頭にtestをつけた名前を使用します。
"""

# test_sample.py テストする側のコード
import unittest
import sample4

class TestStringMethods(unittest.TestCase):

	def test_add_num(self):
		"""
		add_numの単体テスト
		"""
		self.assertEqual(7, sample.add_num(3, 4))

	def test_is_positive(self):
		"""
		is_numの単体テスト
		"""
		self.assertTrue(sample4.is_positive(3))
		self.assertFalse(sample4.is_positive(0))
		self.assertFalse(sample4.is_positive(-1))

"""
テストの実行は以下の通りmオプションをつけてunittestモジュールを実行します。

$ python -m unittest
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK


python -m unittest
__init__.py: pkg1

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK


テストが実行され、結果が出力されました。
上のコードで使用したassertEqualは、
検査値と期待値が等しいことをテストします。
公式ドキュメントには引数の順序に関する言及はないのですが、
JUnitに習うならば期待値、検査値の順序で統一したほうがよいかもしれません。
assertTrue、assertFalseは
検査値がそれぞれTrue、Falseであることをテストします。
"""


print("--- 検査用メソッド ---")


"""
ここからもう少しunittestモジュールについて細かく見ていきましょう。
上の節でassertEqual、assertTrue、assertFalseについて紹介しましたが、
それ以外にTestCaseクラスで提供されている
代表的なテストメソッドには以下のようなものがあります。

メソッド 	                     確認事項
assertEqual(a, b) 	         a == b
assertNotEqual(a, b) 	     a != b
assertTrue(x) 	             bool(x) is True
assertFalse(x) 	             bool(x) is False
assertIs(a, b) 	             a is b
assertIsNot(a, b) 	         a is not b
assertIsNone(x) 	         x is None
assertIsNotNone(x) 	         x is not None
assertIn(a, b) 	             a in b
assertNotIn(a, b) 	         a not in b
assertIsInstance(a, b) 	     isinstance(a, b)
assertNotIsInstance(a, b) 	 not isinstance(a, b)
"""


print("--- テスト用メソッド ---")


"""
ある程度規模のあるプログラムをテストする場合、
テストの実行前や後に処理を追加したい場合が出てきます。
例えば、データベースに接続しテストデータを投入たり、
テスト終了時にテストデータを削除したりロールバックすることが挙げられます。
setUpClass()/tearDownClass()、setUp()/tearDown()、skipTest()
を紹介します。

setUpClass()/tearDownClass()、setUp()/tearDown()

setUpClass()/tearDownClass()は、
テストクラス全体の前後処理を記述します。
setUp()/tearDown()は個別のテストメソッドの前後処理を記述します。
先ほどのサンプルにprint関数で文字出力を追記し、動作を確認してみましょう。
"""

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

"""
 以下、実行時の出力です。

$ python -m unittest
*** 全体前処理 ***
+ テスト前処理
test_add_num開始
test_add_num終了
+ テスト後処理
.+ テスト前処理
test_is_positive開始
test_is_positive終了
+ テスト後処理
.*** 全体後処理 ***

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK


D:\テキストドキュメント１\IT・エンジニア・プログラミング\sublime text3関係\python練習問題\Python学習講座2>python -m unittest
__init__.py: pkg1
*** 全体前処理 ***
+ テスト前処理
test_add_num開始
test_add_num終了
+ テスト後処理
.s*** 全体後処理 ***

----------------------------------------------------------------------
Ran 2 tests in 0.016s

OK (skipped=1)


テストの実行前後で処理が呼び出されていることが確認できます。


テストのスキップ

システム改修で修正中の機能が時など、
テストが通過しないことが予めわかっているため
特定の機能だけスキップしたい場合が出てきますが、
そんな場合はskipデコレーターを使用します。
引数に文字列を指定します。


 @unittest.skip("モジュール修正中のためスキップ")
    def test_is_positive(self):
        """"""
        is_numの単体テスト
        """"""
        print('test_is_positive')
        self.assertTrue(sample.is_positive(3))
        self.assertFalse(sample.is_positive(0))
        self.assertFalse(sample.is_positive(-1))

最初のサンプルのメソッドの1つにデコーレーターをつけて実行してみましょう。

$ python -m unittest
.s
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK (skipped=1)

スキップされ、テストメソッドが実行されていないことが確認できます。
また、ここでは紹介しませんが、
クラスデコレータを使用することによりテストクラス全体をスキップしたり、
skipIfデコレータを使用して条件付きでスキップすることができます。
"""
