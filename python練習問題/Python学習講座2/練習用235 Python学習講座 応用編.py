#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Redisの型 ソート済みセット型 ---")


"""
Redisにはセット型にスコアと呼ばれる数値を付加することができる
ソート済みセット型という型がサポートされています。
オンラインゲームの得点などに利用することができます。
全てのコマンドについては説明できませんのが、
基本的にはRedisコマンドを小文字にしたものがメソッドとして提供されています。
ソート済み型のRedisコマンドの詳細は以下ドキュメントを参考にしてください。

http://redis.shibu.jp/commandreference/sortedsets.html
"""


print("--- ソート済みセット型でランクを算出する ---")


"""
データの追加はzaddメソッドを使用します。
引数にキー、スコア、値を指定します。
サンプルを見てみましょう。ユーザーのスコアを登録するサンプルです。
最後にユーザーのランクをzrankで取得します。
"""


import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)


"""
# ユーザーとスコアを登録
r.zadd('users', 100, 'Yamada')
r.zadd('users', 105, 'Tanaka')
r.zadd('users', 95, 'Suzuki')
r.zadd('users', 80, 'Sato')

# 特定のユーザーのスコアを取得
r.zscore('users', 'Yamada')    # 100

# 特定のユーザーのランクを取得
r.zrank('users', 'Yamada')    # 2
"""

# redis-pyを使ったzaddコマンドの引数について (v3.2.0) より

"""
はじめに

インメモリKVS型DBのRedisをPythonから呼び出す方法として、
redis-pyモジュールを使うやり方があります。
このredis-pyにZADDと呼ばれるデータを格納するコマンドがあります。
このZADDの引数に変更があり、古い記事の呼び出し方ではエラーを吐くので、
新しい呼び出し方を共有します。


ZADDとは

SortedSet型でデータを格納するコマンドです。
SortedSet型は、その名の通り順序付けされた集合の型です。
各データがscoreと呼ばれる値を持っており、それを基にソートされます。


呼び出し方

これまではzadd(key, score, value)やzadd(key, value, score)
といった形でコマンドを叩いていましたが、現バージョンからは以下のようになりました。
"""

dict = {}

dict['Tanaka'] = 105
dict['Suzuki'] = 95
dict['Yamada'] = 100
dict['Sato'] = 80

dict
# {'Yamada': 100, 'Tanaka': 105, 'Suzuki': 95, 'Sato': 80}

"""
スコアに基づいたユーザーランクを簡単に算出することができます。
"""
