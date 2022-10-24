#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- datetimeモジュールとdatetime型 ---")


"""
標準ライブラリのdatetimeモジュールには
日付と時間を扱う型がいくつか用意されています。
このページではdatetimeモジュールと
その中のdatetime型について解説します。
"""


print("--- datetimeモジュール ---")


"""
datetimeモジュールには日付、時間データを様々な方法で
操作する方法が提供されています。
まずは代表的な4種類のオブジェクトを紹介します。

型 	                          説明
date型 	               日付 (年、月、および日) を表します。
time型 	               ローカル時刻を表します。
datetime型 	           dateオブジェクトおよび 
                       timeオブジェクトの全ての情報が入っている
                       単一のオブジェクトです。
timedelta型 	           経過時間、
                       つまり2つの日付や時刻間の差を表します。
"""


print("--- datetime型 ---")


"""
それではdatetimeモジュールのdatetime型から説明します。
モジュール名と型の名前が一緒ですが混同しないように注意してください。
(import文で混乱されている方はこちらで復習してください。)


datetime型変数の生成

datetime型の変数を生成する際は、
引数に年、月、日、自、分、秒、マイクロ秒を順に指定します。
以下のサンプルは、2018-01-02 03:04:05を表す
datetime型の変数を生成しています。
"""

from datetime import datetime

# datetimeオブジェクトの生成
dt_obj = datetime(2018, 1, 2, 3, 4, 5, 000000)
print(dt_obj)    # 2018-01-02 03:04:05

"""
現在日時の取得

datetimeのnowメソッドを使用すると、
現在時刻のdatetime型変数を得ることができます。
"""

from datetime import datetime

# 現在日時の取得
dt_obj_now = datetime.now()
print(dt_obj_now)    # 現在時刻が表示される
# 2022-10-22 10:25:23.760809

"""
日付、時刻要素の取得

datetime型の変数から年、月、日、自、分、秒などの要素を
取得することができます。
は下記の通りそれぞれに対応した属性を使用します。
"""

from datetime import datetime, timedelta

dt_obj = datetime(2018, 1, 2, 3, 4, 5, 000000)

print(dt_obj)    # 2018-01-02 03:04:05
print(dt_obj.year)    # 2018
print(dt_obj.month)    # 1
print(dt_obj.day)    # 2
print(dt_obj.hour)    # 3
print(dt_obj.minute)    # 4
print(dt_obj.second)    # 5
print(dt_obj.microsecond)    # 0

"""
文字列からdatetimeへ変換

strptimeメソッドを使用すると、
文字列からdatetime型に変換することができます。
第1引数に日付時刻の文字列を、
第2引数にフォーマット文字列を指定します。
"""

from datetime import datetime

# 文字列からdatetimeへ(strptimeメソッドの利用)
dt_str = '2017-04-01 12:32:05'
dt_obj = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
print(type(dt_obj))    # <class 'datetime.datetime'>

"""
上のサンプルの年月日の区切りはハイフンですが、
例えばスラッシュを使用したい場合は
フォーマット文字列に'%Y/%m/%d %H:%M:%S'を指定します。


datetimeから文字列への変換

strftimeメソッドを使用すると、
さきほどとは逆にdatetimeから文字列に変換することも可能です。
引数に文字列フォーマットを指定します。
"""

from datetime import datetime

# 文字列からdatetimeに変換
dt_str = '2017-04-01 12:32:05'
dt_obj = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

# datetimeから文字列に変換(strftimeメソッドの利用)
dt_str2 = dt_obj.strftime('%Y/%m/%d %H:%M:%S')
print(dt_str2)    # 2017/04/01 12:32:05

"""
datetimeの加減算

日時の計算にはtimedelta型を使用します。
引数に週(weeks)、日(days)、時(hours)、
分(minutes)、秒(seconds)、ミリ秒(milliseconds)、
マイクロ秒(microseconds)を指定できます。
必要なものだけキーワード引数を指定します。
"""

from datetime import datetime, timedelta

dt_obj = datetime(2018, 1, 2, 3, 4, 5, 000000)
print(dt_obj)    # 2018-01-02 03:04:05

delta = timedelta(days=1)    # 1日分の間隔

dt_obj2 = dt_obj + delta    # 1日分足す
print(dt_obj2)    # 2018-01-03 03:04:05

dt_obj3 = dt_obj - delta    # 1日分引く
print(dt_obj3)    # 2018-01-01 03:04:05

"""
また、datetime型の変数同士を演算することも可能です。
引き算するとその間隔のtimedelta型変数を取得することができます。
"""

from datetime import datetime, timedelta

# 2018-01-02 03:04:05
dt_obj1 = datetime(2018, 1, 2, 3, 4, 5, 000000)

# 2018-02-03 04:05:06
dt_obj2 = datetime(2018, 2, 3, 4, 5, 6, 000000)

# 日時の間隔を求める
delta = dt_obj2 - dt_obj1
print(delta)    # 32 days, 1:01:01

"""
このサンプルでは２つの日時の間隔を引き算で求めています。
次回は日付と時間を表すdate型、time型について解説します。
"""
