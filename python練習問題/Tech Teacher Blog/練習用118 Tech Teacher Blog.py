#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Tech Teacher Blog ---")
print("--- Pythonの辞書をマスターしよう！基本的な使い方から応用まで網羅 ---")


"""
Pythonの辞書を学習し始め、

「もっと詳しく知りたい」
「基本から応用までをまとめて知りたい」

と思う人も多いでしょう。

そこで今回はPythonの辞書についての基本的な知識や
基礎から応用までの使い方を詳しく説明していきます。それでは見ていきましょう。
"""


print("--- Pythonの辞書とは？ ---")


"""
Pythonの辞書とは、Dictionary型と呼ばれる配列の一種です。
{ key1 : value1 , key2 : value2 , . . . }

このように「キー」と「値」のペアで表されたものが辞書です。
カンマで区切ることで、辞書には複数のデータを格納することができます。
"""


print("--- Pythonにおける辞書の使い方 ---")


"""
ここからは、実際にPythonにおける辞書の使い方を説明していきます。

    基本的な使い方
    辞書の追加・変更
    辞書の削除
    辞書のソート
    辞書の検索
    辞書の取得
    キーと値の交換

それでは見ていきましょう。


基本的な使い方

辞書を作成するためにはキーと値をコロン「:」でペアにしてすべての要素を波カッコ「{}」で囲みます。
各要素の間はカンマ「,」で区切ります。

実際にコードを用いて説明していきますね。
"""

x = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}

print(type(x))    # <class 'dict'>
print(x)    # {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}

"""
実行結果から出力されたデータ型が「’dict’」
すなわちDictionary型になっていることが分かりますね。
Python3.6以下では、辞書の要素の並び順は決まっていないため、
print(x)を実行するたびに出力結果が毎回異なることになります。
Python3.7以降では並び順が保存されるようになったためこのようなことは起こりませんが、
古いバージョンのPythonを使っている場合は注意してください。
また、キーは重複できません。
重複していてもエラーにはなりませんが、後から格納された値に上書きされてしまうので注意してください。
次の例を見てみましょう。


キーと値を追加

辞書に新しくキーと値を追加する方法を紹介します。
"""

x = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}

x['E'] = 'e'
print(x)    # {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e'}

"""
また、setdefaultメソッドを使用して追加することもできますよ。
"""

x = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}

x.setdefault('E', 'e')
print(x)     # {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e'}

"""
setdefaultメソッドは2つの引数を受け取るため、「( ‘E’ , ‘e’ )」と記述します。
辞書型オブジェクトの要素として辞書を入れ子にして追加することもできますよ。
"""

x = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
z = {'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h'}

x['dict'] = z    # 値に辞書型オブジェクトzを追加
print(x)
# {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'dict': {'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h'}}


"""
要素の変更

下記のように要素を変更することもできますよ。
"""

x = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}

x['D'] = 'e'    # キーDに対応する要素dがeに変更
print(x)     # {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'e'}

"""
辞書の要素を変更・追加するときにはupdateメソッドが便利です。
"""

x = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
print(x)    # {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}

x.update(A='aa', E='e')
print(x)    # {'A': 'aa', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e'}

x.update({'B': 'bb'})
print(x)    # {'A': 'aa', 'B': 'bb', 'C': 'c', 'D': 'd', 'E': 'e'}

x.update([('C', 'cc'), ['F', 'f']])
print(x)    # {'A': 'aa', 'B': 'bb', 'C': 'cc', 'D': 'd', 'E': 'e', 'F': 'f'}

x.update([('G', 'g')], H='h')
print(x)    # {'A': 'aa', 'B': 'bb', 'C': 'cc', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h'}

"""
キーワード引数による辞書の更新や辞書による辞書の更新、リストによる辞書の更新、
さらには両方を組み合わせた方法まで、さまざまな更新方法がありますよ。


要素を削除

要素を削除する場合には「popメソッド」や「clearメソッド」を使用できます。
"""

# popメゾット
x = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
x.pop('C')
print(x)     # {'A': 'a', 'B': 'b', 'D': 'd'}

"""
このように、popメソッドで引数にキーを指定すると指定したキーに対応する値が辞書から削除されます。
"""

# clearメゾット
x = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
x.clear()
print(x)    # {}

"""
このように、clearメソッドではすべて要素を削除できますよ。


辞書のソート

「ソート」を使うと辞書の要素を並べ替えることができます。
"""

x = {3: 'a', 2: 'b', 4: 'c', 1: 'd'}
sortedDict = sorted(x.items())
print(sortedDict)    # [(1, 'd'), (2, 'b'), (3, 'a'), (4, 'c')]

"""
このように「sorted関数」を使用するとキーが昇順にソートされたことが分かるでしょう。
しかし、出力結果が「[]」で囲まれていることからもわかるように、
辞書型ではなくリスト型になるので注意しましょう。


辞書の検索

辞書型を検索したい場合は「in演算子」「keysメソッド」「valueメソッド」を使用することで、
特定の要素を取り出せます。
"""

x = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
print('B' in x.keys())     # True

"""
上記のコードではkeysメソッドを使用しており、
指定した辞書型オブジェクトに含まれているキーをリスト型として返します。
さらにin演算子を使用することで’B’というキーがそのリストに含まれているかチェックしています。
いま。’B’はxに存在するので「True」と表示されていますね。
"""

x = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
print(5 in x.values())    # False

"""
上記のコードではvaluesメソッドを使用しており、
指定した辞書型オブジェクトに含まれている値をリスト型として返しています。
さらにin演算子を使用することで5という値がリストに含まれているかチェックしますが、
5はx中に存在しないので「False」と表示されますよ。


要素の取得

変数名の後に[取得したい要素のキー]と記述することで簡単に要素を取得することができますよ。
"""

x = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
z = x['C']
print(z)    # c

"""
また、下記のようにgetメソッドを使用して取得することもできますよ。
"""

x = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
print(x.get('A'))    # 存在するキーを指定
print(x.get('E'))    # 存在しないキーを指定
print(x.get('E', 'not found'))    # 存在しないキーとデフォルト値を指定

# a
# None
# not found

"""
すべてのキーを取得することもできますよ。
"""

x = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
x_keys = list(x.keys())
print(x_keys)    # ['A', 'B', 'C', 'D']

"""
また、すべての値を取得することもできますよ
"""

x = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
x_values = list(x.values())
print(x_values)    # ['a', 'b', 'c', 'd']

"""
さらにすべてのキーと値のペアを取得することも可能です。
"""

x = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'}
x_items = list(x.items())
print(x_items)    # [('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd')]

"""
キーと値を交換

辞書のキーと値を入れ替える方法は下記の通りです。
"""

x = {'A': 1, 'B': 2, 'C': 3}
z = {x[i]: i for i in x.keys()}
print(z)    # {1: 'A', 2: 'B', 3: 'C'}


print("--- まとめ ---")


"""
これまで、Pythonにおける辞書の基礎知識や基本から応用までの使い方を説明してきましたが
いかがでしたでしょうか。

今回の要点をまとめると以下のようになります。

    辞書とは波カッコの中にキーと値のペアとして格納されているデータ
    辞書の追加はsetdefaultメソッドを使用
    辞書の削除にはpopメソッド・clearメソッドを使用
    要素を並び替えたい場合はソートを使用
    辞書を検索するにはkeysメソッド・valuesメソッドを使用

Pythonで辞書を使いこなせるようになるとリスト型だけを使用したプログラムより
目的が明確なプログラムを記述することが可能ですよ。
身につけておけば効率よく作業を行うことができるためしっかり学習しておきましょう。
"""
