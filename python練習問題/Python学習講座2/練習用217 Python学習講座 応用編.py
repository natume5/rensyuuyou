#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- SQLAlchemy入門 SQL Expression Language ---")


print("--- SQL Expression Language ---")


"""
SQLAlchemyにはプログラム言語とSQLを分離するために
独自のクエリライクな記法が用意されており、
これをSQL Expression Languageと呼びます。
（長いので以降SELと略すことにします。）
とりあえずORMを使ってみたい方は本稿はスキップして
こちらから読んでいただいても構いません。
SELの利用方法概要

sqlalchemy.sql.expressionモジュールのCRUDに対応した関数、
insert、select、update、deleteを使用することで
SELを使用することができます。
大まかな使い方の手順は、以下のとおりとなります。

    SQLのCRUDに対応したオブジェクトの生成
    executeメソッドで先ほど生成したオブジェクトを指定して実行する

例えば、select文

select id, name from Users where id=1 limit 3;

を実行する場合、以下のように記述します。
usersはメタデータを利用したテーブルオブジェクトとします。
"""

"""
from sqlalchemy.sql import select

sel_select = select([users.c.id, users.c.name]).limit(3)
result = con.execute(sel_select)
for row in result:
    print(row)
"""

"""
また、戻り値はSQLを直接実行した時と同様、
RowProxyという型のオブジェクトが返されます。
それでは、CRUDのサンプルを確認してみましょう。

insert文

まずはinsert文からです。
"""

from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
from sqlalchemy.sql import insert

engine = create_engine('sqlite:///:memory:')
# meta.reflect()
# meta = MetaData(engine, reflect=True)
metadata_obj = MetaData()
metadata_obj.reflect(engine)
users = Table('Users', metadata_obj,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer)
              )

metadata_obj.create_all(engine)

with engine.connect() as con:
    sel_insert = insert(users, values=({"id": 1, "name": 'Suzuki', "age": 20},
                                       {"id": 2, "name": 'Tanaka', "age": 33}, ))
    result = con.execute(sel_insert)
    print(result.rowcount)    # 2

"""
上のサンプルでは、usersテーブルに対しinsert処理を実行しています。


select文

次にselect文です。
先ほどのinsertの後、挿入したデータをselectしてみましょう。
"""


from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
from sqlalchemy.sql import insert, select

engine = create_engine('sqlite:///:memory:')
# meta.reflect()
# meta = MetaData(engine, reflect=True)
metadata_obj = MetaData()
metadata_obj.reflect(engine)
users = Table('Users', metadata_obj,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer)
              )

metadata_obj.create_all(engine)

with engine.connect() as con:
    # selectの確認用にデータを投入
    sel_insert = insert(users, values=({"id": 1, "name": 'Suzuki', "age": 20},
                                       {"id": 2, "name": 'Tanaka', "age": 33}, ))
    result = con.execute(sel_insert)

    # ここからselectのサンプル
    # select id, name from Users where id=3 limit 3;
    sel_select = select([users.c.id, users.c.name]).limit(3)
    result = con.execute(sel_select)
    for row in result:
        print(row)

    # select * from Users where id=1;
    sel_select = select([users])
    result = con.execute(sel_select, id=1)
    for row in result:
        print(row)

# (1, 'Suzuki')
# (2, 'Tanaka')
# (1, 'Suzuki', 20)
# (2, 'Tanaka', 33)
"""
22行目は冒頭の説明で多少説明したとおり、
select文+limitを指定しています。
カラムごとではなく全部取得する場合は
28行目のようにselectの引数にカラムではなくテーブルオブジェクトを指定します。
また、第2引数でwhere条件を指定することが可能です。


update文

update文です。
（サンプルの前半はinsert文のサンプルと同じなので省略します。）
"""

from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
from sqlalchemy.sql import update

engine = create_engine('sqlite:///:memory:')
# meta.reflect()
# meta = MetaData(engine, reflect=True)
metadata_obj = MetaData()
metadata_obj.reflect(engine)
users = Table('Users', metadata_obj,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer)
              )

metadata_obj.create_all(engine)

with engine.connect() as con:
    sel_update = update(users, users.c.name == 'Yamada')
    con.execute(sel_update, id=1)
    

"""
delete文

最後、delete文です。
（こちらもサンプルの前半はinsert文のサンプルと同じなので省略します。）
"""

from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
from sqlalchemy.sql import delete

engine = create_engine('sqlite:///:memory:')
# meta.reflect()
# meta = MetaData(engine, reflect=True)
metadata_obj = MetaData()
metadata_obj.reflect(engine)
users = Table('Users', metadata_obj,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer)
              )

metadata_obj.create_all(engine)

with engine.connect() as con:
    sel_delete = delete(users, users.c.id == 1)
    con.execute(sel_delete)


"""
select文と同様、第2引数でwhere条件を指定することが可能です。
"""


print("--- その他の操作 ---")


"""
CRUDをさらりと紹介しました。
その他よく使う句についてのSELの書き方について紹介しましょう。

whereの複合条件

where条件にandやorをつける場合、以下のように記述します。

sel_select = select([users]).where(and_(users.c.age > 18, users.c.age < 60))
sel_select = select([users]).where(or_(users.c.age > 18, users.c.age < 60))


order by

order byです。
.order_byで引数にasc(カラムオブジェクト)を指定します。
descの場合も同様です。

from sqlalchemy.sql import asc
sel_select = select([users]).order_by(asc(users.c.name))


like

そのまま.likeで引数に曖昧条件を指定します。

sel_select = select([users]).where(users.c.name.like('%zuki%'))


in

これはちょっとわかりづらいのですが、タプルの配列をinの引数に指定します。

user_id_conditions = [(1,), (2,), (3,), (8,)]
sel_select = select([users]).where(tuple_(users.c.id).in_(user_id_conditions))


join

meta定義で外部キーを定義している場合、joinをすることができます。
"""


from sqlalchemy import Table, Column, Integer, String, Text, MetaData, create_engine, ForeignKey
from sqlalchemy.sql import select, insert, join

engine = create_engine('sqlite:///:memory:')
metadata_obj = MetaData()
metadata_obj.reflect(engine)
users = Table('Users', metadata_obj,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer)
              )

posts = Table('Posts', metadata_obj,
              Column('id', Integer, primary_key=True),
              Column('user_id', ForeignKey("Users.id")),
              Column('title', String),
              Column('body', Text)
              )

metadata_obj.create_all(engine)
with engine.connect() as con:
    # selectの確認用にデータを投入
    user_insert = insert(users, values=({"id": 1, "name": 'Suzuki', "age": 20},
                                        {"id": 2, "name": 'Tanaka', "age": 33}, ))
    con.execute(user_insert)

    post_insert = insert(posts, values=({"id": 1, "user_id": 1, "title": "Sample", "body": "記事本文"}, ))
    con.execute(post_insert)

    # ここからjoinのサンプル
    # select * from Users inner join Posts on Users.id = Posts.user_id;
    sel_join = select([users.join(posts)])
    result = con.execute(sel_join)

    for row in result:
        print(row)

# (1, 'Suzuki', 20, 1, 1, 'Sample', '記事本文')
