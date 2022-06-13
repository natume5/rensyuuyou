#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- argparse コマンドライン引数をパースする（オプションパーサ）---")


"""
ページではargparseモジュールを使用してコマンドライン引数のオプションをパース方法について解説します。

コマンドライン引数のパース

Pythonでコマンドライン引数をパースする場合、よく見かける方法としては以下の３つが挙げられます。

    sysモジュールのargvを使用する
    argparseモジュールのArgumentParserを使用する
    サードパーティ製のdocoptを使用する

簡単なスクリプトであればsys.argvでも良いのですが、
ある程度機能が増えてくると任意オプションなどが必要となるため対応が難しくなります。
argparseモジュールは標準ライブラリで用意されているオプションパーサで、
オプションやhelp、デフォルト値の設定、型の指定といったことが簡単にできます。
また、ここでは解説しませんが、docoptを使用するとdocstringに定義することも可能です。


argparseの簡単な使い方

まず、簡単な使い方について解説します（といってもほとんどの場合はこの使用方法で事足りると思います。）。
以下のような引数を定義する場合について考えてみます。

python sample4.py arg1 arg2 --opt1=val1 --opt2=val2

arg1、arg2は順番が決められていて必須、opt1、opt2は任意とします。
以下のスクリプトで、上のようなコマンドを定義することができます。

基本的なフロートしては、ArgumentParserを生成しadd_argumentで引数を追加していくことになります。
実際、パラメータを指定して実行するとパラメータの値がprint出力されることが確認できます。
また、パラメータがない場合は以下のようなusageが出力されます。

usage: sample4.py [-h] [--opt1 OPT1] [--opt2 OPT2] arg1 arg2
sample4.py: error: ambiguous option: --opt=val1 could match --opt1, --opt2

また、helpも自動で実装されます。-hを指定して実行すると、以下のような出力を得ることができます。

python sample4.py -h
usage: sample4.py [-h] [--opt1 OPT1] [--opt2 OPT2] arg1 arg2

positional arguments:
  arg1
  arg2

optional arguments:
  -h, --help   show this help message and exit
  --opt1 OPT1
  --opt2 OPT2
  

help文の定義

それではここから様々なオプションを指定して上のスクリプトに少しづつ肉付けする方法について解説します。
ArgumentParser()でdescriptionを、add_argumentでhelpを指定するとスクリプトと
引数のhelpを追加することができます。
先ほどのスクリプトを以下のように修正してみてください。

parser = argparse.ArgumentParser(description="サンプルスクリプトです。")

parser.add_argument("arg1", help="hogeを指定してください。")
parser.add_argument("arg2", help="fooを指定してください。")
parser.add_argument("--opt1", help="fugaを指定してください。任意です。")
parser.add_argument("--opt2", help="hugaを指定してください。任意です。")
-hオプションをつけて実行すると、以下のように出力されます。

python sample4.py -h
usage: sample4.py [-h] [--opt1 OPT1] [--opt2 OPT2] arg1 arg2

サンプルスクリプトです。

positional arguments:
  arg1         hogeを指定してください。
  arg2         fooを指定してください。

optional arguments:
  -h, --help   show this help message and exit
  --opt1 OPT1  fugaを指定してください。任意です。
  --opt2 OPT2  hugaを指定してください。任意です。
"""


"""
短縮オプション

いくつかのUnixコマンドは、--オプション以外に-オプションという形式の短縮したオプションが用意されています。
--helpと-hみたいなものですね。add_argumentの第1引数に短縮を、
第2引数にverboseをそれぞれに指定します。例えば、-oを--opt1の短縮としたい場合、以下のように追記します。

parser.add_argument("-o", "--opt1", help="fugaを指定してください。任意です。")
"""


"""
requiredによるオプションの必須化

オプション引数でも必須にしたい場合、add_argumentにrequired=Trueを指定します。
例えば、先程のスクリプトのopt1を必須にしたい場合、以下のように記述します。

parser.add_argument("--opt1", required=True, help="fugaを指定してください。
このオプションは必須です。")

なお、位置引数を非必須化することはできません。
"""

