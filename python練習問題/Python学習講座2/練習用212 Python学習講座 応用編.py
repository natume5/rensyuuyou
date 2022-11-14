#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- SQLite3入門 ---")


"""
SQLiteはデータベースの一種で簡単に扱うことができます。
MySQL等のRDBMSと比較すると機能は限定的ですが、
圧倒的なスピードが特徴的で、大量データに対する分析で活用することもできます。
Pythonには標準ライブラリで軽量DBのsqlite3を使用する
モジュールが提供されています。
このページでは、そのsqlite3モジュールについて解説します。
"""


print("--- PythonとSQLite3 ---")


"""
SQLiteは冒頭で記述したとおり非常に軽量なデータベースの一種です。
現在バージョン3であるため、SQLite3と記述されることもあります。
SQLiteの最大のメリットはサーバープロセスを起動する必要がなく、
ファイルで永続化することが可能です。
また、オンメモリで動作させることもでき、気軽にRDBを利用することが可能です。
Pythonは標準ライブラリが用意されており、
簡単にSQLite3にアクセスすることができます。
"""


print("--- 接続とSQLの実行 ---")


"""
sqlite3のインポート

まずは接続とSQLの実行方法について解説します。
使用するモジュールはsqlite3という名称で、
標準ライブラリのためインストールは不要です。
以下でインポートすることができます
"""

import sqlite3

"""
接続

接続は以下のように記述します。
接続
conn = sqlite3.connect('dbファイルパス')

指定したDBファイルが存在しない場合は自動で作成してくれるため、
高い可搬性を実現することができます。
また、特別な名前である :memory: を使うとRAM上にデータベース、
いわゆるインメモリ（若しくはオンメモリ）で作ることもできます。

カーソルの取得とSQLの実行

コネクションからカーソルを取得し、excecuteメソッドでSQLを実行します。
SELECT文の結果取得については後述します。

SQL実行
c = conn.cursor()
c.execute()
テーブル作成と型

上のexecuteの中のSQL文はCREATE文のようなDDLを指定することが可能です。
テーブルを作成する場合、例えば以下のようにCREATE文を実行します。
"""

"""
c.execute('CREATE TABLE articles (id int, title varchar(1024),\
 body text, created datetime)')
"""

"""
なお、SQLiteとPythonとの型の対応は以下のようになります。

Python の型 	SQLite の型
None 	    NULL
int 	    INTEGER
float 	    REAL
str 	    TEXT
bytes 	    BLOB

CREATE文とINSERT文のサンプル

それでは接続からSQL実行までのサンプルです。
以下のサンプルはカレントディレクトリ直下にexample.dbというdbファイルを作成し、
CREATE文でテーブルを作成後、INSERT文でデータを挿入してみます。
"""

import sqlite3

# 接続。なければDBを作成する。
conn = sqlite3.connect('example2.db')

# カーソルを取得
c = conn.cursor()

"""
# テーブルを作成
c.execute('CREATE TABLE articles (id int, title varchar(1024),body text, created datetime)')
"""
# テーブルを作成
c.execute("SELECT * FROM sqlite_master WHERE type='table' and name='articles'")
if not c.fetchone():
    c.execute('CREATE TABLE articles  (id int, title varchar(1024), body text, created datetime)')


# Insert実行
c.execute("INSERT INTO articles VALUES (1,'今朝のおかず',\
	'魚を食べました','2020-02-01 00:00:00')")
c.execute("INSERT INTO articles VAlUES (2,'今日のお昼ごはん',\
	'カレーを食べました','2020-02-02 00:00:00')")
c.execute("INSERT INTO articles VALUES (3,'今夜の夕食',\
	'夕食はハンバーグでした','2020-02-03 00:00:00')")

# コミット
conn.commit()

# コネクションをクローズ
conn.close()

"""
実際、上のサンプルでテーブル作成とデータ挿入がされたことを
以下のsqlite3のコマンドで確認することができます。
お使いの環境に適宜sqlite3をインストールしてください。

$ sqlite3 example.db
.tables

select * from articles;


SELECT文の実行

カーソルを取得後はexecuteメソッドでSELECT文を実行することができます。
実行結果をカーソルから取得する方法は大きく分けると3つあります。

    カーソルをイテレータ (iterator) として扱う
    fetchallで結果リストを取得する
    fetchoneで1件ずつ取得する

いずれも結果レコードはタプル形式で取得できます。
サンプルで確認してみましょう。
"""

