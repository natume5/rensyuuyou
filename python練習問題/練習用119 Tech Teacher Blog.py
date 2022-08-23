#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Tech Teacher Blog ---")
print("--- 【初心者向け】Pythonの関数について解説！引数や戻り値の使い方とは？ ---")


"""


「Pythonの関数ってどうやって使えば良いの？」
「そもそも関数を使うメリットは何？」

本記事ではこのような疑問を解決します。

プログラミングにおいて関数は非常に重要な役割を果たします。
関数を使いこなせるようになると、難しい処理もわかりやすく書くことが可能になり、
より高度なアプリやゲームなどが作れるようになりますよ。

本記事ではPythonの関数の使い方についてまとめました。
関数とは何か？といったことから、
初心者が混乱しがちな「引数」や「戻り値」の意味についても解説してあります。
"""


print("--- Pythonにおける関数とは ---")


"""
まず「そもそも関数とは何か」を説明していきます。
Pythonにおいて関数はどういった位置づけなのか、そもそもなぜ関数が必要なのか。
関数の基礎を初心者でもわかるように説明していますので、ぜひご覧ください。


関数とは何か

関数とは「データを渡すと、そのデータに対応した何らかのデータを返すもの」のことです。
一度作った関数は使いまわせるので、一連の処理をひとまとめにして1つの関数にしておくことが多いです。
たとえばPythonを使って、掲示板を作るとします。
ユーザーがサイト内の様々な場面で掲示板に「書き込む」という動作を行いますよね。
この「書き込む」処理をプログラム内でいちいち書いていては大変です。
そこで「書き込む」処理を1つの関数にまとめるようにします。
そうすればその関数を使うだけで「書き込む」処理を行うことができて、
プログラムのソースコード量を大幅に減らすことができるのです。
「書き込む」以外にも「ログイン」「書き込み削除」などの処理もそれぞれ関数にしてまとめておけば、
より効率的なソースが書けるようになりますね。
このように、同じ処理をプログラム内で何回も使うときに役に立つのが関数です。

関数には大きく分けて2種類あります。

    組み込み関数
    ユーザー定義関数

この2つはまったく異なるものなので、それぞれ解説していきますね。


組み込み関数

「組み込み関数」とは、Python側であらかじめ用意されている関数を指します。
プログラマはいつでもソース上で組み込み関数を呼び出して使うことができます。
Pythonでは多くの組み込み関数が用意されており、
これらを使うことで高度な処理を楽に書くことが可能です。
たとえば、Pythonには「len()」という組み込み関数が用意されており、
これを使うことで、文字列の長さを取得することができます。
他にも組み込み関数は色々ありますが、ここではすべてを紹介することはできません。
他の関数はぜひ自分で調べてみてくださいね。
このように、あらかじめ用意されている関数を組み込み関数と言います。


ユーザー定義関数

Python側に用意されている関数ではなく、プログラマが自分で作って定義した関数を
「ユーザー定義関数」と呼びます。
Pythonでは「def 関数名(引数名):」と記述することで関数を作ることができます。
詳しいユーザー定義関数の作り方は後で詳しく説明しますね。
ユーザー定義関数もコード内のどのタイミングでも呼び出すことができます。
ユーザー定義関数を作ることで、同じ処理を何度も記述しなくてよくなりますし、
コード全体も綺麗にまとまります。
また、後で他の人がコードを見直すときも、関数で処理をまとめてある方が読みやすくなりますね。
自分で作る関数が「ユーザー定義関数」、
あらかじめ用意されている関数が「組み込み関数」と覚えておきましょう。
"""


print("--- 関数の基本と定義方法 ---")


"""
Pythonでは次のようにして関数を定義することができます。
def 関数名(引数名1, 引数名2, ……):
　　　  関数内で行う処理1
　　　  関数内で行う処理2
　　　  ……
　　　  return 戻り値

Pythonでは「def文」を使って関数を定義します。
そして関数内で行いたい処理をdef文の中に書いていきます。
このとき、関数はいくつかの「引数」を持つことができます。
引数を使うことによって、関数にデータを渡すことが可能になるのです。
作成した関数を呼び出すときは次のように書きます。

関数名(引数1, 引数2, ……)

これだけで関数を呼び出すことができますよ。
関数を呼び出すと関数内のソースが処理され、処理が終わったら関数から「戻り値」が返ってきます。
戻り値とは「関数の実行結果」のことです。

次のように記述することで、関数の戻り値を変数に格納することができます。

変数名 = 関数名(引数1, 引数2, ……)

ユーザー定義関数はこのようにして定義するのが基本となります。
"""


