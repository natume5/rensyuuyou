#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- 変数の型を判定する ---")


"""
ここまで、様々な変数の型について学習してきました。
ここではある変数の型が何なのかを確認する方法について学習します
"""


print("--- isinstance関数 ---")


"""
isinstance関数の使い方
pythonは型宣言がないため、
関数の引数や戻り値の型が実行するまでわからない場合があります。
このため、型をチェックする必要が随所で出てきます。
この場合、組込みのisinstance関数を使用します。

isinstance
isinstance(変数, 型)

基本的な型を判定する処理のサンプルです。
"""

def sample(obj):
	""" 引数の型を判定する """

	if isinstance(obj, bool):
		print('bool型です')

	if isinstance(obj, int):
		print('int型です')

	if isinstance(obj, float):
		print('float型です')

	if isinstance(obj, complex):
		print('complex型です')

	if isinstance(obj, list):
		print('list型です')

	if isinstance(obj, tuple):
		print('tuple型です')

	if isinstance(obj, range):
		print('range型です')

	if isinstance(obj, str):
		print('str型です')

	if isinstance(obj, set):
		print('set型です')

	if isinstance(obj, frozenset):
		print('frozenset型です')

	if isinstance(obj, dict):
		print('dict型です')

sample('aaa')    # str型です
sample(1)    # int型です
sample(1.1)    # float型です
sample([1, 2, 3])    # list型です
sample({100, 200})    # set型です
sample({'key': 100})    # dict型です


"""
補足 基本的な変数の型
補足として、isinstance関数の引数に使用する基本的な変数の型を以下に掲載します。

型名	        説明
bool	    真偽値型
int	        整数型
float	    小数型
complex	    複素数型
list	    list型
tuple	    タプル型
range	    range型
str	        文字列型
bytes	    バイト型
set	        集合型
frozenset	イミュータブルな集合型
dict	    辞書型
"""


print("--- 補足 ---")


"""
isinstance関数で変数の型の一致を確認することができましたが、
よく似たものにtypeというものがあります。

変数の型を判定する その2 type関数

classについて学習した後学習しましょう。
"""
