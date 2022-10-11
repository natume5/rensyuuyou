#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- クラスの基本 ---")


"""
前回、オブジェクトとクラスの関係について説明しました。
このページではPythonのクラスの定義方法について説明します。
"""


print("--- クラス定義とインスタンス化 ---")


"""
クラス定義

まずはクラス定義の書き方から説明しましょう。class文を使用します。
後ほど具体的な説明をしますので、
まずはクラスとはこういうものなのだと思ってください。

クラスの定義
class クラス名(継承元クラス名):
    """" クラスのドキュメンテーション """"
    def メソッド1(self, ...):
        処理
        ：

    def メソッド2(self, ...):
        処理
        ：

class文の後にクラス名と継承元クラス名を記述し、
:(コロン)の後に一段落インデントしてブロック内にクラス定義を記述します。
なお、継承元クラス名は省略可能です。
空のクラスを作りたい場合は関数と同様に以下のようにpassを記述します。

class Sample:
    pass


クラスのインスタンス化

次に、クラスからオブジェクトを生成する方法について説明します。
前のページでも解説したとおり、
オブジェクトを生成することをインスタンス化とも呼びます。
以下の文となります。

オブジェクトの生成
変数 = クラス名()
"""


print("--- クラスの構成要素 ---")


"""
クラス定義とインスタンス化について説明しました。
ここから具体例を交えてクラスの構成要素について説明します。
まずは、クラス定義とインスタンス化のサンプルを見てみましょう。
平面座標を表すには2つの数値(x, y)を扱う必要があります。
また、平行移動などもできると便利そうですね。
そういった変数や機能をクラスにひとまとまりにしてみます。
なお、このオブジェクトがもつデータを属性と呼ぶ場合があります。
例えば、オブジェクトOは属性として変数x, yを持つ、といった使い方をします。
"""

class Coordinate:
	""" 座標クラス """

	def __init__(self):
		""" 初期化 """
		self.x = 0
		self.y = 0

	def move(self, x, y):
		""" 平行移動 """
		self.x += x
		self.y += y

	def show_coordinate(self):
		""" 座標を表示する """
		print(self.x, self.y)

	def __str__(self):
		""" 文字列表現を返す """
		return '({0}, {1})'.format(self.x, self.y)

# クラスの利用サンプル
cood = Coordinate()    # インスタンスを生成する
cood.x = 100    # xに代入
cood.y = 200    # yに代入
cood.show_coordinate()    # メソッドを利用する
# 100 200
print(cood)    # 文字列表現を取得する
# (100, 200)

"""
構成要素を確認してみましょう。


インスタンス変数

オブジェクト内部で保持する変数をインスタンス変数と呼びます。
(サンプルコードの6,7行目) インスタンス変数はメンバ変数と
呼ばれることもあります。
Pythonには変数のアクセス修飾子はありません。
基本的にはすべてpubulicであるため、
Javaのように属性毎のgetter、setterの実装はあまり見かけられません。
内部からアクセスする場合は、self.変数名でアクセスします。
(サンプルコードの16行目)
外部からアクセスする場合は、オブジェクト.変数名でアクセスします。
(サンプルコードの25, 26行目)


メソッド

既に用語としての定義はしましたが、
クラスの属性として定義されている関数のことをメソッドと呼びます。
(サンプルコードの14行目)メソッドは必ずselfという引数を持ち、
インスタンス変数を参照する際はself.変数名の書式でアクセスします。


コンストラクタ

インスタンス生成時にクラスに__init__という名前のメソッドが定義されていると、
これが自動的に呼びだされます。
(サンプルコードの4行目)通常、インスタンス初期化処理
（インスタンス変数の初期化など）を記述します。


__str__

オブジェクトの文字列表現を返します。
(サンプルコードの18行目)必ずしも実装する必要はないのですが、
print出力する際に適切な文字列表現があったほうが
開発がスムーズに進むかと思います。
（JavaのtoStringメソッドに相当します。）
"""


print("--- 補足 デストラクタ ---")


"""
生成時に実行される__init__とは逆に、
__del__という名前のメソッドを定義すると、
オブジェクトが削除される際にそのメソッドが自動で実行されますが、
以下の理由より使用は推奨しません。

    いつデストラクタが呼び出されるかわからない
    デストラクタが呼び出される保証がない
    上記理由より予想しない動作をすることがあり、設計が難しい
"""



print("--- Biz.Onlineより ---")
print("--- 【Python入門】クラスの基本を１から解説する―完全版 ---")


"""
Pythonにおけるクラスの定義方法から、
コンストラクタ・メソッド・クラス変数/インスタンス変数まで、
初心者向けに分かりやすく解説します。
このページを理解できれば、
Pythonでクラスを用いて簡単なコーディングができるようになるよう
丁寧に解説します。

オブジェクト指向の基礎がイマイチよくわかっていない方でも大丈夫です。
１から分かりやすく解説していきますので、是非最後までご覧ください。
"""


print("--- Python：クラスの定義方法 ---")


"""
そもそもクラスって何？という方も、
まずはクラスのコーディング方法・構文ルールから学んでいきましょう。
理由としては、コーディングの内容が掴めていない状態で
クラスについての説明を行っても、
クラスが何者であるかを理解することはかなり困難だから。
（これは筆者の体験談です）
そのため、本ページでは「実装方法」⇒「概念」の順に説明します。

まずは、クラスの定義方法です。

クラス定義：構文ルール

class (クラス名称):
　　　クラスの実装①
　　　クラスの実装②
　　　・・・・

class TestClass:
    pass          # pass については以下で解説

「class」に続けて、任意のクラス名を記述すればOK。
これだけでクラスの定義ができます。
尚、クラスの実装内容は、"class" 
よりも１つインデントを下げて記述する必要があります。
（これは、Python共通の仕組みです。
詳細は「Python：基本文法」をご覧ください。）
クラスの命名時に気を付けるポイントは以下の通り。

クラスの命名規約（ PEP8 ）

    クラス名の頭文字は常に大文字で記述する（例：Sample）
    クラス名称が複数ある場合は、常に頭文字を大文字で記載する。
    （例：SampleClassName）
"""


print("--- インスタンスの生成（インスタンス化） ---")


"""
インスタンスの生成（インスタンス化）とは、
クラスからオブジェクトを生成することです。
どういうことか。
クラスは、あくまでも「どのようなものか？を定義した設計書」にすぎません。
クラスとインスタンスを、車で例えると以下のような感じ。

車で例えると・・・？

    クラス　　　　　⇒　設計書
    インスタンス化　⇒　設計書から車を作ること
    インスタンス　　⇒　車

つまり、クラスを定義しただけでは、
まだ実際に「もの」は作られていないということ。
インスタンス化をすることによって、はじめて「もの」が作成されるわけです。
したがってクラスを利用する場合には、
必ずインスタンス化が必要になります。
インスタンスの生成は非常に簡単。
「インスタンス　＝　クラス名()」とするだけ。
"""

