#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- クラスメソッドとスタティックメソッド ---")


print("--- クラスメソッド ---")


"""
クラスメソッドはメソッド内で「クラス自身」を参照することができるメソッドです。
メソッドの第1引数にはそのクラス自身をclsという名前で指定します。
第2引数以降は通常の引数となります。
クラスメソッドを利用するには
組込みのデコレータである@classmethodを利用します。
また、クラスメソッドを呼び出す場合は以下の通り
クラス名とクラスメソッドをドットでつなぎます。

クラスメソッドの呼び出し
クラス名.クラスメソッド(引数)

それではサンプルです。
"""

"""
class Coordinate:
	"""" 座標クラス """"

	def __init__(self, x, y):
		"""" 初期化 """"
		self.x = x
		self.y = y

	def show_coordinate(self):
		"""" 座標を表示する """"
		print(self.x, self.y)

	@classmethod
	def create_origin(cls):
		"""" Coordinateオブジェクトを生成して返す """"
		origin = cls(0, 0)    # 原点の座標を生成して返す
		return origin

# クラスからクラスメソッドを使用する
cood = Coordinate.create_origin()
print(cood.show_coordinate())

# オブジェクトを生成してクラスメソッドを使用する
cood2 = cood(10, 20)
cood3 = cood2.create_origin()
print(cood3.show_coordinate())
"""

"""
上のコードは平面座標を表すCoordinateというクラスを実装しています。
初期化時にx, y座標をしていしますが、
それとは別に13行目～17行目で実装したcreate_origin
というクラスメソッドを使用すると原点座標を得ることができます。
create_originでは引数にclsがあるため、これを利用しています。
また、20行目以降で実装したクラスメソッドを呼び出しています。
また、クラス変数と同様クラスメソッドは
インスタンス化したオブジェクトからもアクセスすることが可能です。
（24行目以降）
"""


print("--- スタティックメソッド ---")


"""
スタティックメソッドはクラスに属しますが、そのクラスに依存しなメソッドです。
つまり、スタティックメソッドはメンバにアクセスすることができません。
また、このことから引数のselfやclsは不要となります。
スタティックメソッドを実行する際は、クラス名.スタティックメソッド名で記述します。
クラスメソッドを利用するには組込みのデコレータである
@staticmethodを利用します。
"""

import math


class Coordinate:
	""" 座標クラス """

	def __init__(self):
		""" 初期化 """
		self.x = 0
		self.y = 0

	def show_coordinate(self):
		""" 座標を表示する """
		print(self.x, self.y)

	@staticmethod
	def calc_dist(cood1, cood2):
		""" 座標間の距離を計算します """
		x = cood1.x - cood2.x
		y = cood1.y - cood2.y
		return math.sqrt((math.pow(x, 2) + math.pow(y, 2)))

cood1 = Coordinate()    # インスタンスを生成する
cood1.x, cood1.y = 100, 100

cood2 = Coordinate()    # インスタンスを生成する
cood2.x, cood2.y = 200, 200

dist = Coordinate.calc_dist(cood1, cood2)
# スタティックメゾットを実行
print(dist)    # 141.4213562373095

"""
例えば上のサンプルでは、座標クラスに座標間の距離を計算する
メソッドを実装していますが、オブジェクトの状態に依存する機能ではないため、
スタティックメソッドとして実装されています。
このように、スタティックメソッドの挙動としては
クラスに属さないただの関数と同じなのですが、
なんらかの方針で関数をクラスに属させたい場合に使用します。
"""



print("--- CodeGraffitiより ---")
print("--- 【Python入門】クラス変数とクラスメソッド、スタティックメソッド ---")


"""
Pythonのクラスにまつわる話題を色々と学んできましたが、
ここではクラス変数とクラスメソッド、スタティックメソッド（静的メソッド）
について扱います。
クラス変数は、クラス定義の中に通常の変数と同じように定義された変数です。
クラスメソッド、スタティックメソッド（静的メソッド）
は通常のメソッドとは違う性質があるのでここで見ていきたいと思います。
"""


print("--- クラス変数 ---")


"""
ではクラス変数について扱っていきましょう。簡単なコードでやっていきます。
次のようなクラスを作って、オブジェクトを呼び出してみます。
"""

