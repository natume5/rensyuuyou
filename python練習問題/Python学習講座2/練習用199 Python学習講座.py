#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- datetimeモジュールとdate型/time型 ---")


print("--- datetime.date ---")


"""
datetimeモジュールのdate型は日付を表す型です。
date型変数の生成

date型変数を生成する場合、引数に順に年月日を指定します。
以下のサンプルは、2017/01/02を表すdate型の変数を生成しています。
"""

from datetime import date

d = date(2017, 1, 2)
print(d)    # 2017-01-02

"""
文字列からdate型への変換

datetimeのstrptimeメソッドに相当するものがないため、
datetime型変数を一旦生成してからdateに変換します。
"""

from datetime import datetime, date

# 文字列からの変換->datetimeを経由する
dt_str = '2017-04-01'
dt_obj = datetime.strptime(dt_str, '%Y-%m-%d')    # datetimeを生成
d = dt_obj.date()    # date型へ変換する
print(d)     # 2017-04-01

"""
現在日付の取得

date.todayを使用するか、datetimeから変換する方法があります。
"""

from datetime import datetime, date

# todayを使用する場合
today = date.today()

# 現在日時から日付に変換する場合
dt_obj_now = datetime.now()
today = dt_obj_now.date()    # date型に変換する
print(today)    # 2022-10-22

"""
日数の計算

datetimeと同様、timedeltaを使用します。
"""

from datetime import timedelta, date

d1 = date(2017, 1, 2)
delta = timedelta(days=3)    # 3日
d2 = d1 + delta     # 3日加算
print(d2)    # 2017-01-05

"""
また、引き算により日付の間隔を算出することが可能です。
"""

from datetime import timedelta, date

d1 = date(2016, 12, 22)    # 2016-12-22
d2 = date(2017, 1, 2)    # 2017-01-02
delta = d2 - d1    # 日付の間隔を取得する
print(delta)    # 11 days, 0:00:00


print("--- datetime.time ---")


"""
datetimeモジュールのtime型は時間を表す型です。
概ねdateオブジェクトと同様なので、サンプルだけ掲載し、説明は割愛します。
なお、time型には演算が定義されていませんので注意してください。
"""

from datetime import datetime, time

# time型変数の生成
t1 = time(13, 0, 0)
print(t1)    # 13:00:00

# 文字列からtimeへの変換(datetimeを経由する)
dt_str = '13:30:15'
dt_obj = datetime.strptime(dt_str, '%H:%M:%S')
t2 = dt_obj.time()
print(t2)    # 13:30:15
