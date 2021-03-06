#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- Python入門　タプル(tuple)型---")


"""
タプルとは

冒頭で述べたとおり、Pythonにはタプル(tuple)型というシーケンスの型があります。
リストと同様に順序付けられた複数の値を格納することが可能です。
リストと異なる点は、一度初期化したタプルの要素は変更できない、という点です。
この性質のことをイミュータブル（不変）と呼びます。
このため、要素を更新、削除したりタプルそのものの順序をソートするような更新系の処理をすることはできません。
（以降、タプル型の変数を単にタプルと記述することがあります。）


タプルの初期化

タプルは丸括弧で要素をカンマ区切りで列挙して記述します。
なお、要素が1つしかない場合は必ずカンマをつけなければなりません。また、丸括弧は省略することも可能です。

サンプルを見てみましょう。
"""

# 要素がないタプル
t1 = ()
print(t1)    # ()

# 要素が一つの場合はカンマをつけないと、単一の値とみなされてしまう
t2 = (1)
print(t2)    # 1(単一の値扱い)

# t2 = (1,)
print(t2)    # (1,)

# カンマ区切りで複数の要素をセットする
t3 = ('a', 'b', 'c')
print(t3)     # ('a', 'b', 'c')

"""
また、末尾にカンマを残しても構いません。
"""

t = (1, 2, 3,)
print(t)    # (1, 2, 3)


"""
タプルの要素数

リストと同様、len関数を使用するとタプルの要素数を得ることができます。
"""

t = (1, 2, 3,)
l = len(t)
print(l)    # 3


"""
リストからタプルへの変換

タプルは組み込み関数のtuple()を使用してリストから生成（変換）する方法があります。
"""

# リストを初期化
l = [1, 2, 3]

# リストからタプルを初期化(リストをタプルに変換)
t = tuple(l)
print(t)    # (1, 2, 3)


"""
タプルからリストへの変換

また、逆にタプルからリストを生成する場合はこちらで触れましたが、list関数で可能となります。
"""

t = (1, 2, 3,)
l = list(t)
print(l)    # [1, 2, 3]

"""
タプルのメリット

リストと比較すると、更新系の処理ができないため不便に感じるかもしれませんが、
一度確定した値を途中で変えさせないで安全に保持・受け渡ししたいときに活躍します。
特に関数のコールシーケンスが複雑な場合、リストのように途中で変更が入る可能性がある場合、
思わぬ不具合が発生する原因になるためタプルを使用したほうがより安全にコーディングすることができます。

また、リストと比較して（少しだけ）処理する際のスピードが速いです。
また、イミュータブルなのでハッシュ化することが可能であるため、後述する辞書のキーとして使用することが可能です。
"""


print("--- Python入門　range型---")


"""
range型とは

range型とは整数を要素とするイミュータブルなシーケンスを作成するオブジェクトで、
組み込み関数のrangeを使用して生成します。
整数列のタプルのようなものなのですが、初期化の方法に大きな特徴があります。
初期化の際にシーケンスのサイズや、値の範囲、スキップ等を指定することができます。
以下、具体的に使ってみることで理解できることと思います。


range型の初期化
まず使ってみる

まず、正確な初期化の構文について学習する前に、とりあえず使ってみましょう。
"""

mg = range(5)
print(mg)    # range(0, 5) 中身は一体・・・？
print(list(mg))    # [0, 1, 2, 3, 4]

"""
1行目でrange型を生成しています。
range(5)と記述することで、これは、0から5未満までの整数が格納されたシーケンスが生成されます。
2行目で生成したオブジェクトをprintで参照していますが、
そのままだとrange(0, 5)と表示されて内容がよくわかりません。
このため、3行目でlist型に変換して内容を確認しています。
list関数の引数にrange型オブジェクトを指定すると、
range型からlist型に変換することができますのでそれを利用しているわけです。
range型の内容を確認する際によく使用するテクニックです。
range型になれるまではlistに変換して中身を確認してみてください。


初期化の構文

range型は組み込み関数のrange関数を使用し生成します。
初期化時にさまざまな条件を引数で指定することが可能です。
正確には以下の構文で範囲やインクリメントを変えることができます。

初期化
range(stop)
range(start, stop[, step])

startとstopで指定された区間のシーケンスが作成されます。stepで要素間の差を指定します。
step引数は省略が可能で、その場合はデフォルト値として1が設定されます。
また、マイナスの値を指定することも可能です。
最初の例のように引数にstopのみを指定することも可能でその場合は0始まりのrangeとなります。

それではここからさらにサンプルを確認してみましょう。
サンプルでは先程と同様、rangeの中を確認するために一旦リストに変換してからprintで出力しています。
"""

