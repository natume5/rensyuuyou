#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- 初めてのプログラミング編 統合開発環境を使ってみよう---")


"""
統合開発環境とは？

　ここまで、整数や文字列の簡単なプログラムを作成しましたが、
これ以降の学習ではよりプログラムが複雑になります。
このため、学習効率を上げるために、統合開発環境と呼ばれるソフトウェアを使ってみましょう。

Pythonを動かしてみようのページで解説したとおり、最初はメモ帳とコマンドプロンプト(ターミナル)、
エクスプローラを開いて実行しました。ですが、実際の開発現場ではメモ帳より機能の充実したエディタや
統合開発環境と呼ばれるソフトウェアを使用します。
英語のIntegrated Development Environmentを略してIDEと呼ばれる場合もあります。

プログラミング用のエディタは、単語を自動的に補完したり、
シンタックスハイライトと呼ばれるコードに色を付けて見やすくしてくれる機能などがあります。
また、統合開発環境はプログラミング用のエディタの機能に加え、
その場でコードを実行したり、ファイルをツリー状に表示するエクスプローラ機能などが用意されています。
メモ帳やプロンプト、エクスプローラを行き来する必要がなくなるわけです。

なお、いくつかのエディタには統合開発環境のような機能が用意されており、
エディタと統合開発環境の境界は近年曖昧になっています。

統合開発環境の例

　2020年時点で人気のある開発環境として以下3つが挙げられます。

    IDLE
    PyCharm
    Visual Studio Code

上記以外にデータ分析に特化した統合開発環境、SpyderやJupyterなどもあります。
それぞれ簡単に紹介します。

IDLE

　IDLEはPythonインストール時に同梱されている統合開発環境です。
つまりPythonをインストールするだけで使えるわけですね。
お世辞にも機能が充実しているとはいえず、実際の開発現場では使用されることは少ないのですが、
プログラミング学習の際によく使用されています。この講座でもこの後使い方について簡単に解説します。

PyCharm

　PyCharmはJetBrainsが開発した統合開発環境で、
有償のProfessional版と無料のコミュニティ版の2種類があります。
大抵の場合はコミュニティ版で問題なく開発できると思います。

Visual Studio Code

　MicroSoftが開発したVisual Studio Codeも人気が高まっている環境です。
Visual Studio Code自体はエディタという位置づけなのですが、
様々なプラグインを設定することにより統合開発環境として使用することが可能です。
無料にもかかわらず、設定次第でPyCharmのProfessional版と同等の機能が使える環境を
構築することも可能です。

IDLEを使ってみよう

　それではシンプルな統合開発環境、IDLEを使用してみましょう。
WindowsではスタートメニューからIDLE Python GUIをクリックして起動してください。
MacOSやLinuxなどのUnix系の環境の型はターミナルにidleと入力してください。

次にIDLEでPythonコードを書いてみましょう。

メニューからFile → NewFileをクリックします。
メモ帳のようなエディタが開きますので、以下のコードを入力してみてください。

print("Hello IDLE!")

以下の画面のようにコードに色がついて見やすくなっています。

次に作成したコードを保存してみましょう。メニューからFile → Saveで適当なフォルダに保存してください。

最後に保存したPythonファイルを実行してみます。エディタを開いた状態でF5キーを押下します。
すると、最初に立ち上がったコマンドライン画面で実行結果が表示されます。

========================= RESTART: C:/pywork/sample.py =========================
Hello IDLE!
>>>

終了する場合は×ボタンをおして終了してください。
また、IDLEを起動して作成したファイルを再度開く場合は、File → Openからファイルを開いてください。
"""

"""
演習

それでは演習です。IDLEで以下のPythonコードを作成し、保存、実行をしてください。

def main():
    int_list = list(range(100))
    for x in int_list:
        print(x)
    

if __name__ == "__main__":
    main()

このコードに書かれている文法等はまだ解説していませんが、
実行すると以下のように0～99までの整数が表示されます。
"""


print("--- 初めてのプログラミング編 キーボードから入力した値を使ってみよう---")


