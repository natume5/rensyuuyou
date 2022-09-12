#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- SQLite3入門---")


"""
SQLiteはデータベースの一種で簡単に扱うことができます。
MySQL等のRDBMSと比較すると機能は限定的ですが、
圧倒的なスピードが特徴的で、大量データに対する分析で活用することもできます。
Pythonには標準ライブラリで軽量DBのsqlite3を使用するモジュールが提供されています。
このページでは、そのsqlite3モジュールについて解説します。

PythonとSQLite3

SQLiteは冒頭で記述したとおり非常に軽量なデータベースの一種です。
現在バージョン3であるため、SQLite3と記述されることもあります。
SQLiteの最大のメリットはサーバープロセスを起動する必要がなく、
ファイルで永続化することが可能です。また、オンメモリで動作させることもでき、
気軽にRDBを利用することが可能です。Pythonは標準ライブラリが用意されており、
簡単にSQLite3にアクセスすることができます。


接続とSQLの実行
sqlite3のインポート

まずは接続とSQLの実行方法について解説します。使用するモジュールはsqlite3という名称で、
標準ライブラリのためインストールは不要です。以下でインポートすることができます。

import sqlite3


接続

接続は以下のように記述します。

接続
conn = sqlite3.connect('dbファイルパス')

指定したDBファイルが存在しない場合は自動で作成してくれるため、
高い可搬性を実現することができます。また、特別な名前である
 :memory: を使うとRAM上にデータベース、
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

c.execute('CREATE TABLE articles  (id int, title varchar(1024), body text, created datetime)')

なお、SQLiteとPythonとの型の対応は以下のようになります。

Python の型 	      SQLite の型
None 	          NULL
int 	          INTEGER
float 	          REAL
str 	          TEXT
bytes 	          BLOB


CREATE文とINSERT文のサンプル

それでは接続からSQL実行までのサンプルです。
以下のサンプルはカレントディレクトリ直下にexample.dbというdbファイルを作成し、
CREATE文でテーブルを作成後、INSERT文でデータを挿入してみます。
"""
"""
import sqlite3

# 接続。なければDBを作成する。
conn = sqlite3.connect("example.db")

# カーソルを取得
c = conn.cursor()

c.execute('CREATE TABLE articles (id int, title varchar(1024),body text, crated datatime)')

# Insert実行
c.execute("INSERT INTO articles VALUES (1, '今朝のおかず','魚を食べました','2020-02-01 00:00:00')")
c.execute("INSERT INTO articles VALUES (2, '今日のお昼ごはん','カレーを食べました','2020-02-02 00:00:00')")
c.execute("INSERT INTO articles VALUES (3, '今夜の夕食','夕食はハンバーグでした','2020-02-03 00:00:00')")

# コミット
conn.commit()

# コネクションをクローズ
conn.close()
"""

"""
実際、上のサンプルでテーブル作成とデータ挿入がされたことを以下のsqlite3のコマンドで
確認することができます。お使いの環境に適宜sqlite3をインストールしてください。

$ sqlite3 example.db
.tables
articles

select * from articles;
1|今朝のおかず|魚を食べました|2020-02-01 00:00:00
2|今日のお昼ごはん|カレーを食べました|2020-02-02 00:00:00
3|今夜の夕食|夕食はハンバーグでした|2020-02-03 00:00:00

SELECT文の実行

カーソルを取得後はexecuteメソッドでSELECT文を実行することができます。
実行結果をカーソルから取得する方法は大きく分けると3つあります。

    カーソルをイテレータ (iterator) として扱う
    fetchallで結果リストを取得する
    fetchoneで1件ずつ取得する

いずれも結果レコードはタプル形式で取得できます。サンプルで確認してみましょう。
"""
"""
import sqlite3

# DBに接続する。なければDBを作成する。
conn = sqlite3.connect('example.db')

# カーソルを取得する
c = conn.cursor()

# 1. カーソルをイテレータ (iterator) として扱う
c.execute('select * from articles')
for row in c:
    # rowオブジェクトでデータが取得できる。タプル型の結果が取得
    print(row)
# (1, '今朝のおかず', '魚を食べました', '2020-02-01 00:00:00')
# (2, '今日のお昼ごはん', 'カレーを食べました', '2020-02-02 00:00:00')
# (3, '今夜の夕食', '夕食はハンバーグでした', '2020-02-03 00:00:00')

# 2. fetchallで結果リストを取得する
c.execute('select * from articles')
for row in c.fetchall():
    print(row)
# (1, '今朝のおかず', '魚を食べました', '2020-02-01 00:00:00')
# (2, '今日のお昼ごはん', 'カレーを食べました', '2020-02-02 00:00:00')
# (3, '今夜の夕食', '夕食はハンバーグでした', '2020-02-03 00:00:00')

# 3. fetchoneで1件ずつ取得する
c.execute('select * from articles')
print(c.fetchone()) # 1レコード目が取得
# (1, '今朝のおかず', '魚を食べました', '2020-02-01 00:00:00')

print(c.fetchone()) # 2レコード目が取得
# (2, '今日のお昼ごはん', 'カレーを食べました', '2020-02-02 00:00:00')

print(c.fetchone()) # 3レコード目が取得
(3, '今夜の夕食', '夕食はハンバーグでした', '2020-02-03 00:00:00')

# コネクションをクローズする
conn.close()

なお、fetchoneを実行した際、レコードがない場合はNoneが返されます。
"""