print("--- 関数の実践方法・具体例 ---")


"""
それでは関数の実践的な使い方を見ていきましょう。

関数を使いこなせてはじめて一人前のプログラマと言えます。
関数の使い方はしっかりと覚えておきましょう。


関数の基本的な使い方

実際に関数を作って動かしてみましょう。

Pythonファイルを作成し、以下のように記述してみてください。
"""


def tashizan(a, b):
    print(a + b)

tashizan(1, 2)    # 3

"""
ここでは「tashizan」関数を定義して、足し算を行っています。
これぐらいならわざわざ関数を使うこともないのですが、簡単な例として取り上げてみました。
まず「def tashizan(a, b):」と記述することで、tashizan関数が定義されます。
tashizan関数は2つの引数「a」「b」を持っています。
そして「print(a+b)」の部分で2つの引数を足して出力していますね。
その下の「tashizan(1,2)」でtashizan関数を呼び出しています。
カッコ内にコンマで区切って「1」「2」と記入することで、
tashizan関数の引数「a」「b」にそれぞれ「1」「2」が代入できます。
そのため「print(a+b)」はここでは「print(1+2)」となり、「3」が出力されているのです。
これが関数の基本的な使い方です。

もう1つ簡単な例を紹介しましょう。
"""


def kakezan(a, b, c):
    return a * b * c

ans = kakezan(3, 4, 5)
print(ans)    # 60

"""
今度は「kakezan」関数を定義して、掛け算を行っています。

今回は「a」「b」「c」の3つの引数を使っていますね。
上の例では「kakezan(3,4,5)」で3と4と5を渡しているので3*4*5で「60」が出力されているのです。
先ほどと異なるのは、関数の戻り値を利用していることです。
kakezan関数内にはprint関数で出力する処理が含まれていないので、
戻り値で積の値を受け取り、関数の外で出力しています。
kakezan関数内の「return a*b*c」で「3*4*5」の値を戻り値として返しています。
そして、返した結果を変数「an」に格納しています。後はprint関数でanの値を出力していますね。
このように、関数の戻り値を利用することで関数の実行結果を取得して利用することができます。
関数を使うときの注意点として、渡す引数の数が、
定義された引数の数より多かったり少なかったりするとエラーが発生します。
たとえば

def kakezan(a, b, c):
　　　　return a*b*c

an = kakezan(3,4)
print(an)

とするとエラーが発生してしまい、正しくプログラムを動かすことができません。
上記の例では、kakezan関数が定義では3つの引数を取るところを、2つしか引数を渡していません。
引数が不足しているのでエラーが出るのです。
引数を渡す場合は必ず数を確認するようにしましょう。
以上が関数の基本的な使い方になります。
後は自分で色々な関数を作ってみてください。


関数から関数を呼び出す

続いて関数の少し応用的な使い方をご紹介します。
ここでは関数から関数を呼び出す方法を解説します。
つまり、Pythonでは関数をネストさせることができるのです。
「ネストってなに？」という方のために詳しく説明しますね。
Pythonファイルに、以下のように記述してみてください。
"""

def keisan():
    def tashizan(a, b):
        print(a + b)
    return tashizan

an = keisan()
an(1,2)    # 3

"""
上記の例ではkeisan関数の中で、さらにtashizan関数を定義していますね。
「keisan()」でkeisan関数を呼び出すと、keisan関数内の処理がまず動きます。
keisan関数内の処理は「tashizan関数を定義する」こと、
そして「tashizan関数そのものを戻り値として返す」ことです。
これによって、keisan関数の戻り値を格納した変数「an」は、
tashizan関数と同じ働きをする関数になっています。
その証拠に、「an(1, 2)」とすると「3」が出力されました。
これはkeisan関数内で定義されたtashizan関数の引数
「a」「b」に「1」「2」を渡したときの結果と同じであることを確認してください。
ここで、keisan関数の戻り値は具体的な数値ではなく「関数そのもの」であることに注意してください。
このようにPythonでは関数から関数を呼び出すという少し複雑なことができます。
Pythonでは関数もオブジェクトの1つとして扱われるため、
こういった書き方もできるようになっているのです。
このような書き方も実践ではよく使うので覚えておきましょう。
"""


print("--- まとめ ---")