class SampleClass1:
	pass

aaa = SampleClass1()    # インスタンス化

"""
これで、クラス"SampleClass1"を基にした実態―インスタンス
 "aaa" が生成されます。
"""

class SampleClass1:
	pass

aaa = SampleClass1()    # インスタンス化
bbb = SampleClass1()    # インスタンス化

"""
上記のように１つのクラスから複数のインスタンスを生成することも可能です。
これでクラスとインスタンスの基本理解はOK。
ここからは、クラスの中身（メソッドやコンストラクタ）について解説していきます。
"""


print("--- Python：メソッド ---")


"""
まずは、メソッドの実装方法。メソッドと言っても、考え方は関数と全く同じ。
クラス内に定義された関数をメソッドと呼んでいるだけです。
"""

# これは「関数」
def sample_function():
	print('Hello World!')

class SampleClass:
	# これは「メソッド」
	def sample_method(self):
		print('Hello World!')

print(sample_function())
# Hello World!

ins = SampleClass()
ins.sample_method()    # Hello World!

"""
関数とは？

複数の処理を１つにまとめて名前を付けたものです。

Pythonでは、def文を用いて関数を定義します。

本ページでは、以下のページで解説している「引数」や「戻り値」
に関する基本知識があると理解が進みます。
ただし、普通の関数とメソッドで１点だけ異なるのが、
メソッドは必ず１つ以上の引数を持つということです。
どういうことか。
構文ルールとサンプルコードを学習しながら、合わせて解説していきます。

メソッドの定義：構文ルール

メソッドの定義

def メソッド名 (self, 引数):
　　　　メソッドの実装①
　　　　メソッドの実装②
　　　　・・・・

メソッドの呼び出し

インスタンス名 .メソッド名()

"""

class SampleClass1:
	def method1(self):
		print('Hello World!')

instance = SampleClass1()     # インスタンス化

instance.method1()    # メソッドの呼び出し
# Hello World!

"""
メソッドを定義する際には、かならず "self" 
という引数を指定する必要があります。
この "self" というのは、インスタンス自身を表す引数で、
必ず１番初めの引数として記述します。
※必ずしも"self"でなければいけないわけではありません。
キーワードは何でもOK（this や myselfなど）。
ただし、Pythonエンジニアの慣例として"self"
と記述することがほぼ決まっています。
他の人でも理解できるように基本"self"と記述するようにしましょう。
この解説だけでは"self"がなにものなのか、
正直まだよくわからない方もいらっしゃるかと思います。
"self" については、初心者向けにもう少し詳しく説明します。


"self" が分からない！という方へ

先ほど "self" はインスタンス自身を表す引数であると説明しました。
これがどういうことかを、実際のコードで説明します。
"""

class SampleClass:
	# メソッド1「引数messageの値を表示する」
	def s_method1(self, message):
		print(message)

	# メソッド2「メソッド1を呼び出す」
	def s_method2(self):
		self.s_method1("Hello World!!")

ins = SampleClass()    # インスタンス化
ins.s_method2()        # メソッドの呼び出し
# Hello World!!

"""
このプログラムを２つに分解してみてみましょう。 まずはこの部分。

    # メソッド１「引数messageの値を表示する」
    def s_method1(self,message):
        print(message)

メソッド "s_method1" では、画面に引数 "message" 
の値を出力する処理を定義しています。
先ほど、解説した通りメソッドには必ず第１引数として、
"self" を指定する必要があるのでした。
次にこの部分。

    # メソッド２「メソッド１を呼び出す」
    def s_method2(self):
        self.s_method1("Hello World!")

メソッド "s_method2" の処理は、先ほど定義した "s_method1" の呼び出し。
引数 "message" には文字列 "Hello World!" を渡しています。
注目していただきたいのがメソッドの呼び出し部分
「self.s_method1("Hello World!")」です。
先ほど解説した通り、メソッドの呼び出し時には
必ずインスタンスを指定する必要があります。
【復習】メソッドの呼び出し方法

メソッドの呼び出し

インスタンス名 .メソッド名()

instance.method1()            # メソッドの呼び出し

ただし、クラスの中ではまだインスタンスが生成されていません。
そのために必要なのが仮のインスタンス名の役割を担う "self" です。
この "self" はこのクラス自身を表しているとも説明できます。
「self.s_method1("Hello World!") 」を日本語に直すと
「このクラスの中の、s_method1を呼び出すよ！」ということ。
これで、なんとなく "self" の意味が分かったのではないでしょうか？
今すぐにはわからなくても、"self" はメソッドを定義する際に必ず
第１引数に指定する必要があると理解しておけばOKです。
"""

class Human:
	def __init__(self, name):
		self.name = name

yamada = Human('山田')
tanaka = Human('田中')
print(yamada.name)    # 山田
print(tanaka.name)    # 田中

"""
ここまでで、クラス・メソッド（self）の理解はOK。次は、コンストラクタについて。
"""


print("--- Python：コンストラクタ ---")


"""
コンストラクタは、オブジェクトが生成される時に一度だけ実行されるメソッドのことです。
基本的には、初期化を目的として利用されます。
基本的にはメソッドの考え方が理解できていればOK。
オブジェクトが生成されるときに実行されるということが
どういうことかが説明できるようになれば、コンストラクタも理解できます。

構文ルール：コンストラクタ

def __init__(self,引数,引数):

コンストラクタは「 __init__ 」という名前で固定です。
init の前後に "_"（アンダーバー）２つです。
"""

class SampleClass():
	def __init__(self):
		self.aaa = 2020
		self.bbb = 'Hello World!'

ins = SampleClass()
print(ins.aaa)    # 2020
print(ins.bbb)    # Hello World!

"""
コンストラクタで、変数 "aaa" と変数 "bbb" を宣言。
その後で、その中身を表示するだけのコードです。
インスタンスが生成される時点で、変数”aaa” "bbb" 
にそれぞれの値を格納しています。
次に、以下のコードをご覧ください。
"""

class SampleClass():
	aaa = 2021        # 変数の初期値　→　2021
	def __init__(self):
		self.aaa = 2020

ins = SampleClass()
print(ins.aaa)    # 2020

"""
結果は「2020」が表示されます。
これは、インスタンスが呼び出された時点で、
自動的にコンストラクタが実行されるためです。
すなわち、変数"aaa"は「2020」で上書きされるのです。
これが、コンストラクタという概念です。簡単ですね。
"""


print("--- Python：デストラクタ ---")


"""
コンストラクタの反対、
インスタンスが破棄されるタイミングで一度だけ呼び出されるメソッドです。
"""