r1 = range(5)
print(list(r1))    # [0, 1, 2, 3, 4]

r2 = range(1, 5)
print(list(r2))    # [1, 2, 3, 4]

r3 = range(1, 5, 2)
print(list(r3))    # [1, 3]

"""
r1は、0から5個の整数シーケンスが生成されています。1づつ大きくなっています。
r2は、1から5個の整数シーケンスが生成されています。1づつ大きくなっています。
r3は、1から5個の整数シーケンスが生成されています。2づつ大きくなっています。


for文での利用

rangeの使い道ですが、最初はlistの初期化とループで利用することが多いかと思います。
PythonではC言語やJavaのようにループカウンタを指定したfor文がないため、
同じような書き方をしたい場合はrangeを利用します。（for文についてはこちらで説明します。）

javaでカウンタを指定したfor文を使用する場合、以下のように記述します。

// javaのfor文
for(i = 0; i < 10; i++){
    // 処理

これをPythonに書き直すと、以下のようになります。


# Pythonの場合
for i in range(0, 10):
	# 処理

もっとも、Pythonではlistのようなイテラブルなオブジェクトについてはカウンタを考慮せずにfor文を使用できるので、
上のようなループはあまり使用されません。
"""


print("--- Python入門　str(文字列)型---")


"""
文字列と初期化

Pythonの文字列はstr型という型で扱われます。
以降、str型変数を単に文字列と記述することがあります。
文字列を初期化する際は以下のようにダブルクォートかシングルクォートで文字列を囲みます。
"""

text1 = 'シングルクォートで囲む'
text2 = "ダブルクォートでもOK"
print(text1)
print(text2)

"""
エスケープシーケンス

改行やタブなどの特殊文字を使用する場合は、エスケープシーケンスとして\マークを使用します。
例えば、ダブルコーテーションでくくった文字列の内部で

「得意なプログラミング言語は"Python"です。」

という文字列を定義する場合について考えてみましょう。

text = "得意なプログラミング言語は"Python"です。"
# SyntaxError: invalid syntax

当然ながら、上のプログラムを実行するとエラーとなり
「SyntaxError: invalid syntax」が出力されます。
ダブルコーテーションを含んだ文字列を定義する場合は以下のように記述します。
"""

text = "特異なプログラミング言語は\"Python\"です。"
print(text)

"""
エスケープシーケンスについて理解できたところで、以下に代表的なものを示します。
エスケープシーケンス 	意味
\t 	タブ
\\ 	\
\' 	シングルコーテーション
\" 	ダブルクコーテーション
\n 	改行


raw文字列

Pythonの文字列定義のクォーテーションの前にrもしくはRを記述すると
raw文字列と呼ばれるエスケープシーケンスで使用した\マークを無効化することができます。

raw文字列
r"文字列"

raw文字列を使用すると、
例えばWindows系のディレクトリパスを記述する際にパスセパレータとエスケープで記述が煩雑になるのを
さけることができます。
"""

path1 = "C:\\work\\pywork"
print(path1)

path2 = r"C:\work\pywork"
print(path2)

"""
上のコードでpath1とpath2は同じ内容ですが、
raw文字列を使用したpath2のほうがスッキリかけることがわかるかと思います。


文字列の結合
文字列の結合

文字列同士を結合する場合は"+"を利用します。
"""

text1 = '今日は'
text2 = 'いい天気'

text3 = text1 + text2
print(text3)    # 今日はいい天気　が出力される


"""
オブジェクトの文字列表現と文字列結合

Pythonのprint文はオブジェクトを引数で指定すると、そのオブジェクトの文字列表現を得ることができます。
例えば、これまで学習してきた数値やリストの値を参照したい場合、以下のようにprint文で確認することができます。
"""

num = 5
print(num)    # 5

l = [1, 2, 3]
print(l)    # [1, 2, 3]


"""
ここで気をつけなければならないことが、文字列として結合するとTypeErrorが発生する、という点です。
よくやりがちなエラーが以下のサンプルです。

num = 5
text = 'text'

print(num) # 5が出力される
print(text + num) # TypeErrorが発生

こんな場合、組込みのstr関数を使うことにより、オブジェクトの文字列表現を取得することができ、
文字列結合することができます。
"""

num = 5
text = 'text'

print(num)    # 5が出力される
print(text + str(num))    # text5


"""
Pythonにこなれてきてもデバッグ文やログ出力で比較的よくやりがちなミスですので、
対処方法について知っておいてください。
"""


