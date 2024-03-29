#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Tech Teacher Blog ---")
print("--- 【初心者向け】Pythonのmap関数とは？基本的な使い方を解説 ---")


"""
Pythonのmap関数の使い方がよく分からないという方も多いかと思います。
map関数は、Python基礎の中でも初心者がつまずきがちな分野です。
なぜなら、map関数は「引数に関数を指定」する必要があるからです。
ですが、map関数は非常に便利なものですので、ぜひ使い方を覚えて欲しいです。
map関数を使うことで、ソースコードの可読性を一気に上げることができます。
本記事では、Pythonのmap関数の使い方をまとめました。
map関数とは何か、map関数の具体的な使い方について解説しています。
サンプルコードも多く掲載しています。
本記事を読むことでmap関数の基礎をおさえることができます。
"""


print("--- Pythonのmapとは ---")


"""
まず、Pythonのmap関数とは何かについて解説します。
map関数は他の関数とは少し使い方が異なります。どういった点が異なるのか、詳しくみていきましょう。


map関数とは、リストやタプルなどの各値に対して、指定した関数を使うことができるものです。
map関数は「高階関数」とも呼ばれています。
高階関数とは、関数を引数として指定できる関数のことです。
たとえば、map関数の引数にabs関数を指定することで、リストの各値を絶対値にすることができます。
map関数は次のような書式で使われます。

map(関数、リストやタプルなどのオブジェクト)

たとえば、リストの各値を2倍にして出力したい場合、通常であれば次のように書くでしょう。
"""

def multi(i):
	return i * 2

list1 = [1, 2, 3, 4, 5]
list2 = []

for l in list1:
	list2.append(multi(l))
	print(list2)	

# [2]
# [2, 4]
# [2, 4, 6]
# [2, 4, 6, 8]
# [2, 4, 6, 8, 10]
"""
for文を使ってリストの値を1つずつ取り出し、関数に与えていくというやり方です。
このやり方でももちろん良いのですが、for文を使うためソースが長くなってしまうのがデメリットですね。
上記のコードは、map関数を使って次のように書き換えられます。
"""

def multi(i):
	return i * 2

list1 = [1, 2, 3, 4, 5]
print(list(map(multi, list1)))

# [2, 4, 6, 8, 10]

"""
map関数の第一引数に関数名、第二引数にリスト名を指定しています。
先ほどと全く同じ実行結果が得られることが確認できるでしょう。
ただし、map関数が返すのはmapオブジェクトであることに注意しましょう。
そのため、map関数の実行結果に対してlist関数を使ってリストに直す必要があります。
map関数を使うと、for文を使う必要がなくなり、コード量が減ります。
この方が可読性も高くなりましたね。これがmap関数を使うメリットです。


map関数と内包表記との違い

map関数とよく似たものに、内包表記というものがあります。
内包表記もmap関数同様、本来for文などのループ処理を使って記述する処理を
簡易化するための機能です。
ただし、書き方はmap関数と全く違います。
内包表記は、次のような書式で記述します。

[式 for 変数名 in リストやタプルなどのオブジェクト]

先ほどのコードを内包表記で書き直すと、次のようになります。
"""

def multi(i):
	return i * 2

list1 = [1, 2, 3, 4, 5]
print([multi(i) for i in list1])

# [2, 4, 6, 8, 10]

"""
先ほど解説したように、map関数を使う場合は、
list関数を使ってmapオブジェクトをリストに直す必要があります。
一方、内包表記の場合list関数を使う必要がなく、返り値をそのまま使うことができますね。
しかし、内包表記の場合は、変数を1つ増やす必要があります。
上記のコードでも「変数i」を増やしています。
どちらの方が読みやすいかは、一概には言えないでしょう。
mapの方が通常の関数と同じように使えるので、初心者にとっては分かりやすいかと思います。
ただ、内包表記の方が慣れてしまえば読みやすいです。
map関数と内包表記、どちらを使うかは好みの問題でしょう。
"""


print("--- Pythonのmap関数を使う方法 ---")


