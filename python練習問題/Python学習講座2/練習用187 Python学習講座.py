#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- 変数の型を判定する その2 type関数 ---")


print("--- type関数 ---")


"""
type関数は引数で指定したオブジェクトのクラス（=型オブジェクト）を返します。
"""

class Sample():
	pass

# オブジェクトを生成
s = Sample()

# sオブジェクトの型を取得する
s_type = type(s)
print(s_type)    # <class '__main__.Sample'>

"""
この他にも動的にクラスを生成することもできるのですが、
応用的な内容であるため別途説明します。
"""


print("--- type関数とisinstance関数 ---")


"""
前述のとおり、type関数を使用して戻り値の一致を判定することで
変数の型の判定が可能なのですが、型の比較では継承関係が考慮されません。
つまり、サブクラスと親クラスは別の型として判定されます。
以下のサンプルコードは、親子関係にある2つのクラス、
Sample1とSample2からオブジェクトを生成し、型を比較しています。
"""

class Sample1():
	""" 適当なクラス """
	pass

class Sample2(Sample1):
	""" Sample1を親とするクラス """
	pass

obj1 = Sample1()    # Sample1型のオブジェクトを生成する
obj2 = Sample2()    # Sample2型のオブジェクトを生成する

# typeを使用した場合、Sample2型はSample1型とはみなされない
print(type(obj1) == Sample1)    # True
print(type(obj1) == Sample2)    # False
print(type(obj2) == Sample1)    # False
print(type(obj2) == Sample2)    # True

# isinstanceを使用した場合、Sample2型はSample1型とみなされる
print(isinstance(obj1, Sample1))    # True
print(isinstance(obj1, Sample2))    # False
print(isinstance(obj2, Sample1))    # True
print(isinstance(obj2, Sample2))    # True

"""
isinstanceの方は、親子にある場合は
同一の型として判定されていることが確認できます。
一方、前述の通り、typeの戻り値での比較はサブクラスから生成したオブジェクトは
親クラスから生成したオブジェクトと同一の型とはみなされていません。
このため、判定時に継承を考慮するかどうかを確認して適切に使い分けましょう。
"""
