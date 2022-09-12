#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- 変数の基本 ---")


"""
Pythonの変数の型はたくさんあるのですが、まずは基礎と全体的な俯瞰をしましょう。
たくさんあって戸惑うかもしれませんが、予め概要を抑えておくと学習がスムーズに進むと思います。
"""


print("--- 変数とは ---")


"""
変数とは、プログラミング上でデータを保持するためのメモリ上の領域、
つまり「データを格納するためのハコ」につけた名前、ラベルのようなものです。
例えば、ハコaに2を、ハコbに3を入れて、足した結果をハコcに格納する場合、
Pythonでは以下のように記述します。
"""

a = 2
b = 3
c = a + b
print(c)

"""
少々回りくどく感じるかもしれませんが、値2と3を格納したハコにa、bとラベルをつけ、
それらを足した5を格納するハコにcというラベルがつけられている、というイメージです。
また、ハコ、つまり変数の中身を表示したい場合、以前学習したprint関数を使用します。
"""


print("--- 変数の基礎 ---")


"""
変数定義

一部のプログラミング言語では、変数宣言や型宣言という
「これからこういった型の変数を使用します」という宣言が必要なのですが、
Pythonの変数は変数宣言や型の宣言は不要で、
先程のコードの通り変数名と値をイコールで結べばそのまま変数として使用することができます。

以下の形式となります。

変数名 = 値

では、サンプルを見てみましょう。以下のコードはPythonの様々な型の変数を定義して
print関数で出力しています。
入門者の方は実際にスクリプトを書いて実行してみることをおすすめします。
"""

a = 1    # 数値
b = 'AAA'    # 文字列
c = [1, 2, 3]    # リスト
d = {'apple': 200, 'orange': 100, 'banana': 150}    # 辞書

# 定義した変数の内容を出力してみる
print(a)    # 1
print(b)    # AAA
print(c)    # [1, 2, 3]
print(d)    # {'apple': 200, 'orange': 100, 'banana': 150}

"""
# 未定義の変数の内容を出力してみる
print(e) # 以下のエラーが出力される
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'e' is not defined

最後にエラーが起きていますが、これは定義していない変数eを出力しようとして、
NameErrorが発生しています。つまり「定義していない変数は使えない」
ということを抑えておいてください。


変数への再代入

宣言した変数に別の値で上書きすることが可能です。
"""

a = 1
print(a)    # 1

a = 'aaa'
print(a)    # aaa

"""
最初に変数aに数値を代入してprintで出力しています。
次にaに文字列を代入して出力しています。
前後で値が変わっていることが確認できると思います。

最初、1が格納されていたハコにaというラベルをつけています。
このラベルを'aaa'が格納されたハコに付け替えています。
元のハコの中身が変わったわけではない、という点に注意してください。


別変数への代入

一旦定義した変数の値に対し、別の変数に紐付けることができます。
"""

a = 'aaa'
b = a
print(b)

"""
文字列'aaa'が入ったハコにaというラベルをつけました。
その後、aが指し示すハコにbという名前もつけている状態です。


複数同時の初期化、代入

また、複数の変数を同時に初期化したり代入することができます。
"""

x, y, z = 1, 2, 3
a, b, c = x, y, z

print(a)    # 1
print(b)    # 2
print(c)    # 3

"""
x, y, zをそれぞれ同時に初期化しています。
また、a, b, cに対し同時にx, y, zを代入しています。
一定のルールで統一性を持たさないと可読性が落ちるため注意してください。


定数

定数とは値の変更を許可しない変数のことです。
例えば、消費税率等を格納する変数は
価格を算出するプログラムが動作している最中に書き換わると困りますので、
多くの言語では定数というものがサポートされています。
このページでも変数の次は定数を学習、といきたいところなのですが、
なんとPythonに定数はありません。
慣習的に大文字の変数を定数とみなす場合がありますが、
変数の書き換え自体を禁止する仕組みはありませんので注意してください。
"""


print("--- 変数の種類 ---")


"""
次回から様々な代表的な変数について学習を進めていきますが、
その前に基本的な変数種類の全体像を俯瞰しておきましょう。
pythonの基本的な変数には以下のようなものがあります。
わからない単語があるかもしれませんが、
学習を進めて実際に手を動かすと理解できるようになると思います。


数値

数値を扱う変数の型で、演算を行うことが可能です。
整数型(int)、実数型(float)、複素数型(complex)が挙げられます。
また、True/Falseを扱う論理型もpythonでは内部的には数値の一種です。

コレクション

複数のオブジェクト（※）の集まりを表現するデータ構造の総称をコレクションと呼びます。
コレクションの代表例としてはリストのようなシーケンス、集合、辞書が挙げられます。(注1)
（プログラミング未経験者向けに、ページ下部にオブジェクトについて補足しています。）

シーケンス型

シーケンス型とは、「データを順番に並べたものをひとかたまりとしたデータ」で、
他のプログラミング言語では配列と呼ばれることもあります。
list型と呼ばれるものがシーケンス型の代表です。
また、イミュータブル（一旦生成すると後から変更ができないこと）
なtuple型というものがあります。
また、Pythonでは文字列もシーケンスなので、シーケンスとしての処理が適用できます。
このことは比較的重要なので覚えておいてください。

集合型

集合型とは「データの集合をひとかたまりとしたデータ」、つまり集合そのものを表します。
重複要素と順序をもたないset型という型が用意されています。
Pythonのset型は集合演算が利用できるという点が特徴的です。
また、frozensetというイミュータブルなものも用意されています。

マッピング型

他のプログラミング言語ではハッシュ型と呼ばれることがあります。
キーと値を持つデータの集まりで、
キーを指定すると目的のデータをすばやく取得することが可能です。
"""


print("--- 補足 変数と値とオブジェクト ---")


"""
初学者向けの補足です。ページ上部で、変数について以下のような説明をしました。

変数名 = 値

この「値」という単語について、サンプルで数値や文字列などを例示しましたが、
「値」というものは全てPythonではオブジェクトと呼ばれるものの一種です。
このため値のことをオブジェクトと呼ぶ場合があります。
オブジェクトとは、上のサンプルのようにデータの「値」を表す以外に何らかの
「機能」を持っている場合があります。
この機能のことをメソッドと呼びます。
オブジェクトについて理解するためにはクラスについても理解する必要がありますが、
これらについては後ほど別途説明します。
このため、当面はオブジェクトとは「何かしらの値」で「何らかの機能を持っている」と考えてください。
また、（ややこしいことに）変数という単語はは上で説明したとおり
オブジェクトに名付けたラベルを指す場合と、
オブジェクトそのものを指す場合とがあるので注意してください。
※1:以前は複数のデータ集合をコンテナと呼び当サイトでもコンテナと記述していたのですが、
近年はDockerなどのコンテナを指す場合が多いためコレクションに記述を改めました。
"""
