#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- Lambda式 ---")


print("--- lambda式とは ---")


"""
lambda(ラムダ)式とは、一時的に利用する無名関数を記述する方法で、
以下の形式で記述します。

lambda式
lambda 引数: 戻り値
サンプルを見てみましょう。
以下のサンプルでは引数xが奇数かどうかを判定した結果を返す関数を
lambda式で記述しています。
"""

func = lambda x: x % 2 == 1

is_odd = func(5)
print(is_odd)    # True

is_odd = func(6)
print(is_odd)    # False

"""
funcには、引数xに対し、
引数xが奇数かどうかを判定した結果を返す関数オブジェクトが格納されます。
わかりづらい方は以下にdefを使った場合と比較してみてください。
"""

def is_odd(x):
	return x % 2 == 1

func = is_odd

is_odd = func(5)
print(is_odd)    # True

is_odd = func(6)
print(is_odd)    # False

"""
簡単な関数だと、lambda式で短く書けることがわかりますね。
"""


print("--- lambda式のメリット ---")


"""
高階関数
では、短く書ける以外にlambda式を使うと何がいいのでしょうか？
そのメリットを説明する前に、高階関数について説明しましょう。
関数オブジェクトのページで説明したとおり、
Pythonの関数はオブジェクトとして扱うことができます。
特に、関数オブジェクトを引数や戻り値にするものを高階関数と呼びます。
高階関数の例
"""

def higher_order(datas, is_target):
	""" 高階関数のサンプル """
	for i in datas:
		if is_target(i):
			print(i)

def is_odd(num):
	return num % 2 == 1

datas = [1, 102, 900, 5, 3]
higher_order(datas, is_odd)
# 1
# 5
# 3

"""
higher_orderは高階関数のサンプルで、
引数で指定されたデータリストに対し、
引数で指定された判定ロジックに該当するデータがあれば
それをprintで出力する関数です。
上記サンプルでは、判定ロジックに「奇数かどうかを判定する関数」を渡しています。
では、「3の倍数かどうかを判定」する場合はどうすればよいでしょうか？
"""

def higher_order(datas, is_target):
	""" 高階関数のサンプル """
	for i in datas:
		if is_target(i):
			print(i)

def is_multipleof3(num):
	return num % 3 == 0

datas = [1, 102, 900, 5, 3]
higher_order(datas, is_multipleof3)
# 102
# 900
# 3

"""
「3の倍数かどうかを判定する関数」を引数に指定しています。
高階関数自身に修正が入らない点にメリットがありますね。

lambda式のメリット
それではいよいよlambda式の使いどころについてです。
もうお気づきの方も多いと思いますが、
高階関数を利用する際の使いきりの関数でわざわざdefで書くのは面倒です。
そこで、上の高階関数をlambda式で書きなおしてみましょう。
"""

def higher_order(datas, is_target):
	""" 高階関数のサンプル """
	for i in datas:
		if is_target(i):
			print(i)

datas = [1, 102, 900, 5, 3]
higher_order(datas, lambda x: x % 2 == 1)

"""
いかがでしょうか。
関数を短く書けた上、使い捨ての小さい関数がなくなったため、
全体的にスッキリして本筋が読みやすくなったのではないでしょうか？
"""



print("--- HEADBOOSTより ---")
print("--- Pythonのlambda（ラムダ）式の書き方と使い方まとめ ---")


"""
lambda（ラムダ）式は、「無名関数」という名前のない関数を作るための式です。
しかし、通常、関数を作るにはdef文があるため、
lambdaが何のためにあるのか分からないという方も多いでしょう。
結論から言うと、lambdaは、sorted()関数やmap()関数、
filter()関数など、引数に関数を受け取る関数を使うときに、
簡潔なコードを書くために使います。
これについて詳しく解説していきます。
"""


print("--- 1. lambda（ラムダ）とは ---")