"""
本記事ではPythonの関数について解説しました。
Pythonの関数の基本的な書き方がおわかりいただけたでしょうか？
関数を自分で作って利用できるようになると、長いソースコードも分かりやすく書くことができて、
仕事でも役立ちます。
ぜひ関数の使い方を覚えてみてくださいね。
関数の使い方を覚えていくには、色々な関数を自分で作って使ってみるのが近道です。
本記事で紹介したサンプルコードを自分で変更してみるなどして、
実行結果がどうなるのか色々確かめてみてくださいね。
"""

print("python3 簡単な関数作成")
print("--- 参考にしたコード ---")
print("bioinformatics より")

"""
基本的な作り方

関数は、def に続いて関数名とコロンを書き、その次の行をインデントし、関数の処理を書く。
例えば、2 つの引数（x と y）を受け取り、その差を返す関数は次のように作成する。
ただし、関数は diff とする。
"""

def diff(x, y):
    sa = x - y
    return sa

diff(30, 10)    # 20

diff(y = 10, x = 30)    # 20


print("---関数の引数に初期値を設定する方法---")

"""
関数の引数に初期値を設定することができる。
初期値が設定された関数が呼び出されると、
引数が与えられていないは初期値を利用するようになる。
例えば、次の関数では 、引数 x が与えられていない場合は x = 30 として初期化を行い、
引数 y が与えられていない場合は y = 0 として初期化を行う。
"""

def diff(x = 30, y = 0):
    sa = x - y
    return sa

diff(20)

diff()


print("---複数個の値を返す方法---")

"""
関数は 1 つの値をしか返せない。
複数の値を返す必要がある場合、リストあるいはディクショナリにして返す。
"""

def plus_and_minus(x, y):
    a = x + y
    b = x - y
    c = [a, b]
    return c

z = plus_and_minus(20, 10)
print(z)    # [30, 10]

"""
また、次のように書くと、タプルとして返すようになる。
"""

def plus_and_minus(x, y):
    a = x + y
    b = x - y
    return a, b

z = plus_and_minus(20, 10)
print(z)


print("---udemyメディア　python 関数の基本が初心者でもわかる！引数や戻り値も理解できる！ より---")


def microwave():
    print("時間を指定します")
    print("温めます")
    print("温めるのをやめます")

microwave()


print("---python 関数における引数---")


def microwave(mode):
    if (mode == "解凍"):
        print("解凍モードで温めます")
    elif (mode == "700ワット"):
        print("700ワットで温めます")
    else:
        print("500ワットで温めます")

microwave("解凍")


print("---python 関数における戻り値---")


"""
最後に、関数における戻り値について解説します。
戻り値とは、簡単に説明すると、データを返してくれることです。
例えば、円の面積を計算するプログラム（関数）を考えてみます。
※円の面積は半径×半径×3.14で求めることができます。
"""

def circleArea(radius):
    result = radius * radius * 3.14
    return result

print(circleArea(10))    # 314.0

"""
まず、circleArea関数の引数をradius（英語で半径という意味）としています。
ソースコード２行目で得られた円の面積をresultという変数に代入しています。
そして、関数を呼び出してみると、「314.0」という出力結果になりました。
ソースコード３行目にある「return」とは、「返す・戻す」という意味で、
関数を呼び出した時にreturnの右に記述したデータを返す（戻す）という役割があります。
returnを使えば、上記のソースコードのように出力結果として表示させるだけでなく、
帰ってきたデータを変数に代入することもできます。以下のソースコードをご覧ください。
"""

smallArea = circleArea(5)
bigArea = circleArea(10)
print(smallArea)    # 78.5
print(bigArea)    # 314.0

"""
ソースコードの１行目と２行目で、radius（半径）が５の円の面積をsmallAreaという変数に、
radius（半径）が10の円の面積をbigAreaという変数に代入することができています。
"""


print("HEADBOOST より")
print("Pythonのdef文で関数を作る方法")
print("3. 戻り値(return文)がある関数とない関数")
print("3.1. 戻り値のある関数")

def greeting():
    return "hello"

print(greeting())    # hello


a = greeting()
print(a)    # hello


print("3.2. 戻り値のない関数")


"""
戻り値 がない関数を見てみましょう。

以下のコードをご覧ください。

先ほどと同じgreeting()という関数ですが、
今度は関数定義の処理文ではreturn文を使わずにprint()を使っています。
"""
def greeting():
    print('hello')

