#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説---")
print("--- 繰り返し処理（for文）の書き方 ---")


"""
Pythonのfor文はwhile文と同じ、繰り返し処理をするための構文です。
本記事では「for文の使い方が知りたい」「forとwhileの違いは何？」といったPython初心者、
プログラミング学習者の方へ、for文の使い方を解説していきます。

forの基本的な書き方

ではforの基本的な書き方を見ていきましょう。
といってもfor文は基本的にはwhile文と同じ繰り返し処理なので、
while文との違いについて触れながら使い方を紹介していきます。 
"""


print("--- whileとforの違いは？ ---")


"""
では何が違うかと言うと、for文は「リスト（配列）や辞書などのイテラブルオブジェクトの処理」
に長けていることです。
例を見てみましょう。以下のコードはforを使って「リスト内の文字列を結合して出力」したプログラムです。
"""

list = ['Hello', 'Python', 'World!']
str = ''
for s in list:
	str += s + " "

print(str)    # Hello Python World!

"""
変数listには計3つの文字列が格納されています。
それをfor文で繰り返し処理しています。forの後に続くsは、
繰り返しのたびにリストから値を一つずつ取り出すための変数です。
この変数sを、あらかじめ用意しておいた変数strに文字列結合の演算子で一つずつ結合し、
最後に出力して終了しています。
同じ処理をwhileで書くとどうなるでしょうか？
"""

list = ['Hello', 'Python', 'World!']
i = 0
str = ''
while i < len(list):
	str += list[i] + " "
	i += 1

print(str)    #  Hello Python World!

"""
forの方がコードが分かりやすいかと思います。
このようにforは「イテラブルオブジェクトの処理」に適した繰り返し処理です。
一方whileは「条件に合致する間繰り返し続ける処理」に適しており、
無限ループなどはwhileで利用されることが多いと言えます。

for 変数 in イテラブル:
    # インデント開始(空白)
    命令1
    命令2
    命令3
# インデント終了
"""


print("--- range関数を使った繰り返し処理 ---")


"""
イテラブルオブジェクトを使わずにforを使いたい場合はrangeを使うと簡単に繰り返し処理ができます。
rangeを使うと単なる繰り返しをもう少しアドバンスドな処理にすることが出来ます。
rangeは「与えられた数値から数値の連続を作成する」関数です。使い方を見てみましょう。
"""

for i in range(5):
	print(i)

# 0
# 1
# 2
# 3
# 4

"""
今回は5を引数に渡しており、0〜4までの数値の連続を作成しているので、結果がこのようになっています。
このように、特に処理したいイテラブルはないが、繰り返し処理が必要な場合、
例えば同じ処理を何回何十回と繰り返す場合はrangeを使うと良いでしょう。
"""


print("--- breakとcontinue ---")


"""
forも繰り返し処理なので、while文と同じようにbreakとcontinueが使えます。
"""


print("--- for文におけるbreakの使い方 ---")


"""
実際に使ってみましょう。まずはbreakからです。
"""

list = [1, 2, 3, 4, "5", 6, True, 8]
sum = 0
for i in list:
	if type(i) is int:
		sum += i
	else:
		break

print(sum)    # 10

"""
リスト内の要素を先頭から足していき、int以外の要素に当たったらbreakで処理を抜けています。
listの5番目の要素は文字列の5なので、5番目の要素の前までの数値が全て足され、
10が結果として出力されています。
"""


print("--- for文におけるcontinueの使い方 ---")


"""
つぎにcontinueを見てみましょう。今のプログラムのbreakをcontinueに置き換えてみてください。
"""

list = [1, 2, 3, 4, "5", 6, True, 8]
sum = 0
for i in list:
	if type(i) is int:
		sum += i
	else:
		continue

print(sum)    # 24


"""
今度は24が出力されました。

先ほどはbreakだったので5番目の要素で終わっていましたが、
今回はcontinueなので「リストの中でint型の要素だけを抽出し、足し合わせる」処理に変わっています。
このように、forとbreak、continueを組み合わせると、
イテラブル内の必要な要素のみにフォーカスして処理をすることが可能です。
"""


print("--- forのネスト ---")


