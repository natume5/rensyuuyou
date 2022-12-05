#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- SQLAlchemy入門 メタデータによるスキーマの定義 ---")


print("--- メタデータ（スキーマ定義言語、SDL） ---")


"""
メタデータとは、テーブルのスキーマをPythonのコード上で定義する方法です。
DBMSに依存しない方法でスキーマを記述することができるのが
大きなメリットといえるでしょう。

スキーマの定義

まずは、サンプルから見てみてください。
"""

from sqlalchemy import Table, Column, Integer, String, MetaData

meta = MetaData()
users = Table('Users', meta,
	          Column('id', Integer, primary_key=True),
	          Column('name', String),
	          Column('age', Integer)
	          )

"""
TableクラスでDBテーブルのスキーマを定義することができます。
また、Columnオブジェクトでテーブルを構成するカラムを定義することができます。
上のサンプルでは、カラムとして、id、name、ageを持つ
Usersテーブルのスキーマをメタデータを使用して記述しています。


定義の確認

cもしくはcolumnsでカラム名や属性を確認できます。
先ほどのUSERSテーブルの属性などを確認してみましょう。
"""

from sqlalchemy import Table, Column, Integer, String, MetaData


meta = MetaData()
users = Table('Users', meta,
	          Column('id', Integer, primary_key=True),
	          Column('name', String),
	          Column('age', Integer)
	          )

# Usersテーブルの確認
print(meta.tables['Users'])    # Users

# 全てのテーブルの確認
for table in meta.tables:
	print(table)    # Users

# columns、もしくはcでカラム名の参照が可能
print(users.columns.name)    # Users.name
print(users.c.name)    # Users.name

# 全てのカラムの確認
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


"""
以下、サンプルの解説です。
テーブル情報の取得

meta.tablesにすべてのテーブル情報が辞書形式で格納されています。

カラムの確認

テーブルオブジェクトにはcもしくはcolumnsという属性があり、
そこでカラムの情報を参照することができます。
また、29行目以降にありますが、c.カラム名.のあと、
type、nullable、primary_keyなどのカラムの属性を参照することができます。
"""


print("--- メタ情報を反映させる ---")


"""
さて、ここからが重要です。先ほど定義したメタデータですが、
engineオブジェクトと連携することにより実際のデータベスに反映することができます。
"""

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
	# DBにアクセスして確認する

	# 投入データの定義
	rows = ({"id": 1, "name": "Sato", "age": 31},
		    {"id": 2, "name": "Suzuki", "age": 18},
		    {"id": 3, "name": "Yamada", "age": 40},
		    {"id": 4, "name": "Kuro", "age": 30},
		    )

	# Insert文を実行する
	for row in rows:
		con.execute("INSERT INTO USERS (id, name, age) VALUES(:id, :name, :age)", row)

	# Select文を実行する
	rows = con.execute("SELECT * FROM USERS")
	for row in rows:
		print(row)

# (1, 'Sato', 31)
# (2, 'Suzuki', 18)
# (3, 'Yamada', 40)
# (4, 'Kuro', 30)
"""
MetaDataの引数にengineオブジェクトを指定します。
meta.create_all()でテーブル定義の内容を
データベスに反映させることができます。
14行目以降は前回行ったSQLのサンプルと同様です。
Create文を実行しなくてもテーブルが生成されていることがポイントです。
特定のテーブルだけ生成する場合は以下のように
テーブルオブジェクトのcreateメソッドを呼び出します。

users.create()

また、テーブルを削除する場合はdropメソッドを使用します。

users.drop()
"""


print("--- メタ情報を生成する ---")


"""
逆にすでに存在するテーブルからメタ情報を生成することも可能です。
この操作をリフレクションと呼びます。
"""


from sqlalchemy import MetaData, create_engine

engine = create_engine('sqlite:///db.sqlite')
meta.reflect()    # metadataを取得， meta=MetaData(engine, reflect=True)と同じ
# meta = MetaData(engine, reflect=True)


# Usersテーブルのカラムの確認
for col in meta.tables['Users'].columns:
	print(col)
# Users.id
# Users.name
# Users.age

"""
サンプルでは、db.sqliteというデータベースに接続後、
メタデータの引数でreflect=Trueを指定することにより
自動的にデータベースのテーブル情報が
メタデータに格納されていることが確認できます。
また、リフレクションは後からでも実行可能です。
"""

meta.reflect(bind=engine)