"""
キーボードからの入力値を使用する

次回から制御文と呼ばれる処理について解説しますが、
その前に準備としてキーボードから入力した値を変数に格納する方法について解説します。

まずは以下のPythonスクリプトを実行してみてください。

print("適当なキーを入力してください")
x = input('>> ')
print(x + "が入力されました。")

このPythonスクリプトを実行すると、コマンドライン上に「適当なキーを入力してください」
というメッセージが表示され、その次に入力待ちの>>の記号が表示されます。
次に値を入力してエンターキーを押してください。

例えば、abcを入力すると以下のように入力内容がメッセージに表示されます。

適当なキーを入力してください
>> abc
abcが入力されました。

変数xにキーボードから入力した値abcが格納されているわけです。
"""

print("適当なキーを入力して下さい")
x = input('>>')
print(x + 'が入力されました。')


"""
数値の入力

ここで注意が必要なのが、入力された値は「文字列である」という点です。
入力した値を数値として計算したい場合は少し工夫が必要です。

具体的には数字の文字列から整数に変換させるint関数というものを使用することになります。

int("数字の文字列")

例えば、"100"という文字列は文字列なので計算できませんが、
int関数で整数に変換することにより計算することが可能となります。
"""

s = '100'
x = int(s)
y = x + 10
print(y)

"""
実行すると、100 + 10の計算結果、110が表示されます。

以下のコードは2つの数字を入力させて、入力された数値を足し算し、結果を表示しています。
"""

print('2つの数の和を求めます。')
print('1つめの数値を入力して下さい。')
x = input('>>')
print('2つめの数値を入力して下さい。')
y = input('>>')

x2 = int(x)
y2 = int(y)
z = x2 + y2
print("2つの数の和:", z)

"""
文字列x, yを数値に変換したものをx2, y2に格納しています。
ただし、このコードは数字以外を入力するとエラーが発生します。
対応方法については本講座では解説しませんが、興味がある方は入門編を学習してください。
"""


"""
演習
演習1

3つの数値を入力させ、和を表示するプログラムを作成してください。
"""

print('3つの数の和を求めます。')
print('1つめの数値を入力して下さい。')
x = input('>>')
print('2つめの数値を入力して下さい。')
y = input('>>')
print('3つめの数値を入力して下さい。')
z = input('>>')

x2 = int(x)
y2 = int(y)
z2 = int(z)
w = x2 + y2 + z2
print("2つの数の和:", w)


print("--- 初めてのプログラミング編 条件分岐を使ってみよう---")


"""
条件分岐とは？

条件によってプログラム上の処理を変化させるような処理のことを条件分岐と呼びます。
例えば年齢が18歳未満の場合と以上の場合で処理を分ける場合について考えてみます。

    年齢が18歳未満の場合、メッセージ「購入できません」を出力する

このような条件分岐をPythonで書いてみましょう。
1行目でキーボードから入力した値をinput_valに格納し、2行目で数値に変換してageに格納しています。
"""

input_val = input("年齢を入力して下さい = ")
age = int(input_val)
if age < 18:
	print("購入できません")
else:
    print("購入可能です！")

"""
input_valの値を色々変更して実行してみてください。

上のコードの通りPythonで条件分岐をする場合、以下のようなif文という文を使用します。

if 条件式:
    条件式が真の場合に実行する処理

条件式とは、ずばりそのまま条件を表す式です。
いくつか数値での例を見てみましょう。
xは数値を格納した変数とします。

例 	意味
x == 10 	    xは10と等しい
x != 10 	    xは10と等しくない
x < 10 	        xは10より小さい
x > 10 	        xは10より大きい
x >= 10 	    xは10以上
10 <= x < 20 	xは10以上20未満

2022/02 上表にて「x != 10」の説明が「xは10と等しい」となっておりましたが誤りです。
「xは10と等しくない」となります。ご指摘くださった方ありがとうございます。

いかがでしょうか？数学で学んだ不等式とほとんど同じなのでなんとなくわかるのではないでしょうか。
ただし大なりイコール、小なりイコールの場合は半角のイコールと合わせて<=、>=と書きます。
このように等しいか、大きいかなど変数や値を比較する演算を比較演算と呼びます。

if文の中はスペース4つ分インデントをつけます。
この、インデントを付けられた箇所を「ブロック」と呼びます。
if文等のブロックは入れ子にすることが可能です。
入れ子の例については末尾の演習で紹介します。
また、分岐を終える場合はインデントを戻します。

もう少し練習してみましょう。
"""

