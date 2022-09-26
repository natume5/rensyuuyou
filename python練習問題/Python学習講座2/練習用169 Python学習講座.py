#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- ジェネレータ ---")


print("--- ジェネレータの基本 ---")


"""
ジェネレータと__next__()メソッド
他のプログラム言語では聞き慣れない言葉だと思いますが、
Pythonの関数にはジェネレータという少し変わった実装をすることができます。
ジェネレータを利用すると、関数の処理の途中で処理を一旦中断して
値を返すことができ(これをyieldと呼びます)、
その後必要に応じて処理を再開することが可能となります。
また、ループ処理で扱うことも可能です。
イメージがわきづらいかと思いますので、さっそくサンプルで確認してみましょう。
"""

def sample_generator():
	""" ジェネレータ関数 """
	yield 'おはよう'
	yield 'こんにちは'
	yield 'こんばんは'

gen_func = sample_generator()    # ジェネレータオブジェクトを生成

text = gen_func.__next__()
print(text)    # おはよう

text = gen_func.__next__()
print(text)    # こんにちは

text = gen_func.__next__()
print(text)    # こんばんは

"""
コードの説明です。
サンプルのジェネレータ関数はyieldを3回持っています。
6行目でsample_generator関数を呼び出していますが、
関数から戻り値を受け取っているわけではなく、
イテラブル(=反復可能)なジェネレータオブジェクトを受け取っています。
9、12、15行目の__next__()メソッドでそれぞれのyieldまで実行されます。
ジェネレータはイテレータの一種なので、組込みのnext関数を利用したり、
ループで処理することが可能です。呼出し後の処理をループで書きなおしてみましょう。
"""

def sample_generator():
	yield 'おはよう'
	yield 'こんにちは'
	yield 'こんばんは'

gen_func = sample_generator()    # ジェネレータオブジェクトを生成する

for text in gen_func:
	print(text)
# おはよう
# こんにちは
# こんばんは


"""
ジェネレータと無限数列
この一風変わったジェネレータですが、利用するメリットはなんでしょうか？
例えば、何項目まで使うかわからない数列を予め生成して、
1つづつ取り出す処理ついて考えてみます。
現実的に使う程度のサイズを見積もって大きなリストを作る方法が考えられますが、
見積もりが悪ければ不足してしまいすし、
ほとんど使わないデータを確保し続けるためメモリがもったいないですね。
そんなときはジェネレータを使いましょう。
以下、フィボナッチ数列をyieldで返すジェネレータ関数のサンプルです。
(フィボナッチ数列とは初項f0=1とその次の項f1=1が与えられていた場合、
fn=fn + fn-1で定義される数列です。)
"""

def fibonacci_generator():
	f0, f1 = 0, 1
	while True:
		yield f0
		f0, f1 = f1, f0 + f1

gen_func = fibonacci_generator()    # ジェネレータオブジェクトを生成

for i in range(0, 10):
	# 10個取得する
	num = next(gen_func)
	print(num)
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

"""
この実装ならば、巨大なリストを予め作らなくても、
必要なときに次の項を取得することができます。
ディレクトリツリーやカテゴリツリーといった最木構造を持ったデータを
表形式に変換する際にも活用することができます。
"""


print("--- ジェネレータのメソッド ---")


"""
ジェネレータのメソッドは、
さきほど紹介した__next__()メソッド以外に、send()メソッド、throw()メソッド、
close()メソッドがあります。

順番に説明していきましょう。

send()メソッド
再開待ちのジェネレータに対し、値を設定します。
sendメソッドで指定した値はyield式の値として設定されます。
"""

def sample_generator():
	text = yield 'おはよう'
	yield text
	yield text

gen_func = sample_generator()    # ジェネレータオブジェクトを生成

text = next(gen_func)
print(text)    # おはよう

text = gen_func.send('こんにちは')
print(text)    # こんにちは

text = next(gen_func)
print(text)    # こんにちは

"""
8行目でジェネレータオブジェクトから値を取得します。
11行目で値を送出し値を設定し、3行目のyieldで返された値を出力します。
14行目のnextでは4行目のyieldで返された値を出力します。


throw()メソッド
再開待ちのジェネレータオブジェクトに対し、例外を送出します。

close()メソッド
再開待ちのジェネレータオブジェクトを正常終了させます。
"""
