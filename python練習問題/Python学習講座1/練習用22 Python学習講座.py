#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- Python入門　変数の型を判定する---")


"""
isinstance関数
isinstance関数の使い方

pythonは型宣言がないため、関数の引数や戻り値の型が実行するまでわからない場合があります。
このため、型をチェックする必要が随所で出てきます。この場合、組込みのisinstance関数を使用します。

isinstance
isinstance(変数, 型)

基本的な型を判定する処理のサンプルです。
"""

def sample(obj):
	""" 引数の型を判定する """

	if isinstance(obj, bool):
		print("bool型です")

	if isinstance(obj, int):
		print("int型です")

	if isinstance(obj, float):
		print("float型です")

	if isinstance(obj, complex):
		print("comlex型です")

	if isinstance(obj, list):
		print("list型です")

	if isinstance(obj, tuple):
		print("tuple型です")

	if isinstance(obj, range):
		print("range型です")

	if isinstance(obj, str):
		print("str型です")

	if isinstance(obj, set):
		print("set型です")

	if isinstance(obj, frozenset):
		print("frozenset型です")

	if isinstance(obj, dict):
		print("dict型です")

sample('aaa')
sample('1')
sample('1.1')
sample([1, 2, 3])
sample({100, 200})
sample({'key': 100})

"""
補足 基本的な変数の型

補足として、isinstance関数の引数に使用する基本的な変数の型を以下に掲載します。
型名 	        説明
bool 	       真偽値型
int 	       整数型
float 	       小数型
complex 	   複素数型
list 	       list型
tuple 	       タプル型
range 	       range型
str 	       文字列型
bytes 	       バイト型
set 	       集合型
frozenset  	   イミュータブルな集合型
dict 	       辞書型
補足

isinstance関数で変数の型の一致を確認することができましたが、よく似たものにtypeというものがあります。

変数の型を判定する その2 type関数

classについて学習した後学習しましょう。
"""


print("--- Python入門　比較演算---")


"""
比較演算

bool型で簡単に説明しましたが、比較演算を使用すると2つの変数を比較し、
比較結果を真理値で得ることができます。Pythonでは以下のような比較演算が使用できます。
リストや辞書のページで解説したinは実は比較演算の一種なのです。

x == y 	x と y は等しい
X != y 	x と y は等しくない
x > y 	x は y よりも大きい
x < y 	x は y よりも小さい
x >= y 	x は y 以上である
x <= y 	x は y 以下である
x in y 	x という要素 が y に存在する
x not in y 	x という要素 が y に存在しない


等しい・等しくない

2変数が等しいかどうかを調べる場合、==演算子を使用します。等しい場合はTrueが、
そうでない場合はFalseが返されます。
"""

x = 3
y = 3
z = 7

b1 = (x == y)
b2 = (x == z)

print(b1)    # True
print(b2)    # False

"""
一方、等しくない場合は!=を使用します。
先ほどとは逆に等しくない場合はTrueが、等しい場合はFalseが返されます。
"""

x = 3
y = 3
z = 7

b1 = (x != y)
b2 = (x != z)

print(b1)    # False
print(b2)    # True


"""
大なり小なり

数学と同様、大なり小なり記号を使用して2変数の大小関係を得ることができます。
Pythonの特徴の1つに、比較演算子を同時に複数使用することができる、ということが挙げられます。
便利な書き方なので、是非活用してみてください。サンプルで確認してみましょう。
"""

x = 3
y = 5
z = 7

b1 = (x < y)
print(b1)    # Trueが出力される

b2 = (x < y < z)
print(b2)    # Trueが出力される

"""
数学の不等号と同じなのですんなり飲み込めたのではないでしょうか。


含まれる・含まれない

リスト、タプル、setなど複数の値を持つコレクションの場合、
in、not inである要素が含まれているかどうかを判定することができます。
以下のコードでは3と4がリストl1に含まれているかどうかを調べています。
"""

l = [1, 3, 5, 7]
b1 = (3 in l)
print(b1)    # True

b2 = (4 in l)
print(b2)     # False


"""
is オブジェクトの同一性

Pythonのオブジェクトはそれぞれユニークなid(識別子)を持っており、これはオブジェクトのIDと呼ばれています。
メモリ上のアドレスの一種だと捉えても差し支えありません。
オブジェクトが同一であるとは、変数が同じアドレスを指している場合のことを指します。

さてそのオブジェクトのIDですが、組み込み関数のid関数でを取得することができます。
2つのオブジェクトが同一のオブジェクトかどうか、つまりIDが等しいかどうかを判定する場合、
イコールではなくisを利用します。一方で、同じ値を持つかどうかの判定は、
先程の説明の通り==演算子を使用します。サンプルで確認してみましょう。
"""

x = [1, 2]
y = x
z = [1, 2]

# IDを確認する
print(id(x))
print(id(y))
print(id(z))

# 同じ値かどうかを判定
b1 = (x == y)
b2 = (x == z)
print(b1)    # True
print(b2)    # True

