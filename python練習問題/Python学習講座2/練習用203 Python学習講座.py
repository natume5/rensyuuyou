#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- configparser 設定ファイルの読み込み ---")


print("--- iniファイル ---")


"""
一般的に、データベースの接続先や、
保存先ファイルといった設定値はソースコードに直接書き込むのではなく
設定ファイルを使用します。
Pythonでは、設定ファイルの読み込み用に、
configparserというini形式に対応したパーサーが用意されています。
ini形式とは以下のような大カッコで括った「セクション」と、
その配下にあるキーと値の組からなる形式です。
セミコロンでコメントを入れることもできます。
Windowsのレジストリなどで使用している拡張形式には
対応していないので注意してください。

; iniファイルの例
[DB]
host = localhost
port = 3306
user = kuro
pass = kuropass
; ここはコメント

[FILE]
; ここもコメント
output = /opt/output.txt
"""


print("--- configparserの使用方法 ---")


"""
それではconfigparserを使用してみましょう。
以下の設定ファイルを読み込んでみます。


基本的な使い方

configparserは、文字列以外に整数、実数、
論理型の変数を扱うことが可能です。
論理型は、yes/no以外にon/offを記述することができます。
まずは基本的な使い方です。セクションとキーを指定して値を取得します。
"""

import configparser

# configファイルの読み込み
config = configparser.ConfigParser()
config.read('sample.ini', encoding='UTF-8')

# 値を文字列で取得する
config['SAMPLE1']['str_key']

# configの型に応じた値を取得する
str_value = config.get('SAMPLE1', 'str_key')
int_value = config.getint('SAMPLE1', 'int_key')
float_value = config.getfloat('SAMPLE2', 'float_key')
bool_value = config.getboolean('SAMPLE2', 'bool_key')

"""
8行目では辞書のようにセクションとキーを指定しています。
この指定の仕方の場合、値は文字列型で取得されるため、
必要に応じて型を変換する必要があります。
このため、11行目以降ではget〜メソッドを使用しています。
この方法を使用すると、型変換をする必要がなくなります。


その他の使い方

おそらく実務上は上記の使い方だけで十分事足りると思いますが、
別の使い方も見ていきましょう。
"""

import configparser


# configファイルの読み込み
config = configparser.ConfigParser()
config.read('sample.ini', encoding='UTF-8')

# セクションを一覧で取得
print(config.sections())

# セクションの取得
sample1 = config['SAMPLE1']

# セクションにもgetメソッドが用意されている
int_key = sample1.getint('int_key')
print(int_key)    # 100

# 代替地の設定
int_key = sample1.getint('it_key2', '0')
print(int_key)    # 0

"""
8行目のようにsections()メソッドを指定すると、
セクションを一覧で取得することができます。
また、11行目にキーにセクション名だけ指定すると、
セクションのオブジェクトが取得でき、
14行目のようにget〜メソッドを使用することができます。
設定がない場合にデフォルト値を指定したい場合は18行目のように、
第2引数を指定します。
"""