"""
この関数を呼び出すと、指定の処理がそのままが実行されます
"""

print(greeting())    
# hello
# None

"""
一見変わらないように見えますが、この関数には戻り値がありません。
そのため関数を呼び出して別の変数に代入して出力してもNone（=何もない）になります。
"""

a = greeting()
print(a)
# hello
# None

"""
このように、return文で書いた処理は、その関数を呼び出した時に、戻り値として出てきます。
それ以外の場合は、処理文が実行されるだけで戻り値はありません。
これが戻り値(return)がある関数とない関数の違いです。
"""


print("4. 引数がある関数")


"""
引数がある関数を作る場合は、丸括弧 () の中に引数として欲しいデータを指定します。
そして、処理文の中で、受け取った引数に対する処理を書きます。
例えば、次のコードをご覧ください。引数nameを指定し、そのnameを定義文の中で処理しています
"""

def greeting(name):
    print(name + 'さん、こんにちは。')

"""
定義文の中で、引数nameと文字列を連結していますが、
文字列は+演算子では文字列としか連結できません
（参照：「Pythonの文字列を連結・結合する方法」）。
そのため、この関数を呼び出す時は、以下のように、引数に必ず文字列を入力します。
そうすると、次のように出力されます。
"""

greeting('太郎')
# 太郎さん、こんにちは。

"""
なお、引数は複数あっても構いません。

次の関数は、第一引数で大人の人数、第二引数で子供の人数を渡すと、
自動で合計料金を計算してくれるものです。
"""

def price(adult, kid):
    return adult * 2000 + kid * 800

"""
引数を2つ設定しているので、この関数を呼び出す時は、引数に2つの値を渡します。
"""

amount = price(2, 3)
print(amount)    # 6400


print("4.1.1. 位置引数とキーワード引数")


"""
さて、作成したprice()関数は、第一引数は大人の人数、
第二引数は子供の人数なので、順番が逆になると出力される結果は異なります。
"""

amount = price(3, 2)
print(amount)    # 7600

"""
このように、引数の位置によって関数の出力結果が異なるものを「位置引数」といいます。
しかし、price()関数のような関数は、位置引数では「大人、子供」の順だったか、
「子供、大人」の順だったか、とどっちがどっちだったかを間違えてしまう可能性があります。
そこで、次のような「キーワード引数」という渡し方をすることもできます。
"""

amount = price(kid=3, adult=2)
print(amount)     # 6400

"""
このようにキーワード引数は、「キー=値」として関数に渡します。
なおキーワード引数を渡す時は、キーはクオテーションマーク(‘)で囲む必要はありません。
もし、そうした場合は、次のように構文エラーになります。

In [5]:

price('kid'=3, 'adult'=2)  # キーをクオテーション(')で囲むとエラー

  File "<ipython-input-15-c9a689cad216>", line 1
    price('kid'=3, 'adult'=2)
         ^
SyntaxError: keyword can't be an expression

しかし、値が文字列の場合は、値はクオテーションマーク(‘)で囲む必要があります。
この位置引数とキーワード引数は、どちらもよく使うので覚えておきましょう。
"""


print("4.2. 初期値のある引数がある関数を書く")


"""
関数の引数には初期値を設定しておくことも可能です。
以下のコードをご覧ください。
この関数は、服のサイズと個数を渡すと料金を計算してくれます。
第二引数のnumには初期値で5を指定しています。
なお、変数unit_priceは辞書型オブジェクトです。
「Pythonの辞書(dict)の基本的操作の全て」で詳しく解説しています。
"""


def calc(size, num=5):
    unit_price = {'S': 120, 'M': 150, 'L': 180}
    price = unit_price[size] * num
    print(f"{size}が{num}着で合計{price}円です。")

calc('L')    # Lが5着で合計900円です。

"""
このcalc()関数は、第二引数には初期値5が設定されているので、
第一引数でサイズだけ渡すと、個数は5個として計算されます。

第二引数を指定すると、指定した個数で計算されます。
"""

calc('S', 10)    # Sが10着で合計1200円です。


print("4.3. 可変長の引数のある関数を書く")
print("4.3.1. 可変長の引数")


