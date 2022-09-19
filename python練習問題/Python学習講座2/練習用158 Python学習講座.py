#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- 辞書のループ処理 ---")


print("--- 3種類の基本ループ処理 ---")


"""
辞書のループは、大別すると以下の3種類あります。

キーのループ
値のループ
キーと値のループ

キーのループ
まず、一番単純なものから説明します。リストと同じ構文でfor、
inでループを行うと辞書のキーがループの変数として使用できます。

for
for key変数名 in 辞書:
    処理

以下のサンプルのようにループ中でキーを用いて値を取得することが可能です。
"""

d = {'key1': 110, 'key2': 270, 'key3': 350}

for key in d:
	print(key)    # key1〜key3が出力される
	print(d[key])    # それぞれのkeyに対応する値が出力される
# key1
# 110
# key2
# 270
# key3
# 350

"""
値のループ
辞書に用意されているvaluesメソッドを利用すると、
dict_valuesという値のイテレータが得られるのですが、
これを使用すると値でループすることができます。

for文とvalues
for 変数名 in 辞書.values():
    処理

以下のサンプルではvaluesメソッドを使用してループ内で辞書の値を出力しています。
"""

d = {'key1': 110, 'key2': 270, 'key3': 350}

for value in d.values():
	print(value)    # 値が出力される
# 110
# 270
# 350

"""
キーと値のループ
辞書に用意されているitemsメソッドを利用すると、
dict_itemsというキーと値のイテレータが得られ、
これを使用してキーと値両方でループすることができます。

items
for key変数名, value変数名 in 辞書.items():
    処理

以下のサンプルではitemsメソッドを使用してループ内で辞書のキーと値を出力しています。
"""

d = {'key1': 110, 'key2': 270, 'key3': 350}

for key, value in d.items():
	print(key, value)    # キーと値が出力される
# key1 110
# key2 270
# key3 350


print("--- ループインデックスを取得する ---")


"""
ここから少し複雑になります。
何番目の要素だけは処理をしない、
等の処理を入れたい場合はループインデックスが必要となります。
リストと同様、組込みのenumerate関数を利用することで取得することができます。

enumerateとの組み合わせ
for ループインデックス, key変数 in enumerate(辞書):
    処理

以下のサンプルではループ内で辞書のキーとループインデックスを出力しています。
"""

d = {'key1': 110, 'key2': 270, 'key3': 350}

for i, key in enumerate(d):
	print(i, key)    # ループインデックスとキーが出力
# 0 key1
# 1 key2
# 2 key3

"""
また、itemsと組み合わせる場合は、丸括弧でキーと値を囲みます。

for + enumerate + items
for ループインデックス, (key変数, value変数) in enumerate(辞書.items()):
    処理

以下のサンプルではループインデックスと、キー、値をループ内で出力しています。
"""

d = {'key1': 110, 'key2': 270, 'key3': 350}

for i, (key, value) in enumerate(d.items()):
	print(i, key, value)    # ループインデックスとkeyと値が出力
# 0 key1 110
# 1 key2 270
# 2 key3 350