"""
defaultによるデフォルト値の設定

add_argumentの引数にdefaultでデフォルト値を指定することができます。
この記述がない場合、Noneが設定されます。

parser.add_argument("--opt1", default=10, help="fugaを指定してください。")
"""

"""
typeによる型の設定

add_argumentの引数にtypeで文字列から変換する型を指定することができます。
例えば、arg1にintを、art2にstrを指定させたい場合、以下のように記述します。

parser.add_argument('arg1', type=int, help="hogeを指定してください。")
parser.add_argument('arg2', type=str, help="fooを指定してください。")

不正な型を指定すると以下のようなエラー原因が表示されます。

optsample.py: error: argument arg1: invalid int value: 'a'
"""

"""
その他のオプション

add_argumentの引数で大抵の設定ができますが、さらに高度な使い方について解説します。
action

オプション引数に対して何を「値」とするかをadd_argumentの引数でactionで設定することができます。
通常、オプション引数は--opt=値の形式で指定しますが、
オプションの指定があれば無関係で何らかの値を使いたい、という場合があります。
例えばバージョン番号を表す--versionなどが挙げられます。

actionを指定するとこういった制御が可能となります。actionには以下を指定することができます。

    store_const：オプションが指定されている場合、constで指定した値を設定する
    store_true：オプションが指定されている場合、Trueを設定する
    store_false：オプションが指定されている場合、Falseを設定する
    version:オプションが指定されている場合、versionで指定した値を設定する

例えば、以下のようなコードを実行した場合、

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--opt1', action='store_const', const=100)
parser.add_argument('--opt2', action='store_true')
parser.add_argument('--opt3', action='store_false')
args = parser.parse_args()
print(args.opt1)
print(args.opt2)
print(args.opt3)

実行結果は以下のようになります。

$ python sample.py --opt1 --opt2 --opt3
100
True
False
"""

"""
また、例えば--versionでバージョンを設定したい場合、以下のようになります。

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--version', action='version', version='1.01')
args = parser.parse_args()
print(args.version)


python sample6.py --version
1.01
"""

"""
nargs

さきほどはオプションに対して値なしの場合についてactionを使用しましたが、
nargsを使用すると複数の値を設定することができるようになります。
opt1に対して3つの値を設定する場合、以下のように記述します。

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--opt1', nargs=3)
args = parser.parse_args()
print(args.opt1)

実行すると、オプションに指定した複数の値がlistで格納されていることが確認できます。

$ python optsample.py --opt1 a b c
['a', 'b', 'c']


typeで初期化処理

typeは型を指定できますが、関数オブジェクトを指定して初期化処理を行うことも可能です。
例えば、--langsにカンマ区切りで複数の値を指定したい場合、
以下のように初期化処理をtypeに指定することができます。

import argparse

def init(lang):
    return lang.split(",")

parser = argparse.ArgumentParser()
parser.add_argument('--langs', type=init)
args = parser.parse_args()
print(args.langs)

実行すると以下のような出力を得ることができます。

$ python optsample.py --langs=ja,en,tw
['ja', 'en', 'tw']
"""


print("--- pandas入門 pandasとは---")


"""
pandasとは？

pandasとはpythonのデータ分析ライブラリの1つで、大きな表データ、行列を扱うことができます。
特に、時系列データを分析する際には最適といえます。

ピボットテーブル、groupby、ソートなどの集計処理や、matplotlibと連携した可視化などが可能であるため、
表計算ソフトの機能の大半は置き換えることができます。

このため、分析以外にもExcelを使用した業務の自動化にも役立てることができるでしょう。
"""
"""
pandasのデメリット

pandasを使用すると色んな分析が簡単にできるようになります。
特に複雑な統計処理が数行でかけてしまう点は大きな魅力でしょう。

分析に最適なライブラリですが、日々の運用で使用するべきかどうかは検討が必要です。

（Python全般に言えることなのですが、）スクリプト言語故に簡単に書ける反面、遅い点がデメリットです。

運用でスピードが求められる場合、並列分散処理したり、
以下で部分的に置き換えられないかどうかの検討もしてください。

    RDB：Joinは圧倒的に速いです。
    高速なコンパイラ型言語(Java、C++など)
    統計ソフト：SPSS、Rなど。
    Excel：意外と侮れません。
"""


