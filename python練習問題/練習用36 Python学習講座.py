#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- Python入門　setattr 属性の追加---")


"""
setattr

オブジェクトに属性を追加することができます。
第1引数に対象となるオブジェクト、第2引数に属性名、第3引数に属性値を設定します。
"""

class User():
	pass

obj = User()
setattr(obj, "name", "Kuro")

print(obj.name)

"""
.で追加しても良いのですが、setattrはdict型のループと相性が良いです。
よく見かけるテクニックとして、インスタンス生成時に属性が多くなる場合、
引数をdictにして属性を追加する、という方法があります。
"""

class User():
	def __init__(self, attrs):
		for k, v in attrs.items():
			setattr(self, k, v)

obj = User({"name": "Kuro", "age": 30, "memo": "very cool!"})
print(obj.name)    # Kuro
print(obj.age)    # 30
print(obj.memo)    # very cool!

"""
属性が多岐にわたる場合、引数で指定すると膨大になりますが、
この方法ならば可変で様々な属性を付加することができます。


補足 getattrとdelattr

補足として、setattrの兄弟、getattrとdelattrを紹介します。


getattr 属性の取得

引数で指定した属性を取得します。第1引数で対象オブジェクトを、第2引数で属性名を指定します。
また、第3引数でデフォルト値を設定できるのがメリットです。

当該の属性がない場合はデフォルト値が返されるため、属性存在検査を事前にする必要がなくなるわけです。

例えば、getattr(obj, 'name')は obj.nameと等価となります。

また、objにnameという属性がないことが予想され、デフォルト値を設定したい場合は
getattr(obj, 'name', 'Nameless')のように記述します。

デフォルト値がなく、指定した属性がない場合hAttributeErrorが送出されます。


delattr 属性の削除

属性を削除することができます。例えば、objというオブジェクトからnameという属性を削除する場合、
delattr(obj, "name")と記述します。
"""


print("--- Python入門　SQLite3入門---")


"""
PythonとSQLite3

SQLiteは冒頭で記述したとおり非常に軽量なデータベースの一種です。
現在バージョン3であるため、SQLite3と記述されることもあります。
SQLiteの最大のメリットはサーバープロセスを起動する必要がなく、ファイルで永続化することが可能です。
また、オンメモリで動作させることもでき、気軽にRDBを利用することが可能です。
Pythonは標準ライブラリが用意されており、簡単にSQLite3にアクセスすることができます。


接続とSQLの実行

sqlite3のインポート

まずは接続とSQLの実行方法について解説します。
使用するモジュールはsqlite3という名称で、標準ライブラリのためインストールは不要です。
以下でインポートすることができます。

import sqlite3

接続

接続は以下のように記述します。

接続
conn = sqlite3.connect('dbファイルパス')

指定したDBファイルが存在しない場合は自動で作成してくれるため、高い可搬性を実現することができます。
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

c.execute('CREATE TABLE articles  (id int, title varchar(1024),
body text, created datetime)')

なお、SQLiteとPythonとの型の対応は以下のようになります。
Python の型 	         SQLite の型
None 	             NULL
int 	             INTEGER
float 	             REAL
str 	             TEXT
bytes 	             BLOB


CREATE文とINSERT文のサンプル

それでは接続からSQL実行までのサンプルです。
以下のサンプルはカレントディレクトリ直下にexample.dbというdbファイルを作成し、CREATE文でテーブルを作成後、
INSERT文でデータを挿入してみます。
"""

import sqlite3

# 接続。なければDBを作成する。
conn = sqlite3.connect('example.db')

# カーソルを取得
c = conn.cursor()

# テーブルを作成
# c.execute('CREATE TABLE articles (id int, title varchar(1024),body text, created datetime)')
c.execute("SELECT * FROM sqlite_master WHERE type='table' and name='articles'")
if not c.fetchone():
    c.execute('CREATE TABLE articles  (id int, title varchar(1024), body text, \
    	created datetime)')

# Insert実行
c.execute("INSERT INTO articles VALUES (1,'今朝のおかず','魚を食べました','2020-02-01 00:00:00')")
c.execute("INSERT INTO articles VALUES (2,'今日のお昼ごはん','カレーを食べました','2020-02-02 00:00:00')")
c.execute("INSERT INTO articles VALUES (3,'今夜の夕食','夕食はハンバーグでした','2020-02-03 00:00:00')")

# コミット
conn.commit()

# コネクションをクローズ
conn.close()

"""
実際、上のサンプルでテーブル作成とデータ挿入がされたことを以下のsqlite3のコマンドで確認することができます。
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

いずれも結果レコードはタプル形式で取得できます。サンプルで確認してみましょう。
"""

# import sqlite3

# DBに接続する。なければDBを作成する。
conn = sqlite3.connect('example.db')

# カーソルを取得する
c = conn.cursor()

# 1. カーソルをイテレータ―(iterator)として扱う
c.execute('select * from articles')
for row in c:
	# rowオブジェクトでデータが取得できる。タプル型の結果が取得
	print(row)

# 2. fetchallで結果リストを取得する
c.execute('select * from articles')
for row in c.fetchall():
	print(row)

# 3. fetchoneで1件ずつ取得する
c.execute('select * from articles')
print(c.fetchone())    # 1レコード目が取得
print(c.fetchone())    # 2レコード目が取得


# コネクションをクローズする
conn.close()

"""
なお、fetchoneを実行した際、レコードがない場合はNoneが返されます。


トランザクション

分離レベルの指定

SQLiteは軽量DBとはいえ、分離レベルを指定することができます。
デフォルトではトランザクションが有効になっていますが、
auto commitを使用する場合はコネクションオブジェクトのisolation_levelをNoneに設定します。
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


TIPS

最後にいくつかのTIPSを掲載します。

テーブルの有無を確認する

さて、このページの最初のコードですが同じコードを2回以上実行すると
CREATE文が既に存在するテーブルと重複してエラーが発生してしまいます。
以下のようにSELECT文と組み合わせると、テーブルの存在判定をすることができます。

# テーブルを作成
c.execute("SELECT * FROM sqlite_master WHERE type='table' and 
name='articles'")
if not c.fetchone():
    c.execute('CREATE TABLE articles  (id int, title 
    varchar(1024), body text, created datetime)')


テーブル一覧を取得する

sqlite3はsqlite_masterにメタ情報が格納されています。
where条件にtype='table'を指定することでテーブル一覧を取得することが可能です。

c.execute("select * from sqlite_master where type='table'")
for row in c.fetchall():
    print(row)


sqlite3.Rowによるカラム名による取得

sqlite3.Rowを使用するとSELECT結果をカラム名で指定して取得することができます。
コネクションオブジェクトのrow_factoryにsqlite3.Rowを設定します。
"""

# import sqlite3

# DBに接続する。なければDBを作成する。
conn = sqlite3.connect('example.db')
conn.row_factory = sqlite3.Row    # row_factoryにsqlite3.Rowを認定

# カーソルオブジェクトを取得する
c = conn.cursor()

c.execute('select * from articles')
for row in c:
	print(row['id'])    # カラム名でアクセスすることが出来る。

# コネクションをクローズする
conn.close()