import sqlite3

# DBに接続する。なければDBを作成する。
conn = sqlite3.connect('example2.db')

# カーソルを取得
c = conn.cursor()

# 1.カーソルをイテレータ(iterator)として扱う
c.execute('select * from articles')
for row in c:
	# rowオブジェクトでデータが取得できる。タプル型の結果が取得
	print(row)

# 2.fetchallで結果リストを取得
c.execute('select * from articles')
for row in c.fetchall():
	print(row)

# 3.fetchoneで1件ずつ取得
c.execute('select * from articles')
print(c.fetchone())    # 1レコード目が取得
print(c.fetchone())    # 2レコード目が取得


"""
# コネクションをクローズする
conn.close()
"""

"""
なお、fetchoneを実行した際、レコードがない場合はNoneが返されます。
"""


print("--- トランザクション ---")


"""
分離レベルの指定

SQLiteは軽量DBとはいえ、分離レベルを指定することができます。
デフォルトではトランザクションが有効になっていますが、
auto commitを使用する場合はコネクションオブジェクトの
isolation_levelをNoneに設定します。
なお、インスタンス生成時に引数で指定することも可能です。

# auto commitを有効にする

# コネクション生成時に指定する場合
conn = sqlite3.connect(dbpath, isolation_level=None)

# 生成後に指定する場合
conn.isolation_level = None

ロールバック

ロールバックする際はrollbackメソッドを使用します。

conn.rollback()

auto commit以外にはDEFERRED、IMMEDIATE、EXCLUSIVEが指定できます。
"""


print("--- TIPS ---")


"""
最後にいくつかのTIPSを掲載します。
テーブルの有無を確認する

さて、このページの最初のコードですが
同じコードを2回以上実行すると
CREATE文が既に存在するテーブルと重複してエラーが発生してしまいます。
以下のようにSELECT文と組み合わせると、
テーブルの存在判定をすることができます。

# テーブルを作成
c.execute("SELECT * FROM sqlite_master WHERE type='table' and name='articles'")
if not c.fetchone():
    c.execute('CREATE TABLE articles  (id int, title varchar(1024), body text, created datetime)')


テーブル一覧を取得する

sqlite3はsqlite_masterにメタ情報が格納されています。
where条件にtype='table'を指定することで
テーブル一覧を取得することが可能です。

c.execute("select * from sqlite_master where type='table'")
for row in c.fetchall():
    print(row)


sqlite3.Rowによるカラム名による取得

sqlite3.Rowを使用するとSELECT結果を
カラム名で指定して取得することができます。
コネクションオブジェクトのrow_factoryにsqlite3.Rowを設定します。
"""

import sqlite3

# DBに接続する。なければDBを作成する。
con = sqlite3.connect('example2.db')
conn.row_factory = sqlite3.Row    # row_factoryにsqlite3.Rowを設定


# カーソルオブジェクトを取得する
c = conn.cursor()

c.execute('select * from articles')
for row in c:
	print(row['id'])    # カラム名でアクセスすることが出来る

# コネクションをクローズする
conn.close()




print("--- まにゅまるスクリプトより ---")


print("--- 【SQlite3】”Cannot operate on a closed database.” と出る時の対処法 ---")


"""
症状

conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute('select * from XXXX where post_content=?;', (post_contain_plane_format,))
conn.commit()

cur.close()
conn.close()

Python3でSQLite3を操作中、
ProgrammingError："Cannot operate on a closed database."
と表示される。


対策

閉じたデータベースでは操作できません、ということらしい。

確認したら、try-except文の分岐内でconn.close()を使用していた。
VSでコード複製してたら間違えてとっちゃってたみたい。。

解決方法は主に以下の二通りで、

conn.cursor()

でデータベースをオープンな状態に戻すか、

conn.close()

の削除ですね。

sqlite3.connectは、なるべくスクリプトの最後でのみ閉じるようにしましょう。

以上、”Cannot operate on a closed database.”
エラーの解決方法でした。

"""