class SampleClass():
	# コンストラクタ
	def __init__(self):
		self.aaa = 2020
		self.bbb = 'Hello World'

	# デストラクタ
	def __del__(self):
		print('さようなら')

ins = SampleClass()
print(ins.aaa)    # 2020
print(ins.bbb)    # Hello World

del ins    # インスタンスの破壊    さようなら
# 2020
# Hello World
# さようなら

"""
「del ins」―。
インスタンスを破棄したタイミングで、デストラクタの処理
「print('さようなら')」の処理が動きます。
そのため、画面に「さようなら」という文字が表示される結果となります。
"""


print("--- クラス内で利用できる変数 ---")


"""
Pythonのクラスの中で利用できる変数は大きく２種類に分解できます。
１つが、クラス変数。もう１つが、インスタンス変数です。


クラス変数

クラス変数は、クラス内で定義する変数のことで、
全てのインスタンスで共通となる変数です。
クラスの定義文直下に記述することで、クラス変数になります。
"""

class SampleClass:
	a = 'Hello World!'    # クラス変数
	def s_method1(self):
		print(self.a)

ins1 = SampleClass()    # インスタンス1
ins1.s_method1()    # 

ins2 = SampleClass()    # インスタンス2
ins2.s_method1()    # 

"""
異なるインスタンス（ins1 / ins2）でも、
同じ「Hello World!」として出力されていることが分かります。


インスタンス変数

インスタンス変数は、クラス変数と異なりインスタンスに依存する変数です。
つまり、インスタンスごとに異なる値になる変数です。
インスタンス変数は、メソッドの直下で "self" の属性として定義します。
"""

class SampleClass():
	# コンストラクタ
	def __init__(self, aaa):
		self.aaa = aaa    # 引数aaaの値をインスタンス変数の初期値とする

ins1 = SampleClass('Hello!')    # 引数aaaに「Hello!」を渡す
print(ins1.aaa)    # Hello!

ins2 = SampleClass('Good Bye!')    # 引数aaaに「Good Bye!」を渡す
print(ins2.aaa)    # Good Bye!

"""
インスタンス変数は、インスタンスごとに異なる値となっていることが分かります。
クラス変数とインスタンス変数の違いは丁寧に理解しておきましょう。
そして最後に「継承」について説明します。
"""


print("--- Python：継承 ---")


"""
継承とは、他のクラスと同じメソッドと
インスタンス変数を持つクラスを定義することです。
既に定義済のクラスの内容を引き継いで新たなクラスを定義するイメージでOK。

構文ルール：継承

class クラス名(継承するクラス名):
　　　　クラスの実装①
　　　　クラスの実装②
　　　　・・・・
"""

class SampleClass:
	a = 'Hello World!'

	def s_method1(self):
		print(self.a)

class Child(SampleClass):    # 「SampleClass」を継承して「child」クラスを定義
	pass

ins = Child()     # インスタンス化
ins.s_method1()    # メソッドの呼び出し     Hello World!   

"""
ハイライト行が継承部分です。
「SampleClass」を継承して「Child」クラスを定義しています。
「Child」クラス自体は、中身はからっぽにしてあります。
ですが、この「Child」クラスは、「SampleClass」を継承しているため、
「SampleClass」のメソッドを備えています。
そのため、画面に Hello World! を表示することができているのです。
復習としてもう１つサンプルコードを載せておきます。
"""

class Human:
	def __init__(self, name):
		self.name = name

class Child(Human):
	pass

yamada = Child('山田')
print(yamada.name)    # 山田

"""
多重継承

Pythonでは、複数のクラスから継承することも可能です。
これを多重継承と呼びます。

構文ルール：多重継承

class クラス名(継承するクラス名1, 継承するクラス名1,・・・ ):
　　　　クラスの実装①
　　　　クラスの実装②
　　　　・・・・

継承したいクラス名を「,（カンマ）」で区切るだけ。
"""

class SampleClass1:         # クラス1
	a = 'Hello World!'

	def s_method1(self):
		print(self.a)

class SampleClass2:        # クラス2
	b = 'Good Bye!'

	def s_method2(self):
		print(self.b)

class Child(SampleClass1, SampleClass2):    # クラス1,2を親としてChildクラスを定義
	pass

ins = Child()
ins.s_method1()    # Hello World!
ins.s_method2()    # Good Bye!

"""
これで、Pythonにおけるクラスの解説は以上です。
以下のコードの意味が分かれば、Pythonにおけるクラス定義の基礎はOK。
"""

class Human:
	def __init__(self, name):
		self.name = name

	def SayHello(self):
		a = 'こんにちは。私は{0}です'.format(self.name)
		print(a)

class Child(Human):
	pass

yamada = Child('山田')
yamada.SayHello()    # こんにちは。私は山田です




print("--- ITCブログより ---")
print("--- 【完全版】Pythonクラスとは？使い方までをわかりやすく解説 ---")


"""
✔このような方へ向けて書かれた記事となります

「Pythonのクラスとは？」

「Pythonのクラスが全然理解できない！」

「Pythonクラスの使いどころが知りたい！」


✔当記事を通じてお伝えすること

    Pythonのクラスとは？例えていうと何？
    Pythonのクラスは何でできてる？
    Pythonクラスの使い方は？

当記事を最後までご覧いただければ、
Pythonのクラスがどんなものかがわかるのはもちろん、
具体例や作り方まで全て理解できます。
"""


print("--- Pythonのクラスって何？ ---")


"""
Pythonは、オブジェクト指向のプログラミング言語です。

オブジェクトとは、「モノ」などと訳すことができ、
プログラミングにおいてはデータや処理の集合体のことをいいます。
つまりオブジェクト指向とは、さまざまなデータや処理の集合体を組み合わせて
一つのシステムを作り上げるプログラミング言語のことをいいます。
このオブジェクトを作るために必ず必要なのがクラスです。
こちらではそのクラスが何なのかをできるだけわかりやすく解説していきます。


Pythonのクラスとは？

Pythonのクラスとは、オブジェクトを作るためのテンプレートです。
例えるなら、

    オブジェクトは、ペッパーくんのようなロボット
    クラスは、そのロボットの設計図

といえるでしょう。

クラス（設計図）では、ロボットの腕・足などパーツや名前・大きさなどの特徴、
その機能を定義します。
オブジェクト（ロボット）は、この設計図を元に作られた一台のロボットです。
プログラミングにおいての具体例を見てみましょう。


Pythonクラスの具体例

Pythonクラスがどんなものかをイメージできるよう具体例を紹介します。
挨拶ロボット（オブジェクト）を作るための設計図（クラス）です。
"""

class Greeting():
	def morning(self):
		print('おはようございます！')

	def evening(self):
		print('こんばんは！')

