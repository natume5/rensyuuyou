#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- SQLAlchemy入門 SQLAlchemyとは---")


"""
SQLAlchemyとは
SQLAlchemyとは、Pythonの中では最もよく利用されているORMの一つです。
ORM以外にも以下の機能を持ちます。

1 データベースへの接続、SQLの実行
2 メタデータ
3 SQL Expression Language
4 ORM

それぞれ簡単に説明しましょう。

データベースへの接続、SQLの実行
SQLAlchemyは様々なデータベースに対して接続してSQLを実行することができます。
サポートするDBMSは以下のとおりです。有名どころは大抵利用可能です。

Firebird
Microsoft SQL Server
MySQL
Oracle
PostgreSQL
SQLite
Sybase
メタデータ
SQLAlchemyにはメタデータと呼ばれるテーブルとPythonのモデルクラスをマッピングする機能があります。
個人的にはSQLAlchemyで最も強力な機能の一つと考えています。

Pythonコードとテーブルを完全に同期させることが可能であり、
テーブルの変更をコードに、コードの変更をテーブルに適用することも可能です。

開発中のマイグレーションの手間を省力化することができます。

SQL Expression Language
JavaのORM、HibernateにはHQLというクエリ言語がありますが、
SQLAlchemyにも同様にクエリを表す記述が用意されています。

SQL Expression Languageを使用することにより、PythonコードとSQLコードが混在しなくなり、
コードの保守性が向上します。

ORM
そして最後がメインのORMです。クエリの実行結果をモデルに格納します。
オブジェクトへのデータセットが自動化されるため、開発を効率化させることができます。
ただし、データ分析のような表形式のデータをそのまま使いたい場合にはやや不向きかもしれません。

SQLAlchemyのインストール
pipでインストールすることが可能です。

1
pip install sqlalchemy
"""


print("--- SQLAlchemy入門 接続とSQL実行---")

"""
engine apiと接続
SQLAlchemyが提供するengineとは、
接続を始めとしたSQLAlchemyの機能を使用するための起点となるオブジェクトです。

engineだけでも最低限のDB操作、つまりデータベースへの接続の作成、
SQLステートメントの送信、および結果の取得を行うことができます。

engineオブジェクトは、create_engine関数を呼び出してデータソース名を渡すことによって作成されます。

engineを使用した簡単なサンプルを見てみましょう。sqlite3のオンメモリのDBに接続し、
SQLを実行してみます。



from sqlalchemy import create_engine
 
engine = create_engine('sqlite:///:memory:')
 
# 接続する
with engine.connect() as con:
 
    # テーブルの作成
    con.execute("CREATE TABLE USERS(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
 
    # Insert文を実行する
    con.execute("INSERT INTO USERS (id, name, age) VALUES(1, 'Kuro', '33')")
    con.execute("INSERT INTO USERS (id, name, age) VALUES(2, 'Sato', '27')")
 
    # Select文を実行する
    rows = con.execute("select * from users;")
    for row in rows:
        print(row)


<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x000001B425A24940>
<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x000001B4259AFCA0>
<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x000001B425A24910>
(1, 'Kuro', 33)
(2, 'Sato', 27)
"""
"""
上のサンプルでは、enginオブジェクトを生成し、6行目のコンテキストで接続されます。
コンテキスト内部でcreate文、insert文といったSQLを実行することができます。

もちろん、コンテキストを使用しなくても記述可能です。


con = engine.connect()
con.execute("・・・")
# :
# :
con.close()
この場合はcloseによるリソースの開放を忘れないようにしましょう。
"""


