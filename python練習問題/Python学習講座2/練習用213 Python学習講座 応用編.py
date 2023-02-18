#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- mysqlclient Python3でMySQLに接続する ---")


print("--- ドライバーについて ---")


"""
Python3でMySQLに接続するドライバーは決め手がない、と言われていますが、
当サイトではmysqlclientをおすすめします。
これはPython2系でよく利用されていたMySQLdbからフォークされたものです。
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



>>> import MySQLdb
>>> connection = MySQLdb.connect(
... user = 'root',
... passwd = 'mininoteSQL3G',
... host = 'localhost',
... db = 'sample',
... charset = 'utf8')
>>> cur = connection.cursor()
>>> sql = 'select id, body, post_code, created from posts'
>>> for result in cur.fetchall():
...     print(result)
...
(1, 'タロー', 25)
(2, 'ジロー', 23)
(3, 'サブロー', 21)
>>> cur.execute("DROP TABLE IF EXISTS blog")
0
>>> cur.execute(""""""CREATE TABLE blog(
... id int,
... title varchar(100),
... body text,
... created datetime
... )"""""")
0
>>> cur.execute("INSERT INTO blog VALUES(1, 'a', 'b', '2022-11-13')")
1
>>> cur.execute("INSERT INTO blog VALUES(2, 'c', 'd', '2022-11-13')")
1
>>> cur.execute("INSERT INTO blog VALUES(3, 'e', 'f', '2022-11-13')")
1
>>> cur.execute("SELECT * FROM blog")
3
>>> print(cur.fetchall())
((1, 'a', 'b', datetime.datetime(2022, 11, 13, 0, 0)), (2, 'c', 'd', datetime.datetime(2022, 11, 13, 0, 0)), (3, 'e', 'f', datetime.datetime(2022, 11, 13, 0, 0)))
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


print("--- SQL実行時にパラメータを指定する ---")


"""
では次に、SQLにパラメーターを渡してみましょう。

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


print("--- 更新系 ---")


"""
最後に更新系の処理です。といっても、select文と同様、
executeメソッドでsqlを実行すればOKです。

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


"""
D:\テキストドキュメント１\IT・エンジニア・プログラミング\sublime text3関係\python練習問題\Python学習講座2>mysql -u root -p
Enter password: *************
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 33
Server version: 8.0.31 MySQL Community Server - GPL

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mydb               |
| mysql              |
| performance_schema |
| sample             |
| shop               |
| sys                |
+--------------------+
7 rows in set (2.22 sec)

mysql> use shop
Database changed

mysql> create table Shohin(
    -> shohin_id char(4) NOT NULL,
    -> shohin_mei VARCHAR(100) NOT NULL,
    -> shohin_bunrui VARCHAR(32) NOT NULL,
    -> hanbai_tanka INTEGER,
    -> shiire_tanka INTEGER,
    -> torokubi DATE,
    -> PRIMARY KEY(shohin_id));
Query OK, 0 rows affected (6.14 sec)

mysql> ALTER TABLE Shohin ADD COLUMN shohin_mei_kana VARCHAR(100);
Query OK, 0 rows affected (1.06 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> ALTER TABLE Shohin DROP COLUMN shohin_mei_kana;
Query OK, 0 rows affected (0.61 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> insert into Shohin values (
    -> '0001', 'Tシャツ', '衣服', 1000, 500, '2009-09-20');
Query OK, 1 row affected (0.97 sec)

mysql> insert into Shohin values(
    -> '0002', '穴あけパンチ', '事務用品', 500, 320, '2009-09-11');
Query OK, 1 row affected (0.12 sec)

mysql> insert into Shohin values(
    -> '0003', 'カッターシャツ', '衣服', 4000, 2800, NULL);
Query OK, 1 row affected (0.03 sec)

mysql> insert into Shohin values(
    -> '0004', '包丁', 'キッチン用品', 3000, 2800, '2009-09-20');
Query OK, 1 row affected (0.05 sec)

mysql> insert into Shohin values(
    -> '0005', '圧力鍋', 'キッチン用品', 6800, 5000, '2009-01-15');
Query OK, 1 row affected (0.08 sec)

mysql> insert into Shohin values(
    -> '0006', 'フォーク', 'キッチン用品', 500, NULL, '2009-09-20');
Query OK, 1 row affected (0.10 sec)

mysql> insert into Shohin values(
    -> '0007', 'おろしがね', 'キッチン用品', 880, 790, '2008-04-28');
Query OK, 1 row affected (0.05 sec)

mysql> insert into Shohin values(
    -> '0008', 'ボールペン', '事務用品', 100, NULL, '2009-11-11');
Query OK, 1 row affected (0.07 sec)

"""