"""
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
"""
"""
TIPS

最後にいくつかのTIPSを掲載します。
テーブルの有無を確認する

さて、このページの最初のコードですが同じコードを2回以上実行すると
CREATE文が既に存在するテーブルと重複してエラーが発生してしまいます。
以下のようにSELECT文と組み合わせると、テーブルの存在判定をすることができます。

# テーブルを作成
c.execute("SELECT * FROM sqlite_master WHERE type='table' and name='articles'")
if not c.fetchone():
    c.execute('CREATE TABLE articles  (id int, title varchar(1024), body text, created datetime)')

テーブル一覧を取得する

sqlite3はsqlite_masterにメタ情報が格納されています。
where条件にtype='table'を指定することでテーブル一覧を取得することが可能です。

c.execute("select * from sqlite_master where type='table'")
for row in c.fetchall():
    print(row)
# ('table', 'articles', 'articles', 2, 'CREATE TABLE articles (id int, title varchar(1024), body text, created datetime)')   

sqlite3.Rowによるカラム名による取得

sqlite3.Rowを使用するとSELECT結果をカラム名で指定して取得することができます。
コネクションオブジェクトのrow_factoryにsqlite3.Rowを設定します。
"""
"""
import sqlite3
 
# DBに接続する。なければDBを作成する。
conn = sqlite3.connect('example.db')
conn.row_factory = sqlite3.Row # row_factoryにsqlite3.Rowを設定

# カーソルオブジェクトを取得する
c = conn.cursor()

c.execute('select * from articles')
for row in c:
    print(row['id']) # カラム名でアクセスすることができる。n
# 1
# 2
# 3

# コネクションをクローズする
conn.close()
"""


print("---mysqlclient Python3でMySQLに接続する---")


"""
ドライバーについて

Python3でMySQLに接続するドライバーは決め手がない、と言われていますが、
当サイトではmysqlclientをおすすめします。これはPython2系でよく利用されていた
MySQLdbからフォークされたものです。

mysqlclientのインストールはpipで可能です。
linux環境では事前に以下のライブラリをインストール必要があります。

# debian系
sudo apt-get install python-dev default-libmysqlclient-dev
sudo apt-get install python3-dev

# rhel系
sudo yum install python-devel mysql-devel
sudo yum install python3-devel

pipは以下の通りです。

pip install mysqlclient
"""
"""
接続及びSELECT文の実行

早速接続してクエリを投げてみましょう。
MySQLdbをインポートし、MySQLdb.connectで接続が可能となります。
引数でユーザ、パスワード、DBホスト、DB、文字コードを指定することができます。

[接続 & selectサンプル]

import MySQLdb

def db_sample():
    """" 接続サンプル """"

    # 接続する 
    con = MySQLdb.connect(
            user='db user',
            passwd='db password',
            host='localhost',
            db='sample',
            charset="utf8")

    # カーソルを取得する
    cur= con.cursor()
    
    # クエリを実行する
    sql = "select id, body, post_code, created from posts"
    cur.execute(sql)

    # 実行結果をすべて取得する
    rows = cur.fetchall()
    
    # 一行ずつ表示する
    for row in rows:
        print(row)

    cur.close()
    con.close()

if __name__ == "__main__":
    db_sample()

カーソルに対し、fetchallを利用すると、行がすべて取得できます。rowはタプル形式です。
以下のような形で出力されます。

[実行結果]
(1, 'aaaaaaaaaa', 1, '2016-10-16 22:51:55')
(2, 'bbbbbbbbbb', 1, '2016-10-16 22:52:03')
(3, 'cccccccccc', 1, '2016-10-16 22:52:06')
(4, 'dddddddddd', 2, '2016-10-16 22:52:11')
(5, 'eeeeeeeeee', 2, '2016-10-16 22:52:17')

先頭の一行だけ取得したい場合は以下のように、fetchoneを利用します。

    row = cur.fetchone()

"""
"""
SQL実行時にパラメータを指定する
では次に、SQLにパラメーターを渡してみましょう。

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
import MySQLdb
 
def db_sample():
    """" 接続サンプル """"
 
    # 接続する 
    con = MySQLdb.connect(
            user='db user',
            passwd='db password',
            host='localhost',
            db='sample',
            charset="utf8")
 
    # カーソルを取得する
    cur= con.cursor()
     
    # クエリを実行する
    sql = "select id, body, post_code, created from posts where id > %s and post_code in %s"
    cur.execute(sql, (1, [1, 2, 3], ))
 
    # 実行結果をすべて取得する
    rows = cur.fetchall()
     
    # 一行ずつ表示する
    for row in rows:
        print(row)
 
    cur.close()
    con.close()
 
if __name__ == "__main__":
    db_sample()
SQL内でパラメータにしたい箇所は%sにし、
cur.executeの第2引数にパラメータをタプルで指定します。
in句の場合、リストが利用できます。
"""
"""
更新系
最後に更新系の処理です。といっても、select文と同様、executeメソッドでsqlを実行すればOKです。

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
import MySQLdb
 
def db_sample():
    """" 接続サンプル """"
 
    # 接続する 
    con = MySQLdb.connect(
            user='db user',
            passwd='db password',
            host='localhost',
            db='sample',
            charset="utf8")
 
    # カーソルを取得する
    cur= con.cursor()
     
    # 更新系SQLを実行する
 
    # insert
    insert_sql = "insert into `sample`.`posts` (`body`, `post_code`, `created`) VALUES (%s, %s, now());"
    cur.execute(insert_sql, ("body text" , 3, ))
     
    update_sql = "update `sample`.`posts` SET `post_code`='3' WHERE `id`=%s;"
    cur.execute(update_sql, (6, ))
 
    delete_sql = "delete from `sample`.`posts` where id = %s;"
    cur.execute(delete_sql, (6, ))
 
 
    cur.close()
    con.close()
 
if __name__ == "__main__":
    db_sample()
"""