"""
DBMS別接続サンプル
それでは、よく使われるOSSのDBMSの接続サンプルを紹介しましょう。

MySQL
ドライバにMySQLdbが使用されます。フォークされたmysqlclientでも問題ありません。
こちらを参考にしてインストールしてください。


from sqlalchemy import create_engine
engine = create_engine('mysql://scott:tiger@localhost/foo')
PostgreSQL
ドライバにpsycopg2が使用されます。事前に以下でインストールしてください。


pip install psycopg2
python側のコードは以下のように記述します。


from sqlalchemy import create_engine
engine = create_engine('postgresql://ユーザー名:パスワード@ホスト:ポート/DB名')
sqlite
こちらは最初のサンプルのとおりです。組み込みのモジュールで接続可能ですので準備いらずで楽ですね。


from sqlalchemy import create_engine
engine = create_engine('sqlite:///sqliteファイル')
また、オンメモリで実行する場合は以下のように記述します。


engine = create_engine('sqlite:///:memory:')
その他は公式の以下をご参照ください。
http://docs.sqlalchemy.org/en/latest/core/engines.html

今後、サンプルでは基本的に準備作業を軽減するため、にsqlite3のオンメモリを主に使用します。
"""


"""
コネクションとSQLの実行
（ほとんど冒頭のサンプルで説明し終わっているのですが）engineオブジェクトを生成した後、
コネクションオブジェクトのexcecuteメソッドで任意のSQLを実行することが可能です。
また、コロン記号をSQL内の変数として使用することができます。

以下、CRUDのサンプルです。


from sqlalchemy import create_engine
 
engine = create_engine('sqlite:///:memory:')
 
# 接続する
with engine.connect() as con:
 
    # Drop文を実行
    con.execute("DROP TABLE IF EXISTS USERS")
 
    # Create文の実行
    con.execute("CREATE TABLE USERS(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
 
    # 投入データの定義
    rows = ({"id": 1, "name": "Sato", "age": 31},
            {"id": 2, "name": "Suzuki", "age": 18},
            {"id": 3, "name": "Yamada", "age": 40},
            {"id": 4, "name": "Kuro", "age": 30},
            )
 
    # Insert文を実行
    for row in rows:
        con.execute("INSERT INTO USERS (id, name, age) VALUES(:id, :name, :age)", **row)
 
    # Select文を実行する
    rows = con.execute("SELECT * FROM USERS")
    for row in rows:
        print(row)
 
    # Update文を実行する
    con.execute("UPDATE USERS SET age=42 WHERE id = :id", **{"id": 3})
 
    # Delete文を実行する
    con.execute("DELETE FROM USERS WHERE id = :id", **{"id": 4})
 
    # 更新の確認
    print("***** 更新後 *****")
    rows = con.execute("SELECT * FROM USERS")
    for row in rows:
        print(row)


<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x000001D04FD9D0A0>
<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x000001D04FD8EF40>
<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x000001D04FD8EE80>
<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x000001D04FD8EF70>
<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x000001D04FD8EEB0>
<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x000001D04FD8EF10>
(1, 'Sato', 31)
(2, 'Suzuki', 18)
(3, 'Yamada', 40)
(4, 'Kuro', 30)
<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x000001D04FD8EFD0>
<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x000001D04FD8EF70>
***** 更新後 *****
(1, 'Sato', 31)
(2, 'Suzuki', 18)
(3, 'Yamada', 42)


**記号で辞書をキーワード引数に展開しています。ですので、以下のように記述しても問題ありません。


con.execute("INSERT INTO USERS (id, name, age) VALUES(:id, :name, :age)", id=row['id'], name=row['name'], age=row['age'])


補足 RowProxy
上のSelect文の実行結果ですが、戻り値はRowProxyという型のオブジェクトで返されます。
print結果がタプル形式のように表示されている通り、添数でアクセス可能です。
また、辞書のような性質も持ち合わせているため、カラム名をキーで指定してアクセスすることも可能です。

例えば上のサンプルでnameカラムの値を取得したい場合、
以下のいずれの記述でも取得することができます。


print(row[1])
print(row["name"])
print(row.name)
"""


print("--- SQLAlchemy入門 メタデータによるスキーマの定義---")


