#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説 ---")
print("--- 関数の応用（ジェネレータの使い方） ---")


"""
ジェネレータとは「関数を一時停止させ、途中までの結果を返却できる」機能のことです。
基本的に関数は最後にreturnして結果を返却しますが、
ジェネレータを使うことで関数の途中の結果を返却することができます。
ここでは「ジェネレータって何？」「ジェネレータでどんなことができるの？」
「ジェネレータを有効活用したい」といった方へ、ジェネレータの使い方を解説します。
"""


print("--- ジェネレータの使い方 ---")


"""
ジェネレータは関数のreturnの箇所をyieldに変えることで作成できます。
"""

def func():
	for i in range(5):
		return i

def generator():
	for i in range(3):
		yield i

# 一般的な関数は呼び出したら戻り値を返して終了
print(f"no_generator=>{func()}")    # no_generator=>0

# ジェネレータを呼び出すとジェネレータオブジェクトが返却される
gen = generator()
print(type(gen))    # <class 'generator'>
# next()で途中結果を取得できる
print(f"generator=>{next(gen)}")    # generator=>0
print(f"generator=>{next(gen)}")    # generator=>1
print(f"generator=>{next(gen)}")    # generator=>2

"""
ジェネレータを呼び出すとジェネレータオブジェクトを返却します。
next()にジェネレータを渡すことでyield時点の途中結果を取得できます
(next()はイテレータの次の値を返す関数なので、ジェネレータはイテレータの一種)。
これがジェネレータの基本的な使い方です。
"""


print("--- ジェネレータでメモリ使用量を節約する ---")


"""
ジェネレータは大きなデータを扱う際にメモリ使用量を節約したり、
メモリリークを発生させないようにする場面で有効です。
"""

import sys

def func():
	nums = []
	for i in range(10000000):
		nums.append(i)
	return nums

nums = func()
print(sys.getsizeof(nums))    # 89095160
with open('sample.txt', mode='w') as f:
	for i in nums:
		f.write(f"{i},")

"""
上のプログラムはnumsリストに0〜10000000までの数値を格納し、
numsのメモリ使用量を出力したあと、sample.txtに全ての数値を書き込んでいます。
使用量はバイト単位なので、約8.2MB使用しています。
これならまだ問題なさそうですが、桁数が1つ増えるごとに使うメモリ容量も10倍になり、
ビッグデータを扱うとなると数値だけでなく文字列も入ってくるので、
1つのプロセスで1GBを超える場合もあります。
numsが大きくなり過ぎるとメモリリークを引き起こし、
最悪プログラムが意図せず止まってしまうこともあります。
このような場面でyieldは役に立ってくれます。ジェネレータを使った方法を見てみましょう。
"""

import sys

def gen():
	nums = []
	for i in range(1000000):
		nums.append(i)
		if len(nums) >= 100000:
			yield nums
			nums = []

gen = gen()
with open('sample.txt', mode='w') as f:
	for nums in gen:
		print(sys.getsizeof(nums))
		for i in nums:
			f.write(f"{i},")
# 800984
# 800984
# 800984
# 800984
# 800984
# 800984
# 800984
# 800984
# 800984
# 800984

"""
ジェネレータはイテレータの仲間なので、
for..in文でループさせながらyield時点での返却値を取得できます。
getsizeofの出力結果を見て分かる通り、
100000件分のデータがnumsに格納されたタイミングで返却されてきているのが分ります。
そのほかの部分は一括で返却される場合とあまり変わりありません。
"""
