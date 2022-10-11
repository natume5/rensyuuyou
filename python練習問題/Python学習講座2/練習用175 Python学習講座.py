#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- オブジェクトへの属性追加 ---")


print("--- 生成後の属性追加と削除 ---")


"""
Pythonでは独自クラスから生成したインスタンスは
属性を外部から追加したり削除することができます。
"""

class Sample:

	def __init__(self):
		self.x = 100

obj = Sample()
obj.y = 200    # Sample型にyを追加することが出来る
print(obj.y)

"""
del obj.x # xを削除することもできる
print(obj.x) # AttributeError: 'Sample' object has no attribute 'x'

上のコードでは、
インスタンス変数にxをもつSample型のオブジェクトを生成していますが、
その後、属性yを追加したりdel文で元々あったxを削除したりしています。
"""


print("--- 空のクラス ---")


"""
先程の属性追加は空のクラスに対しても行うことが可能です。
少し変わった使い方ですが、
関数の戻り値で小さなオブジェクトにセットして返したい時などに
利用することがあります。
"""

class Sample:
	pass

obj = Sample()    # 空のクラスをインスタンス化する
obj.x = 100
obj.y = 200
print(obj.x, obj.y)    # 100 200




















































