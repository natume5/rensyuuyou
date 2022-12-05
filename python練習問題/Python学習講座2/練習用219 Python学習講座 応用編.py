#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- SQLAlchemy入門 ORM その2 さまざまなクエリ ---")


print("--- さまざまなクエリ ---")


"""
session.queryを使用してクエリオブジェクト
（sqlalchemy.orm.query.Query）を生成し
さまざまなクエリを実行することができます。
all()メソッドでオブジェクトを格納したリスト型として結果を取得することができます。

キー指定

where句で主キーを指定する場合、getメソッドを使用します。
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
	print(user.name)    # Suzuki


# select * from users where id =1;
suzuki = session.query(User).get(1)


"""
カラム指定

where句でカラムを指定する場合、filter_byメソッドを使用します。
引数にカラムの値を指定してください。
"""


# select * from users where name="Suzuki"
users = session.query(User).filter_by(name="Suzuki").all()


"""
limit

limitを指定する場合はlimitメソッドを使用します。
"""


# select * from users where age=21 limit 1;
users = session.query(User).filter_by(age=21).limit(1).all()


"""
order

order byを指定する場合はorderメソッドを使用します。
"""

# select * from users where age=21 order by name;
users = session.query(User).filter_by(age=21).order_by(User.name).all()


"""
最初の1件を取得

最初の1件を取得する場合はfirst()メソッドを使用します。
"""


user = session.query(User).filter_by(age=21).order_by(User.name).first()


"""
件数取得

件数を取得する場合はcount()メソッドを使用します。
"""


user_cnt = session.query(User).filter_by(age=21).count()


print("--- filterメソッドによるwhere句 ---")


"""
先ほど、簡単なwhere句としてfilter_byメソッドを使用しましたが、
複雑な検索条件を指定する場合はfilterを使用します。
まずは簡単なサンプルから見てみましょう。where句を単純に使用してみます。
"""

users = session.query(User).filter(User.age == 19).all()


"""
引数の指定が一見奇妙にみえますが、これは真偽値を渡しているわけではありません。
独自の比較演算子が定義されており、比較の結果、
BinaryExpressionという型が取得されます。
気になる方は以下のコードを実行してみてください。
"""

print(type(User.age == 19))
# <class 'sqlalchemy.sql.elements.BinaryExpression'>

"""
filterメソッドを使用すると、AND条件、OR条件、IN句を
以下のように使用することができます。


AND条件
"""

from sqlalchemy import and_

users = session.query(User).filter(and_(User.name == 'Sato',
	User.age == 21)).all()

"""
OR条件
"""

from sqlalchemy import or_

users = session.query(User).filter(or_(User.name == 'Suzuki',
	User.age == 21)).all()

"""
IN句
"""

users = session.query(User).filter(User.age.in_([19, 21])).all()


print("--- 補足 all()について ---")


"""
all()は取得結果のシーケンシャルオブジェクトをlistに変換してくれる糖衣構文です。実装上は以下のようになっています。

# sqlalchemy/orm/query.py
    def all(self):
        """"""Return the results represented by this ``Query`` as a list.

        This results in an execution of the underlying query.

        """"""
        return list(self)

このため、実はall()は使わなくても、以下のような記述をすることもできます。
"""

users = session.query(User).filter(User.age.in_([19, 21]))
for query in users:
	print(query.name)
# Suzuki