"""
ロボットの機能（メソッド）は2つです。

    morningメソッドで、「おはようございます！」を出力
    eveningメソッドで、「こんばんは！」を出力

一台のロボット（オブジェクト）を作ってみます。
"""

greeting_robot = Greeting()

"""
挨拶を実行すると以下のとおりになります。
"""

greeting_robot.morning()    # おはようございます！

greeting_robot.evening()    # こんばんは！

"""
詳しい作り方はのちほど解説しますが、なんとなくイメージはつきましたでしょうか。


Pythonクラスのメリットや使いどころは？

Pythonクラスのメリットは、一度設計図を作れば何度でも使い回せることです。
そのため使いどころは以下のような場面になります。

    ゲーム制作
    アプリ制作

一場面や一キャラクターごとに動作を定義するのではなく、
設計図を元にすればいくつでも同じようなオブジェクトが作れるようになります。
当ブログで紹介しているWebアプリ作成のフレームワーク「Django」
も複数のクラスが備わっていて、場面に応じて自由に使えるのが特徴です。
"""


print("--- Pythonクラスの作り方をわかりやすく解説 ---")


"""
具体例をお見せしましたが、ここでは実際の作り方を丁寧に、
わかりやすく解説していきます。

    Pythonクラスの構成
    属性の定義
    メソッドの定義
    属性に動的な値を入れる
    属性の初期値を設定する

ひとつずつご覧ください。


Pythonクラスの構成

Pythonクラスは主に以下の2種類で構成されています。

    属性：ロボットのパーツや特徴
    メソッド：ロボットの機能

属性やメソッドのない空のクラスも作れます。

class Profile():
    pass

新たなクラス「Profile」に属性とメソッドを追加していきましょう。


属性をコンストラクタで定義する

属性は、クラスの特徴やパーツを記録するためにあります。
コンストラクタと呼ばれる特殊なメソッドを使い定義します。
以下のとおりです。
"""

class Profile():
	def __init__(self):
		self.name = 'Yu'
		self.age = 38

"""
コンストラクタは「__init__」関数のことで、属性は、
「self.属性」で定義していきます。

オブジェクトを作ればいつでも属性にアクセスできるようになります。

>>> me = Profile()
>>> me.name
'Yu'
>>> me.age
38

属性の実行には、メソッドに必要な「()」は不要です。


メソッドを定義する

メソッドは、機能を定義するためのものです。
ここでは自己紹介をするメソッドを作りましょう。
"""

class Profile2():
	def __init__(self):
		self.name = 'Yu'
		self.age = 38

	def introduce(self):
		return f'私の名前は{self.name}です。年齢は{self.age}です。'

"""
メソッド「introduce」を実行してみましょう。
"""

me2 = Profile2()
print(me2.introduce())    # 私の名前はYuです。年齢は38です。

"""
※メソッドの実行には、「()」が必要です。


属性に動的な値を入れる

さて、いままでの例だと、どのロボット（オブジェクト）でも名前は「Yu」、
年齢は「38」になってしまいます。
動的に変える方法として、コンストラクタで引数を受け取る方法があります。
Profile2を書き換えてみましょう。
"""

class Profile3():
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def introduce(self):
		return f'私の名前は{self.name}です。年齢は{self.age}です。'

"""
コンストラクタで、引数「name」「age」を受け取り、属性に代入しています。

この場合は引数を設定しないとエラーになります。

>>> me3 = Profile3()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'

必ず引数に値を入れてください。
"""

me3 = Profile3(name='大谷', age=28)
print(me3.name)    # 大谷
print(me3.age)    # 28
print(me3.introduce())    # 私の名前は大谷です。年齢は28です。

"""
属性の初期値を設定する

引数を忘れるたびにエラーが出てしまうのは大変です。
こちらでは初期値を設定しておくことで、
万一引数の設定を忘れてもエラーにならない方法をお伝えします。
"""

class Profile4():
	def __init__(self, name='イチロー', age=48):
		self.name = name
		self.age = age

	def introduce(self):
		return f'私の名前は{self.name}です。年齢は{self.age}です。'

"""
もし引数を設定しなければ自動的に初期値が代入されます。
"""

me4 = Profile4()
print(me4.introduce())    # 私の名前はイチローです。年齢は48です。


print("--- Pythonクラスの使い方 ---")


"""
定義したPythonクラスの使い方や中級者向けの作り方をお伝えします。

    インスタンスを作る
    クラスの属性を確認する
    他クラスを継承する


インスタンスを作る

Pythonのクラスを活用するにはインスタンス化が必要です。
インスタンス化とはオブジェクトを作ること。
以下のように作ります。

インスタンス名 = クラス名()

インスタンス化したうえで属性やメソッドを使えるようになるのです。


クラスの属性を確認する

初めて見たクラスでは、どのような属性やメソッドがあるかわからない場合が多いです。
そんなときは、dirメソッドにインスタンスを渡せば一目瞭然。
"""

me4 = Profile4()
print(dir(me4))

"""
「__」で囲まれているのは、
クラス全てに備わっている隠しメソッドのようなもの。
独自に設定されている属性やメソッドは、
アンダーバーで囲まれていないものになります。


他クラスを継承する

クラスの使い方として、継承はよく使われる方法です。
なぜなら継承を使えば既存のクラスを一から記述することなく、
簡単に拡張できるから。
たとえば、Profile4に新たなメソッド「質問返し」を追加してみます。
"""

class Profile4():
	def __init__(self, name='イチロー', age=48):
		self.name = name
		self.age = age

	def introduce(self):
		return f'私の名前は{self.name}です。年齢は{self.age}です。'

class ExtendedProfile(Profile4):
	def ask_question(self):
		return "あなたの自己紹介をお願いします。"

"""
「クラス名(継承元クラス)」とすることで、
継承元クラスの属性やメソッドを全て引き継ぐことができます。
インスタンスを作り、実行してみましょう。
"""

instance = ExtendedProfile()
print(instance.introduce())    
# 私の名前はイチローです。年齢は48です。
print(instance.ask_question())
# あなたの自己紹介をお願いします。

"""
DjangoなどのWebフレームワークでは多用することになるので、
ぜひ覚えておきましょう。
"""


print("--- まとめ：クラスはオブジェクトの設計書 ---")


"""
当記事の内容をまとめます。

    Pythonのオブジェクトとは、ロボットに例えられる
    Pythonのクラスとは、ロボットの設計書
    Pythonクラスは、属性とメソッドでできている
    Pythonはインスタンス化して使えるようになる

Pythonのクラスは初心者には少しとっつきにくいかもしれません。
ただし一度覚えれば、先人の知恵を借りながらコーディングができる優れもの。
ぜひいろいろと活用し覚えてください。
とくにフレームワークはクラスの塊です。
使い方まで頭に入れておけばスムーズにアプリケーションが作成できることでしょう。
"""