"""
ここまで解説した引数を複数個設定する関数は、
必ず、定められた個数の引数を渡さなければエラーになってしまいます。
そのため、それらを「必須引数」と言います。
しかし、時には、引数の個数を固定しない関数が必要な場合があります。
そのような場合は、引数の個数を固定しない関数を書くことができます。
これを「可変長の引数」といいます。
可変長の引数のある関数を書くには、次のように、引数に *args を入力します。



In [0]:

def 関数名(*args):
    関数定義（処理文）

*argsに書いた引数は、タプル型で関数に渡されます。
タプルについては「Pythonのタプルの基本的操作まとめ」でご確認ください。
まずは、これを使って、ごく簡単な関数を作ってみます。
引数に入力した要素をそのまま出力するものです。
どちらも関数に渡した引数はタプル型で出力されていることをご確認ください。
また、def文の丸括弧 () の中には *args と書きますが、
その下の定義文の中では argsと書くという点も覚えておきましょう。
"""


def station(*args):
    print(args)

station()    # 引数が0個　()
station('横浜', '名古屋', '京都')    # 引数が3個　('横浜', '名古屋', '京都')

"""
可変長の引数と、必須引数は組み合わせることができます。次のコードをご覧ください。
"""


def route(start, goal, *args):
    route = [start]
    route += list(args)
    route += [goal]
    route_final = '→'.join(route)
    print(route_final)

"""
この関数に、それぞれ引数を渡すと、次のように出力します。
"""


route('東京', '新大阪', '横浜', '名古屋', '京都')
# 東京→横浜→名古屋→京都→新大阪

"""
この関数では第一引数のstartと第二引数のgoalが必須引数です。
これらは渡さなければ必ずエラーになります。
第三引数以降は、可変長の引数なので、入力しなかったからといってエラーになることはありません。
ちなみに関数定義文についても解説しておきます。
まず、必須引数が受け取る値の型は引数に入力した値の型です。
この関数では、第一引数も第二引数も文字列を受け取っています。
一方で、可変長の引数は引数に渡された値をタプル型で受け取ります。
つまり、関数が、文字列とタプルという2つの異なる型のオブジェクトを受け取り、
そのままでは連結できないので、この関数では、どちらもリスト型に変換しています。
なお、関数定義文の中で使っているjoin()メソッドについては
「Pythonの文字列を連結・結合する方法」で解説しています。
"""


print("4.3.2. 可変長のキーワード引数")


"""
**kwargs とすると、その関数は引数を「キーワード引数」で受け取ります。
**kwargsに書いた引数は、辞書型で関数に渡されます。
なお、辞書に関しては「Pythonの辞書(dict)の基本的操作の全て」でご確認ください。
さて、キーワード引数を持つ関数を作るには、次のように書きます。

In [0]:

def 関数名(**kwargs):
    関数定義（処理文）

それでは、これを使って簡単な関数を作って試してみましょう。
def文の丸括弧 () の中には **kwargs と書きますが、
その下の定義文の中では kwargsと書きます。
関数に可変長のキーワード引数を渡す時は、
「キー=値」というようにキーと値を=でつないだものを1つの要素として、カンマ区切りで渡します。
この時キーは文字
そうすると、引数に渡した要素が辞書型で表示されます。
"""


def fruits(**kwargs):
    print(kwargs)

fruits(apple=1, orange=2, banana=3)    # {'apple': 1, 'orange': 2, 'banana': 3}

"""
なお、このキーワード引数の渡し方はdict()関数で辞書を作成する時と全く同じです
（参考：「Pythonの辞書(dict)の作成方法まとめ」）。
可変長のキーワード引数と必須引数も組み合わせることができます。
次の関数をご覧ください。第一引数と、第二引数が必須引数で、以降が可変長のキーワード引数です。
"""


def profile(name, gender, **kwargs):
    data = {'名前': name, '性別': gender}
    data.update(kwargs)
    print(data)

profile('山田', '男', 身長='178cm', 体重='70kg')
# {'名前': '山田', '性別': '男', '身長': '178cm', '体重': '70kg'}


print("5. 関数オブジェクトについて")


"""
実は、関数は、数値や文字列と同じように、変数に代入することができます。
そして、値に関数を代入した変数のことを「関数オブジェクト」といいます
（オブジェクトについては、「Python のオブジェクトとは」で簡単に解説しています）。
関数オブジェクトがあるということは、

    関数も変数に代入したり、
    関数自体を、別の関数の引数として渡したり、

ということができるということです。この点についても触れておきましょう
"""


print("5.1. 変数に関数を代入する（関数オブジェクトを作る）")


"""
まず、関数も変数に代入できるということを見ておきましょう。
単純な関数を作ります。
"""