"""
lambda（ラムダ）は、「無名関数」と呼ばれます。
その名の通り、関数名をつけずに、簡潔に関数を作成するために使う構文です。
lambdaの基本書式は次の通りです。

In [ ]:
lambda 引数1, 引数2, ..., 引数n : 式

このように、lambdaと書いて、「これからlambda式を書きますよ」
とPythonに宣言してから、その右側にまず引数を書き、
コロン( : )で区切ってから、関数定義の処理文を書きます。
通常、独自関数を作成するにはdef文を使います。
見比べるために、次のコードでは、
引数に渡した数値を二乗するsquare()関数をdef文で作っています。
"""


"""def文で関数を作ります。"""
def square(n):
	return n ** 2

"""関数を実行します。"""
print(square(3))    # 9

"""
これと同じものをlambdaで書くと、次のようになります。
"""


"""lambda式で同じ関数を作ります。"""
square = lambda n: n ** 2

"""関数を実行します。"""
print(square(3))    # 9

"""
簡単ですね。

なお、このコードでは、lambda式を変数squareに代入しています。
lambda式を代入して変数は関数オブジェクトとなり、
通常の独自関数として使うことができます。
ただし、PythonのPEP8というコーディングのルールでは、
lambdaを変数に代入して使うことは推奨されていません。
"""


print("--- 2. lambdaはどういう時に使う？ ---")


"""
それでは、lambdaはどのような時に使うのでしょうか。
それは関数の引数に関数を渡したい時です。
Pythonにおけるプログラミングの現場で、このような使い方をもっとも目にするのは、
sorted()関数、map()関数、filter()関数を使う時です。
それぞれ見ていきましょう。


2.1. sorted()関数とlambda
sorted()関数は、リストなどのイテラブルの要素をソートする関数です。
sorted()関数は、キー引数で関数を渡すと、
その関数で定義されているルールの通りに並び替えることができます。
例えば、以下のリストに対して、キー引数を指定せずにsorted()関数にかけると、
通常の並び替え法則（内側のタプルの最初の要素を数値昇順）
にしたがってソートされます。
"""

list = [(0, 5), (2, 3), (1, 4), (3, 2), (5, 0), (4, 1)]
print(sorted(list))
# [(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)]

"""
この時、もし、通常の並び替え法則の通りではなく、
内側のタプルの二番目の要素を数値昇順でソートしたい場合は、
キー引数にlambda式を渡すことで実現することができます。
"""

print(sorted(list, key=lambda x: x[1]))
# [(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)]

"""
なお、sorted()関数だけでなく、
sort()メソッドでも同じようにキー引数を渡すことができます。


2.2. map()関数とlambda
map()関数は、イテラブルの全ての要素に指定の関数を適用して返すものです。

次のように書きます。

map(関数, イテラブル)
これは例えば、既にある数値のリストの各要素を二乗したものが欲しい、
だけど、符号はそのままにしておきたい、など少しひねった操作をしたい時に使います。
def文で関数を作ってから、map()関数でイテラブルを操作するとしたら、
次のように書きます。
"""

"""
nums = [0, -1, 2, -3, 4, -5]

def square(n):
	if n > 0:
		return n ** 2
	else:
		return n ** 2 * -1

new_nums = map(square, nums)
# [0, -1, 4, -9, 16, -25]
print(list(new_nums))
"""



print("--- AVILEN AI Trendより ---")
print("--- Python入門 全人類がわかるlambda(ラムダ)式 ---")


"""
Pythonの文法の中でも少し発展的な内容のlambda(ラムダ)式は、
正直に言って無理して使う必要のない記法でもあります。
(((((しかし高校生にとってブラックコーヒーが飲めることがステータスになったように、
Python初心者にとってlambda(ラムダ)式を書けるようになることは
一つのステータスになるのではないでしょうか))))))
今回はそんなlambda(ラムダ)式のメリットや使い所、表記について解説していきます！
"""


print("--- lambda(ラムダ)式とは ---")