"""
メタデータ（スキーマ定義言語、SDL）
メタデータとは、テーブルのスキーマをPythonのコード上で定義する方法です。
DBMSに依存しない方法でスキーマを記述することができるのが大きなメリットといえるでしょう。

スキーマの定義
まずは、サンプルから見てみてください。

from sqlalchemy import Table, Column, Integer, String, MetaData
 
meta = MetaData()
users = Table('Users', meta,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer)
              )

TableクラスでDBテーブルのスキーマを定義することができます。
また、Columnオブジェクトでテーブルを構成するカラムを定義することができます。
上のサンプルでは、カラムとして、id、name、ageを持つUsersテーブルのスキーマを
メタデータを使用して記述しています。
"""
"""
定義の確認
cもしくはcolumnsでカラム名や属性を確認できます。
先ほどのUSERSテーブルの属性などを確認してみましょう。


from sqlalchemy import Table, Column, Integer, String, MetaData
 
meta = MetaData()
users = Table('Users', meta,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer)
              )
 
# Usersテーブルの確認
print(meta.tables['Users'])
# Users
 
# すべてのテーブルの確認
for table in meta.tables:
    print(table)
# Users
 
# columns、もしくはcでカラム名の参照が可能
print(users.columns.name)    # Users.name
print(users.c.name)    # Users.name
 
# すべてのカラムの確認
for col in users.c:
    print(col)    
# Users.id
# Users.name
# Users.age
 
# primary_keyで主キーを参照可能
for pk in users.primary_key:
    print(pk)    # Users.id
 
# その他のカラムの属性の確認
print(users.c.id.name)    # id
print(users.c.id.type)    # INTEGER
print(users.c.id.nullable)    # False
print(users.c.id.primary_key)    # True
以下、サンプルの解説です。

テーブル情報の取得
meta.tablesにすべてのテーブル情報が辞書形式で格納されています。

カラムの確認
テーブルオブジェクトにはcもしくはcolumnsという属性があり、
そこでカラムの情報を参照することができます。
また、29行目以降にありますが、
c.カラム名.のあと、type、nullable、primary_keyなどのカラムの属性を参照することができます。
"""

"""
メタ情報を反映させる
さて、ここからが重要です。先ほど定義したメタデータですが、
engineオブジェクトと連携することにより実際のデータベスに反映することができます。


from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
 
engine = create_engine('sqlite:///:memory:')
meta = MetaData(engine)
users = Table('Users', meta,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer)
              )
 
# metaデータの内容をデータベースに反映
meta.create_all()
 
with engine.connect() as con:
    # DBアクセスして確認する
 
    # 投入データの定義
    rows = ({"id": 1, "name": "Sato", "age": 31},
            {"id": 2, "name": "Suzuki", "age": 18},
            {"id": 3, "name": "Yamada", "age": 40},
            {"id": 4, "name": "Kuro", "age": 30},
            )
 
    # Insert文を実行
    for row in rows:
        con.execute("INSERT INTO USERS (id, name, age) VALUES(:id, :name, :age)", row)
 
    # Select文を実行する
    rows = con.execute("SELECT * FROM USERS")
    for row in rows:
        print(row)


<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x000001D04FF0A250>
<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x000001D04FD8EDF0>
<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x000001D04FD9D040>
<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x000001D04FD8EF40>
(1, 'Sato', 31)
(2, 'Suzuki', 18)
(3, 'Yamada', 40)
(4, 'Kuro', 30)

MetaDataの引数にengineオブジェクトを指定します。
meta.create_all()でテーブル定義の内容をデータベスに反映させることができます。
14行目以降は前回行ったSQLのサンプルと同様です。
Create文を実行しなくてもテーブルが生成されていることがポイントです。

特定のテーブルだけ生成する場合は以下のようにテーブルオブジェクトのcreateメソッドを呼び出します。

users.create()
また、テーブルを削除する場合はdropメソッドを使用します。

users.drop()
"""