# 同じオブジェクトかどうかを判定
b3 = (x is y)
b4 = (x is z)
print(b3)    # True
print(b4)    # False

"""
yはxの値を代入したものなので、同じオブジェクトを指し示しています。
zはxと同じ値ですが、新たに作成したオブジェクトですので、isで比較するとFalseと評価されます。
"""


print("--- Python入門　if文---")


"""
if文

プログラムを記述している際、特定の条件の場合のみ処理を実行したい場合が出てきます。
例えば、変数xの値が0と等しい場合はその旨を表示させたい、といった場合です。
if文とはこういった条件に応じて処理を分岐させたい場合に使用する文です。

Pythonのif文は以下のように記述します。
なお、bool値や前回学習した比較演算のように真理値を得られるものを条件式と呼びます。

if文
if 条件式:
    条件式が正の場合の処理

例えば、xが0かどうかを判定する場合、以下のようになります。
"""

x = 0
if x == 0:
	print('x = 0')    # ここが出力される


"""
else文

if文の条件を満たさないような場合にも別途処理をしたい場合、else文を使用します。
if-else
if 条件式:
    条件式が正の場合の処理
else:
    条件式が偽の場合の処理

例えば、xが0の場合は「x = 0」それ以外の場合は「x != 0」というメッセージを表示させたい場合、
以下のようになります。
"""

x = 1
if x == 0:
	print('x = 0')
else:
	print('x != 0')    # こちらが出力される


"""
elif文

複数のif文を使いたい場合、elifを使用します。else ifの略ですね。
else文とも組み合わせて使うことができます。条件式を2つ使用したい場合は以下のように記述します。

if-else
if 条件式1:
    条件式1が正の場合の処理
if 条件式2:
    条件式2が正の場合の処理
else:
    条件式が偽の場合の処理

例えば、xが0の場合と1の場合とそれ以外の場合で処理を分けたい場合、以下のように記述します。
"""

x = 1
if x == 0:
	print('x = 0')
elif x == 1:
	print('x = 1')     # こちらが出力される
else:
	print('x != 0 and x != 1')


"""
変数の真理値評価

Pythonでは偽と判定されるものはFalse以外にも多数あるので注意してください。

    False
    None
    ゼロと同値
    __len__メソッドが定義されている型のオブジェクトで0が返された場合
    __nonezero__メソッドが定義されている型のオブジェクトでFalseが返された場合

4番目の具体例ですが、空のシーケンス、マップ、set（''、]、()、{}）などが該当します。
いずれも空の場合はlen関数の値が0になります。

サンプルで動作を確認してみましょう。
"""

if l:
	print('True')    # Trueが出力される
else:
	print('False')

if 0:
	print('True')
else:
	print('False')    # Falseが出力される

if 0.0:
	print('True')
else:
	print('False')    # Falseが出力される

if 0.1:
	print('True')    # Trueが出力される
else:
	print('False')

if []:
	print('True')
else:
	print('False')     # Falseが出力される

if None:
	print('True')
else:
	print('False')    # Falseが出力される

if "":
	print('True')
else:
	print('False')    # Falseが出力される

"""
また、サンプルの最後の例のとおり、文字列もシーケンスの一種なので、
から文字列は長さ0、つまりFalseと評価されます。
"""


print("--- Python入門　for文---")


"""
for文の基本

for文とは冒頭で述べたとおり繰り返し処理を行うための文です。Pythonのfor文は以下のように記述します。

for文
for ループ内変数 in イテラブルな変数:
    ループ内処理

イテラブルというのはリストや辞書といった複数の要素からなり、反復処理が可能な性質をもつことを指し、
以下のような型がそれに該当します。

    リスト
    タプル
    文字列
    set
    range
    辞書

[参考] range型

いくつか例を見ていきましょう。


リストのfor文

リストの要素の先頭から順番に表示する場合、以下のように記述します。
"""

datas = ['a', 'b', 'c']

for v in datas:
	print(v)    # listの各値が表示される


"""
rangeのfor文

rangeで初期値、限界、増分を指定すると、
C言語やJavaのループカウンタを利用したループ処理を行うことができます。
"""

for v in range(1, 5, 2):
	print(v)    # 1から2飛ばしで5まで出力される。この場合、1, 3が出力される


"""
辞書のfor文

辞書もfor文でループ処理可能です。リストなどの同様の書き方も場合、
キーのみのループになりますが、辞書のメソッドを使用することでキー、値のループも可能となります。
今回は紹介のみにとどめ、次回もう少し細かく説明します。


キーのループ

前述のとおり、通常のfor文の場合はキーをループ処理することができます。
"""

d = {'key1': 110, 'key2': 270, 'key3': 350}

for key in d:
	print(key, d[key])


"""
valueのループ

値でループしたい場合はvaluesメソッドを利用します。
"""

d = {'key1': 110, 'key2': 270, 'key3': 350}
for value in d.values():
	print(value)    # 値が出力される


