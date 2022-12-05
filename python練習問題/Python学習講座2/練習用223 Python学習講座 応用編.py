#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Flaskで作る簡易分析ツール1 ---")


print("--- これから作るもの ---")


"""
業務で分析を行う際、いろいろ試しながらデータセットと
結果の両方を管理するのは意外と面倒なものです。
このため、Flaskを利用してデータと結果を保存して
人に見せられるようなWebアプリケーションを作成してみましょう。
今回は以下のような散布図行列を題材とします。

CSV、TSV形式データの入力データに対し、
散布図行列を作成してデータを保存します。
また、保存したデータを一覧から参照できるようにします。
データの保存先にはsqlite3を使用しますので、
コマンドラインから使用できるようにしておいてください。
(Macをお使いの方は大抵そのままで使えると思います。)

作成する画面は以下のとおりです。

    新規分析画面：データの登録を行い散布図行列を作成します。
    一覧画面：過去に登録した分析の一覧です。
             分析データの削除と参照画面への遷移を行うことができます。
    参照画面：分析の結果を参照します。

また、あくまでもLan内で使用する簡易ツールということで、
ノンプログラマの分析の方にも実装できるよう、以下の方針で説明を行います。

    とにかくお手軽に
    エラーハンドリングなし
    認証なし
    csrfトークンもなし
"""


print("--- 画面毎の仕様 ---")


"""
各画面のレイアウトです。
新規分析画面

データの登録とタイトルを入力することができます。
送信ボタンをクリックすると、登録したデータに対する散布図行列を作成し、
参照画面で参照することができます。

テキストエリア「分析データ」には以下のような多変量のデータをペーストします。
一行目はヘッダーとします。

参照画面

登録したデータや分析結果を参照します。


一覧画面

過去に登録したデータを一覧で参照します。
"""


print("--- データベース定義 ---")


"""
データベースにはsqlite3を使用します。
テーブルは結果格納用にresultsというテーブルのみを使用します。
定義は以下のとおりです。

resultsテーブルの定義

カラム 	      属性 	                     説明
id 	integer primary key autoincrement 	分析データのキー
title 	text not null 	                分析データのタイトル
data 	text not null 	                分析データ本体
img 	text not null 	                分析結果の画像
                                       （散布図行列）
created  datetime default CURRENT_TIMESTAMP   分析日時
"""
