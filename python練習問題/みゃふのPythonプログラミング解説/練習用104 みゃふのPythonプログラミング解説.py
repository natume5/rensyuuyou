#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説 ---")
print("--- リスト要素の数え上げ（Counter） ---")


"""
Counterは「リストの要素の数え上げ」をするためのモジュールです。
リスト内の要素を数え、要素名をキーに、要素数を値に格納した結果を得ることができます。
collectionsライブラリには他にも色々な標準モジュールがありますが、
最も使われるのがこのCounterでしょう。
要素の数え上げをしたい場合にわざわざ自前の関数を用意する必要がないので、ぜひ覚えておきましょう。
"""


print("--- Counterの使い方 ---")


"""
実際にCounterを使ってみましょう。
collectionsは標準ライブラリなので、
pip等でインストールせずともそのままインポートできます。
"""

from collections import Counter

l = ['a', 'b', 'c', 'b', 'a', 'd', 'a', 'c']
counter = Counter(l)
print(counter)     # Counter({'a': 3, 'b': 2, 'c': 2, 'd': 1})

"""
リストをCounter()にそのまま渡すことで、
それぞれの要素数をカウントした結果をCounterクラスとして受け取っています。
Counterクラスは辞書型のサブクラスなので、辞書と同じことが可能です。
"""

for k, v in counter.items():
	print(f"{k} => {v}")
# a => 3
# b => 2
# c => 2
# d => 1

"""
これがCounterの基本的な使い方です。
"""


print("--- Counterの機能 ---")


"""
elements()

elements()を使うことで、各要素のカウント分の要素を持ったイテレータを作成できます。
list()に通すことで、順番は変わりますが元のリストと同じ要素を持ったリストに戻すことができます。
"""

l = ['a', 'b', 'c', 'b', 'a', 'd', 'a', 'c']

counter = Counter(l)
print(list(counter))    # ['a', 'b', 'c', 'd']
# Counterクラスをそのままリスト化すると重複を除いた要素を取得できる

print(list(counter.elements()))    # ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd']
# elements()を通すことで元のリストを取得できる(順番は変わる)


"""
most_common()

most_common()を使えば出現回数が多い要素順に(要素, 要素数)
というタプルのリストを作成できます。
"""

print(counter.most_common())    # [('a', 3), ('b', 2), ('c', 2), ('d', 1)]


"""
update()とsubtract()

update()はAのCounterにBのCounterの要素を足し算できます。
"""

l = ['a', 'b', 'c', 'a', 'b', 'c']
l2 = ['b', 'c', 'c', 'c']

c = Counter(l)
c2 = Counter(l2)
c.update(c2)
print(c)    # Counter({'c': 5, 'b': 3, 'a': 2})

"""
反対に、subtract()は引き算ができます。
"""

l = ['a', 'b', 'c', 'a', 'b', 'c']
l2 = ['b', 'c', 'c', 'c']

c = Counter(l)
c2 = Counter(l2)
c.subtract(c2)
print(c)    # Counter({'a': 2, 'b': 1, 'c': -1})

"""
dictのupdateは同じ要素があれば値を置き換える動きをしますが、
Counterのupdateは値を足し合わせるので異なる動きをします。
また、subtract()は結果がマイナスの場合もそのまま出力します。


各演算子

+や-、&、|を使うことで、複数のCounterクラスの加算や減算をしたり、
積集合、和集合を取得することができます。
"""

l = ['a', 'b', 'c', 'a', 'b', 'c']
l2 = ['a', 'b', 'c', 'c', 'c']

c = Counter(l)
c2 = Counter(l2)
print(c + c2)    # 加算
print(c - c2)    # 減算
print(c & c2)    # 積集合(各Counterの同じ要素の中で、最も少ない要素数を取得)
print(c | c2)    # 和集合(各Counterの同じ要素の中で、最も多い要素数を取得)

# Counter({'c': 5, 'a': 3, 'b': 3})
# Counter({'a': 1, 'b': 1})
# Counter({'c': 2, 'a': 1, 'b': 1})
# Counter({'c': 3, 'a': 2, 'b': 2})

"""
+はupdate()と同じ結果になりますが、-はsubtract()と違い、
カウントが0以下になった場合はキーごと除外しています。
&は各Counterの要素の中で、それぞれ最も少ない要素数を取得しています。
例えばa要素は1つ目のCounterには2つ、2つ目には1つありますので、
少ない方の1が取得できています。
|は&と反対に最も多い要素数を取得できますので、a要素には2が入ってきます。
"""