# 例としてhello関数を作ります。
def hello():
    print(hello)

# 実行してみましょう
hello()

"""
この hello 関数を、変数 greeting に代入します。
そうすると、hello 関数を greeting() と書くことで使用することができます。
"""

# hello関数を別の変数に代入します。
greeting = hello

# すると、変数greetingでhello関数を実行できるようになります。
greeting()


print("5.2. 関数を別の関数の引数として渡す")


"""
次に、関数は、別の関数の引数として渡すことができるということを見ておきましょう。
これができるようになると、コードでできることの幅が広がりますので、ここで覚えておいて下さいね。
それでは、以下のコードをご覧ください。
"""

# thank youと表示する関数です。
def thanks():
    print('thank you')


# no thank youと表示する関数です。
def no_thanks():
    print('no thank you')


# 以下のようにfuncと入れると、引数に関数名を渡し、実行することが出来ます。
def do(func):
    func()

# それぞれ実行してみましょう
do(thanks)    # thank you
do(no_thanks)    # no thank you

"""
このコードでは、まず、 thanks 関数と no_thanks 関数という 2 つの関数を作っています。
そして、3 つめの do 関数にご注目ください。

do 関数は、

def do(func):
    func()

と書いています。

一行目は、do という名前の関数を作り、(func) と書くことによって、
do 関数の引数には、他の関数を渡すということを意味します。
このように、(func)と書くと、引数に渡す値は別の関数になるので覚えておきましょう。
二行目は、func() と書いています。
これは、do 関数の引数に渡した関数を実行するという意味です。
それぞれの実行結果をご覧ください。
do(thanks) では thanks 関数が、do(no_thanks) では
 no thanks 関数が実行されていますね。
Python では、このように、ある関数の引数を、別の関数にすることができます。
"""


print("5.3. 関数オブジェクトを使うと書けるコードの幅が広がる")


"""
このように、関数オブジェクトを知っていると、書けるコードの幅が大きく広がります。
関数オブジェクトを知っているということは、具体的には、以下の2つができるということを
知っているということです。

    関数も変数に代入することができる。
    関数自体を、別の関数の引数として渡すことができる。

それでは、この2つの特徴を利用したコードを見てみましょう。
まずは、後者の特徴を利用したコードです。以下をご覧ください。
"""


# 関数オブジェクトを利用すると書けるコードの幅が広がります。
condition = 1
if condition == 1:
    do(thanks)
else:
    do(no_thanks)
# thank you

"""
このコードは、if 文の条件を満たす時は、thanks 関数を実行し、満たさない時は、
no_thanks 関数を実行するという内容になっています。
 if 文については、「初心者のための Python の if 文（条件分岐）の基礎と使い方まとめ」
 で復習しておきましょう。
次に、2 つの特徴の両方を活用したコードです。以下をご覧ください。
"""

# 子供の料金を計算する関数 child を作ります。
def child(num):
    return 400 * num

# 大人の料金を計算する関数 adult を作ります。
def adult(num):
    return 1000 * num

# 子供か大人かによって料金の計算を振り分けます。
def calc(func, num=1):    # 第一引数に関数を、第二引数に人数を入れます。
    price = func(num)    # 料金は第一引数に渡した関数で計算されます。
    return price

# ３つの関数を合わせて以下のようなコードを作ることができます。
from random import randint    # randomモジュールからrandint関数をインポートする

age = randint(10, 31)
num = randint(1, 6)
if age < 18:
    price = calc(child, num)    # 18歳より下の場合、子供料金で計算します。
else:
    price = calc(adult, num)    # 18歳以上の場合、大人料金で計算します。

print(f"{age}才のお客様が{num}名で、料金は{price}円です。")
# 24才のお客様が3名で、料金は3000円です。

"""
分かりますでしょうか？

このコードでは、calc 関数の第一引数に、先に作った child 関数と、adult 関数を渡しています。
そして calc 関数の中で、変数 price に、第一引数に渡した関数を代入しています。
そのため、 price を実行すると、計算結果が表示されます。
最後のコードは、この 3 つの関数を使って、18 才以上か、それより下かによって、
子供料金と大人料金を振り分ける内容になっています。
モジュールのインポートと randint 関数については、
「Pythonのモジュールについて抑えておくべき知識とよく使うもの一覧」で解説しています。
難しいと感じた場合は、実際に、上のコードを、一行ずつ自分の手で入力してみてください。
それだけで理解が深まっていきます。
"""

