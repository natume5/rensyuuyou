#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説 ---")
print("--- データベースの使い方（SQLite）  ---")


"""
データ解析や機械学習をする場合はデータの蓄積が必要になりますが、
それを簡単に行えるのがSQLiteの魅力です。
SQLiteは軽量データベースの一つで、Pythonの標準ライブラリとして準備されています。
ここでは「SQLiteって何？」「どうやって使うの？」「データを登録したり取り出したりしてみたい」
といった方へ、SQLiteの使い方を解説します。
"""


print("--- SQLiteの使い方 ---")


"""
実際にSQLiteを使ってみましょう。
ここではデータベースの作成やテーブルの作成、
データの登録・更新・削除・参照といった処理を解説します。


データベースの作成とカーソルの取得

connect()の引数にデータファイル名を渡すことで、データベースを作成できます。
既に存在するデータベースの場合は単純に接続するだけ、
新しいデータベースの場合はデータを保存するためのデータファイルを作成します。
"""

import sqlite3

db = sqlite3.connect('example2.db')
c = db.cursor()

"""
今回はexample.dbというデータファイルを作成しました。
connect()の戻り値はconnectionオブジェクトが返却され、これがデータベースを表しています。
また、db作成後にcursor()を呼び出しています。
このカーソルはデータベース技術の一つで、検索結果からデータを処理するための仕組みです。


テーブルを作成する

まずはデータを格納するためのテーブルを作成しましょう。
SQLを実行するにはCorsorオブジェクトのexecute()を使います。
"""

c.execute('CREATE TABLE user(id integer, name text)')
c.close()    # 最後にカーソルを閉じる

# データベースの作成とカーソルの取得までは全て共通なので省略します

"""
上記の例ではuserというテーブルを作成しました。
作成したテーブルやデータはデータファイルに保存されるので、
上記のコードを2回実行すると「既にuserテーブルは存在している」というエラーになります。


データを登録する

データを登録する場合も同じくexecute()を使います。
ただし、テーブル作成と違いINSERTはDML（データ操作言語）なので、
コミット処理が必要になります（これをしないとデータが登録されません）。
コミット処理はConnectionオブジェクトのcommit()を使います。
"""

db = sqlite3.connect('example2.db')
c = db.cursor()

c.execute('INSERT INTO user VALUES(1, "user_1")')
db.commit()    # これが必要
c.close()


"""
データを複数行同時に登録する

execute()で1件ずつデータを登録するのも良いですが、
executemany()を使うことでより簡潔に複数行のデータを登録できます。
"""

import sqlite3

db = sqlite3.connect('example2.db')
c = db.cursor()

data = [
    (2, 'user_2'),
    (3, 'user_3'),
    (4, 'user_4'),
    (5, 'user_5'),
]

c.executemany('INSERT INTO user VALUES(?, ?)', data)
db.commit()
c.close()


"""
登録したデータを参照する

実際にデータが登録されているかを確認してみましょう。
SELECTで取得したデータを取り出すにはfetchall()を使います。
"""

import sqlite3

db = sqlite3.connect('example2.db')
c = db.cursor()

r = c.execute('SELECT * FROM user')
print(r.fetchall())

# [(1, 'user_1'), (2, 'user_2'), (3, 'user_3'), (4, 'user_4'), (5, 'user_5')]

"""
fetchall()で取得したデータはタプルのリスト形式で返却されます。
また、forを使えばfetchall()を使わずに取得したデータにアクセスできます。
"""

import sqlite3

db = sqlite3.connect('example2.db')
c = db.cursor()

c.execute('SELECT * FROM user')
for row in c:
    print(row[0], row[1])
# 1 user_1
# 2 user_2
# 3 user_3
# 4 user_4
# 5 user_5


"""
上記の例ではデータがタプルで返ってくるため、
row[0]のようにインデックス番号を指定する必要がありました。
これだとどのカラムを参照しているのか分かりづらいので、
カラム名で取り出せるように変更してみましょう。
"""

import sqlite3

db = sqlite3.connect('example2.db')
db.row_factory = sqlite3.Row    # これが必要
c = db.cursor()

c.execute('SELECT * FROM user')
for row in c:
    print(row["id"], row["name"])
# 1 user_1
# 2 user_2
# 3 user_3
# 4 user_4
# 5 user_5

"""
sqlite3.Rowオブジェクトをdbのrow_factoryに設定することで、
SELECTの結果をカラム名で取得できるようになります。


データの更新と削除

登録されているデータを更新したり、削除する場合は、登録のときと同じくexecute()を使います。 
"""

# import sqlite3

def print_user_table(c):
    c.execute('SELECT * FROM user')
    for row in c:
        print(row['id'], row['name'])

db = sqlite3.connect('example2.db')
db.row_factory = sqlite3.Row
c = db.cursor()
print('更新前')
print_user_table(c)
c.execute('UPDATE user SET name = "update_user" WHERE id=2')    # 更新
c.execute('DELETE FROM user WHERE id=4')    # 削除
db.commit()
print('更新後')
print_user_table(c)
c.close()
# 更新前
# 1 user_1
# 2 user_2
# 3 user_3
# 4 user_4
# 5 user_5

# 更新後
# 1 user_1
# 2 update_user
# 3 user_3
# 5 user_5

"""
上記の例ではidが2のユーザのnameを「update_user」に変更し、idが4のユーザを削除しています。
"""


print("--- SQLiteのエラー処理 ---")


"""
一意キーエラーや外部参照エラーなど、データベース処理にエラーはつきものです。
データベースとやり取りをする時は基本的にtry〜exceptで例外処理を入れておきましょう。
SQLiteのエラー内容はsqlite3.errorから取得できます。
"""

# import sqlite3

db = sqlite3.connect('example2.db')
db.row_factory = sqlite3.Row
c = db.cursor()

try:
    c.execute('CREATE TABLE user(id integer, name text)')
    # 既に作成されているテーブルを作成しようとしています
except sqlite3.Error as e:
    print('SQLite Error: ' + e.args[0])     # SQLite Error: table user already exists
c.close()

"""
userテーブルはすでに作成されているので、table user already existsが返却されました。
"""
