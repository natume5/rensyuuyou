#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説---")
print("--- 【Python】datetimeモジュールを使って時刻を取得する方法まとめ（初心者向け）  ---")


"""
Pythonには、日付や時刻を表現する為のデータ型が用意されています。
データ型は日付ならdata、時刻ならtimeと幾つか種類があるのですが、
こうした時間に関わるデータ型をまとめているのがdatetimeモジュールです。
本稿では、このdatetimeモジュールを使って様々な処理を行うやり方について紹介していきます。
一通り網羅していますので、使い方を忘れてしまった時の参照用としても使っていただければ嬉しいです。
"""


print("--- datetimeモジュールとは？ ---")


"""
datetimeモジュールには、日付や時刻を操作するクラスが用意されています。

使用場面の例

    取得したデータの日付が最新であるかを判定
    更新した日付をデータベースやcsvファイルに書き込みたい時
    受け取った文字列の日付をdate型に変換

システムによって様々ですが、datetimeモジュールを扱えるようになると、
日付に関する処理を命令できるようになります。
標準でインストールされているモジュールの為、Pythonの環境を構築していればすぐに使用できます。
"""


print("--- datetimeモジュールの使い方 ---")


"""
datetimeは日時を扱うためのモジュールで、日時の取得や曜日の取得、
日時の比較や文字列変換などが可能です。
Pythonが実行できる状態であれば既に利用できる状態なので、
ソースコードの上部にdatetimeをimportしてくればすぐに利用できます。

import datetime

では、実際にdatetimeモジュールを利用してみましょう。

現在日付の取得

現在の日時を取得するにはdate.today()を使います。
"""

import datetime as d

print(d.date.today())    # 2022-08-01

"""
結果は「yyyy-mm-dd」の状態で取得できます。
"""

# import datetime as d

print(type(d.date.today()))    # <class 'datetime.date'>

"""
datetimeで取得したデータはdatetimeの型で取得するので、
比較をする際は両方の型を合わせる必要があります。

型変換はこの後で紹介します。


タイムゾーンの設定

datetimeモジュールでは日本の自国だけでなく世界中のタイムゾーンから取得することも出来ます。
海外の時間を取得したい場合はpytzもimportしてきましょう。
pytzはタイムゾーンを取得出来るサードパーティーライブラリで、
公式も使用を推奨しているポピュラーなライブラリです。
今回は東京・ロンドン・ニューヨークの時刻をそれぞれ取得してみます。
"""

import pytz
from datetime import datetime

print(datetime.now(pytz.timezone('Asia/Tokyo')))
print(datetime.now(pytz.timezone('Europe/London')))
print(datetime.now(pytz.timezone('America/New_York')))

# 2022-08-01 13:46:04.082976+09:00
# 2022-08-01 05:46:04.082976+01:00
# 2022-08-01 00:46:04.098641-04:00

"""
時刻の読み方ですが、東京の場合『2022年5月6日15時21分10秒』となります。
なお末尾についている『+09:.00』は協定世界時（UTC）との時差を示すものです。
UTCはイギリスの都市が標準なので同国から離れるほど時差も大きくなっていることがわかりますね。
速度面や性能面を重視する際はtimezoneが推奨されていますが、少々記述が複雑になります。
"""

# import datetime as d

tz = d.timezone(d.timedelta(hours=9), name='JAPAN')
print(d.datetime.now(tz))    # 2022-08-01 13:50:05.806871+09:00

"""
自分で時差を設定する必要があるので、使い分けましょう。


今日の年、月、日をそれぞれ取得する

タイムゾーン取得では時刻情報がまとめて吐き出されましたが、それぞれ分けて出力する方法もあります。
それぞれ日時を分解するにはformatメソッドを使いましょう。
以下では年からマイクロ秒までを各行で取得しています。
"""

# import datetime as d

now = d.datetime.now()
print("年:{0}".format(now.year))
print("月:{0}".format(now.month))
print("日:{0}".format(now.day))
print("時:{0}".format(now.hour))
print("分:{0}".format(now.minute))
print("秒:{0}".format(now.second))
print("マイクロ秒:{0}".format(now.microsecond))

# 年:2022
# 月:8
# 日:1
# 時:13
# 分:58
# 秒:19
# マイクロ秒:916768