"""クロージャを使ってみましょう"""
def charge(price):
    def calc(num):    # charge関数の中でcalc関数を作っています。
        return price * num    # calc関数は、price * numを返します。
    return calc    # charge関数はcalc関数の戻り値を返します。

"""関数オブジェクトを作ります。"""
child = charge(400)
# 関数オブジェクト child を作ります。子供料金を400円としています。
adult = charge(1000)
# 関数オブジェクト adult を作ります。大人料金を1000円としています。

"""関数オブジェクトを実行してみましょう。"""
print(child(3))    # 1200
print(adult(4))    # 4000


print("6. 関数の中に関数を作る（クロージャ、 関数閉包）")


"""
次に、クロージャ（関数閉包）について見てみましょう。
クロージャとは、関数の中に、関数を定義するものです。
次のコードをご覧ください。
"""


# クロージャを作ってみましょう
def charge(price):
    def calc(num):    # charge 関数の中で calc 関数を作っています。
        return price * num    # calc 関数は、price * num を返します。
    return calc    # charge 関数は calc 関数の戻り値を返します。


# 関数オブジェクトを作ります。
child = charge(400)
# 関数オブジェクト child を作ります。子供料金を400円としています。
adult = charge(1000)
# 関数オブジェクト adult を作ります。大人料金を1000円としています。


# 関数オブジェクトを実行してみましょう。
print(child(3))    # 1200
print(adult(4))    # 4000

"""
解説しますね。

まず、charge 関数は、その中に書いた calc 関数の結果を返す関数です。
そして、charge 関数の引数は price = 価格を渡します。
しかし、それだけでは、この関数はまだ機能しません。次のように、返されます。

In [2]:

charge(400)

<function __main__.charge.<locals>.calc>

この関数が機能するには、料金以外に、calc 関数に対して、
 num = 人数を引数として渡す必要があります。そこで、まず次のように書きます。

child = charge(400)
adult = charge(1000)

これによって、 charge 関数を、それぞれ、変数 child と adult に代入しています。
その際に、同時に charge 関数の引数を渡しています。
これで、関数オブジェクトの child と adult が作られました。
それぞれ、price = 価格は既に定義されているので、後は、num = 人数を引数に渡すと、
処理を実行することができます。

それが、次のコードですね。

child(3)
adult(4)

このように、クロージャを実行する時は、まず外側の関数を、別の変数に代入します。
その際に、外側の関数の引数を渡します。それによって、関数オブジェクトが作られます。
そして、新しく作った関数オブジェクトを実行する時に、内側の関数の引数を渡します。
最初は分かりにくいかもしれません。
そのような時は、ご自身の手で、一行ずつ写経してみてください。
コードの写経は、手っ取り早く内容を理解するための最も効率的な方法です。
"""


print("7. 比較関数を作る")


"""
ここでは、関数の別の使い方を解説します。
「Pythonのリストをソートする方法まとめ」で解説している
 sort メソッドや sorted 関数を思い出してください。

これらでは、要素が長い順にソートする時は、次のように書いていました。

'''sort メソッド'''
list.sort(key=len)
 
'''sorted 関数'''
sorted(list, key = len)

引数に “key = len”と渡されていますね。
”len” は文字列やリストの長さを返す関数です
（「Pythonのリストの長さ（要素の数）を確認する方法まとめ」）。
他にも、引数に “key=str.lower()”と渡せば、大文字小文字の区別なくソートすることができます。
これは、ある関数を、「比較関数」として使えるということを意味します。
文字で細かい説明をするより、実例を見た方が理解が早いと思いますので、早速、以下をご覧ください。
def 文で、size 関数を作っています。
"""


# def文で関数、sizeを作ります。
def size(item):    # item はオブジェクトの要素を引数とする時に使います
    sizeList = ["XS", "S", "M", "L", "XL"]
    pos = sizeList.index(item)
    return pos     # sizeList の要素のインデックス番号を返します。


"""
size 関数は、ブロック内で定義している XS, S, M, L, XL が引数として渡された場合のみ、
その位置を返す関数です。コード内で使っている index メソッドについては、
「Pythonのリストを検索する方法まとめ」をご覧ください。
それでは、size 関数を確認してみましょう。
"""


# size 関数はリスト内の要素の位置を返す関数です。
print(size('M'))    # 2
print(size('XL'))    # 4













