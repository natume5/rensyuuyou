#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- デフォルト引数 ---")


print("--- デフォルト引数 ---")


"""
Pythonの関数にはデフォルト引数と呼ばれる記法があります。
これを使用すると関数定義時に引数にデフォルト値を設定することが可能です。
以下のように記述します。

関数定義
def 関数名(引数1=デフォルト値1, 引数2=デフォルト値2, ・・・):

それではサンプルです。以下のサンプルは2数の和を計算する関数です。
ただし、引数を指定しない場合はそれぞれ0が設定されます。
"""

# デフォルト引数の例
def sample_function(x=0, y=0):
	z = x + y
	return z


# パラメータを指定して呼び出す
z1 = sample_function(5, 5)
print(z1)    # 10

z2 = sample_function(5)
print(z2)    # 5

z3 = sample_function()
print(z3)    # 0

"""
デフォルト引数の注意点として、
デフォルト引数の後ろに通常の引数を設定することは不可という点です。
以下のコードはSyntaxErrorが発生し、実行することができません。


# デフォルト引数の後ろに通常の引数
def sample_function(x=0, y):
    z = x + y
    return z
 
 
sample_function(2, 3)
# SyntaxError: non-default argument follows default argument
"""


print("--- デフォルト引数を使用する際の注意点 ---")


"""
ここまでで関数定義で引数のデフォルト値を設定できることを説明しましたが、
1点重要な注意点があります。まずは以下のサンプルを見てください。
"""

def sample(x, arg=[]):
	arg.append(x)
	return arg

print(sample(1))    # [1]
print(sample(2))    # [1, 2] !?
print(sample(3))    # [1, 2, 3] !!??

"""
引数のリストに0を加えるsample関数を3回呼び出していますが、
2回め以降は設定されていないものが戻り値に加えられてしまっています。
これはデフォルト引数の評価は最初の1回しか行われないため、
appendのような破壊的な操作を行うと、
デフォルト引数の値が1回めの呼び出しで[1]に、
2回めの呼び出しで[1, 2]に書き換わってしまうからです。
対策として、デフォルト引数にはイミュータブルなものを使用することで破壊されないようにし、
if文等で引数が空の場合の初期値設定の処理を加える、という方法があります。
"""

def sample(x, arg=None):
	if arg is None:
		arg = []

	arg.append(x)
	return arg

print(sample(1))    # [1]
print(sample(2))    # [2]
print(sample(3))    # [3]