class Bird():
	def __init__(self, name):
		self.kind = '鳥類'
		self.name = name

	def whats_bird(self):
		print(self.name, self.kind)

duck = Bird('アヒル')
duck.whats_bird()    # アヒル 鳥類
crow = Bird('カラス')
crow.whats_bird()    # カラス 鳥類

"""
Birdクラスの中に初期化メソッドを定義して、
種類を示すkindという変数に「鳥類」という値を持たせます。
もう一つ、引数としてnameを定義します。
そしてwhats_birdというメソッドを作って名前と種類を表示させる
コードにしています。
「アヒル」と「カラス」を入れてインスタンス化してそれぞれ呼び出してみます。

それぞれ与えた名前と、種類が呼び出されています。
これは特に問題無い話だと思います。
ここでは、self.kind = “鳥類” がどちらにも共通しています。
これをクラス変数としてコードを書き換えるとこうなります。
"""

class Bird():
	kind = '鳥類'    # クラス変数

	def __init__(self, name):
		self.name = name

	def whats_bird(self):
		print(self.name, self.kind)

duck = Bird('アヒル')
duck.whats_bird()    # アヒル 鳥類
crow = Bird('カラス')
crow.whats_bird()    # カラス 鳥類

"""
共通した部分をメソッド定義の中から取り出して、
クラスのブロック定義の部分に持って行き、selfをつけずに変数として定義します。
これがクラス変数です。

結果は先ほどと同じになります。
duckもcrowも別々のオブジェクトですが、
クラス変数の値の「鳥類」はどちらにも使われています。
このように、クラス変数は全てのオブジェクトの中で共有されるのが特徴です。
"""


print("--- クラスメソッドとスタティックメソッド ---")


"""
今度はクラスメソッドとスタティックメソッドについて見ていきましょう。
上で使ったコードをもっと単純にして次のように変えてみました。
"""

class Bird():
	kind = '鳥類'

	def __init__(self):
		self.name = 'カラス'

bird1 = Bird()
print(bird1)    # <__main__.Bird object at 0x00000247FA102400>
bird2 = Bird
print(bird2)    # <class '__main__.Bird'>

"""
クラス変数と、初期化したnameに値が与えられているだけです。
これをコードのようにクラスの丸括弧()をつけた場合と、
つけない場合で呼び出してみるとこうなります。

丸括弧をつけた上側はオブジェクトになっていますが、下側はクラスのままです。
そこで、次のようにnameを呼び出してみます。
"""

class Bird():
	kind = '鳥類'

	def __init__(self):
		self.name = 'カラス'

bird1 = Bird()
print(bird1.name)    # カラス
bird2 = Bird
"""
print(bird2.name)    # AttributeError: type object 'Bird' has no attribute 'name'

するとこうなります。
オブジェクト化された上側は結果が表示されていますが、
下側は初期化メソッドが実行されていないので、
nameの属性が読み込まれません。
次はこのクラスのクラス変数にアクセスしてみます。
"""

class Bird():
	kind = '鳥類'

	def __init__(self):
		self.name = 'カラス'

bird1 = Bird()
print(bird1.kind)    # 鳥類
bird2 = Bird
print(bird2.kind)    # 鳥類

"""
このようにクラス変数は、オブジェクト化しなくても呼び出すことができました。
今度は同様にクラス変数を呼ぶのですが、
クラス変数を呼び出すメソッドを定義したコードを作ってみます。
"""

class Bird():
	kind = '鳥類'

	def __init__(self):
		self.name = 'カラス'

	def whats_bird(self):
		print(self.kind)

bird1 = Bird()
bird1.whats_bird()    # 
bird2 = Bird

"""
bird2.whats_bird()    # TypeError: whats_bird() missing 1 required positional argument: 'self'


こちらも丸括弧をつけた場合と、つけ無い場合とで
メソッド内のクラス変数を表示させてみるとこうなります。

先ほどは呼ぶことができていたクラス変数も、メソッドで呼び出す形にしてしまうと、
オブジェクト化して無ければ呼ぶことができません。
"""


print("--- @classmethodとcls ---")


"""
こういう時に、これを表示させるにはクラスメソッドを利用します。
それには@classmethodとclsを使います。clsはclassの意味です。
上のコードを次のように書き換えます。
"""

