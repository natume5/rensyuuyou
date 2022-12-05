#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- SQLAlchemy入門 ORM その4 リレーションとJOIN ---")


print("--- relationshipとjoin ---")


"""
あるテーブルのレコードに対して、別のテーブルのレコードが複数紐づくようなリレーションです。
例えば、ブログシステムにおけるユーザーと投稿の関係などがこれに該当しますね。
子テーブルに外部キーを定義し、親テーブルクラス内で以下のように
relationship関数を使用します。

子属性 = relationship("子テーブル")

前回のサンプルにOne To Manyのリレーション定義を追加したサンプルを見てみましょう
"""


from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# DB接続
engine = create_engine('sqlite:///:memory:')

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	age = Column(Integer)

	posts = relationship("Post", backref="users")
	# Postとのリレーション

class Post(Base):
	__tablename__ = 'posts'
	id = Column(Integer, primary_key=True)
	users_id = Column(Integer, ForeignKey('users.id'))
	title = Column(String)
	body = Column(Integer)

	user = relationship('User')    # Userとのリレーション

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
users = session.query(User).join(Post, User.id == Post.users_id).all()

for user in users:
	print("%sさんの投稿" % (user.name))
	for post in user.posts:
		print("|- タイトル: %s" % (post.title, ))
	print('')

"""
以下のような実行結果が得られます。
前回のサンプルと異なり、結果オブジェクトが階層化されていることが確認できます。
"""

# Suzukiさんの投稿
# |- タイトル: 朝の体操
# |- タイトル: 今日の夕食

# Tanakaさんの投稿
# |- タイトル: 仕事
# |- タイトル: Python楽しい

"""
また、relationship関数の引数にback_populates、backref、
uselistなどの引数を指定することにより、
関係の双方向性やユニーク性を定義することができます。
これらの組み合わせによりOne To Many、Many To One、
One To One、Many To Many、
アソシエーションといった関係を定義することができます。
"""
