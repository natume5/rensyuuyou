#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- Python入門　set型の基本---")


"""
setの初期化と注意点
setの初期化

set型オブジェクトの初期化は、中括弧の中にカンマ区切りで要素を列挙します。
"""

# setの初期化
s = {"A", "B", "C"}
print(s)    # {"C", "B", "A"}

# 初期化に重複があっても・・・
s = {"A", "B", "C", "A"}
print(s)    # {'C', 'B', 'A'}

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
print(s)    # {'A', (1, 2, 3)}


"""
リストからset型変数を生成する

組込みのset関数を使用すると、リストからset型変数を生成することができます。
"""

l = ['a', 'b', 'c', 'a']    # listを生成
s = set(l)    # set関数を使用
print(s)    # {'a', 'b', 'c'}

"""
ユニークな要素のsetになっていることがわかります。


setの繰り返し処理

set型変数はリストなどと同様に繰り返し処理が可能です。
setのfor文
for 変数 in set型オブジェクト:
    処理
"""

data_set = {'a', 'b', 'c'}
for s in data_set:
  print(s)    # 集合の要素が出力される

"""
実行結果はa,b,cが出力されます。


set型変数の更新操作

set型変数の更新ですが、要素の追加にadd、要素の削除にremove、discardを使います。
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

# s.remove(99)    KeyErrorが発生する

s.discard(99)
print(s)    # {1, 2, 3}

"""
99を削除する際、removeではエラーが発生しますが、discardの場合はエラーが発生していないことが確認できます。


frozenset イミュータブルなset

最後にset型の兄弟であるfrozensetについて紹介します。
初期化の後変更させないようなsetを作りたい場合はfrozenset型を使用します。
オブジェクト生成時に引数にlistのようなイテラブルなオブジェクトを指定します。
"""

fs = frozenset(['a', 'b', 'c'])

"""
変更不可という点を除き、ほとんどの操作はsetとおなじであるため、細かい説明は割愛します。
"""


print("--- Python入門　set型と集合演算---")


"""
setの集合演算

それではset型の集合演算について見ていきましょう。
基本となるUnion、Intersection、Differenceと包含関係の判定について説明します。

Union(和集合)

2つの集合の和を取ります。setオブジェクトがもつunionメソッドを利用します。
戻り値にunionした新たなsetが返されます。もとのsetには変更ありません。

union
setオブジェクト1.union(setオブジェクト2)
"""

s1 = {'A', 'B', 'C'}
s2 = {'C', 'D', 'E'}
s = s1.union(s2)    # s1とs2をunionする
print(s)    # {'E', 'D', 'C', 'B', 'A'}
print(s1)   # {'B', 'A', 'C'} 変更なし


"""
Intersection(積集合)

2つの集合の積、つまり共通要素を取り出します。setオブジェクトがもつintersectionメソッドを利用します。

intersection
setオブジェクト1.intersection(setオブジェクト2)
"""

s1 = {'A', 'B', 'C'}
s2 = {'C', 'D', 'E'}
s = s1.intersection(s2)
print(s)    # {'C'}


"""
Difference(差集合)

2つの集合の差、つまり元の集合に存在し、比較対象の集合に存在しない要素を取得します。
setオブジェクトがもつdifferenceメソッドを利用します。

difference
setオブジェクト1.difference(setオブジェクト2)

uniot、intersectionと異なり、演算順序で違いがあるので注意してください。
"""

s1 = {'A', 'B', 'C'}
s2 = {'C', 'D', 'E'}

# s1-s2
s = s1.difference(s2)
print(s)    # {'B', 'A'}

# s2-s1
s = s2.difference(s1)
print(s)    # {'D', 'E'}

"""
以下の計算となり、演算順序で違いが出ていることが確認できます。注意してください。
s1 - s2 = s1にあってs2にないもの = A, B
s2 - s1 = s2にあってs1にないもの = D, E


包含判定

ある集合が別の集合を含むかどうか、
または含まれるかどうかを判定するメソッドがsetオブジェクトに用意されています。

含まれているかどうかを判定

ある集合s1が別の集合s2に含まれている場合、s1はs2のsubset(サブセット=部分集合)であるといいます。
setオブジェクトのissubsetメソッドを利用して判定することができます。

issubset
setオブジェクト1.issubset(setオブジェクト2)
"""

s1 = {'A', 'B'}
s2 = {'A', 'B', 'C'}
s1.issubset(s2)    # True

"""
s1はs2の部分集合なので、Trueが返されています。


含んでいるかどうかを判定

ある集合s1が別の集合s2に含まれている場合、
s1はs2のsuperset(スーパーセット)であるといいます。
スーパーセットを上位集合と訳すこともありますが、和訳を見かけることは少ないですね。
少し話がそれましたが、setオブジェクトのissupersetメソッドを利用して判定することができます。

issuperset
setオブジェクト1.issuperset(setオブジェクト2)
"""

s1 = {'A', 'B', 'C'}
s2 = {'A', 'B'}
s1.issuperset(s2)    # True

"""
s2はs1の部分集合なので、Trueとなります。
"""


print("--- Python入門　dictionary(辞書)型---")


"""
dictionary型の基本
dictionary型とは

Pythonに限らず、プログラミングでdictionaryというと、
キーに対して値が設定された表のようなデータ構造を指します。
日本語訳の辞書やプログラミング言語によってはハッシュと呼ぶ場合があります。

