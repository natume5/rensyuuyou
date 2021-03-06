#!/usr/bin/python
# -*- coding: UTF-8 -*-


# シーケンス
"""
リスト と タプル は、どちらも整数値で インデックス(添字) を指定して、
登録されている要素を参照できるオブジェクトでした。

次の例は、リストオブジェクト [10, 20, 30, 40, 55] の、1番目と3番目の要素を参照して足し合わせています。
"""
values = [10, 20, 30, 40, 55]
print(values[0] + values[2])


"""
タプルオブジェクトでも、全く同じように要素を参照できます。
"""
values = (10, 20, 30, 40, 55)
print(values[0] + values[2])


"""
また、文字列オブジェクト も、インデックスを指定して文字列中の文字を参照できるオブジェクトです。
リストやタプルと同じように、[] にインデックスを指定し、その位置の文字を参照できます。

次の例は、文字列 "HELLO" の、1番目と3番目の文字を参照しています。
"""
values = "HELLO"
print(values[0] + values[2])

"""
リスト・タプル・文字列はいずれも コレクション に属するオブジェクトですが、コレクションの一種で、
整数値のインデックスを指定して要素を参照できるオブジェクトのことを、

    シーケンス (Sequence)

と呼びます。
"""


# コレクションとシーケンスの違い
"""
リストやタプルなどのオブジェクトは、コレクションの一種で、他のオブジェクトを登録し、集約できるオブジェクトです。

シーケンスとは、コレクションのうちで、集約する要素が一定の順序で並んでいて、
その順序(インデックス)を使ってその要素を指定できる種類のオブジェクトのことを指します。

コレクションに属するオブジェクトでも、リストやタプルとは違って、辞書 は、
順序を指定して要素を指定することはできません。
このため、辞書はコレクションですが、シーケンスではありません。

Pythonには、辞書の他にもシーケンスに属さないオブジェクトがあり、
この先もう少しだけPythonの学習をすすめると、そういった種類のオブジェクトについても学ぶことになります。
"""


# シーケンスの比較演算子
"""
タプルやリスト、文字列などのシーケンスオブジェクトは、 <、 <=、>、>= などの演算子で、値の大小を判定できます。
"""
list1 = ['a', 'b', 'c']
list2 = ['a', 'b', 'd']

print(list1 <= list2)    # list1 < list2 なのでTrue


list3 = ['a', 'b', 'c']
list4 = ['a', 'b', 'b']

print(list3 <= list4)     # list3 > list4 なのでFalse

"""
シーケンスではない、辞書オブジェクトなどのコンテナオブジェクトは、 < などによる大小の比較はできません。
比較すると、次のようなエラーとなります。

dict1 = {"dog": "犬", "cat": "猫"}
dict2 = {"dog": "犬", "cat": "猫"}

print(dict1 <= dict2)

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-95-f273e382d9ed> in <module>
      2 dict2 = {"dog": "犬", "cat": "猫"}
      3 
----> 4 print(dict1 <= dict2)

TypeError: '<=' not supported between instances of 'dict' and 'dict'

シーケンス同士の値の比較は、先頭の要素から順番に同じインデックス同士の値を比較して、
先に小さい値となったシーケンスが小さい値となります。

例えば、上記のように (1, 2, 3) と (1, 2, 4) を比較した場合、

    最初の要素の 1 と 1 を比較する。同じ値なので、次の値をチェックする。
    ２番めの要素の 2 と 2 を比較する。同じ値なので、次の値をチェックする。
    3番目の要素の 3 と 4 を比較する。 3 < 4 なので、(1, 2, 3) は (1, 2, 4) よりも小さい。
のように比較を行います。

比較するシーケンス同士の長さが異なる場合、短いシーケンスの要素と
長いシーケンスの要素を比較してすべて等しければ、短い要素のほうが小さい値となります。

たとえば、長さが 3 のタプル (1, 2, 3) と、長さが 4 のタプル (1, 2, 3, 4)は、
長さ 3 のタプルの要素はすべて長さ 4 のタプルと一致しますので、長さが短い (1, 2, 3) 
が小さい値のタプルとなります。
"""

value1 = (1, 2, 3)
value2 = (1, 2, 3, 4)

print(value1 < value2)


# コレクションのアンパック
"""
変数 では、代入文を使って、変数に値を代入する方法を解説しました。
普通の代入文は、右辺の値を、左辺に指定した変数に代入します。
"""
variable = 1000    # variableに1000を代入
print(variable)


# コレクションのアンパック
"""
代入式の右辺がコレクションなどの場合には、左辺に複数の変数名を指定して、
コレクションの要素を一括して変数に代入できます。

たとえば、右辺が [1, 2, 3] のように、要素が3つあるリストの場合、
左辺に var1, var2, var3 と3つの変数名を指定できます。
"""
list_obj = [1, 2, 3]
var1, var2, var3 = list_obj    # var1, var2, var3 に、list_objの要素を順に代入

print(var1, var2, var3)

"""
このように記述すると、変数 var1、var2、var3 には、
右辺のリストオブジェクトの要素が一つずつ順番に代入されます。
この場合、var1 には list_obj の最初の要素である 1が、var2、var3 には、
それぞれ2番目と3番目になる 2 と 3 が代入されます。

このように、コレクションの要素を一括して変数に代入する方法を、アンパック(unpack) といいます。

右辺には、リストオブジェクト以外にタプルなどのコレクションも指定できます。
"""

var1, var2, var3 = (1, 2, 3)    # タプルのアンパック
print(var1, var2, var3)