print("--- creiveより ---")
print("--- 【Python初心者】クラス(class)の意味・具体例を分かりやすく説明 ---")


"""
Python初学者にとっての難関がクラス(class)です。

書き方はシンプルですが、
概念がとても難しく雑な理解で済ませてしまう人が多くいます。
その原因は、クラスの意味について調べても、
その定義に難しい言葉(「オブジェクト指向」「インスタンス」)
などを使っていることにあります。
そこでこの記事では、できるだけ難しい言葉を使わず、
クラスとは何なのかをイメージで説明します。
クラスを使いたくなる気持ちに焦点を当てています。
その反面、厳密な定義からは遠ざかってしますがご了承ください
(そのため、Python公式ドキュメントのリンクも紹介しております)。
"""


print("--- Pythonのクラス(class)とは ---")


"""
Pythonの公式ドキュメントでは、classについて以下のように説明しています。

    クラスはデータと機能を組み合わせる方法を提供します。
    新規にクラスを作成することで、新しいオブジェクト 型を作成し、
    その型を持つ新しいインスタンスが作れます。
    クラスのそれぞれのインスタンスは自身の状態を保持する属性を持てます。
    クラスのインスタンスは、その状態を変更するための(そのクラスが定義する)
    メソッドも持てます。
    引用元: 9. クラス -Python公式ドキュメント 

といっても、「オブジェクト型」「インスタンス」「属性」「インスタンス」
などPythonを学習したての人には理解しがたい単語が並んでいます
(他の解説サイトも同じような単語を使っていて混乱する)。
もちろん厳密な説明を行う上では、
上記の難解な言葉の理解が必須になるのですが、
ここではあえてそれらの単語を使わずにイメージをお伝えします。
Pythonのクラスとは、あるデータに必要な情報を持たせる設計図だと思ってください。
具体例をお伝えしましょう。
人間というクラスを作るとします。
すると人間には、どのような要素が必要でしょうか…?
名前・身長・体重・年齢・性別・趣味…などなど。
ここでは、名前・身長・体重・年齢・性別・趣味を人間を構成するのに
最低限必要な情報だとし、これらを含んだ人間クラスをつくります。
ここで、Maoという変数を用意します。
Maoという変数は、プログラミング上ではただの変数であり、
何か1つのデータしか持つことができません。
しかし、このMaoという変数に人間クラスを指定することで、
名前・身長・体重・年齢・性別・趣味などの情報を持たせることができるのです
(つまりMaoという変数が人間扱いされるのです)。
また、人間クラスには動作も指定することができます
(人間の世界でいうと、歩く・寝るなどでしょうか)。
この「何でもなかった変数に人間クラスを指定する」という気持ちを忘れずに、
記事を最後まで読めば、クラスの大まかな概念を理解できるでしょう。
"""


print("--- Pythonのクラス(class)の基本的な定義 ---")


"""
Pythonでは、基本的にclassを以下のように定義します。
class (クラス名):
    def __init__(self):
        (初期化時に行いたい処理)
    (追加の関数)

①classと書く
②クラス名を書く(単語ごとに大文字から始めるのが一般的 e.g.ClassName)
③「:」を書く
④ def _init_(self):を書く(これはクラスを立ち上げたと同時に
  したい処理を書く)
⑤初期化時に行いたい処理を書く
⑥追加の関数があれば書く

これだけの説明では分かりにくいと思うので、具体例をみてみましょう。
ここでは、名前・身長・体重というデータをもつ人間クラスをつくり、
BMIを計算する処理を追加します。
BMIは、体重kg ÷ (身長m)2で計算できます。
"""

class Human:
	def __init__(self):
		self.name = ''
		self.weight = 0.0    # kgで入力
		self.height = 0.0    # mで入力

	def bmi_cal(self):
		self.bmi = self.weight / self.height * 2

"""
これで人間特徴を持った設計図を作ることができました。
それでは、Maoという変数に人間の特徴を持たせましょう。
"""

Mao = Human()    # Maoに人間の特徴(名前・身長・体重)を持たせる

# Maoに具体的な情報を与える
Mao.name = '真央'
Mao.weight = 50
Mao.height = 1.62

# 真央のBMIを算出
Mao.bmi_cal()

# 真央のBMIを出力
print(Mao.name, 'のBMI: ', round(Mao.bmi, 2))    # 小数第３位で四捨五入

# 真央 のBMI:  61.73

"""
ここで押さえておきたいのは、Maoという変数が
「’真央’という名前」や「50という体重」「1.62という身長」を有している点です。
もちろん、同じHumanクラスを用いて、他の人間をつくることもできます。
"""

Yuki = Human()    # Yukiに人間の特徴(名前・身長・体重)を持たせる

# Yukiに具体的な情報を与える
Yuki.name = '有希'
Yuki.weight = 45
Yuki.height = 1.53

# 有希のBMIを算出
Yuki.bmi_cal()

# 有希のBMIを出力
print(Yuki.name, 'のBMI: ', round(Yuki.bmi, 2))    # 小数第３位で四捨五入

# 有希のBMI: 58.82


print("--- Pythonでのクラス(class)と関数の違い ---")


"""
クラスを勉強したばかりでよく思うのが、
「クラスで書いても関数で書いてもあまり変わらないのでは？」ということ。
試しに、上記のMaoのBMIを計算するプログラムを関数で書いてみます。
"""

def bmi_cal(name, weight, height):
	bmi = weight / height * 2
	print(name, 'のBMI: ', round(bmi, 2))

Mao_name = '真央'
Mao_weight = 50
Mao_height = 1.62

bmi_cal(Mao_name, Mao_weight, Mao_height)

# 真央のBMI: 61.73

"""
結果はもちろん同じですが、クラスと関数の違いはどこにあるのでしょうか？

その答えは、‘真央’、50、1.62というデータ間の関係性にあります。
クラスでは同じ人間(Mao)が持つデータとして
名前・体重・身長の間に関係性がありましたが、
関数ではMao_name、Mao_weight、Mao_heightと別の変数で扱っているので、
互いに関係性がありません。
初級の段階ではそのままでも問題はないのですが、
中級・上級になるにつれクラスを使うことでできることが増えてくるので、
今のうちから慣れておきましょう。
(今回は複雑になるので説明しませんが、
意欲のある方は「カプセル化」「継承」「オーバーライド」
などのキーワードを頭の片隅に置いておいてください)。


最後に: クラスは初級のPython学習で最上級に難しい！

クラスは、Pythonの学習を進めていく中でも難しい機能・概念だと思います。
この記事では難しい言葉を使わず説明しました。
より厳密な定義を知りたい方は、
Pythonの公式ドキュメントも併せてお読みくださいね。
"""


print("--- とほほのWWW入門より ---")
print("--- とほほのPython入門 - クラス ---")