"""
keyとvalueのループ

キー、値の両方をループで取得したい場合は、items()メソッドを利用します。
"""

d = {'key1': 110, 'key2': 270, 'key3': 350}
for key, value in d.items():
	print(key, value)    # keyと値が出力される


"""
ループインデックスを取得する場合

何番目の要素だけは処理をしない、等の処理を入れたい場合はループインデックスを利用しますが、
これはenumerate関数で取得することができます。


リストの場合
"""

l = ['a', 'b', 'c']

for i, value in enumerate(l):
	print(i, value)    # ループインデックスとリストの値が出力


"""
辞書の場合
"""

dic = {'key1': 110, 'key2': 270, 'key3': 350}

for i, value in enumerate(dic):
	print(i, value)     # ループインデックスと値が出力

for i, (key, value) in enumerate(dic.items()):
	print(i, key, value)    # # ループインデックスとkeyの値が出力


"""
break

breakを使用するとループの途中で抜けることができます。
サンプルで確認してみましょう。
以下のコードでは、リストの各値をprintで出力していますが、
1より大きい値を出力した後breakでループを抜けています。
"""

data_list = [1, 2, 3]    # 空のリスト

for data in data_list:
	print(data)
	if data > 1:
		break

"""
実行してみると、2まで出力された後、breakが実行され処理が終了します。


for-else

Pythonのfor文はelseと併用することができます。elseブロックに記述した処理は、以下の動作となります。

    forループ処理回数によらず実行される
    breakした場合は実行されない

サンプルで動作を確認してみましょう。
"""

data_list = []    # 空のリスト

for data in data_list:
	print(data)
else:
	print('ループ処理が終わりました')    # ここが出力される

"""
ループで回すリストが空なので、forブロック内の処理は行われませんが、elseブロック内の処理は呼びだされます。
また、breakと組み合わせて使用する場合が多いです。
例えば、数値のリストで負の数の要素をループで見つけ、なければその旨を表示する場合、以下のように記述します。
"""

l = [0, 3, 1, 10]
for x in l:
	if x < 0:
		print('負の数を探知しました')
		break
else:
	print('負の数は見つかりませんでした')

"""
breakしない場合は最後のメッセージが表示されますが、breakすると最後のメッセージは表示されません。


continue

continueを使用すると、その回の後続処理をスキップすることができます。
以下のサンプルでは数値のリストをループで処理し、printで表示させますが、
マイナスの場合は処理をスキップしています。
"""

l = [0, 3, 1, -10, 11, 6]
for x in l:
	if x < 0:
		print('負の数を探知しました。処理をスキップします。')
		continue
	else:
		print(x)


print("--- Python入門　辞書のループ処理---")


"""
3種類の基本ループ処理

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

d = {'key': 110, 'key2': 270, 'key3': 350}
for key in d:
	print(key)    # key1～key3が出力される
	print(d[key])    # それぞれのkeyに対応する値が出力される


"""
値のループ

辞書に用意されているvaluesメソッドを利用すると、dict_valuesという値のイテレータが得られるのですが、
これを使用すると値でループすることができます。

for文とvalues
for 変数名 in 辞書.values():
    処理

以下のサンプルではvaluesメソッドを使用してループ内で辞書の値を出力しています。
"""

d = {'key': 110, 'key2': 270, 'key3': 350}
for value in d.values():
	print(value)    # 値が出力される


"""
キーと値のループ

辞書に用意されているitemsメソッドを利用すると、dict_itemsというキーと値のイテレータが得られ、
これを使用してキーと値両方でループすることができます。

items
for key変数名, value変数名 in 辞書.items():
    処理

以下のサンプルではitemsメソッドを使用してループ内で辞書のキーと値を出力しています。
"""

d = {'key': 110, 'key2': 270, 'key3': 350}
for key, value in d.items():
	print(key, value)    # キーと値が出力される


"""
ループインデックスを取得する

ここから少し複雑になります。何番目の要素だけは処理をしない、
等の処理を入れたい場合はループインデックスが必要となります。
リストと同様、組込みのenumerate関数を利用することで取得することができます。

enumerateとの組み合わせ
for ループインデックス, key変数 in enumerate(辞書):
    処理

以下のサンプルではループ内で辞書のキーとループインデックスを出力しています。
"""

d = {'key': 110, 'key2': 270, 'key3': 350}

for i, key in enumerate(d):
	print(i, key)    # ループインデックスとキーが出力

"""
また、itemsと組み合わせる場合は、丸括弧でキーと値を囲みます。
for + enumerate + items
for ループインデックス, (key変数, value変数) in enumerate(辞書.items()):
    処理

以下のサンプルではループインデックスと、キー、値をループ内で出力しています。
"""

d = {'key': 110, 'key2': 270, 'key3': 350}

for i, (key, value) in enumerate(d.items()):
	print(i, key, value)    # ループインデックスとkeyと値が出力