dictionary型が適しています例として、商品コードと商品名を格納したい場合が挙げられます。
この場合、商品コードがキー、商品名が値となります。

以降、dictionary型やdictionary型変数を単に辞書と記述する場合があります。


辞書の初期化

では早速dictionary型変数を使ってみましょう。
初期化は中括弧の中に、コロンで区切ったキーと値の組をカンマ区切りで列挙します。
サンプルで見てみましょう。
"""

d = {'key1': 110, 'key2': 270, 'key3': 350}
print(d)    # {'key1': 110, 'key2': 270, 'key3': 350}


"""
値へのアクセス

値へアクセスする方法は2通りあります。ひとつはリストと同様にキーを大括弧で添字を指定する方法です。
この方法は、存在しないキーを指定するとエラーが発生します。
"""

d = {'key1': 110, 'key2': 270, 'key3': 350}
print(d['key1'])    # 110が出力される

"""
print(d['hoge']) # KeyErrorが発生する

また、getメソッドを使う方法もあります。以下のコードは上のサンプルをgetメソッドを使ったものに書きなおしています。
"""

d = {'key1': 110, 'key2': 270, 'key3': 350}
print(d.get('key1'))    # 110が出力される
print(d.get('hoge'))    # Noneが出力される

"""
KeyErrorが発生せずNoneが返されます。キーがない場合にNoneを取得したい場合に使えます。
一方でキーがない場合はエラーで処理したい場合は大括弧を使用しましょう。


値の更新

添字でアクセスしたものに対して値を代入することにより更新することができます。
以下のコードでは、key1というキーに対応する値110を200に更新しています。
"""

d = {'key1': 110, 'key2': 270, 'key3': 350}
d['key1'] = 200    # 200に更新
print(d['key1'])    # 更新後の200が出力される


"""
値の追加

新たなキーで更新と同様に代入すると新たな要素を追加することができます。
以下のコードでは、key4というキーに対して値400を追加しています。
"""

d = {'key1': 110}
d['key4'] = 400    # 値を追加
print(d)    # {'key1': 110, 'key4': 400}


"""
dict()による生成

若干説明が前後しますがdictionary型の生成でもう一つ、
組み込み関数のdict()を使用する方法があります。
この場合は一旦オブジェクトを生成して後から値を設定することになります。
"""

d = dict()
d['key1'] = 110
d['key2'] = 270
d['key3'] = 350
print(d)    # {'key1': 110, 'key2': 270, 'key3': 350}

"""
また、パラメータで辞書を指定すると同じ辞書を生成することができます。
"""

d1 = {'key1': 110, 'key2': 270, 'key3': 350}
d2 = dict(d1)
print(d2)    # {'key2': 270, 'key1': 110, 'key3': 350}


"""
dictionaryの要素数

dictionaryの要素数を確認する場合はリストと同様にlen関数を利用します。
"""

d = {'key1': 110, 'key2': 270, 'key3': 350}
print(len(d))    # 要素数の3が出力される


print("--- Python入門　イミュータブルとid関数---")


"""
イミュータブルとは
イミュータブルとは

イミュータブルとは、後から値を変更することができない性質を指します。
ここまでさまざまな基本的な変数の型について学習してきましたが、以下の変数はイミュータブルです。

    bool型
    数値型
    文字列型
    タプル型
    range型

上の文章を読んで、以下のような反論を思いつく方がいるかもしれません。

text = "abc"
text = "def"

「変数textに"abc"を定義して、あとから"def"に変更した、つまり文字列は変更できたのではないか？」
と思われた方は、再度変数への再代入を参照してみてください。代入という操作では、
元々あった値（つまりハコの中身）は変更されないのです。


id関数とオブジェクトの同一性

上で述べたとおり、Pythonの文字列型はイミュータブル、
つまり生成後にオブジェクトの状態を変更することができない型です。

以前学習した通り、再度代入したり、+演算子で結合する操作ができますが、
こういった操作をした場合は元のオブジェクトとは異なるオブジェクトが生成されます。
組込みのid関数について学習した後、文字列がイミュータブルであることを確認してみましょう。


id関数

Pythonのオブジェクトには、固有の番号が振られています。
組込みのid関数はそのオブジェクトの固有の番号を取得します。
"""

num = 100
text = 'aaaa'
dic = {'key': 200}

print(id(num))    # 変数numの固有番号が出力される
print(id(text))    # 変数textの固有番号が出力される
print(id(dic))    # 変数dicの固有番号が出力される

"""
同じオブジェクトであれば同じ番号を取得することができます。
文字列型の同一性確認

では確認してみましょう。
"""

text1 = 'aaa'
text2 = text1
text3 = text1 + 'bbb'

print(id(text1))
print(id(text2))    # text1を参照している
print(id(text3))    # text1とはIDが異なる

text1 = 'bbb'
print(id(text1))    # もともとのIDとは異なる

"""
変数text1という文字列に対し、text2は参照先がtext1なのでIDが同じです。
しかし、text1に文字列を加えた場合はIDが変わっていることが確認できます。
また、text1に対し別の文字列を代入してもやはり
IDが代わり元のオブジェクトとは別のオブジェクトが生成されたことが確認できます。
"""
