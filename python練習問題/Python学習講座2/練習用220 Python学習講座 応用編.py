#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- SQLAlchemy入門 ORM その3 JOIN ---")


print("--- リレーションがない場合のJOIN ---")


"""
JOINの方法はいくつかあるのですが、
まずはテーブル間のリレーションを無視した一番単純な方法を紹介します。
一般的にORMはJOINするとテーブルのリレーションが考慮された
階層構造のオブジェクトを取得できるのですが、
その方法については次回にリレーションと合わせて紹介します。

FULL OUTER JOIN

session.queryで複数テーブルを指定すると、
FULL OUTER JOINされた結果を取得することができます。

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
"""


print("--- サンプル ---")


"""
ユーザーテーブルと、ユーザーに紐づく投稿テーブルに対して
INNER JOINとLEFT OUTER JOINを利用したサンプルです。
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
	"""
	Userテーブルクラス
	"""

	# テーブル名
	__tablename__ = 'users'

	# 個々のカラムを定義
	id = Column(Integer, primary_key=True)
	name = Column(String)
	age = Column(Integer)

class Post(Base):
	"""
	postテーブルクラス
	"""

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
session.add(Post(users_id=1, title="今日の夕食", body="カレーライスがとても美味しかった"))
session.add(Post(users_id=2, title="仕事", body="今日はDjangoでAPI作成"))
session.add(Post(users_id=2, title="Python楽しい", body="Python楽しいですよね！！"))
session.commit()

# inner joinのサンプル
users_posts = session.query(User, Post).join(Post, User.id == Post.users_id).all()

for user_posts in users_posts:
	print("%sさんの投稿 タイトル:%s" % (user_posts.User.name, user_posts.Post.title, ))

print('*****')
# left outer joinのサンプル
users_posts = session.query(User, Post).outerjoin(Post, User.id == Post.users_id).all()

for user_posts in users_posts:
	if user_posts.Post is not None:
		print("%sさんの投稿 タイトル:%s" % (user_posts.User.name, user_posts.Post.title, ))
	else:
		pass
		print("%sさんの投稿 なし" % (user_posts.User.name, ))


"""
以下の結果を取得することができます。
テーブルのリレーションが定義されていないため、
結果のオブジェクトは階層構造になっておらず冗長になっている点に注目してください。
"""

# Suzukiさんの投稿 タイトル:朝の体操
# Suzukiさんの投稿 タイトル:今日の夕食
# Tanakaさんの投稿 タイトル:仕事
# Tanakaさんの投稿 タイトル:Python楽しい
# *****
# Suzukiさんの投稿 タイトル:今日の夕食
# Suzukiさんの投稿 タイトル:朝の体操
# Tanakaさんの投稿 タイトル:Python楽しい
# Tanakaさんの投稿 タイトル:仕事
# Satoさんの投稿 なし
