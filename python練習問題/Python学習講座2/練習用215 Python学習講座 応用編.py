#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- SQLAlchemy入門 接続とSQL実行 ---")


print("--- engine apiと接続 ---")


"""
SQLAlchemyが提供するengineとは、
接続を始めとしたSQLAlchemyの機能を使用するための起点となるオブジェクトです。
engineだけでも最低限のDB操作、つまりデータベースへの接続の作成、
SQLステートメントの送信、および結果の取得を行うことができます。
engineオブジェクトは、create_engine関数を呼び出して
データソース名を渡すことによって作成されます。
engineを使用した簡単なサンプルを見てみましょう。
sqlite3のオンメモリのDBに接続し、SQLを実行してみます。


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


<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x000002B3AA8ACCD0>
<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x000002B3AA8ACB80>
<sqlalchemy.engine.cursor.LegacyCursorResult object at 0x000002B3AA8ACCA0>
(1, 'Kuro', 33)
(2, 'Sato', 27)


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


print("--- DBMS別接続サンプル ---")


"""
それでは、よく使われるOSSのDBMSの接続サンプルを紹介しましょう。

MySQL

ドライバにMySQLdbが使用されます。
フォークされたmysqlclientでも問題ありません。
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

こちらは最初のサンプルのとおりです。
組み込みのモジュールで接続可能ですので準備いらずで楽ですね。

from sqlalchemy import create_engine
engine = create_engine('sqlite:///sqliteファイル')

また、オンメモリで実行する場合は以下のように記述します。

engine = create_engine('sqlite:///:memory:')

その他は公式の以下をご参照ください。
http://docs.sqlalchemy.org/en/latest/core/engines.html

今後、サンプルでは基本的に準備作業を軽減するため、
にsqlite3のオンメモリを主に使用します。
"""


print("--- コネクションとSQLの実行 ---")


"""
（ほとんど冒頭のサンプルで説明し終わっているのですが）
engineオブジェクトを生成した後、
コネクションオブジェクトのexcecuteメソッドで任意のSQLを
実行することが可能です。
また、コロン記号をSQL内の変数として使用することができます。
以下、CRUDのサンプルです。
"""


from sqlalchemy import create_engine


engine = create_engine('sqlite:///:memory:')

# 接続する
with engine.connect() as con:
    # Drop文を実行
    con.execute("DROP TABLE IF EXISTS USERS")

    # Create文の実行
    con.execute("CREATE TABLE USERS(id INTEGER PRIMARY KEY,\
     name TEXT, age INTEGER)")

    # 投入データの定義
    rows = ({"id": 1, "name": "Sato", "age": 31},
        {"id": 2, "name": "Suzuki", "age": 18},
        {"id": 3, "name": "Yamada", "age": 40},
        {"id": 4, "name": "Kuro", "age": 30},
        )

    # Insert文を実行
    for row in rows:
        con.execute("INSERT INTO USERS (id, name, age) \
            VALUES(:id, :name, :age)", **row)

    # Select文を実行する
    rows = con.execute("SELECT * FROM USERS")
    for row in rows:
        print(row)

    # Update文を実行する
    con.execute("UPDATE USERS SET age=42 WHERE id = :id", **{"id": 3})

    # Delete文を実行する文を実行する
    con.execute("DELETE FROM USERS WHERE id = :id", **{"id": 4})

    # 更新の確認
    print("***** 更新後 *****")
    rows = con.execute("SELECT * FROM USERS")
    for row in rows:
        print(row)


"""
(1, 'Sato', 31)
(2, 'Suzuki', 18)
(3, 'Yamada', 40)
(4, 'Kuro', 30)
***** 更新後 *****
(1, 'Sato', 31)
(2, 'Suzuki', 18)
(3, 'Yamada', 42)


**記号で辞書をキーワード引数に展開しています。
ですので、以下のように記述しても問題ありません。

con.execute("INSERT INTO USERS (id, name, age) VALUES(:id, :name, :age)", id=row['id'], name=row['name'], age=row['age'])
"""


print("--- 補足 RowProxy ---")


"""
上のSelect文の実行結果ですが、
戻り値はRowProxyという型のオブジェクトで返されます。
print結果がタプル形式のように表示されている通り、添数でアクセス可能です。
また、辞書のような性質も持ち合わせているため、
カラム名をキーで指定してアクセスすることも可能です。

例えば上のサンプルでnameカラムの値を取得したい場合、
以下のいずれの記述でも取得することができます。

print(row[1])
print(row["name"])
print(row.name)
"""