class Bird():
	kind = '鳥類'

	def __init__(self):
		self.name = 'カラス'

	@classmethod    # デコレータを入れる
	def whats_bird(cls):    # selfの代わりにcls
		print(cls.kind)    # selfの代わりにcls

bird1 = Bird()
bird1.whats_bird()    # 鳥類
bird2 = Bird
bird2.whats_bird()    # 鳥類

"""
メソッドに@classmethodというデコレータを入れて、
自分を示すselfの代わりにクラスを示すclsをを使います。

先ほどオブジェクト化されずに表示できなかったクラス変数も、
こちらでは表示することができています。
次のようにしても、どちらもアクセスすることができます。
"""

Bird.whats_bird()    # 鳥類
print(Bird.kind)    # 鳥類

"""
このように、クラスメソッドを使えば、
オブジェクトを作らなくてもメソッドにアクセスすることができるのです。
"""


print("--- @staticmethod ---")


"""
次は静的メソッド（スタティックメソッド）を見ていきましょう。
デコレータの@staticmethodを使っていきます。
上のコードに一つメソッドを次のように加えます。
"""

class Bird():
	kind = '鳥類'

	def __init__(self):
		self.name = 'カラス'

	@classmethod
	def whats_bird(cls):
		print(cls.kind)

	@staticmethod    # デコレータを付けます
	def whatch(times):    # 引数は特に必要なく、selfは使いません。
		print('今日は{}回、飛んでいるのを見ました！'.format(times))

Bird.whatch(10)    # 今日は10回、飛んでいるのを見ました！

"""
watch()というメソッドを用意しました。スタティックメソッドを作るには、
デコレータの@staticmethodを付けます。
クラスに定義するメソッドには引数にかならすselfを入れますが、
静的メソッドを作る時には必要ありません。clsも必要ありません。
ここでは回数を使う為にtimesを引数に用意してみました。
10を引数に入れて呼び出しています。

呼び出しが実行されて表示されているのがわかります。
このスタティックメソッドは、クラスの中の他のデータにアクセスしないので、
デコレータの@staticmethodを外して、
クラスの外に関数定義を置いてそのまま利用しても同じ動きを得ることはできます。
ただ、他のコードとの違いとこのクラスとの関連性を考えて
スタティックメソッドとして利用していますが、
あまりスタティックメソッドとしてコードを書く機会は少ないとも言われています。
こういう書き方があるということだけ頭に入れておきましょう。
"""


print("--- まとめ ---")


"""
Pythonのクラス変数は、クラス定義の中でのグローバル変数のような動きをします。
クラス変数は全てのオブジェクトの中で共有されるのが特徴です。
selfを付けずに定義します。
クラスメソッドはデコレータとして@classmethodと、
selfの代わりにclsを使って定義します。
クラスメソッドを利用すると、オブジェクトを作らなくてもアクセスすることができます。
スタティックメソッドは、デコレータに@staticmethodを付けて定義します。
引数にselfは必要ありません。そのまま実行できます。
"""



print("--- commteblog ---")
print("--- Python : クラスの使い方 4（クラスメソッド、スタティックメソッド、クラス変数） ---")


"""
クラス変数やクラスメソッドは、クラスオブジェクトの属性なので、
インスタンスを生成することなくアクセスできる。
スタティックメソッドも、インスタンスを生成することなくアクセスできるが、
インスタンス変数やクラス変数にはアクセスできない。
"""


print("--- ポイント ---")


"""
クラスメソッドの特徴

    処理を追加する機能を持つ
    クラス全体に影響を与える
    インスタンス変数にはアクセスできない
    インスタンス生成せずにアクセス可能
    @classmethod デコレータを付加する
    第一引数は cls と記述

スタティックメソッドの特徴

    インスタンス生成せずにアクセス可能
    インスタンス変数やクラス変数にはアクセス不可
    @staticmethod デコレータを付加する
    第一引数は self や cls を取らない

クラス変数の特徴

    クラスオブジェクトに紐づき、クラス全体で共有される
"""


print("--- デコレータとは ---")


"""
デコレータとは、関数やクラスの前後に処理を追加する機能のこと。
先頭に @ がつく。クラスメソッドは、デコレータの一種である。

Python において、メソッドは次の 3 つのタイプがある。
インスタンスメソッドはデコレータがついてないが、それ以外はデコレータがついている。

各 メソッドの違い
メソッドのタイプ 	    デコレータ 	      第一引数
インスタンスメソッド 	  なし 	        self
クラスメソッド 	  @classmethod 	    cls
静的メソッド 	  @staticmethod 	オブジェクト以外
"""


