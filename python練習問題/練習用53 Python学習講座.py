#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- SQLAlchemy入門 ORM その1---")


"""
SQLAlchemyが提供するORM機能を使用すると、
DBのデータをPythonオブジェクトとみなして扱うことができるようになります。


テーブルクラスの定義
テーブルクラスの定義
大抵のORMではテーブルに対応するクラスを定義します。
本講座では便宜上テーブルクラスと呼ぶことにします。
また、テーブルクラスから生成したオブジェクトをテーブルオブジェクトと呼ぶことにします。
これはDBの1レコードに相当します。

SQLAlchemyではテーブルクラスを定義する際、
Baseと呼ばれる型オブジェクトを継承したクラスを作成します。

サンプルです。Userテーブルに対応するテーブルクラスを定義してみます
"""
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
 
Base = declarative_base()
 
 
class User(Base):
    """"""
    Userテーブルクラス
    """ """
 
    # テーブル名
    __tablename__ = 'users'
 
    # 個々のカラムを定義
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
"""
"""
テーブル生成
以前学習したメタデータを使用してテーブルクラスの情報をDBに反映することができます。
Baseからmetadataを取得することができますので、
ここで学習した通りの方法でテーブル生成することができます。

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
meta = Base.metadata
meta.create_all(engine)
"""
"""
ORMとCRUD
接続とデータを格納するクラスの定義ができました。
セッションについて簡単に説明した後ORMを使ってみましょう。

セッション
ORMを使用したCRUDについて学習する前にORMを使用したことがない方向けに、
セッションについて雑に説明します。ORMのセッションとはコードとDBで同期を取る仕組みと思ってください。

テーブルクラスのオブジェクトがRDBの1レコードに相当しますが、
セッションを介してオブジェクトの状態をDBに反映させることができます。

SQLAlchemyのセッションはsessionmakerを使用します。引数にengineを指定します。


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
それではORMのCRUD処理について見ていきましょう。

Insert
まずはInsertです。session.addメソッドに生成したテーブルオブジェクトを指定します。

例えば、新規ユーザーSuzukiさんのデータをinsertする場合、以下のように記述します。


suzuki = User(name="Suzuki", age=19)
session.add(suzuki)
session.commit()
Select
session.queryメソッドでクエリオブジェクトを取得し、selectを実行することができます。
次回細かいクエリの実行方法について学習します。

users_obj = session.query(User).all()
getで主キーを指定することができます。

suzuki = session.query(User).get(1)
Update
テーブルオブジェクトを生成したりqueryメソッドで取得した後、
属性を更新してaddすると更新処理が実行されます。
例えば先ほどinsertしたSuzukiさんのデータを修正する場合、以下のようになります。


suzuki = session.query(User).get(1)
suzuki.age = 20
session.add(suzuki)
session.commit()
Delete
最後はDeleteです。session.deleteメソッドに削除対象のテーブルオブジェクトを指定します。


session.delete(suzuki)
補足 サンプル
補足として、上記サンプルをまとめたものを掲載します。
"""
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
# DB接続
engine = create_engine('sqlite:///:memory:')
 
# Base
Base = declarative_base()
 
 
# テーブルクラスを定義
class User(Base):
    """"""
    Userテーブルクラス
    """"""
 
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
 
 
# 挿入用レコード作成
suzuki = User(name="Suzuki", age=19)
session.add(suzuki) # insert処理
session.commit()    # commit
 
# select * from users;
users_obj = session.query(User).all()
for user in users_obj:
    print(user.name)    # Suzuki
 
# select * from users where id = 1;
suzuki = session.query(User).get(1)
suzuki.age = 20
 
# update
session.add(suzuki)
session.commit()
 
# delete
session.delete(suzuki)


簡単なCRUD処理について学習しました。次回は様々なクエリの記述方法について学習しましょう。
"""


print("--- SQLAlchemy入門 ORM その2 さまざまなクエリ---")