"""
文字列を代入すると、1文字ずつ分割して代入されます
"""
var1, var2, var3 = "ABC"    # 文字列のアンパック
print(var1, var2, var3)


"""
アンパック代入を行う場合は、右辺のコレクションの要素数と、
左辺に指定する変数の数が一致する必要があります。一致しない場合は、次のようなエラーになります。

var1, var2 = "ABC" # 文字列のアンパック
print(var1, var2)

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-61-08fa34f2a626> in <module>
----> 1 var1, var2 = "ABC" # 文字列のアンパック
      2 print(var1, var2)

ValueError: too many values to unpack (expected 2)

この例では、長さが3の文字列を、var1 と var2 という２つの変数に代入しようとしていますが、
文字が一つ余ってしまうためにエラーとなります。
"""


# アンパックの使用例
"""
アンパックを利用した代入は、Pythonプログラミングで頻繁に利用されます。

タプルの書き方 では、例として、東京都にある人形町駅の緯度と経度を、次のようなタプルで記述しました。

ningyocho = (35.686321, 139.782211)

このタプルから、駅の緯度と経度を取り出し、出力してみましょう。

タプルから値を取り出すには、インデックスを指定して値を取り出す方法があります。
この方法で処理を記述すると、こうなります。
"""
ningyocho = (35.686321, 139.782211)    # (経度, 緯度)のタプル

ido = ningyocho[0]    # ningyochoから緯度を取り出す
keido = ningyocho[1]    # ningyochoから経度を取り出す

print("人形町は緯度:", ido, "経度:", keido)


"""
この書き方でも間違いではないのですが、2行にわけてそれぞれ緯度と経度を取り出すのは、
ちょっとまだるっこしい感じがしませんか？

このような場合、アンパックを使うと、
"""
ningyocho = (35.686321, 139.782211)    # (経度, 緯度)のタプル

ido, keido = ningyocho    # ningyochoから緯度と経度を取り出す

print("人形町は緯度:", ido, "経度:", keido)

"""
のように、一行ですっきりと記述出ます。
"""


# 関数とアンパック
"""
また、アンパックは、複数の値を戻り値とする 関数 でよく使われます。

合計感染者数を for 文で求める では、次のような、伝染病の合計感染者数を求める処理を書きました。

cases = [100, 125, 110, 135, 93, 95, 93]

total = 0 # 合計感染者数の初期値 0 を設定
for cases_of_day in cases:
    total = total + cases_of_day

print("合計感染者数は:", total)

このプログラムで、ついでに毎日の感染者数の平均値も求めてみましょう。

平均値は

    合計感染者数 ÷ データの日数 

で求められます。

この場合、データの日数 は 変数 cases の要素の数ですから、len(cases) で求められます。
ですから、平均値を求める処理を追加すると、次のようになります。
"""
cases = [100, 125, 110, 135, 93, 95, 93]

total = 0    # 合計感染者数の初期値 0 を設定
for cases_of_day in cases:
    total = total + cases_of_day

# 合計患者数 ÷ データの日数で平均感染者数を求める
average = total / len(cases)

print("合計感染者数は:", total)
print("平均感染者数は:", average)


# 合計値と平均値を求める関数を作成する
"""
この、合計値と平均値を求める処理を 関数 にして、病気の感染者だけでなく、
数値のコレクションならどんなデータでも合計値と平均値を求められるようにしてみましょう。

この関数は、total_and_average() という名前にしましょう。引数 として リスト などを指定すると、
戻り値 としてコレクションの要素の合計値と平均値を求めます。

関数 total_and_average() の定義は、次のようになります。
"""
def total_and_average(values):
    total = 0    # 合計値の初期値0を設定
    for value in values:
        total = total + value

    # データの件数を求める 
    num = len(values)

    # 合計値÷件数で平均値を求める
    average = total / num

    # 戻り値として(合計値、平均値)のタプルを返す
    return(total, average)

"""
関数で計算した結果は、return文 を使って、戻り値として返します。

しかし、関数 total_and_average() は合計値と平均値の2つを計算しますが、 
return文 に指定できる戻り値は一つだけです。

そこで、return文には (合計値, 平均値) のタプルを指定し、二つの値を一つのタプルにまとめて返り値とします。 
このようにすれば、total_and_average() を利用するときには、タプルのアンパックを利用して
"""

values = [100, 200, 20, 50, 90]
total, average = total_and_average(values)
print(values, "の", "合計は", total, "平均は", average, "です。")


"""
のように書けます。

もう一つの例として、total_and_average() を修正し、
コレクションに含まれるデータの件数も戻り値として返すようにしてみましょう。
この関数は total_and_average_and_number() という名前とし、返す値が二つから三つになります
"""

def total_and_average_and_number(values):
    total = 0    # 合計値の初期値0を設定
    for value in values:
        total = total + value

    # データの件数を求める 
    num = len(values)

    # 合計値÷件数で平均値を求める
    average = total / num

    # 戻り値として(合計値、平均値)のタプルを返す
    return(total, average, num)

"""
total_and_average_and_number() を利用するときも、
同じようにタプルのアンパックを利用して次のように書けます。
"""

values = [100, 200, 20, 50, 90]
total, average, number = total_and_average_and_number(values)
print(values, "の", "合計は", total, "平均は", average, "件数は", number, "です。")

"""
このように、戻り値としてタプルを使い、
複数の値を一度に返す関数はとてもよく使われます。テクニックとして覚えておきましょう。
"""