"""
そもそもlambda(ラムダ)式とは、無名関数と呼ばれる関数を書くための記法になります。
数字と演算子を使って書いたものが数式と呼ばれるように
lambda(ラムダ)式記法を使って書いたものが無名関数と呼ばれます。
正直細かいところはどうでもいいので、
無名関数とlambda(ラムダ)式は関係あるんだなぁ～くらいの認識でいてください。


lambda(ラムダ)式はいつ使う？

lambda(ラムダ)式が使えると、ちょっとした処理を一行でまとめて書くことが出来ます。
名前付きの関数を１つ定義するのは面倒くさいけど、
対象に処理を加えたいときに使います。
例えば「このリストだけ要素を二乗したいなぁ～」
なんていう時はまさにlambda(ラムダ)式の出番です。


lambda(ラムダ)式の書き方

lambda(ラムダ)式の基本的な書き方は次のようになっています。

lambda 引数1,引数2...: 処理

例えばこんな感じです。

 lambda a,b: a+b

lambda(ラムダ)式の引数に値を渡したい時は次のように書くことで値を渡せます。

(lambda 引数:処理)(渡す値)　#①

#実際に書いてみるとこんな感じ。(見にくくなるのでprint()は省略します) 
"""

print((lambda a, b: a + b)(1, 99))    # 100

"""
もしくはlambda(ラムダ)式ごと変数に渡してあげてから値を渡すことも出来ます。

func = lambda 引数1,引数2...: 処理 #②
print(func(渡す値))
#実際に書いてみるとこんな感じ。(見にくくなるのでprint()は省略します)
"""

func = lambda a, b: a + b
print(func(1, 199))    # 200


print("--- lambda(ラムダ)式を用いた演習 ---")


"""
折角なのでlambda式を使っていくつか演習をしてみましょう！
1,変数gretに文字列”Hello”を格納して、Worldと結合させて出力せよ。
2,変数num1とnum2に数字3と9を格納して、
それぞれを二乗した後にそれらを加算して出力せよ。
3,任意の数字を格納した変数xが偶数なら”True”、奇数なら”False”を出力せよ。

Hello World #1問目
90 #2問目
True #3問目 x = 6の時
"""

# 1
gret = 'Hello'
gret2 = ((lambda gret: gret + 'World')(gret))
print(gret2)

# 2
num1 = 3
num2 = 9

num3 = ((lambda num1, num2: num1 ** 2 + num2 ** 2)(num1, num2))
print(num3)

# 3
x = 2

print((lambda x: x % 2 == 0)(x))


print("--- 高層関数とは ---")


"""
高層関数とは、”引数に関数を取る関数“です。
例としてmap関数やfilter関数があります。
map関数はリストの全ての要素に関数処理を適用してくれる関数です。
filter関数はリスト全ての要素に関数処理を適用し、
Trueのものだけを返してくれる関数です。
どちらもリストの全ての要素に対して関数処理を適用してくれるところがとても便利です。
高層関数の別の記事で詳しく説明します！


lambda(ラムダ)式と高層関数

高層関数は引数に関数を取るため、
何かしらの処理をする関数を引数として渡すことが出来ます。
もちろん普通の関数を引数として渡すことも出来ますが、
lambda(ラムダ)式で書いた無名関数を引数として渡してあげると
とても綺麗に書くことが出来ます。！
[演習] list_1 = [0,1,2,3,4,5,6,7,8,9] の全ての要素を2乗して、
新たにlist_2に格納してください。
※比較のため普通に関数を定義した場合と
lambda(ラムダ)式を用いた場合の2通り書いてください
"""

