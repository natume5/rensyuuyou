#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Redisの型 ハッシュ型 ---")


"""
Redisにはハッシュと呼ばれる辞書っぽい型が用意されています。
全てのコマンドについては説明できませんのが、
基本的にはRedisコマンドを小文字にしたものがメソッドとして提供されています。
ハッシュ型のRedisコマンドの詳細は以下ドキュメントを参考にしてください。

http://redis.shibu.jp/commandreference/hashes.html
"""


print("--- Redisのハッシュ型 ---")


"""
ハッシュ型の注意点としては、以下の2点が挙げられます。

    文字列のみ使用可能
    ネストはサポートされていない

では操作をしてみましょう。
"""


print("--- ハッシュの基本操作 ---")


"""
データの挿入

hsetで単一の値を更新、hmsetで複数の値を更新できます。
以下のサンプルは、ユーザー情報を一時的に格納する例です。
"""

import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

# user01として名前とランクを格納
r.hmset('user01', {'name': 'Yamada', 'rank': 'gold'})

# user01の情報に都道府県名を追加
r.hset('user01', 'pref', 'Tokyo')


"""
データの取得

次にハッシュ型で挿入したデータをhgetメソッドを使用して取得してみましょう。
また、hmgetで複数のフィールドを取得することができます。
例えばuser01の情報を取得する場合、以下のように記述します。
"""

# 単一フィールドを取得
r.hget('user01', 'name')     # b'Yamada'

# hmgetで複数フィールドを取得
r.hmget('user01', 'name', 'rank')    # [b'Yamada', b'gold']

"""
その他、まとめて取得する際に使うものとして、
ハッシュの全てのキーを取得するhkeysメソッド、
全フィールドを取得するhvalsメソッド、
全てのフィールドとキーを取得するhgetallメソッドが挙げられます。
"""

r.hkeys('user01')    # [b'rank', b'name', b'pref']

r.hvals('user01')    # [b'gold', b'Yamada', b'Tokyo']

r.hgetall('user01')    #{b'name': b'Yamada', b'pref': b'Tokyo', b'rank': b'gold'}

"""
こういったメソッドの利用により、
Redisのハッシュ型ではRDBライクなデータ取得を行うことが可能です。
参照時のパフォーマンスを上げたい場合に利用を検討してみてください。
"""