print("--- クラス変数 ---")


"""
クラス変数は、クラスオブジェクトに紐づく変数である。
クラス全体のインスタンスで同じ変数が共有される。
"""

class Hoge:
	a = 'Hellooo!'

print(Hoge.a)    # Hellooo!


print("--- クラスメソッド ---")


"""
クラスメソッドはクラス全体に影響を与え、クラスに加えた変更は、
すべてのオブジェクトに影響を与える。
"""

class Hoge:
	@classmethod
	def a(cls):    # クラスメソッド
		print('Hellooo!')

print(Hoge.a())
# Hellooo!
# None

"""
デコレータである @classmethod を入れると、
その次のメソッドはクラスメソッドになる。
このとき、メソッドの第一引数（cls）はクラス自体となる。
第一引数は、self でなく cls とする。
呼び出しは、クラス.メソッド(引数)とする。
次に示すコードは、クラス変数、クラスメソッドを使った例である。
クラス変数である class_val は、
クラス全体のインスタンスで同じ変数が共有されている。
"""

class Python():
	class_val = 1

	def __init__(self, val):
		self.instance_val = val

	def instance_method(self):
		print(self.class_val, self.instance_val)

	@classmethod
	def class_method(cls):
		print(cls.class_val)

# インスタンスメソッド呼び出し
P = Python(10)
P.instance_method()    # 1 10

# クラスメソッド呼び出し
print(Python.class_val)    # 1


print("--- スタティックメソッド ---")


"""
スタティックメソッドも、インスタンスを生成することなくアクセスできるが、
インスタンス変数やクラス変数にはアクセスできない。
スタティックメソッドを定義する場合は、@staticmethod デコレータを入れる。
静的メソッドとも呼ばれる。このメソッドは、オブジェクトを作らずに実行可能である。
"""

class A:
	@staticmethod
	def s():
		print('static')

	@classmethod
	def c(cls):
		print('class')

A.s()    # static
A.c()    # class




print("--- りっぱなパセリは突っ走るより ---")
print("--- Python classmethodとstaticmethodを使う意味を考える  ---")


"""
Pythonのclassについて学んでいくと、
インスタンスメソッドだけでなくクラスメソッドとスタティックメソッド
なるものの存在に出会います。
これらの実装方法についてはいろんな記事で紹介されていますし、
実装自体はデコレータを一つ書くだけで簡単なので、使うだけならすぐに使えます。
ただ、なぜわざわざこれらを使い分けるのか？
についての記事には出会ったことがありませんでした。
ずっと疑問だったclassmethodとstaticmethodの使い分けについて、
そもそもなぜ使い分ける必要があるのか？なんのメリットがあるのか？について、
ようやく自分の中で腑に落ちてきたので気持ちをメモしておきたいと思います。
"""


print("--- classmethodとstaticmethodとは ---")


"""
軽くおさらいしておきます。

classmethod

クラスメソッドです。以下の様に@classmethodをクラス関数につけるだけです。
慣習で第一引数を普段使うselfではなく、clsと書きます。
"""

class MyClass:
	CLASS_PArAM = 100

	def __init__(self, instance_param):
		self.instace_param = instance_param

	@classmethod
	def method(cls):
		print(cls.CLASS_PARAM)
		# print(cls.instance_param) これはできない

"""
関数内ではインスタンス変数にはアクセスできませんが、
クラス変数にはアクセスができます。
また、他のクラスメソッドやスタティックメソッドにもアクセス可能です。
要するにインスタンス変数に用事がない場合に使用できます。


staticmethod

スタティックメソッドです。
インスタンスメソッドやクラスメソッドと異なり、指定される第一引数はなく、
必要な引数を1番目から書きます。
"""

class MyClass:
	CLASS_PARAM = 100

	def __init__(self, instance_param):
		self.instance_param = instance_param

	@classmethod
	def method(cls):
		print(cls.CLASS_PARAM)
		# print(cls.instance_param) これはできない

	@staticmethod
	def method_2(param):
		print('Static!!', param)
		# cls.method() できない
		# print(cls.CLASS_PARAM)　できない
		# print(self.instance_param) できない