print("--- Python入門　シーケンスの共通処理---")

"""
シーケンスの共通処理

リスト、タプル、文字列等、どのシーケンス型にも使用できる共通的の演算や関数があります。
すでに説明したものも含まれますが、復習も兼ねてまとめて整理してみましょう。
以下の演算や関数を使用することができます。

演算 	                      説明
x in s 	            シーケンスsに要素xが含まれている場合にTrueを返します
x not in s 	        シーケンスsに要素xが含まれていない場合にTrueを返します
s + t 	            2つのシーケンスsとtを結合します。
s * n または n * s 	シーケンスs同士をn回結合します。
s[i] 	            0始まりのインデックスを指定してシーケンスsのi番目の要素を取得します。
s[i:j] 	            シーケンスsのi番目からj番目までのスライスを返します。
s[i:j:k] 	        シーケンスsのi番目からj番目までのk毎のスライスを返します。
len(s) 	            シーケンスsの長さ(=要素数)を返します。
min(s) 	            シーケンスsの最小の要素を返します。
max(s) 	            シーケンスsの最大の要素を返します。
s.index(x) 	        シーケンスsの中で要素xが最初に出現するインデックスを返します。
s.count(x) 	        シーケンスsの中で要素xが出現する回数を返します。


共通処理の解説

以下、よく使うものを中心に解説していきます。
包含判定(in、not in)

シーケンスsとオブジェクトxが要素に含まれているかどうかを判定するにはx in sと書きます。
また、含まれていないかどうかを判定するにはx not in xと書きます。
"""

list_data = ['a', 'b', 'c', 'd']

# 含まれているかどうかを判定する
b1 = 'a' in list_data    # 文字列'a'がリストに含まれているかどうかを判定
print(b1)    # True

b2 = 'x' in list_data    # 文字列'x'がリストに含まれているかどうかを判定
print(b2)    # False

# 含まれていないかどうかを判定する
b3 = 'a' not in list_data    # 文字列'a'がリストに含まれているかどうかを判定
print(b3)    # False

b4 = 'x' not in list_data    # 文字列'x'がリストに含まれているかどうかを判定
print(b4)    # True


"""
結合(+、*)

+演算子でシーケンス同士を結合することができます。
また、*演算子で指定回数分結合を繰り返すことができます。
"""

list_data1 = ['a', 'b', 'c']
list_data2 = ['d', 'e', 'f']

# リストの結合
new_list = list_data1 + list_data2
print(new_list)     # ['a', 'b', 'c', 'd', 'e', 'f']

# 結合の繰り返し
new_list = list_data1 * 3    # list_data1 + list_data1 + list_data1と同じ
print(new_list)    # ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']


"""
スライス文

リスト型のスライス文は既に説明しましたが、文字列もシーケンス型なので同様の操作が可能です。
文字列でのスライス文を見てみましょう。
"""

text = 'ABCDEFG'

# 0番目から2番目の手前まで
print(text[0:2])    # AB

# 開始インデックスの省略
print(text[:2])    # AB

# 2番目から最後まで
print(text[2:7])    # CDEFG

# 最後を省略
print(text[2:])    # CDEFG

# 1つ飛ばしで
print(text[0:7:2])    # ACEG

"""
リストの時と同様にスライスが使用できます。


要素数

len関数で要素数を確認することができます。リスト、タプル、文字列で確認してみましょう。
"""

# リストの場合
l = [1, 2, 3]
print(len(l))    # 3

# タプルの場合
t = ('a', 'b', 'c', 'd')
print(len(t))    # 4

# 文字列の場合
text = 'abcdefg'
print(len(text))    # 7


"""
最初に出現するインデックス

indexメソッドで指定した要素が何番目のインデックスに存在するのか、
出現する最初のインデックスを取得することができます。
なお、見つからない場合はValueErrorが発生します。
"""

l = ['a', 'b', 'c', 'd']

print(l.index('c'))   # 2

"""
print(l.index('x')) # ValueError: 'x' is not in list


以下、文字列の場合です。含まれる文字のインデックスを取得することができます。
部分文字列を指定することも可能です。
"""

text = 'abcdefg'
print(text.index('b'))    # 1
print(text.index('ef'))    # 3

"""
print(text.index('x')) # ValueError: substring not found


出現する回数

countメソッドで出現する回数をカウントすることができます。
"""

text = "abcdefg abcdefg"

print(text.count('b'))    # 2

print(text.count('ef'))    # 2

print(text.count('x'))    # 0
