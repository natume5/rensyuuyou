#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- SQLAlchemy入門 ORM その1 ---")


print("--- テーブルクラスの定義 ---")


"""
テーブルクラスの定義

大抵のORMではテーブルに対応するクラスを定義します。
本講座では便宜上テーブルクラスと呼ぶことにします。
また、テーブルクラスから生成したオブジェクトをテーブルオブジェクトと呼ぶことにします。
これはDBの1レコードに相当します。
SQLAlchemyではテーブルクラスを定義する際、
Baseと呼ばれる型オブジェクトを継承したクラスを作成します。
サンプルです。Userテーブルに対応するテーブルクラスを定義してみます。
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy import create_engine


engine = create_engine('sqlite:///:memory:')

Base = declarative_base()

class User(Base):
	"""
	Userテーブルクラス
	"""

	# テーブル名
	__tablename__ = 'users'

	# 個々のカラムを定義
	id = Column(Integer, primary_key=True)
	name = Column(String)
	age = Column(Integer)

# テーブルクラスのテーブルを生成
Base.metadata.create_all(engine)
"""
テーブル生成

以前学習したメタデータを使用してテーブルクラスの情報を
DBに反映することができます。
Baseからmetadataを取得することができますので、
ここで学習した通りの方法でテーブル生成することができます。
"""

from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///:memory:')
metadata = MetaData()
b_md = Base.metadata
b_md.create_all(engine)


print("--- ORMとCRUD ---")


"""
接続とデータを格納するクラスの定義ができました。
セッションについて簡単に説明した後ORMを使ってみましょう。

セッション

ORMを使用したCRUDについて学習する前にORMを使用したことがない方向けに、
セッションについて雑に説明します。
ORMのセッションとはコードとDBで同期を取る仕組みと思ってください。
テーブルクラスのオブジェクトがRDBの1レコードに相当しますが、
セッションを介してオブジェクトの状態をDBに反映させることができます。
SQLAlchemyのセッションはsessionmakerを使用します。
引数にengineを指定します。
"""

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

"""
それではORMのCRUD処理について見ていきましょう。

Insert

まずはInsertです。
session.addメソッドに生成したテーブルオブジェクトを指定します。
例えば、新規ユーザーSuzukiさんのデータをinsertする場合、
以下のように記述します。
"""

"""
suzuki = User(name='Suzuki', age=19)
session.add(suzuki)
session.commit()
"""


"""
Select

session.queryメソッドでクエリオブジェクトを取得し、
selectを実行することができます。
次回細かいクエリの実行方法について学習します。
"""

"""
user_obj = session.query(User).all()
"""

"""
getで主キーを指定することができます。
"""

"""
suzuki = session.query(User).get(1)
"""

"""
Update

テーブルオブジェクトを生成したりqueryメソッドで取得した後、
属性を更新してaddすると更新処理が実行されます。
例えば先ほどinsertしたSuzukiさんのデータを修正する場合、
以下のようになります。
"""

"""
suzuki = session.query(User).get(1)
suzuki.age = 20
session.add(suzuki)
session.commit()
"""

"""
Delete

最後はDeleteです。
session.deleteメソッドに削除対象のテーブルオブジェクトを指定します。
"""

"""
session.delete(suzuki)
"""


print("--- 補足 サンプル ---")


"""
補足として、上記サンプルをまとめたものを掲載します。
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DB接続
engine = create_engine('sqlite:///:memory:')

# Base
Base = declarative_base()

# テーブルクラスを定義
class User(Base):
	"""
	userテーブルクラス
	"""

	# テーブル名
	__tablename__ = 'users'

	# 個々のカラムを定義
	id = Column(Integer, primary_key=True)
	name = Column(String)
	age = Column(Integer)

# テーブルクラスのテーブルを生成
Base.metadata.create_all(engine)

# セッション生成
Session = sessionmaker(bind=engine)
session = Session()

# 挿入レコード作成
suzuki = User(name='Suzuki', age=19)
session.add(suzuki)    # insert処理
session.commit()    # commit

# select * from users;
users_obj = session.query(User).all()
for user in users_obj:
	print(user.name)

# selsct * from users where id =1;
suzuki = session.query(User).get(1)
suzuki.age = 20

# update
session.add(suzuki)
session.commit()

# delete
session.delete(suzuki)

# Suzuki

"""
簡単なCRUD処理について学習しました。
次回は様々なクエリの記述方法について学習しましょう。
"""