"""
クラス(class)

Python の クラス(class)は次のように定義します。
クラス名は慣習的に大文字で始めます。
"""

class Myclass:
	""" A simple example class """    # 三重クォートによるコメント

	def __init__(self):    # コンストラクタ
		self.name = ''

	def getName(self):     # getName()メソッド
		return self.name

	def setName(self, name):    # setName()メソッド
		self.name = name

a = Myclass()     # クラスのインスタンスを生成
a.setName('Tanaka')    # setName()メソッドをコール
print(a.getName())     # getName()メソッドをコール　Tanaka

"""
クラス定義の冒頭には、""""..."""" で ドキュメントストリング 
を記述することができます。
Python

def MyClass:
    """"A sample class""""
    (略)


クラス変数・インスタンス変数(attribute)

クラスは、インスタンス変数 と クラス変数 を持つことができます。
インスタンス変数は「インスタンス.変数名」で表され、
インスタンス毎に独立の変数です。
コンストラクタ __init__(後述)の中で初期化することをお勧めします。
"""

class MyClass:
	def __init__(self):
		self.name = ''    # インスタンス変数

a1 = MyClass()
a1.name = 'Tanaka'

a2 = MyClass()
a2.name = 'Suzuki'

print(a1.name)    # Tanaka
print(a2.name)    # Suzuki

"""
クラス変数は「クラス名.変数名」で表され、
すべてのインスタンスで共通の変数です。
"""

class Myclass:
	PI = 3.14    # クラス変数

print(Myclass.PI)    # 3.14

"""
下記は、クラス変数を用いてインスタンスの個数をカウントアップするサンプルです。
"""

class Myclass:
	count = 0    # クラス変数を初期化

	def __init__(self):
		Myclass.count += 1    # クラス変数をカウントアップ

a1 = Myclass()
a2 = Myclass()
print(Myclass.count)    # 2

"""
クラス変数やインスタンス変数は、動的に追加することができます。
"""

class Myclass:
	pass

a1 = Myclass()
a1.name2 = 'Tanaka'    # インスタンス変数の追加
Myclass.PI2 = 3.141593    # クラス変数の追加

"""
インスタンス変数が存在しない場合、
「インスタンス.変数名」はクラス変数を参照することに注意してください。
「インスタンス.変数名」に値を代入した時点でインスタンス変数が生成され、
以降はインスタンス変数が参照されます。
"""

class Myclass:
	PI =  3.14

a1 = Myclass()
a2 = Myclass()
print(a1.PI)    # クラス変数 Myclass.PI(3.14)が参照される 3.14
a1.PI = 3.141593    # インスタンス変数a1.PIが生成される
print(a1.PI)    # インスタンス変数 a1.PI(3.141593)が参照される 3.141593
print(a2.PI)    # クラス変数 Myclass.PI(3.14)が参照される 3.14

"""
Python では private や protected 
などのスコープを制御する機構は実装されておらず、
クラス変数、インスタンス変数はすべてどこからでも参照可能(public)となります。
"""


print("--- メソッド(method) ---")


"""
クラスが持つ関数は メソッド と呼ばれます。
メソッドもまた、どこからでも参照可能(public)です。
メソッドの第一引数には、クラスのインスタンスを指定し、
第二引数以降で、メソッドの引数を受け取ります。
"""

class Myclass:
	name = ''
	def setName(self, name):    # 第一引数は自インスタンス(self)
		self.name = name

a = Myclass()
a.setName('田中')


print("--- アクセス制限(_, __) ---")


"""
Python では private や protected 
などのアクセス修飾子はサポートされていません。
アンダーバー(_)で始まる変数や関数は
外から参照しないという慣習的ルールがあります。
アンダーバー2個(__)で始まる変数や関数は参照が制限されます。
"""

class Myclass:
	def __init__(self):
		self.name = 'tanaka'
		self._name = 'yamada'
		self.__name = 'suzuki'

	def hello(self):
		print('hello')

	def _hello(self):
		print('hello!')

	def __hello(self):
		print('hellooo!')

a = Myclass()

print(a.name)        # 参照できる    hello
print(a._name)       # 参照できるが慣習的に参照しない    hello!
# print(a.__name)    # 参照できない(AttributeError例外)

a.hello()            # 参照できる
a._hello()           # 参照できるが慣習的に参照しない
# a.__hello()        # 参照できない(AttributeError例外)

"""
とは言っても、__ で始まる変数や関数も、_クラス名__変数名 
に名前変換されるだけで、下記の様にするとアクセスできてしまうそうです。

print(a._MyClass__name)
a._MyClass__hello()
"""


print("--- コンストラクタ(__init__) ---")


"""
__init__() メソッドは、クラスのインスタンスが生成された際に呼び出されます。
コンストラクタ とも呼ばれます。
"""

class Myclass:
	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

a = Myclass('Tanaka')
print(a.getName())     # Tanaka


print("--- デストラクタ(__del__) ---")


"""
__del__() メソッドは、クラスのインスタンスが消滅する際に呼び出されます。
デストラクタ とも呼ばれます。
"""

class Myclass:
	def __init__(self):
		print('INIT!')

	def __del__(self):
		print('DEL!')

a = Myclass()    # INIT!
del a            # DEL!


print("--- 文字列化(__str__) ---")


"""
__str__() は、インスタンスを暗黙的に文字列に変換する際の変換処理を
定義します。
"""

class Myclass:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'My name is ' + self.name

a = Myclass('Yamada')
print(a)             # My name is Yamada


print("--- 継承(inheritance) ---")


"""
他のオブジェクト指向言語と同様、クラスを継承することもできます。
下記の例では、MyClassクラスを継承した、
MyClass2サブクラスを定義しています。
サブクラスでは、親クラスが持つアトリビュートやメソッドを継承して
利用することができます。
"""

class Myclass:
	def hello(self):
		print('Hello!')

class Myclass2(Myclass):
	def world(self):
		print('world')

a = Myclass2()
a.hello()    # Hello!
a.world()    # world

"""
サブクラスでは、親クラスのメソッドを上書き(オーバーライド)することができます。
"""

class Myclass:
	def hello(self):
		print('Hello!')

class Myclass2(Myclass):
	def hello(self):    # 親クラスのhello()メソッドをオーバーライド
		print('Hello!!')

a = Myclass2()
a.hello()    # Hello!!


print("--- 親クラス(super()) ---")


"""
super() は 親クラス を参照します。
第一引数にはクラス、第二引数にはインスタンスを指定します。
下記の例では、サブクラスのコンストラクタの中で、
親クラスのコンストラクタを呼び出しています。
"""

class MyClass1(object):
	def __init__(self):
		self.val1 = 123

class MyClass2(MyClass1):
	def __init__(self):
		super(MyClass2, self).__init__()
		self.val2 = 456

