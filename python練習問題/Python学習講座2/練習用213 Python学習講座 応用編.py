#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- mysqlclient Python3でMySQLに接続する ---")


print("--- ドライバーについて ---")


"""
Python3でMySQLに接続するドライバーは決め手がない、と言われていますが、当サイトではmysqlclientをおすすめします。これはPython2系でよく利用されていたMySQLdbからフォークされたものです。

mysqlclientのインストールはpipで可能です。linux環境では事前に以下のライブラリをインストール必要があります。

# debian系
sudo apt-get install python-dev default-libmysqlclient-dev
sudo apt-get install python3-dev

# rhel系
sudo yum install python-devel mysql-devel
sudo yum install python3-devel

pipは以下の通りです。

pip install mysqlclient
"""


print("--- ドライバーについて ---")


"""
接続及びSELECT文の実行

早速接続してクエリを投げてみましょう。
MySQLdbをインポートし、MySQLdb.connectで接続が可能となります。
引数でユーザ、パスワード、DBホスト、DB、文字コードを指定することができます。

[接続 & selectサンプル]

import MySQLdb

def db_sample():
    """""" 接続サンプル """"""

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


connection = MySQLdb.connect(
... user = 'root',
... passwd = 'mininoteSQL3G',
... host = 'localhost',
... db = 'sample',
... charset = 'utf8')
>>> cur = connection.cursor()
>>> sql = "select id, body, post_code, created from posts"
>>> cur.execute(sql)
>>> cur.execute("DROP TABLE IF EXISTS name_age_list")
0
>>> cur.execute(""""""CREATE TABLE name_age_list(
... id INT(11) AUTO_INCREMENT NOT NULL,
... name VARCHAR(30) NOT NULL COLLATE utf8mb4_unicode_ci,
... age INT(3) NOT NULL,
... PRIMARY KEY (id))"""""")
0
>>>cur.execute(""""""INSERT INTO name_age_list (name, age)
... VALUES ('タロー', '25'),
... ('ジロー', '23'),
... ('サブロー', '21')"""""")
3
>>>cur.execute("SELECT * FROM name_age_list")
3
>>>for row in cur:
...     print(row)
...
(1, 'タロー', 25)
(2, 'ジロー', 23)
(3, 'サブロー', 21)
>>> connection.commit()
>>> connection.close()


カーソルに対し、fetchallを利用すると、行がすべて取得できます。
rowはタプル形式です。以下のような形で出力されます。
[実行結果]
(1, 'aaaaaaaaaa', 1, '2016-10-16 22:51:55')
(2, 'bbbbbbbbbb', 1, '2016-10-16 22:52:03')
(3, 'cccccccccc', 1, '2016-10-16 22:52:06')
(4, 'dddddddddd', 2, '2016-10-16 22:52:11')
(5, 'eeeeeeeeee', 2, '2016-10-16 22:52:17')

先頭の一行だけ取得したい場合は以下のように、fetchoneを利用します。

    row = cur.fetchone()
"""
































































