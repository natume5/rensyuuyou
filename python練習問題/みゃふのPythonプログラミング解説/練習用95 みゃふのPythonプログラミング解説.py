#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説 ---")
print("--- ORMライブラリの使い方（SQLAlchemy） ---")


"""
SQLAlchemyは「PythonのためのORMライブラリ」です。
Python用ORMはいくつかありますが、SQLAlchemyが最も定番なので、
迷ったらこのライブラリを使うと良いでしょう。
ここでは「ORMって何？」「SQLAlchemyのインストール方法は？」
「SQLAlchemyの使い方が知りたい」といった方へ、ORMおよびSQLAlchemyについて解説します。
"""


print("--- ORMとは ---")


"""
ORMはObject Relational Mapperの略で、
「データベース(RDB)とオブジェクト指向プログラミング間の違いを吸収してくれるライブラリやシステム」
のことです。
オブジェクト指向プログラミングとは「現実世界の物事を『データ(状態)』と『動作』
のセットで表現するプログラミングのやり方」のことです。
ORMを使うことで、オブジェクト指向側の「現実世界の物事に即したデータモデル」と、
データベース側の「検索処理に最適化された表形式のデータモデル」の間にある違い
（インピーダンス・ミスマッチと言います）を吸収してくれます。
実際のイメージは、Python側から「仮想」に作ったデータベースをオブジェクト指向で
扱えるようにするといった感じです。
"""


print("--- SQLAlchemyのインストール ---")


"""
まずはSQLAlchemyをインストールしましょう。今回は「SQLite」を使う前提で進めます。
Python3であれば、SQLiteはデフォルトでインストールされています。
なのでSQLAlchemyをpipコマンドインストールすれば完了です。

$ pip install SQLAlchemy
"""


print("--- SQLAlchemyの使い方 ---")


"""
ここからはSQLAlchemyの使い方を見ていきましょう。
なお、SQLAlchemyを使う際は最初に次のモジュールを読み込みます。
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound


"""
データベースエンジンを作成する

どのデータベースを使う場合でも、まずはデータベースエンジンを作成する必要があります。

SQLiteでデータベースエンジンを作成する場合はファイルパスを指定します。

"""
engine = create_engine('sqlite:///sample1.db')

"""
今回はsample.dbというファイルをデータベースにします。
create_engine()にファイルパスを指定することで、データベースエンジンを作成しました。
今回はSQLiteを使っていますが、MySQLやPostgresqlといった他のデータベースでも、
SQLAlchemyを使う場合はこのデータベースエンジンを作るところから始まります。
そして、一度データベースエンジンを作ったら、それ以降の処理はどのデータベースでも同じです。
なのでSQLAlchemyを使えば、create_engine()の引数を変えるだけで
複数のデータベースを切り替えることも可能です。


テーブルの定義をPython側で作成する

次にデータベース内のテーブルの定義をPython側で作成します。
まずベースモデルというものを作成します。これがテーブルの元になります
"""

Base = declarative_base()

"""
次にテーブルのクラスを作成します。クラスとはテーブルの設計図のことです。
次のように作成します。
"""

class User(Base):
	__tablename__='user'    # テーブル名
	id=Column(Integer, primary_key=True)    # 主キー
	name = Column(String(255))
	age = Column(Integer)

"""
これでuserテーブルの定義ができました。
userテーブルにはid, name, ageのカラムがあり、主キーはidです。
このテーブルをSQLiteに作成するには次のコードを実行します。
"""

Base.metadata.create_all(engine)

"""
ここまでのソースコードを全てつなぎ合わせて実行すると、sample.db内にuserテーブルが作成されます。


セッションの作成

SQLAlchemyでSQLを実行するにはセッションを作成する必要があります。
セッションとは「データベースにアクセスしているユーザを見分けるid」です。
RDBではデータの一貫性が求められるので、
正確なトランザクション処理をするためにこのセッションが必要になります。
"""

SessionClass = sessionmarker(engine)    # セッションを作るクラスを作成
session = SessionClass()

"""
これでsession変数にセッションが作成されました。


SQLAlchemyでINSERT

今度は実際にデータを作成してみましょう。データの作成はsession.add()を使います。 
"""

session.add(User(name="sato", age=27))
session.add(User(name="suzuki", age=29))
session.add(User(name="tanaka", age=28))
session.commit()

"""
先ほど作成したUserクラスのnameとageに値を入れ、
それをsession.add()に渡すことでデータが作成されます（INSERTと同じ）。
sato, suzuki, tanakaの3つのデータが作成されます。
idは主キーなので指定がなくても問題ありません。
最後に作成したデータを session.commit() とすることで確定できます。


作成したデータを参照する

データがちゃんと作成されたか確認してみましょう。
データの参照はsession.query()を使います。
"""

users = session.query(User)
for u in users:
    print("id = {}, name = {}, age = {}".format(u.id, u.name, u.age))

# id = 1, name = sato, age = 27
# id = 2, name = suzuki, age = 29
# id = 3, name = tanaka, age = 28

"""
session.query()にUserクラスを指定することで、Userテーブルに作成したデータを取得できます。
users変数にはリスト形式のようなデータ構造でデータが返却されてくるので、
for文でループ処理が可能です。
後は「u.Userクラスで指定したカラム名」で中身のデータを参照できます。
特に何も指定しない場合は全件データを取得できますが、
フィルタ(WHERE条件)をかけたい場合はfilter()を使います。
"""

users = session.query(User).filter(User.age <= 28)    # 28歳以下

for u in users:
    print("id = {}, name = {}, age = {}".format(u.id, u.name, u.age))

# id = 1, name = sato, age = 27
# id = 3, name = tanaka, age = 28

"""
今回は1つの条件しか指定していませんが、
複数条件を指定したい場合はカンマで区切ることで追加指定可能です。
また、主キー（今回はid）でフィルタリングしたい場合はfilter()よりget()を使う方が楽です。
"""

u = session.query(User).get(2)     #id = 2
print("id = {}, name = {}, age = {}".format(u.id, u.name, u.age))

# id = 2, name = suzuki, age = 29

"""
get()で取得できるデータは1件なので、
filter()と異なりリストではなく単体のデータが返却されます。


データを更新する

session.query()で取得したデータを変更することで、データの更新ができます。
"""

u = session.query(User).get(2)
print("変更前のname = {}".format(u.name))    # 変更前のname = suzuki
u.name = "ito"

#もう一度取得する
u2 = session.query(User).get(2)
print("変更後のname = {}".format(u.name))    # 変更後のname = ito

"""
データを削除する

session.delete()にsession.query()で取得したデータを渡すことで、データの削除ができます。
"""

user = session.query(User).get(2)
session.delete(user)

# 全件取得
users = session.query(User)
for u in users:
	print(u.name)

# sato
# tanaka

"""
id = 2のデータを削除したことで、全件取得してもsuzukiが取得されなくなりました。
また、delete()は検索条件にマッチした全てのデータを一括で削除することもできます。
"""

session.query(User).filter(User.age <= 28).delete()    # 2
#全件取得
users = session.query(User)
for u in users:
    print(u.name)

# 