print("--- pandas入門 pandasの基礎知識---")


"""
pandasのデータ形式

pandasには大きく分けて3つのデータ形式があります。
Series

一次元の配列です。一列しかない行列とみなしても構いません。

indexと呼ばれる行ラベルをつけることができます。
Dataframe

行と列をもった配列データです。seriesを複数まとめたもととみなして見良いでしょう。pandas入門のメインです。
Panel

3次元の配列データです。白状すると管理人はこのデータ形式を業務で使用したことがないので、
当面は説明する予定はありません。


pandasの用語

学習を始める前に、pandas特有の用語を抑えておきましょう。

以下の説明だけだと何のことかわからないと思いますが、
実際にDataframeを生成して操作すると理解できると思います。


index

SeriesやDataframeの行データに付与することができるラベルのことをindexと呼びます。
行ラベルと呼称することもあります。

indexを使用してSeriesやDataframeの行データにアクセスすることができます。


columns

Dataframeの列データに付与することができるラベルのことをcolumnsと呼びます。
列のラベルと呼称することもあります。

indexを使用してDataframeの列データにアクセスすることができます。


integer-location

行(列)形式なので、番号指定でデータにアクセスすることもできます。
このアクセス方法をinteger-locationと呼びます。
"""


print("--- pandas入門 Seriesの基本---")


"""
前回ご説明したとおり、Seriesはシーケンスオブジェクトにindexと呼ばれるラベルをつけることができ、
DataFrameの一部として扱うことができます。

読者がコピペしやすいように記述していますが、スクリプトを毎回書くのは手間がかかるため
ipythonを使用することをおすすめします。


生成

まずはSeriesを生成してみましょう。
ラベル無しで生成する

基本的な生成方法です。シーケンスオブジェクトをコンストラクタの引数に指定します。
リストである必要はなくnumpy.array等でもかまいません。
"""

import pandas as pd
s = pd.Series([10, 20, 30])
print(s)

"""
以下のように出力されます。

0    10
1    20
2    30
dtype: int64

まず、左側の0〜2がindexと呼ばれる行の名前です。特に指定しない場合は0始まりの整数が付与されます。
"""

"""
indexにラベルをつける

indexは独自にラベルを指定することも可能です。
"""

# import pandas as pd

s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s)

"""
以下のように出力されます。

a    1
b    2
c    3
d    4
dtype: int64

indexがa、b、、、となっていることが確認できます。


辞書から生成する

以下の通り辞書から生成することも可能です。
"""

# import pandas as pd

s = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(s['a'])
print(s.a)

"""
Seriesにアクセスする

indexを指定して要素を取得することができます。[]を使用した添字で指定する方法と、
.で指定する方法の2種類あります。

import pandas as pd
s = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(s['a']) # 1が出力
print(s.a) # 1が出力

また、デフォルトのindexを使用している場合はスライスを使用して部分を切り出すことができます。
"""

# import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s[0:2])

# 0    10
# 1    20
# dtype: int64


"""
Seriesの更新

要素を更新する際は代入します。例えば0番目を更新する際は以下のようにします。
"""

s = pd.Series([10, 20, 30, 40])
s[0] = 100
print(s)

# 0    100
# 1     20
# 2     30
# 3     40
# dtype: int64

"""
また、スライスを使用して部分的に更新することも可能です。
"""

s = pd.Series([10, 20, 30, 40])
s[0:2] = pd.Series([100, 200]) # 代入はlistでも可
print(s)
print(list(s))

# 0    100
# 1    200
# 2     30
# 3     40
# dtype: int64
"""
pythonのlist型に変換

シーケンス型ですので以下でlistメソッドで変換することができます。
"""
