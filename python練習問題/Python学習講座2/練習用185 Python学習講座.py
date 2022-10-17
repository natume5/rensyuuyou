#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- __new__メソッド ---")


print("--- __new__ ---")


"""
特殊メソッドの__new__は、インスタンスの初期化前に
「インスタンスを生成するために」処理が実行されます。
実装する際、__new__メソッドの第1引数はclsを指定しますが、
クラスオブジェクトです。
また、戻り値にそのクラスのインスタンスを指定した場合、
そのインスタンスの___init__メソッドが呼びだされます。
サンプルで動作を確認してみましょう。
"""

class MyClass:
	def __new__(cls):
		print('__new__')
		print(cls)

	def __init__(self):
		print('__init__')

	def __str__(self):
		return 'test'

obj = MyClass()
print(obj)    
# <class '__main__.MyClass'>
# None

"""
__new__()メソッドが呼び出されていますが、インスタンスを返していないため、
オブジェクトが生成されず、__init__()メソッドが呼び出されていない点に
注目してください。
また、__new__()メソッドの引数は、クラスオブジェクトであることが解ると思います。
"""


print("--- イミュータブルクラスの継承 ---")


"""
通常、先程のサンプルのような実装はせず、
__new__ではインスタンスを生成しそれを返します。
使いどころの1つとして、イミュータブルなクラスを継承する場合が挙げられます。
イミュータブルなクラスを継承した場合、以下のような記述ができません。

class MyClass(イミュータブルクラス):
    def __init__(self, value):
        self.value = value

__init__処理の時点で既にイミュータブルなインスタンスが生成されているため、
selfを書き換えることはできないからです。
このため、以下のサンプルように__new__を利用することで
この問題を回避することができます。
"""

class MyStr(str):

	def __new__(cls, text):
		print('__new__')
		return super().__new__(cls, text)

	def __init__(self, text):
		print('__init__')

	def __str__(self):
		return "***** " + super().__str__()

obj = MyStr('my_str')    # __new__  __init__
print(obj)    # ***** my_str

"""
イミュータブルなクラスstrを継承したクラスを記述していますが、
__new__で親クラスのインスタンスを生成したものを返しています。
（本来、上記サンプルで__init__は不要なのですが、
__new__の後に__init__が呼び出されていることを確認するために記述しています。）
"""