"""
例題1

先程のコードを真似して入力した値がが20より大きい場合、
「入力した値は20より大きいです」というメッセージを出すプログラムを作成してください。
また、処理の最後に「処理が終了しました。」というメッセージを表示させてください。
"""

input_val = input("x = ")
x = int(input_val)
if x > 20:
    print("入力した値は20より大きいです")
else:
    print("入力した値は20より小さいです！")

print("処理が終了しました。")

"""
例題2

先程のコードを値が100と等しい場合「入力した値は100と等しいです」
というメッセージを出すプログラムに書き直してみてください。
"""

input_val = input("数値を入力してください")
x = int(input_val)
if x == 100:
    print("入力した値は100と等しいです")
else:
    print("入力した値は100と等しくありません")

print("処理が終了しました。")


"""
コメントを付けてみよう

さて、ここで大変重要な用語を解説します。それは「コメント」です。
コメントとは、プログラム上に記述することができる注釈で、実行しても処理に影響しないものを指します。
また、ブロック内のコメントはインデントをつける必要があります。

Pythonのコメントは#を使用します。以下は最初のコードに対してコメントを付けた例となります。

# キーボードから年齢を入力
input_val = input("年齢 = ")

# intに変換
age = int(input_val)

# ageが18より小さい場合はメッセージを表示する
if age < 18:
    # メッセージ表示
    print("購入できません")

分岐や今後説明するループ処理、関数などが増えると読み手にコードの意図を
正しく伝える必要が出てきますが、その際にコメントを活用するようにしてください。
"""

"""
複数の条件分岐を使ってみよう

elseを使用すると、if文の条件に合致しない場合の処理を行うことができます。
例えば、18歳未満は500円、それ以外1000円といった料金計算をするプログラムを組んでみましょう。
以下のようなコードが考えられます。
"""

input_val = input("年齢を入力してください")
age = int(input_val)
if age < 18:
    price = 500
else:
    price = 1000

print("値段:", price)

"""
また、elif（英語のelse ifの略）を使用すると複数並べることも可能です。
例えば、先程のコードについて、18歳未満は500円、18歳以上65歳未満は1000円、
それ以外は700円というように条件を変えてみます。
"""
# キーボードから年齢を入力
input_val = input("年齢を入力してください")

# intに変換
age = int(input_val)

if age < 18:
    price = 500
elif 18 <= age < 65:
    price = 1000
else:
    price = 700

print("値段:", price)


"""
演習
演習問題

会員かどうかと年齢を入力させ、以下の料金計算をするプログラムを作成してください。
また、適宜コメントを記入してください。

    会員の場合
        18歳未満：100円
        18歳以上：1000円

    非会員の場合
        18歳未満：1000円
        18歳以上：2000円

解答例

前述のとおり、if文などのブロックは入れ子にすることができます。
解答例ではif文が入れ子になっています。
"""

# 会員を入力
input_kaiin = input("会員の場合はYを入力してください。>>:")

# 年齢を入力
input_age = input("年齢を数字で入力してください。>>")

# 年齢の入力値を整数に変換
age = int(input_age)

# 会員/非会員で処理分岐
if input_kaiin == "Y":
    # 会員の場合

    # 年齢で条件分岐
    if age < 18:
        # 18歳未満の場合
        price = 100
    else:
        # それ以外の場合
        price = 1000

else:
    # 会員以外の場合

    # 年齢で処理分岐
    if age < 18:
        # 18歳未満の場合
        price = 1000
    else:
        # それ以外の場合
        price = 2000

print("値段:", price)
