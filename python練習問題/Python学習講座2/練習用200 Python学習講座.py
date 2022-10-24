#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- jsonモジュール JSONのエンコードとデコード ---")


print("--- dict型からJSON文字列に変換 ---")


"""
dumpsによる辞書からJSONへの変換

json.dumpsを使用すると、dict型からJSONに変換することができます。
また、引数にindentを指定すると
指定した数だけスペースでインデントをつけた見やすい形に整形してくれます。
"""

import json

# dict型からJSoN文字列に変換する
dict_data = {"items": [{"id": 1, "name": "pen"},
 {"id": 2, "name": "apple"},
  {"id": 3, "name": "painapple"}], "status": "sell"}

# JSONの文字列形式
json_str = json.dumps(dict_data)
print(json_str)    
# {"items": [{"id": 1, "name": "pen"}, {"id": 2, "name": "apple"}, {"id": 3, "name": "painapple"}], "status": "sell"}

# インデントを付ける
json_str = json.dumps(dict_data, indent=2)
print(json_str)    
#   "items": [
#     {
#       "id": 1,
#       "name": "pen"
#     },
#     {
#       "id": 2,
#       "name": "apple"
#     },
#     {
#       "id": 3,
#       "name": "painapple"
#     }
#   ],
#   "status": "sell"
# }

"""
ASCIIエンコード

また、デフォルトではASCIIにエンコードされますので、
ASCIIエンコードしない場合はensure_ascii=Falseを指定します。
"""

import json

# 日本語が格納された辞書
dict_data = {"items": [{"id": 1, "name": "ペン"},
 {"id": 2, "name": "アップル"},
  {"id": 3, "name": "パイナップル"}], "status": "sell"}

# asciiエンコードする場合
json_str = json.dumps(dict_data, ensure_ascii=True)    
# 日本語部分が\u30da\u30f3のように出力される。
print(json_str)
# {"items": [{"id": 1, "name": "\u30da\u30f3"},
#  {"id": 2, "name": "\u30a2\u30c3\u30d7\u30eb"},
#  {"id": 3, "name": "\u30d1\u30a4\u30ca\u30c3\u30d7\u30eb"}], "status": "sell"}

# asciiエンコードしない場合
json_str = json.dumps(dict_data, ensure_ascii=False)
print(json_str)
# {"items": [{"id": 1, "name": "ペン"},
#  {"id": 2, "name": "アップル"},
#  {"id": 3, "name": "パイナップル"}], "status": "sell"}


print("--- loads JSON文字列から辞書に変換 ---")


"""
今度は逆にJSON文字列から辞書に変換してみましょう。
json.loadsを使用します。
"""

import json

# JSON文字列から辞書に変換する
json_str = '{"items": [{"id": 1, "name": "ペン"},\
 {"id": 2, "name": "アップル"},\
  {"id": 3, "name": "パイナップル"}], "status": "sell"}'
dict_data1 = json.loads(json_str)
print(type(dict_data1))    # <class 'dict'>
print(dict_data1)
# {'items': [{'id': 1, 'name': 'ペン'}, {'id': 2, 'name': 'アップル'}, {'id': 3, 'name': 'パイナップル'}], 'status': 'sell'}


print("--- load JSONファイルからdict型に変換 ---")


"""
また、JSONファイルの場合はread()で一旦文字列に変換しなくても
loadを使用することでファイルオブジェクトから辞書に変換することが可能となります。
"""

import json

# JSONファイルから辞書に変換する
f = open('json_file1.json', 'r', encoding='UTF-8')
dict_data2 = json.load(f)
print(type(dict_data2))    # <class 'dict'>
