#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説 ---")
print("--- JSONモジュールの使い方 ---")


"""
「json」はJavaScriptのオブジェクトの記述方法と似ている「軽量なデータ交換フォーマット」で、
データを扱うアプリケーションで主に使われています。
Pythonではjsonをうまく扱うためのモジュールが数多く用意されていますので、
それぞれの使い方を解説します。
"""


print("--- jsonを辞書とリストの組み合わせに変更する  ---")


"""
json文字列をPythonの辞書とリストの組み合わせに変換するには
json.loads()またはjson.load()を使います。
json.loads()は文字列を、json.load()はjsonファイルをそれぞれ引数に取り変換します。
次の例はjson.loads()を使って文字列を変換しています。
"""

import json

json_str = '{"id": "001", "numbers": [1, 2, 3], "colors": ["blue", "yellow", "red"]}'
json_obj = json.loads(json_str)
print(json_obj)
print(json_obj['id'])
print(json_obj['numbers'])

# {'id': '001', 'numbers': [1, 2, 3], 'colors': ['blue', 'yellow', 'red']}
# 001
# [1, 2, 3]

"""
json_strはjson文字列が格納されており、json.loads()
を使って辞書とリストの組み合わせに変換しています。
結果をみてわかる通り、[‘id’]は001を、[‘numbers’]は数値のリストを取得できています。
また、jsonファイルを直接変換する場合はjson.load()を使います。

ファイル[sample2.json]

{
  "id": "001",
  "numbers": [
    1,
    2,
    3
  ],
  "colors": [
    "blue",
    "yellow",
    "red"
  ]
}
"""

import json

json_file = open('./sample2.json', 'r')    # readでオープン
json_obj = json.load(json_file)
print(json_obj)
print(json_obj['id'])
print(json_obj['numbers'])

# {'id': '001', 'numbers': [1, 2, 3], 'colors': ['blue', 'yellow', 'red']}
# 001
# [1, 2, 3]


print("--- 辞書とリストの組み合わせをjsonに変換する ---")


"""
先ほどとは反対方向に、辞書とリストの組み合わせとjsonに変換する場合は
json.dumps()やjson.dump()を使います。
json.dumps()は文字列へ、json.dump()はファイルへ直接書き込みできます。
次の例はjson.dumps()を使って文字列へ変換しています。
"""

import json

python_obj = {'id': '001', 'numbers': [1, 2, 3], 'colors': ['blue', 'yellow', 'red']}
json_str = json.dumps(python_obj)
print(json_str)
print(type(json_str))

# {"id": "001", "numbers": [1, 2, 3], "colors": ["blue", "yellow", "red"]}
# <class 'str'>

"""
json.dumps()で辞書をjson文字列へ変換しています。
type(json_str)の出力結果を見ても分かる通り、ちゃんと文字列へ変換されていますね。
また、json.dump()は直接ファイルへjsonを書き込みたいときに使います。
"""

import json

python_obj = {'id': '001', 'numbers': [1, 2, 3], 'colors': ['blue', 'yellow', 'red']}
json_file = open('output.json', 'w')    # writeで開く
json.dump(python_obj, json_file)
json_file.close()

# output.json
# {"id": "001", "numbers": [1, 2, 3], "colors": ["blue", "yellow", "red"]}