"""
関数内ではインスタンス変数やクラス変数、他の関数にもアクセスできません。
クラスの他の実装に依存しない関数です。
要するに独立した関数として実装できる場合に使えます。
"""


print("--- 使い方は分かった。で？？ ---")


"""
使い方は冒頭記載した通り難しくありません。
それぞれの制約も割とシンプルだと思います。
ただ、おそらくほとんどの人の感想は以下の様なものでしょう。
「なるほど、メソッドにも種類があるのね。で？？
全部インスタンスメソッドで書けばいいんじゃない？」
実際その通りで、上記の例においても以下の様に
全部インスタンスメソッドとして実装できます。
"""

class MyClass:
	CLASS_PARAM = 100

	def __init__(self, instance_param):
		self.instance_param = instance_param

	def method(self):
		print(self.CLASS_PARAM)

	def method_2(self, param):
		print('Static!!', param)


print("--- 使い分けるメリット（個人見解） ---")


"""
使い分けるメリットとしては以下の5つかなと考えています。（2021/11に2個追加）

    可読性・保守性
    ファクトリー関数
    名前空間の制御
    インスタンス化の手間を省く
    パフォーマンス

一個ずつ気持ちを書いていきます。


可読性・保守性

人によって答えの異なる分野だとは思いますが、
個人的には各種メソッドを使い分けるもっとも大きなメリットだと考えています。
デコレータが出てくるし、selfだったり、clsだったり、
第一引数なしだったりでややこしいから逆に可読性下がるんじゃないか
といった意見もきっとあると思います。
ただ、他人のコードを読んだり、修正する機会が増えてきて感じたのは、
「インスタンス変数が絡む関数は読むのが大変な傾向にある」ということです。
特に、別の関数で操作されたインスタンス変数が
さらに別の関数で登場してくる様なケースは割としんどくて、
一直線にコードが読めないのと、
インスタンス変数への意識に脳のリソースを奪われる感じがあってとても疲れます。
個人的には読むのがしんどい = 修正もしんどいなので、
保守の観点でもやはり辛いです。
やりたいことの都合上、インスタンス変数を操作せざるを得ないことは
ままあると思うのでそれ自体は頑張るだけなのですが、
全部インスタンスメソッドとして実装されていると、
この関数はどこかでインスタンス変数を操作しているのか？？
という割と大事な情報が、関数を全部読むまでわからないという事態になります。
関数の頭にデコレータで@staticmethodと書いてあれば、
「この関数はインスタンス変数にはアクセスしないのか」
とすぐにわかるので読むのも楽ですしそれはイコール修正するときも気が楽です。
長くなりましたが、つまるところ、インスタンス変数やクラス変数・関数への依存が
一目見てわかるのは可読性・保守性の観点から大きなメリットではないか
というのが私の気持ちです。


ファクトリー関数

もう一つ大きな要素です。
適切な名前がわからないので、仮にファクトリー関数と名付けます。
やりたいことはインスタンス作成用の関数を_init_とは別に用意することです。
例えば以下のような。
"""

class PreData:
	def __init__(self, a: int, b: int):
		self.a = a
		self.b = b

class Product:
	def __init__(self, d: int, e: int):
		self.d = d
		self.e = e

	@classmethod
	def from_pre_data(cls, pre_data: PreData):
		return cls(
			d=pre_data.a * 2,
			e=pre_data.b * 10
		)

	@staticmethod
	def from_pre_data_static(pre_data: PreData):
		return Product(
			d=pre_data.a * 2,
			e=pre_data.b * 10
		)

pre_data = PreData(5, 10)
product1 = Product.from_pre_data(pre_data)
product2 = Product.from_pre_data_static(pre_data)