"""
前回、ORMで簡単なCRUDの記述方法について学習しました。
今回はもう少し複雑なクエリの記述方法について学習しましょう。


さまざまなクエリ
session.queryを使用してクエリオブジェクト（sqlalchemy.orm.query.Query）
を生成しさまざまなクエリを実行することができます。
all()メソッドでオブジェクトを格納したリスト型として結果を取得することができます。

キー指定
where句で主キーを指定する場合、getメソッドを使用します。


# select * from users where id = 1;
suzuki = session.query(User).get(1)
カラム指定
where句でカラムを指定する場合、filter_byメソッドを使用します。
引数にカラムの値を指定してください。


# select * from users where name="Suzuki"
users = session.query(User).filter_by(name="Suzuki").all()
limit
limitを指定する場合はlimitメソッドを使用します。


# select * from users where age=21 limit 1;
users = session.query(User).filter_by(age=21).limit(1).all()
order
order byを指定する場合はorderメソッドを使用します。


# select * from users where age=21 order by name;
users = session.query(User).filter_by(age=21).order_by(User.name).all()
最初の1件を取得
最初の1件を取得する場合はfirst()メソッドを使用します。


user = session.query(User).filter_by(age=21).order_by(User.name).first()
件数取得
件数を取得する場合はcount()メソッドを使用します。


user_cnt = session.query(User).filter_by(age=21).count()
"""
"""
filterメソッドによるwhere句
先ほど、簡単なwhere句としてfilter_byメソッドを使用しましたが、
複雑な検索条件を指定する場合はfilterを使用します。

まずは簡単なサンプルから見てみましょう。where句を単純に使用してみます。


users = session.query(User).filter(User.age == 19).all()
引数の指定が一見奇妙にみえますが、これは真偽値を渡しているわけではありません。
独自の比較演算子が定義されており、比較の結果、BinaryExpressionという型が取得されます。
気になる方は以下のコードを実行してみてください。


print(type(User.age == 19))
# <class 'sqlalchemy.sql.elements.BinaryExpression'>
filterメソッドを使用すると、AND条件、OR条件、IN句を以下のように使用することができます。

AND条件

from sqlalchemy import and_
users = session.query(User).filter(and_(User.name == 'Sato', User.age == 21)).all()

OR条件

from sqlalchemy import or_
users = session.query(User).filter(or_(User.name == 'Suzuki', User.age == 21)).all()

IN句

users = session.query(User).filter(User.age.in_([19, 21])).all()
"""
"""
補足 all()について
all()は取得結果のシーケンシャルオブジェクトをlistに変換してくれる糖衣構文です。実装上は以下のようになっています。


# sqlalchemy/orm/query.py
    def all(self):
        """"""Return the results represented by this ``Query`` as a list.
 
        This results in an execution of the underlying query.
 
        """"""
        return list(self)
このため、実はall()は使わなくても、以下のような記述をすることもできます。


users = session.query(User).filter(User.age.in_([19, 21]))
for query in users:
    print(query.name)
"""


print("--- SQLAlchemy入門 ORM その3 JOIN---")


"""
リレーションがない場合のJOIN
JOINの方法はいくつかあるのですが、
まずはテーブル間のリレーションを無視した一番単純な方法を紹介します。
一般的にORMはJOINするとテーブルのリレーションが考慮された階層構造のオブジェクトを
取得できるのですが、その方法については次回にリレーションと合わせて紹介します。

FULL OUTER JOIN
session.queryで複数テーブルを指定すると、FULL OUTER JOINされた結果を取得することができます。


session.query(テーブル1, テーブル2).all()
INNER JOIN
FULL OUTER JOINの結果をフィルタリング、
もしくはjoinすることでINNER JOINの結果を取得することができます。


# FULL OUTER JOINの結果をフィルタリング
session.query(テーブル1, テーブル2).filter(テーブル1.id == テーブル2.hoge_id)
 
# FULL OUTER JOINの結果をさらにjoin
session.query(テーブル1, テーブル2).join(テーブル1, テーブル1.id == テーブル2.hoge_id)
LEFT OUTER JOIN
同様に、FULL OUTER JOINの結果を再度LEFT OUTER JOINすると、
LEFT OUTER JOINの結果を得ることができます。


# FULL OUTER JOINの結果をさらにjoin
session.query(テーブル1, テーブル2).join(テーブル1, テーブル1.id == テーブル2.hoge_id)
サンプル
ユーザーテーブルと、
ユーザーに紐づく投稿テーブルに対してINNER JOINとLEFT OUTER JOINを利用したサンプルです。
"""
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
 
