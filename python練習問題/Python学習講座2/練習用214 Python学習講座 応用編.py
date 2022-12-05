#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- SQLAlchemy入門 SQLAlchemyとは ---")


print("--- SQLAlchemyとは ---")


"""
SQLAlchemyとは、Pythonの中では最もよく利用されているORMの一つです。
ORM以外にも以下の機能を持ちます。

1 データベースへの接続、SQLの実行
2 メタデータ
3 SQL Expression Language
4 ORM

それぞれ簡単に説明しましょう。


データベースへの接続、SQLの実行

SQLAlchemyは様々なデータベースに対して接続してSQLを実行することができます。
サポートするDBMSは以下のとおりです。有名どころは大抵利用可能です。

    Firebird
    Microsoft SQL Server
    MySQL
    Oracle
    PostgreSQL
    SQLite
    Sybase


メタデータ

SQLAlchemyにはメタデータと呼ばれる
テーブルとPythonのモデルクラスをマッピングする機能があります。
個人的にはSQLAlchemyで最も強力な機能の一つと考えています。
Pythonコードとテーブルを完全に同期させることが可能であり、
テーブルの変更をコードに、コードの変更をテーブルに適用することも可能です。
開発中のマイグレーションの手間を省力化することができます。


SQL Expression Language

JavaのORM、HibernateにはHQLというクエリ言語がありますが、
SQLAlchemyにも同様にクエリを表す記述が用意されています。

SQL Expression Languageを使用することにより、
PythonコードとSQLコードが混在しなくなり、コードの保守性が向上します。


ORM

そして最後がメインのORMです。
クエリの実行結果をモデルに格納します。
オブジェクトへのデータセットが自動化されるため、
開発を効率化させることができます。
ただし、データ分析のような表形式のデータを
そのまま使いたい場合にはやや不向きかもしれません。
"""


print("--- SQLAlchemyのインストール ---")


"""
pipでインストールすることが可能です。

pip install sqlalchemy
"""