"""
メタ情報を生成する
逆にすでに存在するテーブルからメタ情報を生成することも可能です。
この操作をリフレクションと呼びます。


from sqlalchemy import MetaData, create_engine
 
engine = create_engine('sqlite:///db.sqlite')
meta = MetaData(engine, reflect=True)    # ←これじゃできない meta.reflect(bind=engine)
 
# Usersテーブルのカラムの確認
for col in meta.tables['Users'].columns:
    print(col)

# Users.id
# Users.name
# Users.age

サンプルでは、db.sqliteというデータベースに接続後、
メタデータの引数でreflect=Trueを指定することにより
自動的にデータベースのテーブル情報がメタデータに格納されていることが確認できます。

また、リフレクションは後からでも実行可能です。

meta.reflect(bind=engine)
"""


print("--- SQLAlchemy入門 SQL Expression Language---")


"""
SQL Expression Language
SQLAlchemyにはプログラム言語とSQLを分離するために独自のクエリライクな記法が用意されており、
これをSQL Expression Languageと呼びます。（長いので以降SELと略すことにします。）
とりあえずORMを使ってみたい方は本稿はスキップしてこちらから読んでいただいても構いません。

SELの利用方法概要
sqlalchemy.sql.expressionモジュールのCRUDに対応した関数、
insert、select、update、deleteを使用することでSELを使用することができます。
大まかな使い方の手順は、以下のとおりとなります。

SQLのCRUDに対応したオブジェクトの生成
executeメソッドで先ほど生成したオブジェクトを指定して実行する

例えば、select文

select id, name from Users where id=1 limit 3;
を実行する場合、以下のように記述します。usersはメタデータを利用したテーブルオブジェクトとします。


from sqlalchemy.sql import select
 
sel_select = select([users.c.id, users.c.name]).limit(3)
result = con.execute(sel_select)
for row in result:
    print(row)
また、戻り値はSQLを直接実行した時と同様、RowProxyという型のオブジェクトが返されます。

それでは、CRUDのサンプルを確認してみましょう。
"""
"""
insert文
まずはinsert文からです。


from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
from sqlalchemy.sql import insert
 
engine = create_engine('sqlite:///:memory:')
meta = MetaData(engine, reflect=True)
users = Table('Users', meta,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer)
              )
 
meta.create_all()
 
with engine.connect() as con:
    sel_insert = insert(users, values=({"id": 1, "name": 'Suzuki', "age": 20},
                                       {"id": 2, "name": 'Tanaka', "age": 33},))
 
    result = con.execute(sel_insert)
    print(result.rowcount)

# 2

上のサンプルでは、usersテーブルに対しinsert処理を実行しています。
"""

