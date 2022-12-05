#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Redisの型 セット型 ---")


"""
セット型は文字列型の順不同の集合です。
PythonのSetとよく似ていますが、やはりこちらも論理演算ができる点が特徴です。
また、異なる集合間で要素を移動させることが可能ですので、
なんらかのグループを扱うこともできます。
全てのコマンドについては説明できませんのが、
基本的にはRedisコマンドを小文字にしたものがメソッドとして提供されています。
セット型のRedisコマンドの詳細は以下ドキュメントを参考にしてください。

http://redis.shibu.jp/commandreference/sets.html
"""


print("--- セット型の基本操作 ---")


"""
ではまず、セット型の基本操作です。
要素の追加、取得、削除は以下のように行います。
"""

import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

# 集合を追加
r.sadd('fruits', 'apple', 'orange', 'banana')

# 要素数を取得
r.scard('fruits')    # 3

# 指定した要素が存在するかどうか調べる
r.sismember('fruits', 'apple')    # True

# 要素を全て取得する
r.smembers('fruits')    # {b'apple', b'banana', b'orange'}

# 要素をpopする(取り出して削除)
r.spop('fruits')    # b'apple'

# 要素を削除する
r.srem('fruits', 'banana')


print("--- セット型の論理演算 ---")


"""
2つのセット型で論理演算をしてみましょう。
sunion、sinter、sdiffメソッドでそれぞれ
論理和、論理積、論理差が実行できます。
引数に演算対象のセット型のキーを指定します。
サンプルでは果物の名前が格納されている2つの集合
fruits1、fruits2に対し、論理和、論理積、論理差の演算をしてみます。
"""

# セット型を定義
r.sadd('fruits1', 'apple', 'orange', 'banana')
r.sadd('fruits2', 'banana', 'orange', 'strawberry', 'cherry')

# 論理和
r.sunion('fruits1', 'fruits2')
# {b'apple', b'banana', b'cherry', b'orange', b'strawberry'}

# 論理積
r.sinter('fruits1', 'fruits2')
# {b'banana', b'orange'}

# 論理差
r.sdiff('fruits1', 'fruits2')
# {b'apple'}

"""
集合の論理演算もRDBにはないRedisの強みの1つと言えるでしょう。
"""
