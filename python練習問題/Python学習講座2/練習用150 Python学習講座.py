#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- set型の基本 ---")


"""
Pythonにはset型という集合を表す変数の型が用意されています。
リストやタプルは同じ値を重複して追加することができ、
追加した際の順序を保持することができました。
一方でsetは順序は保持せずユニークな値を持ちます。
"""


print("--- setの初期化と注意点 ---")


"""
setの初期化

set型オブジェクトの初期化は、中括弧の中にカンマ区切りで要素を列挙します。
"""

# setの初期化
s = {'A', 'B', 'C'}
print(s)    # {'A', 'B', 'C'}

# 初期化時に重複があっても・・・
s = {'A', 'B', 'C', 'A'}
print(s)    # {'A', 'B', 'C'}

"""
2番目の例のように、重複した値をセットしても1つとして扱われます。
setの注意点 「TypeError unhashable type」

また、格納する値はハッシュ化可能でなければなりません。
これは、setは要素のユニークさを判定する際にハッシュ値を利用するためです。
例えばリストはハッシュ化可能ではないためsetに挿入することはできません。
TypeError unhashable typeが発生します。

s = {'A', [1, 2, 3]}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

ハッシュ化可能なタプルを利用すれば解決します。
"""

s = {'A', (1, 2, 3)}
print(s)    # {(1, 2, 3), 'A'}

"""
リストからset型変数を生成する

組込みのset関数を使用すると、リストからset型変数を生成することができます。
"""

l = ['a', 'b', 'c', 'a']
s = set(l)    # set関数を使用
print(s)    # {'c', 'b', 'a'}

"""
ユニークな要素のsetになっていることがわかります。
"""


print("--- setの繰り返し処理 ---")


"""
set型変数はリストなどと同様に繰り返し処理が可能です。

setのfor文

for 変数 in set型オブジェクト:
    処理
"""

data_set = {'a', 'b', 'c'}
for s in data_set:
	print(s)    # 集合の要素が出力される

# a
# b
# c 


print("--- set型変数の更新操作 ---")


"""
set型変数の更新ですが、要素の追加にadd、
要素の削除にremove、discardを使います。
順序は持たないため、listのようにインデックスを指定する方法はありません。

setの要素追加

要素追加はaddメソッドを使います。以下の構文となります。

要素追加
setオブジェクト.add(追加するオブジェクト)
"""

s = {1, 2, 3}
s.add(4)
print(s)    # {1, 2, 3, 4}


"""
setの要素削除
要素削除はremoveとdiscardの2つが用意されています。
removeは存在しないオブジェクトを指定するとKeyErrorが発生します。

remove
setオブジェクト.remove(削除するオブジェクト)
一方、discardは存在しないオブジェクトを指定しても何も起こりません。

discard
setオブジェクト.discard(削除するオブジェクト)
サンプルで確認してみましょう。
"""

s = {1, 2, 3, 4}
s.remove(4)
print(s)    # {1, 2, 3}
# s.remove(99)    # KeyErrorが発生する KeyError: 99

s.discard(99)
print(s)    # {1, 2, 3}

"""
99を削除する際、removeではエラーが発生しますが、
discardの場合はエラーが発生していないことが確認できます。


frozenset イミュータブルなset
最後にset型の兄弟であるfrozensetについて紹介します。
初期化の後変更させないようなsetを作りたい場合はfrozenset型を使用します。
オブジェクト生成時に引数にlistのようなイテラブルなオブジェクトを指定します。
"""

fs = frozenset(['a', 'b', 'c'])

"""
変更不可という点を除き、ほとんどの操作はsetとおなじであるため、
細かい説明は割愛します。
"""
