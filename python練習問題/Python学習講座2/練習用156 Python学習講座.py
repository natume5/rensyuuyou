#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- if文 ---")


print("--- if文 ---")


"""
プログラムを記述している際、特定の条件の場合のみ処理を実行したい場合が出てきます。
例えば、変数xの値が0と等しい場合はその旨を表示させたい、といった場合です。
if文とはこういった条件に応じて処理を分岐させたい場合に使用する文です。
Pythonのif文は以下のように記述します。
なお、bool値や前回学習した比較演算のように
真理値を得られるものを条件式と呼びます。

if文
if 条件式:
    条件式が正の場合の処理
例えば、xが0かどうかを判定する場合、以下のようになります。
"""

x = 0
if x == 0:
	print('x = 0')    # x = 0 ここが出力される


print("--- else文 ---")


"""
if文の条件を満たさないような場合にも別途処理をしたい場合、else文を使用します。

if-else
if 条件式:
    条件式が正の場合の処理
else:
    条件式が偽の場合の処理

例えば、xが0の場合は「x = 0」それ以外の場合は「x != 0」
というメッセージを表示させたい場合、以下のようになります。
"""

x = 1
if x == 0:
	print('x = 0')
else:
	print('x != 0')    # x != 0 こちらが出力される


print("--- elif文 ---")


"""
複数のif文を使いたい場合、elifを使用します。
else ifの略ですね。else文とも組み合わせて使うことができます。
条件式を2つ使用したい場合は以下のように記述します。

if-else
if 条件式1:
    条件式1が正の場合の処理
elif 条件式2:
    条件式2が正の場合の処理
else:
    条件式が偽の場合の処理
例えば、xが0の場合と1の場合とそれ以外の場合で処理を分けたい場合、
以下のように記述します。
"""

x = 1
if x == 0:
	print('x = 0')
elif x == 1:
	print('x = 1')    # x = 1 こちらが出力される
else:
	print('x != 0 and x != 0')


print("--- 変数の真理値評価 ---")


"""
Pythonでは偽と判定されるものはFalse以外にも多数あるので注意してください。

False
None
ゼロと同値
__len__メソッドが定義されている型のオブジェクトで0が返された場合
__nonezero__メソッドが定義されている型のオブジェクトでFalseが返された場合

4番目の具体例ですが、空のシーケンス、マップ、
set（''、]、()、{}）などが該当します。
いずれも空の場合はlen関数の値が0になります。
サンプルで動作を確認してみましょう。
"""

if 1:
	print('True')    # True
else:
	print('False')

if 0:
	print('True')
else:
	print('False')    # False

if 0.0:
	print('True')
else:
	print('False')     # False

if 0.1:
	print('True')    # True
else:
	print('False')

if []:
	print('True')
else:
	print('False')    # False

if ():
	print('True')
else:
	print('False')    # False

if None:
	print('True')
else:
	print('False')    # False

if "":
	print('True')
else:
	print('False')    # False

"""
また、サンプルの最後の例のとおり、文字列もシーケンスの一種なので、
から文字列は長さ0、つまりFalseと評価されます。
"""