"""
l_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l_2 = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 普通に関数定義した場合
l_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def squr(x):
	xx = x ** 2
	return xx

eq1 = map(squr, l_1)
print(list(eq1))

"""
"""
#lambda(ラムダ)式を用いた場合

eq2 = map(lambda x: x ** 2, range(10))
print(list(eq2))    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
"""
"""
このようにlambda式と高層関数を組み合わせると
コードの行数を大幅に省略することが出来ました。
※コードは行数を減らせばいいというものでもないので、
見やすさ重視で書いてください。


lambda(ラムダ)式とfor文

lambda(ラムダ)式でfor文を書くのはどうすればよいのでしょうか？
lambda(ラムダ)式は一行で処理を書く必要があるため
lambda(ラムダ)式の中にfor文を書くことは出来ません。
複数行に渡ってlambda(ラムダ)式の中の処理を書きたい場合は、
普通に関数定義して書きます。
しかし、for文のような動作をするコードを書くことは出来ます！
そう！お気づきの通りmap関数とlambda(ラムダ)式の組み合わせです。
先ほどの演習１の問題をもう一度見てみましょう！

[演習] list_1 = [0,1,2,3,4,5,6,7,8,9] の全ての要素を2乗して、
新たにlist_2に格納してください。

先程はこれを関数定義やlambda(ラムダ)式で書きましたが、
for文で書くことも出来ます。
"""
"""
list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 普通に関数定義した場合

def squr(x):
	xx = x ** 2
	return xx

eq1 = map(squr, list_1)
print(list(eq1))    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
"""
# lambda式を用いた場合

"""
eq2 = map(lambda x: x ** 2, range(10))
print(list(eq2))    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

"""

# for文で書いた場合

list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = []

for i in list_1:
	square = i ** 2
	list_2.append(square)
print(list_2)    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

"""
lambda(ラムダ)式とIf文

lambda(ラムダ)式を使ってif文を書くことは出来ます。

lambda 引数1,引数2...: 処理

lambda(ラムダ)式の基本的な書き方の処理の部分にif文を加えるだけです。
この時、if文を含む処理の部分には三項演算子という記法を使って書きます！

#三項演算子
lambda 引数1,引数2...:(条件がTrueのときの値) if (条件) else (条件がFalseのときの値)

この三項演算子とlambda(ラムダ)式を組み合わせることで、
一行でif文を書くことが出来ます！
演習をしてみましょう！

[演習]与えられた数字の偶数か奇数を判定するプログラムを作りましょう。

この演習をlambda(ラムダ)式を使って解答してください！
lambda(ラムダ)式を使わない場合の解答は次のようになります。
"""

def even_odd(i):
	if i % 2 == 0:
		print('偶数です')
	else:
		print('奇数です')

even_odd(10)    # 偶数です

"""
いかがでしょうか？
解答例は次のようになります！
"""

even_odd_lambda = (lambda x: '偶数です' if i % 2 == 0 else '奇数です')
print(even_odd_lambda(5))    # 奇数です

"""
さて、これでlambda(ラムダ)式を使ってfor文とif文を書けるようになりました。
最後に総復習できる演習問題をやってみましょう。
"""


print("--- 演習問題 ---")


"""
lambda(ラムダ)式とif文とfor文を組み合わせた問題
[演習] lambda式を使って list_1 = [0,1,2,3,4,5,6,7,8,9,10] 
の全ての要素について偶数か奇数か判定して、その結果をlist_2に格納してください。

['偶数です', '奇数です', '偶数です', '奇数です', '偶数です', '奇数です', '偶数です', '奇数です', '奇数です', '偶数です']

いかかがでしょうか？
この問題ではlambda式とmap関数とif文とfor文と
三項演算子とリスト化の知識を使います！

解答は次のようになっています！
"""

list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
# どうしても一行で書きたかったコード
list_2 = list(map(lambda x: "偶数です" if x % 2 == 0 else "奇数です"), list_1)
"""
"""
# 見やすくなったコード
func = (lambda x: "偶数です" if x % 2 == 0 else "奇数です")
l_2 = list(map(func, list_1))
print(l_2)
"""

"""
以上がlambda(ラムダ)式の説明となります！
ちょっとした関数処理を加える時にちょうどいい記法なので、
適材適所で活用していきましょう
"""









