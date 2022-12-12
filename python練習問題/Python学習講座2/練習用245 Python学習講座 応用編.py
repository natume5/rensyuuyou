#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- IPython 入門 ---")


print("--- IPythonとは ---")


"""
データ分析でよく利用するIPythonですが、どういったものなのでしょうか？
IPython公式の説明を引用してみます。

    強力なインタラクティブシェル
    Jupyterのカーネル
    インタラクティブなデータの視覚化とGUIツールキットの使用をサポート
    柔軟で組み込み可能なインタプリタをプロジェクトから読み込める
    並列コンピューティングのための使いやすい高性能ツール


簡単にいうと、データ分析のための分析・可視化ツールを
対話形式で利用できるライブラリです。
Jupyterについては今後別途ご紹介する予定です。
この対話形式は非常に協力なので、データ分析をする目的以外にも使えます。
僕は通常のPythonの対話形式よりIPythonの方が便利なので、
対話形式の場合はほとんどIpythonを使用します。
"""


print("--- IPython入門 ---")


"""
(このページではデータ分析関連の内容は書きません。
IPythonの初歩的な操作についてご説明します。)

IPythonには通常のPythonの対話形式より強力な点は補完機能、
オブジェクト内容表示、外部シェル実行機能などがあります。
詳細は以下のチュートリアルをご参照ください。
Introducing IPython


インストールと起動

まずはインストールです。以下のpipコマンドでインストール可能です。
anacondaを利用している場合は、予めインストールされているので不要です。

pip install ipython

ipythonと打ち込むと以下のように起動します。

$ ipython
Python 3.5.1 (default, Apr 24 2016, 23:33:22) 
Type "copyright", "credits" or "license" for more information.

IPython 5.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]:


タブキーによる自動補完

まず、通常のPythonと比較して、
圧倒的に便利なのがこのタブキーによる自動補完機能です。
途中まで入力してTabキーを押下すると、補完候補が選べます。

# 適当に変数を定義する
In [1]: var_hoge = 1
# 途中まで入力してTabキーを押下する↓
In [2]: v


?コマンド

オブジェクトの内容を確認する際、便利なのが?コマンドです。
変数やオブジェクトのあとに?をつけると、その説明が表示されます。

[出力例]

In [3]: var_hoge?
Type:        int
String form: 1
Docstring:  
int(x=0) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4


マジック関数

予め用意されているユーティリティ的な関数です。以下の形式で利用します。

%[マジック関数名] パラメータ
複数行パラメータとして渡したい場合は、%%をつけます。
この説明だけだと、何のことかわけがわからないと思いますので、
いくつか例を交えて説明します。
全ては説明しきれないので、詳細はBuilt-in magic commandsを参照してください。

%timeit

%timeitは後に渡されたパラメータを実行する時間を返します。
例えば、1000個のリストを生成する実行、
その最大値を算出する時間を調べたい場合、以下のようになります。

In [3]: %timeit range(1000)
680 ns ± 17 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

In [1]: %%timeit x = range(10000)
   ...: max(x)
   ...:
   ...:
867 µs ± 105 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

In [2]: %%timeit x = range(10000)
   ...: max(x)
   ...:
   ...:
811 µs ± 61.8 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)


%run

runは外部のpythonスクリプトを起動します。
例えば、文字列を出力するsample.pyというスクリプトがあった場合、
以下のように実行します。

In [3]: %run sample.py
This is a sample


%history, %save, %load

%historyで履歴を確認します。
%saveは履歴の中で保存したいものを番号指定してスクリプトとして保存できます。
当然saveしたものをloadすることができます。
サンプルを見てみましょう。

In [1]: s = 'sample'

In [2]: print(s)
sample

In [3]: %history
s = 'sample'
print(s)
%history

In [4]: save save_sample.py 1 2
The following commands were written to file `save_sample.py`:
s = 'sample'
print(s)

In [5]: load save_sample.py

In [6]: # %load save_sample.py
   ...: s = 'sample'
   ...: print(s)
   ...: 
sample

In [7]: %run save_sample.py
sample

実行したスクリプトの説明です。
1から2行目まで適当な文を実行しています。
3行目で履歴を確認し、
4行目で1行目から2行目をsave_sample.pyというファイルに保存しています。
5行目でsave_sample.pyをloadし6行目でその内容が表示されています。
7行目で%runでそのスクリプトを実行しています。


その他のマジック関数

%editでエディタが起動し、
対話モードの途中で指定したスクリプトを編集することができます。
%debugでデバッグモードとなります。
その他にも色々あってすべては紹介しきれないのですが、
%quickrefでマジック関数のリファレンスが表示されますので一読しておくと良いでしょう。

システムコール

!の後、bash等のシェルの入力が可能になります。

In [12]: !pwd
/home/work/ipython


設定ファイル等

通常、~/.ipython/profile_defaultに配置されます。
また、その中の~/.ipython/profile_default/startup/
にスクリプトを配置すると、それらがIPython起動時に毎回実行されます。


終了方法

通常のPythonの対話モードと同様でquit()で終了します。
"""


print("--- タブ補完、?コマンド、マジック関数の3つがポイント ---")


"""
いかがだったでしょうか。
タブ補完、?コマンド、マジック関数の3つを抑えれば
通常のPythonの対話モードより断然効率的に
使用できるようになると思いますのでおすすめです。
"""
