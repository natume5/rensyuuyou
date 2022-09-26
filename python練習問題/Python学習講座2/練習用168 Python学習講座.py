#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- 内部関数（inner function）とnonlocal宣言 ---")


print("--- 内部関数（inner function） ---")


"""
Pythonでは、関数内部に関数を定義することが可能です。
この関数を内部関数（inner function）と呼びます。
"""

def outer_function():
	""" 外側の関数 """
	print('outer')

	def inner_function():
		""" 内側の関数 """
		print('inner')

	inner_function() 

outer_function()
# outer
# inner

"""
先ほどの関数オブジェクトの考え方を応用すると、
関数の戻り値として内部関数を返すことができます。
以下のサンプルでは、outer_functionを呼び出すと
戻り値にinner_functionを関数オブジェクトとして返しています。
"""

def outer_function():
	""" 外側の関数 """
	print('outer')

	def inner_function():
		""" 内側の関数 """
		print('inner')

	# 内側の関数をオブジェクトとしてreturnする
	f = inner_function
	return f

f = outer_function()    # outer
# 受け取った内側の関数を実行する
f()    # innerが出力される    # inner

"""
最初は違和感があるかもしれませんが、
「関数を実行すると戻り値に関数が得られる」
という実装は様々なライブラリを利用する際に見られるので知っておいてください。
"""


print("--- nonlocal宣言 ---")


"""
内側で定義した関数から外側のローカル関数を参照することが可能です。
内側の関数で外側のローカル変数を変更したい場合、
nonlocal宣言を記述することでできるようになります。
global宣言と似ていますね。
"""

def outer_function():
	""" 外側の関数 """

	x = 100
	print(x)    # 100が出力される

	def inner_function():
		""" 内側の関数 """
		nonlocal x
		x = 200
		print(x)    # 200が出力される

	inner_function()
	print(x)    # 200が出力される

outer_function()

"""
外側の関数の変数が内部関数で変更されたことが確認できます。
"""



print("--- shelokuma tech blog ---")
print("--- Python | inner関数とノンローカル宣言の使い方 ---")


"""
Pythonでは，関数の中に関数を定義することができる．
中の関数をinner関数と呼ぶ．
外側の関数からinner関数を呼び出すため，
inner関数の処理は外からは分からなくできる．
なお，ノンローカル宣言をすると，
外側の関数の変数をinner関数の変数に置き換えることができる．
以下にinner関数とノンローカル宣言の説明をする．
"""


print("--- ■inner関数の作成 ---")


"""
関数(外側関数)を定義し，その中に定義する関数をinner関数と呼ぶ．
外側関数を呼び出すことによってinner関数での処理を行うことができる．
以下では7行目の外側関数(outer)によって，
4行目のinner関数の処理が実行される．
"""

# 1の処理(基本的なinner関数)
def outer():
	def inner():
		print('Hello')
	inner()

outer()    # Hello


print("--- ■ノンローカル宣言の利用 ---")


"""
以下にノンローカル宣言なしの構文(#1の処理)とありの構文(＃2の処理)を記載する．
#1と#2の構文の違いは，15行目の”nonlocal programming”の有無である．
ノンローカル宣言にするには，変数の前に”nonlocal”を付ける．
"""

# 1の処理(ノンローカル宣言なし)
def outer():
	programming = 'PHP'
	def inner():
		programming = 'Python'
		print(f'inner処理: programming is {programming}')
	inner()
	print(f'outer処理: programming is {programming}')

outer()
# inner処理: programming is Python
# outer処理: programming is PHP


# 2の処理(ノンローカル宣言あり)
def outer():
	programming = 'PHP'
	def inner():
		nonlocal programming    # ノンローカル宣言
		programming = 'Python'
		print(f'inner処理: programming is {programming}')
	inner()
	print(f'outer処理: programming is {programming}')

outer()
# inner処理: programming is Python
# outer処理: programming is Python

"""
■実行結果

#1の結果：出力した値(Python, PHP)は異なる
#2の結果：#2の処理の14行目の変数"PHP"が
16行目の変数"Python"に置き換わることによって，
出力した値は同じ"Python"となる．
"""
