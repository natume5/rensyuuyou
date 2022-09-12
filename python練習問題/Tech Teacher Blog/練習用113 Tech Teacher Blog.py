#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Tech Teacher Blog ---")
print("--- 【完全マスター】！Pythonのindexの使い方を徹底解説！ ---")


"""
Python初心者の方で「なんとなくindexメソッドの使い方は掴めてきたけど、
まだイマイチよく分からない」と悩んでいる方もいるでしょう。
そこで今回は、indexの基礎知識からindexメソッドの使い方まで詳しく説明していきます。
indexメソッドの使い方をマスターするためにも、ぜひ最後までご覧くださいね。
"""


print("--- indexについて ---")


"""
「index」とは、list型変数のある要素がlistの中で何番目かを示すもので、
もし指定された値が存在しなければエラーを起こします。

1.　list1 = [ ‘A’ , ‘B’ , ‘C’ , ‘D’ , ‘E’ ]
2.　　　　 0 1 2 3 4　　　＃　インデックス番号
3.　　　　 -5 -4 -3 -2 -1　　 ＃　負のインデックス

このようにindexは1からではなく0から始まるので注意してくださいね。
また、「indexメソッド」はシーケンスの値に当てはまるインデックスを返すメソッドです。
シーケンスとは複数の要素をまとめて管理できる型のことで、
他のプログラミング言語では配列と呼ばれています。
indexメソッドはリスト・タプル・文字列などのシーケンスに使用でき、
セット型・辞書型には使用できないので注意しましょう。
補足としてリスト・タプル・文字列とはなにかをまとめておきます。


リスト 	任意の型のデータを格納でき、要素には順序があるためインデックスを使用して
        要素を指定することが可能です。リストの要素は変更することができ、
        他のプログラミング言語での配列のように扱えます。
タプル 	こちらもリストと同様、任意の型のデータを格納でき、
        要素には順序があるためインデックスを使用して要素を指定することが可能です。
        リストと違う点は、タプルの要素は変更できないということです。
文字列 	文字が連なったものですが、0文字の文字列や1文字だけの文字列もあります。
        0文字の文字列のことを空文字列と呼びます。
"""


print("--- indexメソッドの使い方 ---")


"""
Pythonにおけるlistの要素のインデックス、
つまり要素が何番目に格納されているかを表す番号を取得する方法を紹介していきます。

indexメソッドは次のように使用します。

1.　シーケンス . index ( ‘value’ )


リストの要素が重複していない場合の使い方

リストの要素が重複していない場合には「index( )メソッド」を使用します。
実際にコードを用いて詳しく説明していきます。
"""

mylist = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
print(mylist.index('bbb'))    # 1

print(mylist.index('eee'))    # 4

"""
指定した要素が存在しない場合、ValueErrorが発生するので注意してください。
1.　print( mylist . index ( ‘fff’ ) )
2.　ValueError : ‘fff’ is not in list

このようにmylistに「’fff’」という要素は含まれていないため、エラーが返ってきます。


リストの要素が重複している場合の使い方

リストの要素が重複している場合の
「index( )メソッド」は最初に見つかった
要素に対応するインデックスだけを返すので注意してください。
"""

mylist = ['aaa', 'bbb', 'ccc', 'ccc', 'aaa']

print(mylist)    # ['aaa', 'bbb', 'ccc', 'ccc', 'aaa']

print(mylist.index('aaa'))    # 0


"""
すべてのインデックスをリストで取得したい場合には、
組み込み関数「enumerate( )」とリスト内包表記を使用します。
「リスト内包表記」とは通常のリスト生成では複雑になってしまうようなプログラムを
1行で記述する表記方法です。
「enumerate( )関数」を使用して重複のあるlist型変数から
要素を取得する場合の記述方法は次の通りです。

1.　[ i for i , x in enumerate ( list型変数 ) if x == value ]

実際にコードを使用して説明していきます。
"""

mylist = ['aaa', 'bbb', 'ccc', 'ccc', 'aaa']

for idx, val in enumerate(mylist):
	print(idx, val)

# 0 aaa
# 1 bbb
# 2 ccc
# 3 ccc
# 4 aaa

"""
このenumerate( )を利用して、次のように該当している全インデックスを取得することもできます。
"""

mylist = ['aaa', 'bbb', 'ccc', 'ccc', 'aaa']

idxlist = []
for idx, val in enumerate(mylist):
	if val == 'ccc':
		idxlist.append(idx)

print(idxlist)    # [2, 3]

"""
要素が1つだけ含まれている場合・リストに含まれていない場合は空のリストを返送することができ、
繰り返し使用するようであれば関数にしておくと便利でしょう。
"""

mylist = ['aaa', 'bbb', 'ccc', 'ccc', 'aaa']

# 要素が1つだけ含まれている
print([i for i, x in enumerate(mylist) if x == 'bbb'])    # [1]

# リストに含まれていない値
print([i for i, x in enumerate(mylist) if x == 'fff'])    # []

# 繰り返し使用する場合
def my_index_multi(list1, x):
	return [i for i, _x in enumerate(mylist) if _x == x]

print(my_index_multi(mylist, 'aaa'))    # [0, 4]

print(my_index_multi(mylist, 'bbb'))    # [1]

print(my_index_multi(mylist, 'fff'))    # []


"""
リストのリスト

リストの中にリストがある場合はどうなのでしょうか。見ていきましょう。


list1 = [[111, 222, 333], ['red', 'blue', 'green']]
list2 = 222
list3 = ['red', 'blue', 'green']

x = list1.index(list2)
z = list1.index(list3)

print(x)
print(z)

ValueError: 222 is not in list

「222」はlist1の中の子リストには存在しますがlist1そのものにあるわけではありません。
その結果index( )メソッドを使用することはできません。


最大値のインデックスを取得

「max( )」を使うと、最初に見つかった最大値の要素のインデックスが返送されます。
"""

list = [111, 555, 777, 333, 777]

print(list.index(max(list)))    # 2

"""
最大値が複数存在して、そのすべてのインデックスを取得したい場合は
次のようにリスト内包表記を使用します。
"""

list = [111, 555, 777, 333, 777]

print([i for i, v in enumerate(list) if v == max(list)])    # [2, 4]


print("--- リスト以外でindexメソッドを使う方法 ---")


"""
リスト以外にもタプルや文字列でもindexメソッドを使用することができます。
ここからはタプルや文字列でindexメソッドを使用する方法を詳しく説明していきます。


タプル

タプルもリストと同じように「index( )メソッド」を持っているため次のように記述することが可能ですよ。
"""

tuple = ('aaa', 'bbb', 'ccc')

print(tuple.index('bbb'))    # 1


"""
文字列

文字列の位置を取得する場合のコードは次のようになっています。
"""

str = 'HelloWorld'

print(str.index('l'))    # 2


"""
また、文字数を指定して抽出することもできます。
"""

str = 'python'

print(str[0])    # p

print(str[5])    # n

# 負の値を使用すると文字列の後から指定可能
print(str[-1])    # n

print(str[-6])    # p


print("--- まとめ ---")


"""
今回indexメソッドの基礎知識や使い方について説明してきましたがいかがでしたでしょうか。
今回説明した要点をまとめると次のようになります。

    indexとはシーケンスのある要素が何番目かということを表すもの
    indexは0から始まり、負のインデックスは1番右側が-1となる
    リストに含まれていない値を指定するとValueErrorが発生する
    リストの要素が重複している場合は最初のインデックスだけを返す
    indexメソッドはリスト以外にもタプルや文字列にも使用できる

indexを使用することによって要素の番号を取得することができます。しっかり押さえておきましょう。
"""
