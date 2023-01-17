#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- NumPy入門 通常の関数をユニバーサル関数に変換する frompyfunc ---")


"""
前回はnumpyが提供する代表的なユニバーサル関数を紹介しましたが、
実はnpには様々な関数をユニバーサル関数に変換する関数、
frompyfuncが用意されています。
このページではfrompyfuncを使用してユニバーサル関数を自前で作ってみましょう。
（関数オブジェクトについて理解していると理解がスムーズになると思います。）
"""


print("--- frompyfunc ---")


"""
冒頭で紹介したとおり、frompyfuncというNumPyの関数を使用すると、
通常の関数をユニバーサル関数に変換することができます。
引数に対象となる関数オブジェクト、引数の数と出力の数を指定します。
戻り値としてユニバーサル関数オブジェクトが返されます。

サンプルその1

まずはPythonの組込み関数strをfrompyfuncでユニバーサル関数化してみましょう。
strは1つの引数に対し、文字列表現を1つ返す関数です。
"""

import numpy as np

# frompyfuncで新たな関数を作る
new_str = np.frompyfunc(str, 1, 1)

# ndarrayを生成
a = np.array([1, 2, 3])

# frompyfuncで作った関数を使用
print(new_str(a))
# array(['1', '2', '3'], dtype=object) 文字列になっていることが確認できる

"""
['1' '2' '3']

frompyfuncから新たに作った関数を使用すると、
ndarrayそれぞれの要素に対して文字列表現が取得できていることが確認できます。


サンプルその2

もちろん、同様の方法で自前の関数をユニバーサル関数化することも可能です。
2つの引数に対し、和と差の2つを返す関数をユニバーサル関数化してみましょう。
"""

import numpy as np

def sumsub(x, y):
	return x + y, x - y

# frompyfuncで新たな関数を作成
new_func = np.frompyfunc(sumsub, 2, 2)

# ndaarrayを2つ生成
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])

# frompyfuncで作った関数を使用
sum, sub = new_func(x, y)

print(sum)

print(sub)

"""
[4 4 4]
[-2 0 2]

frompyfuncの引数には元の関数sumsubの引数、戻り値の数を指定しますので、
上のサンプルでは2, 2を指定しています。
結果として、それぞれの要素に対して足し算、
引き算が実行されていることが確認できます。
"""
