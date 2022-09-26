#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- キーワード引数 ---")


print("--- 位置引数とキーワード引数 ---")


"""
Pythonでは引数の指定方法が２つあります。
1つはこれまで解説したとおりオーソドックスに順番に指定する方法です。
このような指定方法を位置引数と呼びます。
2つ目は、キーワード引数と呼ばれ、
引数名=値の形式で引数の順序に関係なく指定することができます。
サンプルで確認してみましょう。
"""

def sample_function(arg1, arg2):
	print(arg1, arg2)


sample_function('a', 'b')    # 順番に引数を指定する a b
sample_function(arg1='c', arg2='d')    # キーワードを指定する c d
sample_function(arg2='e', arg1='f')    # キーワードの場合は順番通りでなくていい f e
sample_function('c', arg2='d')    # 後方の引数のみキーワード指定 c d

"""
関数を3回呼び出しています。コード中のコメントで書いたとおり、
キーワード引数の場合は順番どおりでなくても問題なく動くことが確認できます。
引数が多くなると引数への設定値を誤って書いてしまうことがありますが、
キーワード引数を使用するとこういった事故を防ぐことができます。
なお、キーワード引数の後ろに位置引数を設定することは許可されていません。
一方、後方の引数のみキーワード指定することは可能です。
以下のサンプルはエラーが発生します。


def sample_function(arg1, arg2):
    print(arg1, arg2)
 
sample_function('c', arg2='d') # 後方の引数のみキーワード指定
sample_function(arg1='c', 'd') # キーワード引数の後ろに位置引数を指定
# SyntaxError: positional argument follows keyword argument
"""


print("--- 引数の展開 ---")


"""
また、関数呼び出し時に複数の位置引数やキーワード引数を指定することが可能で、
関数側で自動的に引数が変数に展開されます。

位置引数をまとめて指定する
def 関数名(*リスト):
キーワード引数をまとめて指定する
def 関数名(**辞書):

以下のサンプルでは関数の呼び出し時に位置引数、
キーワード引数をそれぞれまとめて指定しています。
"""

def sample_function(arg1, arg2):
	print(arg1, arg2)

# 位置引数をまとめて指定する例
arglist = ['a', 'b']
sample_function(*arglist)    # a b

# キーワード引数をまとめて指定する例
argdict = {'arg1': 'a', 'arg2': 'b'}
sample_function(**argdict)    # a b




print("--- pixelbeat sandboxより ---")
print("--- Web開発とデータエンジニアリング ---")
print("--- [Python]可変長引数と引数展開でコードをスッキリさせる ---")


"""
Pythonには可変長引数という便利な機能があります。


可変長引数とは
関数の定義で引数の最初に*(アスタリスク)をつけることで、
関数の呼び出し側で、引数の数を任意に変更できます。
"""

def variable_args(*args):
	print(len(args), 'items:')
	print('-------------------')
	for arg in args:
		print(arg)
	print('-------------------')

variable_args('First', 1, 2, 3)
variable_args('Second', 4, 5, 6, 7)

# 4 items:
# -------------------
# First
# 1
# 2
# 3
# -------------------
# 5 items:
# -------------------
# Second
# 4
# 5
# 6
# 7
# -------------------

"""
慣例的にargsを使うようですが、引数名は何でも良いです。
場合によって渡す引数の数を変えたい場合などに使えます。


キーワード可変長引数
関数の定義で引数の最初に**(アスタリスク2個)をつけることで、
関数の呼び出し側で、キーワード引数の名称、数を任意に変更できます。
"""

def variable_kwargs(**kwargs):
	print(len(kwargs), 'items')
	print('-------------------')
	for k, v in kwargs.items():
		print(k, ':', v)
	print('-------------------')

variable_kwargs(first=1, second=2)
variable_kwargs(third='three', fourth='four', fifth='five')

# 2 items
# -------------------
# first : 1
# second : 2
# -------------------
# 3 items
# -------------------
# third : three
# fourth : four
# fifth : five
# -------------------

"""
こちらも慣例的にkwargsという名前を使ってますが、何でも良いです。


引数展開
リストや辞書に*をつけると、それらを展開して引数として渡すことができます。
具体的なコードを交えて説明します。

リストの展開
さきほど作ったvariable_argsメソッドに、リストを渡してみます。
"""

l1 = ['First', 1, 2, 3]

print('------そのまま渡す-------')
variable_args(l1)
# ------そのまま渡す-------
# 1 items:
# -------------------
# ['First', 1, 2, 3]
# -------------------

print('------展開して渡す-------')
variable_args(*l1)
# ------展開して渡す-------
# 4 items:
# -------------------
# First
# 1
# 2
# 3
# -------------------

"""
*なしでは、l1というリストを1つの引数として渡しているだけですが、
*をつけると、リストの中身を一つずつ引数として渡すことができます。
上記例では言い換えると、
variable_args('First', 1, 2, 3)
と同じ意味になります。

タプルでも同様です。


辞書の展開
さきほど作ったvariable_kwargsメソッドに辞書を展開して渡します。
引数の前に**をつけて渡します。
"""

d1 = {'first': 1, 'second': 2}
variable_kwargs(**d1)
# 2 items
# -------------------
# first : 1
# second : 2
# -------------------

"""
なお、**なしでそのまま渡すとエラーになります。

コード

variable_kwargs(d1)
実行結果

Traceback (most recent call last):
(中略)
TypeError: variable_kwargs() takes 0 positional arguments but 1 was given

引数の展開では、リストや辞書の中身を展開して渡しているだけなので、
関数の定義元が可変長引数である必要はありません。
以下のようなメソッドでも使えます。
ただし、リストの中身は引数の数と一致している必要があります。
"""

def fixed_args(arg1, arg2):
	print(arg1)
	print(arg2)

l2 = ['Fixed', 'args']
fixed_args(*l2)
# Fixed
# args


"""
まとめ
可変長引数、キーワード可変長引数によって、
関数に汎用性・拡張性を持たせることができます。
また、引数の展開によって、関数呼び出し時のコードをやすくまとめることができます。
*のせいでなんだか小難しい印象を与えがちですが、慣れると非常に便利です。
"""




