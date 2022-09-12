#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説 ---")
print("--- 関数の応用（高階関数） ---")


"""
高階関数は「関数を引数や戻り値として扱っている関数」のことです。
一般的にプログラミングでは関数の引数や戻り値には変数や定数、
またはリテラルをそのまま記述することが多いですが、
高階関数を使えるプログラミング言語では関数の引数や戻り値に関数を指定することができます。
ここではPythonを使って高階関数の使い方を解説します。
"""


print("--- 関数を引数で受け取る ---")


"""
まずは関数を引数で受け取る方法を見ていきましょう。
"""

# 数値の符号を反転させる関数
def inversion(val):
	return val * -1


# リストの要素に関数を適用する関数
def apply_func(list, func):
	return_list = []
	for val in list:
		return_list.append(func(val))
	return return_list


list = [2, -3, 1, 0, -5]
print(apply_func(list, inversion))

"""
inversion関数は受け取った数値の符号を反転させる簡単な関数です。
apply_func関数は1つ目の引数のリストの各要素に2つ目の引数の関数を適用し、
最後に作成されたリストを返却する高階関数です。
結果を見て分かる通り、apply_func内でinversion関数を使って符号が反転されています。
引数の前に*を付けると、複数の関数を同時に適用することもできます。
"""

# 数値の+と-を反転させる関数
def inversion(val):
	return val * -1

# 数値を2倍にする関数
def double(val):
	return val * 2

# 数値が1以上の場合は1、それ以下の場合は0にする関数
def firing(val):
	if val >= 1:
		return 1
	else:
		return 0

# リストの要素に関数を適用する関数
def apply_func(list, *funcs):
	return_list = []
	for val in list:
		for func in funcs:
			val = func(val)
		return_list.append(val)
	return return_list

list = [2, -3, 1, 0, -5]
print(apply_func(list, inversion, double, firing))

"""
apply_funcの2つ目の引数に*を付けました。
これは可変長変数といい、任意の数の引数を受け取れるようになります。
apply_funcではリストの各要素にinversion関数と、
新しく追加したdouble関数とfiring関数を順番に適用しています。
"""


print("--- 関数を戻り値で渡す ---")


"""
次に関数を戻り値で渡すパターンの高階関数を見てみましょう。
"""

def add_all(*vals):
	sum = 0
	for val in vals:
		sum = sum + val
	return sum

# add_all関数を返却する高階関数
def high_func():
	return add_all

func = high_func()
print(func(2, 4, 1, 3, 6))    # 16

"""
add_all関数は受け取った数値を全て合計するだけの関数です。
high_func関数はそのadd_all関数をそのまま返却する高階関数です。
func = high_func()でfuncにadd_all関数のオブジェクトを格納し、
そのfuncに引数を指定することで内部の関数を使うことができます。
また、high_func関数の内部で戻り値の関数を定義することも可能です。
"""

# 関数内に返却する関数を定義
def high_func():
	def add_all(*vals):
		sum = 0
		for val in vals:
			sum = sum + val
		return sum
	return add_all

func = high_func()
print(func(2, 4, 1, 3, 6))    # 16


print("--- 代表的な高階関数 ---")


"""
最後に組み込みで用意されている代表的な高階関数をご紹介します。

map()

map()は1つ目の引数に渡した関数を2つ目に渡したイテレータの各要素に適用できる高階関数です。
「関数を引数で受け取る」で自前で用意したapply_func()が似ています。
"""
"""
l = [2, -3, 1, 0, -5]
print(list(map(abs, l)))   # [2, 3, 1, 0, 5]
"""
"""
abs()はそれぞれの要素を絶対値にして返却します。
map()はリストではなくmapオブジェクトを返却するので、
リストで受け取る場合は戻り値をlist()に通す必要があります。
また、map()はイテレータであればなんでも良いので、タプルや辞書、文字列を渡することも可能です。
下の例は文字列を渡しています。
"""

s = 'こんにちは'
print("".join(map(lambda c: f"{c} ", s)))

"""
辞書を渡すとキーに対して関数を適用します。
キーと値両方を関数に渡したい場合はitems()を使います。
"""
"""
d = {"a": 1, "b": 2, "c": 3}
print(list(map(lambda v: f"{v[0]}{v[1]}", d.items())))    # ['a1', 'b2', 'c3']
"""

"""
filter()

filter()はイテレータの各要素を関数に通し、結果がTrueになったものだけ返却する高階関数です。
"""
"""
l = [1, 2, 3, 4, 5]
print(list(filter(lambda : x <= 3, l)))    # [1, 2, 3]
"""

"""
lambda関数を1つ目の引数に渡し、3以下の数値のみリストから抽出して出力しています。
こちらもリスト以外のイテレータを渡せます。
"""

s = 'たみゃたふのぱたいそたんたぷろたぐたらみたんたぐきたょうたしつた'
print("".join(filter(lambda c: c != 'た', s)))    # みゃふのぱいそんぷろぐらみんぐきょうしつ


"""
reduce()

recude()はイテレータの全要素に関数を通し、1つの値に集約させる高階関数です。
難しいことを言っているように思われるかもしれませんが、
例えばリストの中の数値を全て足し合わせたり、
また引き算したりした結果を出力するという話なので、そこまで難しくはありません。
"""

from functools import reduce

l = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a + b, l))    # 15

"""
reduceはpython3からfunctoolsライブラリのモジュールになったので、
まずインポートする必要があります。
また、reduce()に渡す関数は2つの引数を取る関数でなくてはなりません。
なので上の例ではlambda式でaとbを引数に取っています。
リストの中から初めに1と2を取り出し、足し算して3を出力し、
その3と次の3を足し算して6、その次の4と足し算して...というように動作しています。
なので、結果的に1 + 2 + 3 + 4 + 5になり、15が出力されています。
今回はlambdaで自前で関数を用意しましたが、
単純な四則演算であればoperatorライブラリから関数をインポートできます。
"""

from functools import reduce
from operator import add, sub, mul, truediv

l = [10, 2]
print(reduce(add, l))    # 12
print(reduce(sub, l))    # 8
print(reduce(mul, l))    # 20
print(reduce(truediv, l))    # 5.0

"""
例をみて分かる通り、足し算はadd、引き算はsub、掛け算はmul、
割り算はtruedivがそれぞれ用意されています。
"""
