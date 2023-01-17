#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- pandas入門 DataFrame DB入出力 ---")


"""
CSV、TSVなどのファイル連携と並んでよく使うのがDBからの入出力です。
ここではsqlite3を使用しますが、
コネクションオブジェクトを変えれば他のものも使用可能です。
"""


print("--- read_sql select文の結果をDataFrameに格納する ---")


"""
pandas.io.sqlを使用します。

以下のサンプルは、articleテーブルをメモリ上のsqlite3に作成し、
レコードを2件挿入後、select文の結果をDataFrameに格納しています。
read_sqlの引数にSQL文とコネクションを設定します。
"""

import sqlite3
import pandas as pd
import pandas.io.sql as psql


# sqlite3に接続
con = sqlite3.connect(':memory:')
cur = con.cursor()

# サンプルテーブルを作成
cur.execute('CREATE TABLE articles (id int, title varchar(1024), body text, created datetime)')

# サンプルテーブルを挿入
cur.execute('insert into articles values (1, "sample1", "AAAA", "2017-07-14 00:00:00")')
cur.execute('insert into articles values (2, "sample2", "BBBB", "2017-07-15 00:00:00")')

# Select文からDataFrameを作成
df = psql.read_sql('SELECT * FROM articles;', con)
print(df)

"""
   id    title  body              created
0   1  sample1  AAAA  2017-07-14 00:00:00
1   2  sample2  BBBB  2017-07-15 00:00:00
"""


print("--- to_sql DataFrameの内容をDBに格納する ---")


"""
to_sqlでDataFrameの内容をDBに格納することも可能です。
先ほどのサンプルの続きで、データを1行追加して更新してみましょう。
"""

df2 = pd.DataFrame([['sample3', 'CCC', '2017-07-16 00:00:00']],
	columns=['title', 'body', 'created'], index=[2])
df2.to_sql('articles', con, if_exists='append', index=None)

print(df2)

"""
     title body              created
2  sample3  CCC  2017-07-16 00:00:00

to_sqlの引数にはテーブル名、コネクションを指定します。
if_existsはデータが既に存在している場合の挙動を設定し、
appendかrepleceを選ぶことができます。
簡単にDBと連携ができるため、こちらも分析以外でも重宝すると思います。
"""


print("--- sqlite以外の場合 ---")


"""
2018/08/19追記
冒頭でも書きましたが、
コネクションを変えればMySQLなどの他のRDBを使用することが可能です。
が、sqlite以外はsqlalchemyのengineの使用が必須となりました。
以下にデータ挿入のサンプルを示します。


from sqlalchemy import create_engine

engine = create_engine('mysql://%s:%s@%s:%s%s' % (user,
password, host, port, schema))
with engine.begin() as con:
   df.to_sql('table_name', con=con, if_exists='append',
   index=False)

"""
