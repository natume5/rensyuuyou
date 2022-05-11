#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("---Python3系の基礎文法（関数の使い方、クロージャ、ラムダ関数）---")
print("関数の基本的な使いかた")

def print_sum(num1, num2):
	print(num1 + num2)

print_sum(10, 20)    # 30


"""
位置引数

先頭から順に対応する位置の仮引数に値をコピーする引数のことを「位置引数」と呼ぶ。
"""

def print_args(arg1, arg2, arg3):
	print("arg1:", arg1, "arg2:", arg2, "arg3:", arg3)


print_args(1111, True, 'Python')    # arg1: 1111 arg2: True arg3: Python


"""
キーワード引数

仮引数の名前を指定して実引数を指定することもでき、この場合は「キーワード引数」として扱われる。
""" 

def print_args(arg1, arg2, arg3):
	print("arg1:", arg1, "arg2:", arg2, "arg3:", arg3)

print_args(arg2="two", arg1="one", arg3="three")    # arg1: one arg2: two arg3: three


"""
デフォルト引数値の指定

仮引数にデフォルト値を指定することもできる。
呼び出し元が対応する実引数を渡さなかった場合に、デフォルト値が使われる。
"""

def print_args(arg1, arg2, arg3='default value'):
	print("arg1:", arg1, "arg2:", arg2, "arg3:", arg3)

# デフォルト値が使われる場合 (実引数を渡していない)
print_args("one", "two")    # arg1: one arg2: two arg3: default value

# デフォルト値が使われない場合 (実引数を渡している)
print_args("one", "two", "three")    # arg1: one arg2: two arg3: three


"""
*による位置引数のタプル化

関数定義時に、仮引数の一部として*を使うと、可変個数の位置引数をタプルにまとめてセットする。
"""

def print_args(*args):
	print("args tuple:", args)

# 引数を複数個指定
print_args("one", "two", "three")     # args tuple: ("one", "two", "three")

# 引数なし
print_args()    # args tuple: ()

"""
必須の位置引数がある場合には、下記のような使い方も可能。
"""

def print_args(arg1, arg2, *args):
	print("arg1:", arg1)
	print("arg2:", arg2)
	print("args:", args)

print_args("one", "two", 1, 10, 100)    # arg1: one arg2: two args: (1, 10, 100)


"""
**によるキーワード引数の辞書化

関数定義時に、**を使うと、キーワード引数を辞書にまとめてセットすることができる。
"""

def print_kwargs(**kwargs):
	print("kwargs:", kwargs)


print_kwargs(arg1="one", arg2="two", arg3="three")
# kwargs: {"arg1": "one", "arg2": "two", "arg3": "three"}


"""
引数に関数をセット

関数の引数として関数を扱ったり、関数からの戻り値として関数を返したりできる。
"""

def print_string():
	print("print_string")

def execute_func(arg_func):
	arg_func()

execute_func(print_string)     # print_string


"""
関数内関数

関数の中で関数を定義することもできる。
"""

def outer():
	def inner():
		print("inner function")
	inner()

outer()    # inner function


"""
クロージャ

関数内関数をクロージャとして機能させ、動的に関数を生成することも可能
"""

def todays_weather(arg1):
	def return_weather():
		return "It's" + arg1 + "today."
	return return_weather

day1 = todays_weather(" sunny day ")
day2 = todays_weather(" cloudy ")

print(day1())    # "It's sunny day today."
print(day2())    # "It's cloudy today."


"""
ラムダ関数
"""
# ラムダ関数を使わない実装
def return_sum(num1, num2):
	return num1 + num2

print("answer:", return_sum(10, 20))    # answer: 30


# ラムダ関数を使った実装
return_sum = lambda num1, num2: num1 + num2
print("answer:", return_sum(10, 20))     # answer: 30


"""
map()と組み合わせたラムダ関数の活用例

map()と組み合わせると、引数で渡されたリストのようなiterablesな要素を、
funcに渡して処理してくれる下記のような実装も可能。（※1）

[追記]
※1：値を返す場合に限られ、内容は式のみで文(if文、for文、while文など)は書けない。
[/追記]
"""
"""
>>> help(map)
Help on class map in module builtins:

class map(object)
 |  map(func, *iterables) --> map object
 |
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
"""

num_list = list(range(1, 6))
print(num_list)    # [1, 2, 3, 4, 5]

print(list(map(lambda x: x**2, num_list)))    # [1, 4, 9, 16, 25]