"""
2行目で日時を全て取得しておき、3行目以降で分解していきます。
3行目以降に{0}が利用されていますが、{}に入る数字はformatメソッドの引数を指定します。
例えばformatメソッドに複数引数が入っているとします。
"""

print("年:{0}".format(now.year, "Python×業務効率化の解説サイト"))    # 年:2022

"""
このようにformatメソッドにある引数のどれを利用したいかを、{}に指定しましょう。
もちろん複数ある場合でも、上記のコードの場合0を利用すれば日付を取得できます。


weekdayメソッド（曜日の取得）

曜日を取得するにはweekday()を使います。
weekday()を使うと0〜6の数値が取得できます。
0が月曜、1が火曜、2が水曜...と、月曜から順番にそれぞれの数値と曜日が紐づいています。
次のコードではweekday()で取得した数値から曜日の名称を取得しています。
"""

# import datetime as d

week_name = {0: "月曜", 1: "火曜", 2: "水曜", 3: "木曜", 4: "金曜", 5: "土曜", 6: "日曜"}

now = d.datetime.now()
thursday = d.datetime(2022, 5, 5)
print(week_name[now.weekday()])    # 月曜
print(week_name[thursday.weekday()])    # 木曜

"""
15行目は現在の曜日を表示し、16行目では指定した日付の曜日を表示しています


strftime・strptimeメソッド (日時⇔文字列の変換)

「現在日付の取得」で少し触れたように、datetimeで作成した日時は文字列ではなく
datetimeクラスなので、文字列として扱いたい場合は変換が必要です。
datetimeを文字列に変換するには先ほどのformatメソッドを使う方法もありますが、
そのほかにstrftimeメソッドを使う方法があります。
strftime()の2つ目の引数に書式コードを指定することでフォーマットの指定が可能です。
日付→文字列に変換したい場合はstrftimeメソッドを使いましょう。
"""

# import datetime as d

now = d.datetime.now()
now_str = d.datetime.strftime(now, "%Y/%m/%d %H:%M:%S")
print(now_str)    # 20220801 14:18:28
print(type(now_str))    # <class 'str'>

"""
文字列→日付に変換したい場合はstrptimeメソッドを利用します
（※似ていますが「str“p”time」なので注意してください）。
"""

# import datetime as d

str_datetime = "2022/08/01 14:18:28"
datetime = d.datetime.strptime(str_datetime, "%Y/%m/%d %H:%M:%S")
print(datetime)    # 2022-08-01 14:18:28
print(type(datetime))    # <class 'datetime.datetime'>

"""
条件分岐などで日付の比較を行いたい場合は、どちらも同じ型に合わせましょう。
"""


print("--- timeライブラリの使い方 ---")


"""
最後にdatetimeではありませんが、時刻を取得する用途で使われるライブラリ、
timeを紹介しておきたいと思います。timeは時間を扱うためのライブラリで、
システム時間の取得、時刻のフォーマット変換などが可能です。
timeライブラリも標準でインストールされているので、importすれば利用できます。

UNIX時間での現在時刻の取得

UNIX時間はエポック秒とも呼ばれており、
UTCの1970年01月01日00時00分00秒からの秒数が表示される時刻表示です。
"""

import time

print(time.time())    # 1659331983.8222752

"""
UNIX時間からの時間が表示されます。
1970年01月01日からの経過秒数で現在時刻を表示されても…という感じなので、
続いてUNIX時間を分かりやすく表示させるための方法を紹介します。


現在時刻の取得

t.gmtimeメソッドを使えば、datetimeで見たように人間にもわかりやすい時刻を取得することが出来ます。
具体的には次にオブジェクトを入力すれば、任意の時刻情報を取得することが出来ます。

年	tm_year
月	tm_mon
日	tm_mday
時	tm_hour
分	tm_min
秒	tm_sec
曜日を0～6で表した数値	tm_wday
年の頭から数えた経過日数	tm_yday
サマータイムのフラグ	tm_isdst

具体的に見てみましょう。今回は「時」と「分」を取得してみます。
"""

import time as t

print(str(t.gmtime().tm_hour) + "時" + str(t.gmtime().tm_min) + "分")
# 5時38分

"""
分かりやすい時刻が取得出来ました。
"""


print("--- まとめ ---")


"""
今回はdatetimeモジュールとライブラリのtimeを使った時間に関係する処理のやり方を紹介しました。
時間に関係すると言っても用途によって利用するメソッドやデータ型が異なってくるのでご注意ください。
"""