"""
上記のように、ある別のデータ構造から
該当インスタンスを作成する関数を作りたくなるケースはままあるかと思います。
（個人的にはよく使います）
こういった関数をinstancemethodで実装するのは無理
（できなくはないが）なので、必然的に、
classmethodかstaticmethodとして実装することになるでしょう。
（PreDataにto_productのようなinstancemethod
を作る方法もあると思いますが、それはまた別の論点だと思うので、
一旦置いておきます。）
オブジェクト間の連携がわかりやすくなる（と思う）ので、
実装の幅を広げる意味でも、classmethod, staticmethod
を使うメリットになるのではないでしょうか。
なお、例に示したように、classmethodでもstaticmethodでも
どちらでも実装可能なので、どちらで実装するべきなのかとても気になっています。
個人的には、自分自身のインスタンスを作っているのがわかりやすいので、
classmethodの方がいいのかなという意見です。


名前空間の制御

こちらは可読性に関しての別の視点のお話です。
どこに何が書いてあるかをわかりやすくするために、
適切にモジュールやクラスを切っていくと思うのですが、
大切なのは上手に階層構造を作ることなのかなと考えています。
例えばあるファイル（モジュール）に4つのスタティックな関数があったとして、
役割としては2つのグループに分かれているとします。
この際ファイル（モジュール）を分割しても良いですが、
行数そんなにないし、ファイルが無駄にたくさん増えるのも気持ち悪いので、
モジュール内でグルーピングしたくなることがあります。
スタティックな関数をモジュール内でグルーピングする場合、
以下のようにstaticmethodを使うことになります。
（後述するインスタンス化の手間を減らすため）
"""

# グルーピングせずにフラットに4つ並べる
def func_1():
	pass

def func_2():
	pass

def func_3():
	pass

def func_4():
	pass

# 意味合いの近い関数をクラスでグルーピング化してまとめる
class GruoupA:
	@staticmethod
	def func_1():
		pass

	@staticmethod
	def func_2():
		pass

class GroupB:
	@staticmethod
	def func_3():
		pass

	@staticmethod
	def func_4():
		pass

"""
この例については、正直どちらがいいのかなんとも言えないところです。
classでグルーピングすることで、関数呼びだしの名前空間も制御できるので、
やり方次第では有用かもしれないというイメージを持っています。
無駄にグルーピングすると逆にわかりにくくなるケースも出てくると思うので、
乱用すべきではないと思いますが、
選択肢として一つ持っておくのはありかなと考えています。


インスタンス化の手間を省く

残りはおまけ程度ですが、一応記載しておきます。
こちらは割とわかりやすいメリットです。
インスタンスメソッドを使うときは一度インスタンス化しないとダメですが、
クラスメソッドやスタティックメソッドであればその必要がありません。
無駄な処理をするのってすごく気持ちが悪いですし、
やはりスマートでかっこいい実装ができた方がテンションもあがるので、
こういう細かいところもこだわっていきたいなという気持ちです。

# インスタンスメソッドとして実装されている場合
object = MyClass()
object.method()

# クラスメソッドとして実装されている場合
MyClass.method()


パフォーマンス

最後です。これはまだ実感としてもっているわけではないのですが
理論的にはという話です。
毎回インスタンス化しなくていいということは、
処理も減るし、無駄なインスタンスにメモリを使わなくて良いということです。
クラスの関数をいろんなところで使う場合に、
インスタンスメソッドとして実装していると
10個、20個とインスタンスを作るはめになりますが、それが全部不要になります。
塵も積もればなんとやらなので、
規模の大きいシステムの場合はこういった細かいところの配慮も
大事になってくるのかもしれないです。


まとめ

ということでようやく謎が解けた気分なので気持ちを書いてみました。
（まだまだ謎も多いですが）
こういう考えであることを職場の方と相談したところ、
共感していただけてこれまで全部インスタンスメソッドで実装していたんですが、
これからはそれぞれ使い分けて行こうぜという話になりました！
正解はないのかもしれませんが、
こういうところの思想についていろんな方とお話ししてみたいものです。
（ご意見待ってます）
"""



print("--- Python-izmより ---")
print("--- インスタンスメソッド ---")


"""
Pythonにおけるインスタンスメソッドの概要です。
インスタンスメソッドはインスタンス化してから呼び出す必要があります。

インスタンスメソッドの基本

インスタンスメソッドはいわゆる通常のメソッドです。
第一引数にはクラスのインスタンス自身を表すselfが必要となります。
"""

class TsetClass:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	# インスタンスメソッド
	def sample_instancemethod(self, display_x=True, display_y=True):
		if display_x:
			print('x is {}'.format(self.x))
		if display_y:
			print('y is {}'.format(self.y))

test_class_1 = TestClass(100, 50)
test_class_1.sample_instancemethod(display_x=False)


