a = MyClass2()
print(a.val1)    # 123
print(a.val2)    # 456


print("--- 多重継承 ---")


"""
Python では多重継承がサポートされています。
下記では、MyClassA, MyClassB 両方を継承する 
MyClassC を定義しています。
"""

class MyClassA:
	def funcA(self):
		print('MyClassA:funcA')

class MyClassB:
	def funcB(self):
		print('MyClassB:funcB')

class MyClassC(MyClassA, MyClassB):    # 多重継承
	pass

a = MyClassC()
a.funcA()     # MyClassAのメソッドも    MyClassA:funcA
a.funcB()     # MyClassBのメソッドも使用できる    MyClassB:funcB



print("--- キノブログより ---")
print("--- 【Python超入門コース】13.クラス｜クラスとは、「データ」と「処理」をまとめたもの【プログラミング初心者向け入門講座】 ---")


print("--- クラスとは？ ---")


"""
クラスにはインスタンスやコンストラクタなどの概念がでてきます。
私自身、プログラミングを勉強し始めたときに、
これを理解するのに時間がかかりました。
私が何冊も書籍を読んで、
こういう順番であれば理解しやすいというプロセスで説明します。
最後まで見ていただければ理解できるかと思うので、最後まで見ていってください。
また、最後に確認問題もありますのでぜひ挑戦してみてください。
まずクラスについて説明します。
クラスとは、「データ」と「処理」をまとめたものになります。
Pythonでは、「データ」のことをアトリビュートといい、
「処理」のことをメソッドといいます。
"""


print("--- アトリビュートとメソッド ---")


"""
アトリビュートは、クラス内で定義された変数のことです。
アトリビュートは、変数と同じように、
数値や文字列を代入したり、参照したりすることができます。
クラスにアトリビュートを作ることを「アトリビュートを定義する」と言います。
アトリビュートと変数の違いは、クラスの中にあるかクラスの外にあるかの違いです。
次にメソッドについて説明します。
前のレッスンで関数は、いろいろな「処理」をまとめて1つにしたものと説明しました。
メソッドも関数と同じで、いろいろな「処理」をまとめて1つにしたものです。
簡単にいうと、メソッドは、クラス内に定義された関数です。
メソッドも関数と同じようにdefで定義します。
まとめると、アトリビュートはクラス内の変数、
メソッドはクラス内の関数ということになります。
"""


print("--- クラスの定義 ---")


"""
クラスを作ることをクラスを定義すると言います。
このレッスンでどんなクラスを定義するか説明します。
クラス名はStudentとします。
そのクラスに生徒の名前を代入する「name」というアトリビュートを定義します。
そして、数学と英語の点数の平均を計算するavgというメソッドを定義します。
コードを書いていきましょう
"""

class Student:

	def avg():
		print((80 + 70) / 2)

"""
まずclassと書いて、次にクラス名を書きます。
今回はStudentというクラス名なので、Student。
クラス名の最初の文字は小文字でも定義はできますが、
最初の文字を大文字にするのは、Pythonの慣習となっています。
クラス名の最初の文字は大文字にしましょう。
コロンを書いて改行です。
"""


print("--- メソッドの定義 ---")


"""
次にメソッドを定義していきます。
数学と英語の点数の平均を計算するメソッドです。
平均を算出するので、平均という意味のaverageを省略して、
avgというメソッド名にします。
まずdefと書いて、メソッド名。
丸括弧を書いて、コロン。改行です。
数学が80点、英語が70点を取れたとして、それらを足して2で割ります。
表示させるためにpirnt関数でくくりましょう。
ここまで見た通り、メソッドは関数の定義のやり方と同じです。
ただし、引数について、メソッドと関数に違うところがあります。
スライドで説明します。
メソッドを定義する場合、必ず1つ引数を記述しなければならないです。
関数の場合は、渡したい引数がない場合、空欄でもよいです。
しかし、メソッドの場合は、
渡したい引数がない場合でも必ず引数が1つ必要になります。
この引数は、どんな引数名でもよいのですが、selfと書くのが慣習です。
つまり、メソッドに渡したい引数がない場合、メソッドの引数にselfを記述します。
メソッドに渡したい引数が1つの場合、
メソッドの引数にselfと渡したい引数名の合計2つ。
メソッドに渡したい引数が2つの場合、
メソッドの引数にselfを含めた合計3つの引数を記述します。
コードを書いていきましょう。
"""

class Student:

	def avg(self):
		print((80 + 70) / 2)

"""
今回はメソッドに渡す引数がないので、引数の記述は、selfのみです。
このselfの役割は、Pythonがプログラムの実行で使っているものです。
理屈が少し複雑なので、メソッドの引数には、
どんな場合でもselfと書くと覚えてしまいましょう。
これでメソッドの定義は終わりです。
クラスを実際に使ってみたいと思いますが、
クラスはこのままでは使うことができません。
クラスは、クラスから作られたインスタンスを変数に代入してから使います。
クラスは、インスタンスになって初めて使えるようになります。
コードを書いて、クラスの使い方を見ていきましょう。
"""

class Student:

	def avg(self):
		print((80 + 70) / 2)

a001 = Student()
a001.avg()    # 75.0


print("--- クラスの使い方（インスタンス化） ---")


"""
数学が80点、英語が70点という点数は、
aという学級の出席番号001番の人が取ったとします。
変数名をa001とします。
イコールを書いて、クラス名を書き、丸括弧を書きます。
これで、クラスを使えるようになりました。
クラスを使えるような状態にすることを
「インスタンス化」「オブジェクト化」「オブジェクト生成」と言ったりします。
インスタンスとは、実体という意味です。
ですから、インスタンス化とは、実体化という意味です。
つまり、インスタンス化とは、クラスという型から、
インスタンスという実際に使える「モノ」を作ることを言います。
変数にインスタンスを代入して、インスタンスとして使えるようになったa001は、
これからa001インスタンスと呼ぶことにします。
次にメソッドの実行方法についてです。
a001にドットをつけて、メソッド名です。
丸括弧も忘れないでください。
それでは実行してみましょう。

実行結果：
75.0


平均点の75点が表示されました。
ここまでは、80点と70点を直接、メソッド内に記述していました。
これだと生徒が変わるごとにメソッドの書き換えが必要です。
これを引数で渡して計算できるようにしましょう。
そうすることで、クラスの書き換えは不要になり、クラスを使い回すことができます。
"""

class Student:

	def avg(self, math, english):
		print((math + english) / 2)

a001 = Student()
a001.avg(80, 70)    # 75.0

"""
クラス内に記述しているメソッドの2番目の引数をmathとします。
3番目の引数をenglishとします。
そのmathとenglishの引数を、print関数のところに記述します。
avgメソッドに80点と70点を渡して実行してみましょう。

実行結果：
75.0

75が表示されました。
"""