"""
最後にforのネストを見ていきましょう。
ネストとは入れ子とも呼ばれ、「forの中にforを書く」ことです。
もう少し分かりやすく言うと、繰り返し処理であるforの中にもう一つ繰り返しのプログラムを書くことであり、
つまり二重、三重のループを発生させるコードということになります。
では例を見てみましょう。
"""
"""
for i in range(3):
	print("外-" + str(i + 1) + "回")
	for j in range(3):
		print("  内-" + str(j + 1) + "回")
"""
# 外-1回
#     内-1回
#     内-2回
 #    内-3回
# 外-2回
#     内-1回
#     内-2回
#    内-3回
# 外-3回
#     内-1回
#     内-2回
#     内-3回

"""
これは「3回繰り返し処理をするforを3回繰り返す」プログラムです。
一見複雑ですが、一つずつ処理を追っていけば、実はそこまで難しくはありません。
まずは外側のforが実行され、「外-1回」が出力されます。次に内側のforが実行されます。
内側のforは単純に3回print()を呼び出すので、「内-1回〜内-3回」を出力します。
終わったら外側のforに移動します。
変数iには次の数値が代入されているので「外-2回」が出力されます。
後は同じ処理を繰り返しているだけです。内側のforが3回実行されたら繰り返しを抜け出し、
処理が終わります。
forのネストはよく使われますが、処理の流れが追いにくいので、
書く場合はどのように処理が流れるのか注視する必要があります。
"""


print("--- ループカウンタも同時に取得する - enumerate() ---")


"""
リストなどのイテラブルをループする際、ループカウンタも同時に取得したい場合はenumerate()を使います。
enumerate()にイテラブルを渡すことで、ループカウンタとイテラブルの要素の2つを返却してくれます。
"""

list = ['Hello', 'Python', 'World!']
for i, s in enumerate(list):
	print("{}, {}".format(i, s))

# 0, Hello
# 1, Python
# 2, World!

"""
また、enumerate()は第二引数に数値を指定することで、
どの数値からループカウンタを返却するかを指定できます。
"""

list = ['Hello', 'Python', 'World!']
for i, s in enumerate(list, 10):    # ループカウンタを10からスタート
	print("{}, {}".format(i, s))


print("--- 複数のリストの要素を同時取得する - zip() ---")


"""
複数のリストやタプルなどのイテラブルを同時にループしながら要素を取得したい場合はzip()を使います。
"""

l_name = ["sato", "suzuki", "tanaka"]
l_score1 = [89, 61, 54]
l_score2 = [77, 91, 82]

for name, score1, score2 in zip(l_name, l_score1, l_score2):
	print("{}\t{}\t{}".format(name, score1, score2))

# sato 	 89 	 77
# suzuki 61 	 91
# tanaka 54 	 82

"""
上記の例では3つのリストの要素を同時に取得しprint()で出力しています。
また、zip()の引数として指定したリストの中で、要素数が少ないリストが存在する場合、
少ない方の要素数を基準にループします。
"""

l_name = ["sato", "suzuki", "tanaka"]
l_score1 = [89, 61]
l_score2 = [77, 91, 82]

for name, score1, score2 in zip(l_name, l_score1, l_score2):
	print("{}\t{}\t{}".format(name, score1, score2))

"""
l_score1の要素が2つしかないので、他2つのリストの要素の内容が削られて出力されました。
もし足りない分の要素を任意の値で埋めたい場合はitertoolsモジュールのzip_longest()を使います。
"""

from itertools import zip_longest

l_name = ["sato", "suzuki", "tanaka"]
l_score1 = [89, 61]
l_score2 = [77, 91, 82]

for name, score1, score2 in zip_longest(l_name, l_score1, l_score2, fillvalue=0):
	# fillvalueで任意の値を指定
	print("{}\t{}\t{}".format(name, score1, score2))

# sato    89      77
# suzuki  61      91
# tanaka  0       82

"""
tanakaさんのスコアが1つ足りない分を0に置き換えるために、fillvalueで0を指定しています。
fillvalueを指定しない場合はNoneになります。


まとめ

以上、for文を使った繰り返し処理の基本的な書き方、break、continue、range、
多重ループについて解説しました。whileとは同じ処理が可能でもメリットや書き方が異なるので、
それぞれの違いを意識しながらプログラムを組むと良いでしょう。 
"""
