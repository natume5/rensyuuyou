#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- None型 ---")


print("--- 値が存在しないことを表すNone ---")


"""
変数に値が存在しない場合、PythonではNoneを利用します。
CやJava、C#のnullに相当します。
ある変数valにNoneを代入する場合は以下のように記述します。
"""

val = None

"""
変数をとりあえず初期化する際に使用できます。
"""


print("--- Noneかどうかを判定する ---")


"""
変数がNoneかどうかを判定する際はifを使います。
（if文についてはまだ説明していませんが、別途説明します。
わからない方は一旦飛ばして構いません。）
"""

val = None

if val is None:
	print('val is None')    # val is None この行が出力される


print("--- Noneの評価と空文字 ---")


"""
また、None自体はif文でFalseと評価されます。
"""

val = None

if val:
	print('True')
else:
	print('False')    # この行が出力される

"""
ただし、偽として評価されるものは他にもあるので注意してください。
例えば空文字がそれに該当します。
"""

val = ''

if val:
	print('True')
else:
	print('False')    # この行が出力される


print("--- Noneの文字列表現 ---")


"""
Noneを使用する際にもう１点、注意が必要なのが文字列表現です。
Noneをprint関数などで出力してみましょう。
"""

var = None
print(var)    # Noneが出力される

"""
Noneという文字列が出力されるため、
ログなどで空文字を期待した実装をする際には注意が必要です。
"""