"""
select文
次にselect文です。先ほどのinsertの後、挿入したデータをselectしてみましょう。


from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
from sqlalchemy.sql import insert, select
 
engine = create_engine('sqlite:///:memory:')
meta = MetaData(engine, reflect=True)
users = Table('Users', meta,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer)
              )
 
meta.create_all()
with engine.connect() as con:
    # selectの確認用にデータを投入
    sel_insert = insert(users, values=({"id": 1, "name": 'Suzuki', "age": 20},
                                       {"id": 2, "name": 'Tanaka', "age": 33},))
    result = con.execute(sel_insert)
 
    # ここからselectのサンプル
    # select id, name from Users where id=3 limit 3;
    sel_select = select([users.c.id, users.c.name]).limit(3)
    result = con.execute(sel_select)
    for row in result:
        print(row)
 
    # select * from Users wehre id=1;
    sel_select = select([users])
    result = con.execute(sel_select, id=1)
    for row in result:
        print(row)

(1, 'Suzuki')
(2, 'Tanaka')
(1, 'Suzuki', 20)
(2, 'Tanaka', 33)

22行目は冒頭の説明で多少説明したとおり、select文+limitを指定しています。

カラムごとではなく全部取得する場合は28行目のようにselectの引数にカラムではなく
テーブルオブジェクトを指定します。また、第2引数でwhere条件を指定することが可能です。
"""
"""
update文
update文です。（サンプルの前半はinsert文のサンプルと同じなので省略します。）


# 前半省略
 
from sqlalchemy import update
 
sel_update = update(users, users.c.name == 'Yamada')
con.execute(sel_update, id=1)


with engine.connect() as con:
...     sel_inssert = insert(
... users, values=({"id": 1, "name": 'Suzuki', "age": 20},
...                {"id": 2, "name": 'Tanaka', "age": 33},))
...     sel_update = update(users, users.c.name == 'Yamada')
...     con.execute(sel_update, id=1)
...     result = con.execute(sel_insert)
...     print(result.rowcount)
...
<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x0000025BA8E85D90>




delete文
最後、delete文です。（こちらもサンプルの前半はinsert文のサンプルと同じなので省略します。）


# 前半省略
 
from sqlalchemy import delete
 
sel_delete = delete(users, users.c.id == 1)
con.execute(sel_delete)
select文と同様、第2引数でwhere条件を指定することが可能です。

engine = create_engine('sqlite:///:memory:')
>>> meta = MetaData(engine)
>>> users = Table('Users', meta,
...               Column('id', Integer, primary_key=True),
...               Column('name', String),
...               Column('age', Integer)
...               )
>>> meta.create_all()
>>> with engine.connect() as con:
...     sel_insert = insert(
... users, values=({"id": 1, "name": 'Suzuki', "age": 20},
...                {"id": 2, "name": 'Tanaka', "age": 33},))
...     sel_delete = delete(users, users.c.id == 1)
...     con.execute(sel_delete)
...     result = con.execute(sel_insert)
...     print(result.rowcount)


<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x0000025BA8F6C460>
2

select文と同様、第2引数でwhere条件を指定することが可能です。
"""

"""
その他の操作
CRUDをさらりと紹介しました。その他よく使う句についてのSELの書き方について紹介しましょう。

whereの複合条件
where条件にandやorをつける場合、以下のように記述します。


sel_select = select([users]).where(and_(users.c.age > 18, users.c.age < 60))
sel_select = select([users]).where(or_(users.c.age > 18, users.c.age < 60))
order by
order byです。.order_byで引数にasc(カラムオブジェクト)を指定します。descの場合も同様です。


from sqlalchemy.sql import asc
sel_select = select([users]).order_by(asc(users.c.name))
like
そのまま.likeで引数に曖昧条件を指定します。


sel_select = select([users]).where(users.c.name.like('%zuki%'))
in
これはちょっとわかりづらいのですが、タプルの配列をinの引数に指定します。


user_id_conditions = [(1,), (2,), (3,), (8,)]
sel_select = select([users]).where(tuple_(users.c.id).in_(user_id_conditions))
"""
"""
join
meta定義で外部キーを定義している場合、joinをすることができます。


from sqlalchemy import Table, Column, Integer, String, Text, MetaData, create_engine, ForeignKey
from sqlalchemy.sql import select, insert, join
 
engine = create_engine('sqlite:///:memory:')
meta = MetaData(engine)
users = Table('Users', meta,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer)
              )
 
posts = Table('Posts', meta,
              Column('id', Integer, primary_key=True),
              Column('user_id', ForeignKey("Users.id")),
              Column('title', String),
              Column('body', Text)
              )
 
meta.create_all()
with engine.connect() as con:
    # selectの確認用にデータを投入
    user_insert = insert(users, values=({"id": 1, "name": 'Suzuki', "age": 20},
                                        {"id": 2, "name": 'Tanaka', "age": 33},))
    con.execute(user_insert)
 
    post_insert = insert(posts, values=({"id": 1, "user_id": 1, "title": "Sample", "body": "記事本文"},))
    con.execute(post_insert)
 
    # ここからjoinのサンプル
    # select * from Users inner join Posts on Users.id = Posts.user_id;
    sel_join = select([users.join(posts)])
    result = con.execute(sel_join)
 
    for row in result:
        print(row)


<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x0000028A86256040>
<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x0000028A86294F10>
(1, 'Suzuki', 20, 1, 1, 'Sample', '記事本文')
"""