"""
次に、Pythonのmap関数を使う方法について解説します。
map関数と他の関数を組み合わせて、具体的に何ができるのかみていきましょう。
次の5つのやり方を解説していきます。

    型変換を行う
    絶対値を取得する
    リストを結合させる
    2つのリストの数値を加算する
    lambda式と組み合わせる

map関数を使えば、これらの処理も少ないコード量で記述することができます。
1つ1つのやり方について、詳しく解説します。


型変換を行う

map関数を使うことで、リストの値の型を変換することができます。
"""

list1 = [1, 2, 3, 4, 5]

print(list(map(str, list1)))

# ['1', '2', '3', '4', '5']

"""
上記のコードは、map関数内でstr関数を使っています。
str関数は数値を文字列を変換するものです。
実行結果を見て分かる通り、list1の値が全て文字列に変換されています。
次は、文字列を数値に変換する方法をみていきましょう。
"""

list1 = ["1", "2", "3", "4", "5"]

print(list(map(int, list1)))

# [1, 2, 3, 4, 5]

"""
上記のコードは、map関数内でint関数を使っています。
int関数は文字列を数値に変換するものです。
実行結果を見て分かる通り、list1の値が全て数値に変換されています。
文字列に変換する場合はstr、数値に変換する場合はintを使いましょう。


絶対値を取得する

次に、絶対値を取得する方法をみていきます。
"""

list1 = [-1, 2, -3, 4, -5]

print(list(map(abs, list1)))

# [1, 2, 3, 4, 5]

"""
上記のコードではmap関数内でabs関数を使用しています。
abs関数は絶対値を返却してくれる関数です。
実行結果を見ると、list1に格納された値が全て正の数になっていることが分かるかと思います。


リストを結合させる

次に、リストを結合させ1つの文字列として出力させる方法をみていきましょう。
"""

list1 = [1, 2, 3, 4, 5]

print('|'.join(map(str, list1)))

# 1|2|3|4|5

"""
上記のコードは、まずstr関数によってlist1の値を文字列に変換しています。
次にjoin関数によって文字列同士を「|」で結ぶようにしています。
このようにstr関数とjoin関数を組み合わせることで、リストを結合させることが可能です。


2つのリストの数値を加算する

次に、2つのリストの数値を加算する方法をみていきましょう。
"""

def add(a, b):
	return a + b

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

print(list(map(add, list1, list2)))

# [7, 9, 11, 13, 15]

"""
上記のコードは、map関数の第二引数と第三引数にリストを指定しています。
map関数は複数のリストを指定することで、それらに対し関数を使うことができます。
add関数によって、list1とlist2の値を加算して出力しています。


lambda式と組み合わせる

最後に、map関数とlambda式を組み合わせる方法を紹介しましょう。
lamda式を使うことで、名前を持たない無名関数を作成することができます。
Pythonで関数を作る場合、def文で関数名を定義するのが普通ですが、
lambda式を使えばその必要がなくなります。
たとえばlambda式は次のような使い方をします。
"""

multi = lambda i: i * 2

print(multi(2))

# 4

"""
上記のコードでは、値を2倍にする無名関数を作成しています。
無名関数の返り値はmultiに格納しています。
multiに引数を指定することで、値を2倍にすることができます。
また、上記のコードはさらに簡略化することができます。
"""

print((lambda i: i * 2)(2))

# 4

"""
このように記述すれば、multi変数も不要になります。
lambda式を活用することで、コード量を減らすことができます。
そして、lambda式はmap関数と組み合わせることで、さらに便利に活用することができるのです。
例をみていきましょう。
"""

list1 = [1, 2, 3, 4, 5]
print(list(map(lambda i: i * 2, list1)))

# [2, 4, 6, 8, 10]

"""
上記のコードでは、map関数の第一引数に、lambda式によって関数を指定しています。
そして、第二引数で指定したリストの値を2倍にしています。
このように、lambda式はmap関数と組み合わせることでコード量を一気に減らせます。
このような書き方も覚えておくと良いでしょう。
"""