class Student:

	def avg(self, math, english):
		print((math + english) / 2)

a001 = Student()
a001.avg(30, 70)    # 50.0

"""
メソッドに渡す引数を30点と70点にしてみましょう。
平均の50が表示されるはずです。
実行してみましょう。

実行結果：
50.0
50が表示されました。
"""


print("--- アトリビュートの定義 ---")


class Student:

	def avg(self, math, english):
		print((math + english) / 2)

a001 = Student()
a001.avg(80, 70)

a001.name = 'sato'
print(a001.name)
# 75.0
# sato

"""
次にアトリビュートについてみていきましょう。
アトリビュートは、クラス内に定義された変数のことです。
a001にドット。アトリビュートを書いて、
値を代入します。
値はsatoさんとしましょう。
これでアトリビュートの定義は終わりです。
print関数で表示させてみましょう。
実行してみましょう。

実行結果：
75.0
sato
メソッドの結果の75とアトリビュートのsatoが表示されました。
"""

class Student:

	def avg(self, math, english):
		print((math + english) / 2)

a001 = Student()
a001.avg(80, 70)

a001.name = 'sato'
print(a001.name)

"""
print(a001.gender)

仮に、性別という意味のgender
というまだ定義していないアトリビュートを表示させてみましょう。
もちろん、定義していないのでエラーになります。
実行してみましょう。
エラーです。
このように未定義のアトリビュートはエラーになります。


class Student:

    def avg(self, math, english):
        print((math + english)/2)

a001 = Student()
a001.avg(80,70)

a001.name = "sato"
print(a001.name)

a002 = Student()
print(a002.name)

また、a002というインスタンス名でインスタンス化をした後に、
nameのアトリビュートを表示させてみましょう。
実行してみましょう。
エラーとなりました。
このようにアトリビュートは、インスタンスごとに存在します。
逆の言い方をすれば、インスタンスごとに、
アトリビュートを定義しなければなりません。
つまり、インスタンスごとにアトリビュートが存在するので、
新しいインスタンスを作るごとに、アトリビュートを定義する必要があります。
そのため、10個インスタンスを作ったとすると、
インスタンスごとにアトリビュートを10個定義する記述をしなければなりません。
先ほどの例でいうと、「a001.name」のような記述をインスタンスごとに10個、
記述しなければなりません。
その不便さを解消するものがコンストラクタです。
"""


print("--- コンストラクタ ---")


class Student:

	def __init__(self):
		self.name = ""

	def avg(self, math, english):
		print((math + english) / 2)

a001 = Student()
a001.name = 'sato'
print(a001.name)    # sato
#     ←空欄

a002 = Student()
print(a002.name)

"""
コンストラクタは、インスタンス化するときに、
自動的に実行されるメソッドのことです。
コンストラクタは、初期化メソッドとも言います。
初期化メソッドは、インスタンス化をすれば、必ず実行されるメソッドです。
そのため、後から使うアトリビュートは、
初期化メソッドで自動的に作っておけばよいのです。
初期化メソッドの記述方法を見ていきましょう。
初期化メソッドもメソッドです。
メソッドなので、まずdefと記述します。
アンダースコアを2つ。initと書いて、もう一度アンダースコアを2つ。
丸括弧を記述します。
メソッドを定義する場合、最初は必ずselfを書くのでselfを記述。
コロンを書いて改行。
これで初期化メソッドの記述は終わりです。
フィールドには、佐藤さん、鈴木さんといったような名前を代入したいので、
nameのアトリビュートを定義しましょう。
self、ドット、nameでアトリビュートを定義することができます。
ちなみに、ここでもselfが出てきました。
selfと書くことにより、selfにインスタンスが代入されます。
引数のselfにa001が代入され、self.nameがa001.nameとなるイメージです。
ここは難しい理屈なので、そういう仕組みになっているのだと思って覚えておきましょう。
ここでは、ダブルクオテーション2つで、空の値を代入させておきましょう。
では、インスタンス化をして、a001とa002のnameの中を見てみましょう。
avgメソッドの記述は消しておきます。
a001にはsatoが、先ほどエラーになったa002には
初期化メソッドでアトリビュートを作ったので、
エラーにならず、空の値が入っているはずです。
実行してみましょう。

実行結果：
sato
エラーにならずに、satoと空の値が表示されました。
"""

class Student:

	def __init__(self):
		self.name = ''

	def avg(self, math, english):
		print((math + english) / 2)

a001 = Student()
a001.name = 'sato'
print(a001.name)    # sato

a002 = Student()
a002.name = 'tanaka'
print(a002.name)    # tanaka

"""
a001にsatoを代入してみましょう。
a002にtanakaを代入してみましょう。
実行してみます。

実行結果：
sato
tanaka
satoとtanakaが表示されました。
"""

class Student:

	def __init__(self, name):
		self.name = name

	def avg(self, math, english):
		print((math + english) / 2)

a001 = Student('sato')
print(a001.name)

a002 = Student('tanaka'
	print(a002.name)

"""
アトリビュートは、インスタンス化と同時に代入することもできます。
初期化メソッドの第2引数にnameという引数を記述します。
ダブルクォーテーションで空を代入していたところに、nameを記述します。
イメージとしては、第2引数のnameを初期化メソッド内のnameが受けて、
それをself.nameに代入します。
では、a001にインスタンス化と同時に"sato"を渡してみましょう。
a002インスタンスにも"tanaka"を渡します。
表示させてみましょう。

実行結果：

sato
tanaka
satoさんとtanakaさんが表示されました。
"""


print("--- クラスの便利なところ ---")


"""
以上がクラスの使い方です。
最後に、クラスの便利なところはどんなところでしょう？
クラスは1度、定義しておけば、後からいくらでもインスタンスを作ることができます。
車を作る「設計図」がクラス、たい焼きを作る「金型」がクラスと表現したりもします。
もう1つ表現するなら、クラスは、パソコンで使うコピペです。
コピペでどんどんインスタンスを作ることができます。
もしクラスがなければ、
生徒ひとりひとりのためにStudentクラスを書かなければいけないので面倒です。
クラスがあるから効率よくプログラミングすることができます。
"""


print("--- 確認問題 ---")


"""
最後に確認問題をやっていきましょう。
このレッスンでは新しい用語がたくさん出てきたので、確認してみましょう。

① a001のことは何と言うでしょうか？
② Student()は何を呼び出しているのでしょうか？
③ def init(self):の部分は何と言うでしょうか？
④ sef.nameは何を定義しているのでしょうか？
⑤ def avg(self, math, english):は何と言うでしょうか？

1がインスタンス
2がクラス
3がコンストラクタ、初期化メソッドとも言います。
4はアトリビュート
5はメソッドです。
"""