# DB接続
engine = create_engine('sqlite:///:memory:')
 
# Base
Base = declarative_base()
 
 
# テーブルクラスを定義
class User(Base):
    """"""
    Userテーブルクラス
    """"""
 
    # テーブル名
    __tablename__ = 'users'
 
    # 個々のカラムを定義
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
 
 
class Post(Base):
    """"""
    Postテーブルクラス
    """"""
 
    # テーブル名
    __tablename__ = 'posts'
 
    # 個々のカラムを定義
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    body = Column(Integer)
 
 
# テーブルクラスのテーブルを生成
Base.metadata.create_all(engine)
 
# セッション生成
Session = sessionmaker(bind=engine)
session = Session()
 
# サンプルデータ挿入
session.add(User(id=1, name="Suzuki", age=19))
session.add(User(id=2, name="Tanaka", age=21))
session.add(User(id=3, name="Sato", age=21))
 
session.add(Post(users_id=1, title="朝の体操", body="ラジオ体操で元気いっぱい"))
session.add(Post(users_id=1, title="今日の夕食", body="カレーラスがとても美味しかった。"))
session.add(Post(users_id=2, title="仕事", body="今日はDjangoでAPI作成。"))
session.add(Post(users_id=2, title="Python楽しい", body="Python楽しいですよね！！"))
session.commit()
 
# inner joinのサンプル
users_posts = session.query(User, Post).join(Post, User.id == Post.users_id).all()
 
for user_posts in users_posts:
    print("%sさんの投稿 タイトル：%s" % (user_posts.User.name, user_posts.Post.title,))
 
print('*****')
# left outer joinのサンプル
users_posts = session.query(User, Post).outerjoin(Post, User.id == Post.users_id).all()
 
for user_posts in users_posts:
    if user_posts.Post is not None:
        print("%sさんの投稿 タイトル：%s" % (user_posts.User.name, user_posts.Post.title,))
    else:
        pass
        print("%sさんの投稿 なし" % (user_posts.User.name,))


Suzukiさんの投稿 タイトル:朝の体操
*****
Suzukiさんの投稿 タイトル:今日の夕食
*****
Tanakaさんの投稿 タイトル:仕事
*****
Tanakaさんの投稿 タイトル:Python楽しい
*****

Suzukiさんの投稿 タイトル:今日の夕食
Suzukiさんの投稿 タイトル:朝の体操
Tanakaさんの投稿 タイトル:Python楽しい
Tanakaさんの投稿 タイトル:仕事
Satoさんの投稿 なし
"""
"""
以下の結果を取得することができます。
テーブルのリレーションが定義されていないため、
結果のオブジェクトは階層構造になっておらず冗長になっている点に注目してください。


Suzukiさんの投稿 タイトル：朝の体操
Suzukiさんの投稿 タイトル：今日の夕食
Tanakaさんの投稿 タイトル：仕事
Tanakaさんの投稿 タイトル：Python楽しい
*****
Suzukiさんの投稿 タイトル：今日の夕食
Suzukiさんの投稿 タイトル：朝の体操
Tanakaさんの投稿 タイトル：Python楽しい
Tanakaさんの投稿 タイトル：仕事
Satoさんの投稿 なし
"""
