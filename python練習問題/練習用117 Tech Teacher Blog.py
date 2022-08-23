#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Tech Teacher Blog ---")
print("--- Pythonのdatetimeを使いこなそう！現在日時取得から文字列変換まで ---")


"""
Pythonを学習していると

「datetimeモジュールの使い方がわからない」
「もっと網羅的にdatetimeについて知りたい」

などといった悩みを抱えることもありますよね。
そこで今回はdatetimeモジュールに関する知識や使い方を詳しく説明していきます。
"""


print("--- datetimeモジュールについて ---")


"""
「datetimeモジュール」とは、Pythonで日付や時刻に対して
さまざまな操作をすることができるモジュールで、現在の時刻の取得から日時の計算、
指定した形式での表示などを行うことができますよ。

datetimeモジュールのオブジェクトは以下の通りです。

    datetime：日付と時刻を扱う
    date：日付を扱う
    time：時刻を扱う
    timedelta：時間差を扱う

ここで、モジュール・オブジェクト・メソッドの関係性を紹介します。

モジュール 	     よく使用する処理があらかじめまとめて定義されているファイル
オブジェクト 	 文字列・リスト・日付などのことで、データを扱うのに便利な関数を持っている
メソッド 	     オブジェクトが持っている関数

つまり、モジュール・オブジェクト・メソッドの関係性をまとめると
次のような階層構造になっていることがわかります。

モジュール　例： datetime
└ オブジェクト　例:：datetime
└ メソッド　例:：now( ) , strftime( )

それでは、datetimeモジュールに入っている4つのオブジェクトについて説明していきます。
"""


print("--- datetimeオブジェクトについて ---")


"""
datetimeオブジェクトは日付と時刻の両方の情報を持っているオブジェクトで、
「year」「month」「day」「hour」「minute」「second」「microsecond」
などを利用してそれらの情報にアクセスできますよ。
datetimeモジュールを使用するには、「import」を忘れないように注意しましょう。
"""

import datetime

"""
datetime . now ( )

datetimeオブジェクトで、現在の日付と時刻を取得するには
「datetime . now ( )メソッド」を使用します。
"""

dt_now = datetime.datetime.now()
print(dt_now)    # 2022-08-18 14:44:21.591900

print('年:', dt_now.year)     # 年: 2022

print('月:', dt_now.month)    # 月: 8

print('日:', dt_now.day)    # 日: 18

print('時:', dt_now.hour)    # 時: 14

print('分:', dt_now.minute)    # 分: 44

print('秒:', dt_now.second)    # 秒: 21

print('マイクロ秒:', dt_now.microsecond)    # マイクロ秒: 591900

"""
このように「datetime.datetime.now()」とすることで、
変数「dt_now」に現在の日付や時刻を格納できました。
この変数に対して「year」などのメソッドを使用することで、
年月日時分秒マイクロ秒を取得できますよ。


datetimeオブジェクトのコンストラクタ

datetimeオブジェクトでは、任意の日付や時刻を作成することができますよ。

1.　＃　datetimeオブジェクトのコンストラクタ
2.　datetime ( year , month , day , hour=0 , second=0 , maicrosecond=0 , tzinfo=None )
3.　＃　year・month・day以外は省略でき、省略した場合は初期値の0となる

実際にコードを用いて説明していきます。
"""

dt = datetime.datetime(2020, 1, 1, 12, 30, 20, 1230)
print(dt)    # 2020-01-01 12:30:20.001230

print(dt.minute)    # 30

print(dt.microsecond)    # 1230

dt = datetime.datetime(2020, 1, 1)

print(dt)    # 2020-01-01 00:00:00

print(dt.minute)    # 0


print("--- dateオブジェクトについて ---")


"""
dateオブジェクトは日付の情報を持っているオブジェクトで、
「year」「month」「day」などの属性にアクセスすることができますよ。


day . today ( )

dateオブジェクトで現在の日付を取得するには「date . today ( )メソッド」を使用します。
"""

d_today = datetime.date.today()
print(d_today)    # 2022-08-20

print(d_today.year)    # 2022

print(d_today.month)    # 8

print(d_today.day)    # 20

"""
このように、「datetime.date.today()」とすることで、
変数「d_today」に現在の日付を格納することができます。
この日付型変数に様々なメソッドを使用することで簡単に現在の日付を取得することができますよ。


dateオブジェクトのコンストラクタ

dateオブジェクトのコンストラクタは下記のようになっており、いずれも省略できないので注意しましょう。

1.　＃　すべて必須
2.　date ( year , month , day )

実際にコードを用いて説明していきます。
"""

d = datetime.date(2020, 1, 1)
print(d)    # 2020-01-01

print(d.month)    # 1

"""
このようにすべて必須ですので入力するのを忘れないようにしましょう。
"""


print("--- timeオブジェクトについて ---")


"""
timeオブジェクトは時刻の情報を持っているオブジェクトで、
「hour」「minute」「second」「microsecond」といった属性にアクセスすることができますよ。


time.time ( )

現在の時刻を取得するには「timeモジュール」をインポートして「time.time( )メソッド」を使用します。

time( )メソッドを使用すると現在のUNIX時間をfloat型で取得できます。
UNIX時間とは、UTCの1970年1月1日0時0分0秒からの経過秒数のことです。
"""

import time

ut = time.time()

print(ut)     # 1660955147.419349

"""
処理の経過時間も測定することができますよ。


timeオブジェクトのコンストラクタ

timeオブジェクトのコンストラクタは次のようになっており、いずれも省略することができます。
1.　＃　省略した場合は0となる
2.　time ( hour=0 , minute=0 , second=0 , microsecond=0 , tzinfo=None )

実際にコードを用いて説明していきます。
"""

t = datetime.time(12, 30, 20, 1230)
print(t)     # 12:30:20.001230

print(t.minute)    # 30

t = datetime.time()
print(t)    # 00:00:00

"""
このように省略すると初期値の0になることが分かるでしょう。
"""


print("--- timedeltaオブジェクトについて ---")


"""
timedeltaオブジェクトは、2つの日時の時間差や経過時間を表すオブジェクトで、
日数・秒数・マイクロ秒数の情報を持っており「days」「seconds」「microseconds」
でアクセスできます。
また、「total _ seconds ( )メソッド」でトータル秒数を取得することもできますよ。


timedeltaオブジェクトを使用した引き算・足し算

timedeltaを使用することで日付の引き算や足し算を簡単に行うことができますよ。
実際にコードを用いて説明していきます。
"""

today = datetime.date.today()
day_after_tomorrow = datetime.timedelta(days=5)

print(today + day_after_tomorrow)    # 2022-08-25
print(today)     # 2022-08-20
"""
現在の日付2020年5月18日から5日後の日付を表示することができました。
このとき、取得される日時はUTC時刻のため、日本での現地時間と異なることに注意してください。
このようにtimedeltaクラスの引数として任意の数値を渡すことで
日時の計算が簡単に行えるようになりますよ。
また、下記のように日付を比較することも簡単ですよ。
"""

tomorrow = today + datetime.timedelta(days=1)
yestarday = today - datetime.timedelta(days=1)

print('今日は明日よりも後:' + str(today > tomorrow))    # 今日は明日よりも後:False

print('昨日は今日よりも前:' + str(yestarday < today))    # 昨日は今日よりも前:True

"""
上記のように昨日・今日・明日の日付を作成して比較することもできますよ。


datetimeオブジェクト同士の引き算でtimedeltaオブジェクト作成

datetimeオブジェクト・dateオブジェクトなど、
datetimeオブジェクト同士を引き算するとtimedeltaオブジェクトを取得することができます。
"""

today = datetime.datetime.now() - datetime.datetime(1970, 1, 1)
print(today)    # 19224 days, 10:00:44.730769

print(today.days)    # 19224

print(today.seconds)    # 36044

print(today.microseconds)    # 730769

print(today.total_seconds())    # 1660989644.730769

"""
このようにdatetimeオブジェクト同士の引き算でtimedeltaオブジェクトが取得できますよ。


timedeltaオブジェクトのコンストラクタ

timedeltaオブジェクトのコンストラクタは次のようになっており、いずれも省略することができますよ。
1.　＃　省略した場合は初期値の0となる
2.　timedelta ( days=0 , seconds=0 , microseconds=0 , milliseconds=0 , minutes=0 , hours=0 , weeks=0 )

timedeltaオブジェクトが持っている情報は、
あくまで「days」「seconds」「microseconds」のみなので注意してください。
"""

td_1w = datetime.timedelta(weeks=1)
print(td_1w)    # 7 days, 0:00:00

print(td_1w.days)    # 7


print("--- strftime( )・strptime( )について ---")


"""
ここからはstrftime( )とstrptime( )について説明していきます。
最後に違いやそれぞれの覚え方も紹介しますので、ぜひ最後までご覧くださいね。


strftimeとは

「strftime( )メソッド」とは、「date」「time」または「datetimeオブジェクト」
を使用して日付と時刻を表す文字列を返すメソッドです。
使用可能な書式化コードは下記の通りです。


コード                         意味
%a  ロケールの曜日名を省略形で表示。
%A  ロケールの曜日名を表示。
%b  ロケールの月名を省略形で表示。
%B  ロケールの月名を表示。
%c  ロケールの適切な日付および時刻の表示。
%d  10進数で月の始めから何日目かを表示。
%f  10進数でマイクロ秒を表示。
%G  ISO weekの内過半数を含んだ西暦表記のISO 8601 year。
%H  10進数で24時間計での時を表示。
%I  10進数で12時間計での時を表示。
%j  10進数で年の初めから何日目かを表示。
%m  10進数で月を表示。
%M  10進数で分を表示。
%p  ロケールのAM・PMに対応する文字列。
&S  10進数で秒を表示。
%u  月曜日を1とする10進数表記のISO 8601 weekday。
%U  10進数で年の初めから何週目かを表示。年明けから最初の日曜日までの全ての曜日は0週目。
%w  曜日を10進表記した文字列を表示。表示は日曜日が0・土曜日が6。
%W  10進数で年の初めから何週目かを表示。年明けから最初の月曜日までの全ての曜日は0週目。
%x  ロケールの適切な日付を表示。
%X  ロケールの適切な時刻を表示。
%y  10進数で上2桁のない西暦年を表示。
%Y  10進数で上2桁が付いている西暦年を表示。
%Z  タイムゾーン名。タイムゾーンがない場合は空文字列。
%%  文字「%」を表示。


曜日名や月名の「%a」「%A」「%b」「%B」は、ロケールによって
取得できる文字列が違うので気をつけましょう。
では、実際にコードを用いて使い方を説明していきます。
"""

today = datetime.datetime.now()
print(today.strftime('%Y - %m - %d %H: %M: %S'))   # 2022 - 08 - 20 10: 52: 00 

print(today.strftime('%Y%M%d'))    # 20225220

print(today.strftime('%A, %B %d, %Y'))    # Saturday, August 20, 2022

print(today.strftime('%Y年%m月%d日'))     # 2022年08月20日

print('日番号:', today.strftime('%j'))     # 正月を001とした場合
# 日番号: 232

print('週番号:', today.strftime('%U'))    # 週の始まりは日曜日で正月が00とした場合
# 週番号: 33

"""
文字列ではなく数値で取得したい場合は
「int ( )」で整数に変換すれば数値を取得することができますよ。


strptimeとは

「strptime( )」とは、指定した日付や時刻の文字列から
「datetimeオブジェクト」を作成することができるメソッドで、
元の文字列に対応する書式化の文字列を指定する必要がありますよ。
"""

date_str = '2020 / 5 / 18 16 : 34'
date_dt = datetime.datetime.strptime(date_str, '%Y / %m / %d %H : %M')
print(date_dt)    # 2020-05-18 16:34:00

#　strftime( )メソッドを使用することで元の文字列と違うフォーマットで表示
print(date_dt.strftime('%Y年%M月%d日 %H時%M分'))
# 2020年34月18日 16時34分

"""
また、datetimeオブジェクトに変換すればtimedeltaオブジェクトとの演算をすることができますので、
同じフォーマットで10日前の日付の文字列を作成することもできますよ。
"""

date_str = '2020年5月18日'
date_format = '%Y年%m月%d日'
td_10_d = datetime.timedelta(days=10)

date_dt = datetime.datetime.strptime(date_str, date_format)
date_dt_new = date_dt - td_10_d
date_str_new = date_dt_new.strftime(date_format)

print(date_str_new)    # 2020年05月08日


"""
strftime( )とstrptime( )の違い

strftime( )・strptime( )、どちらも日付と文字列を変換するメソッドです。
どっちがどっちのメソッドだったか悩まないように、ここでは違いや覚え方を紹介します。
「strftime( )」の「f」は「format」からきています。formatとは「書式」という意味があり、
書式があるのは文字列のみなので、「日付→文字列」の変換をするメソッドがstrftime( )となります。
また、strftimeの「f」を「from」とみなして考えると「str from time」となります。
つまり、時間・日付から文字列という意味になるため、
strftimeは日付から文字列に変換するメソッドとなります。
「strptime( )」の「p」は「parse」からきています。
parseとは「解析する」という意味があり、解析が必要なのは文字列なので、
「文字列→日付」の変換をするメソッドがstrptime( )となります。

また、strptimeは「from」ではない方と覚えると良いでしょう。

それぞれの違いは以下の通りです。

    strftime：日付から文字列
    strptime：文字列から日付
"""


print("--- まとめ ---")


"""
これまでPythonのdatetimeについて説明してきましたが、いかがでしたでしょうか。

今回説明した要点をまとめると以下のようになります。

    datetimeモジュールとは、日付や時刻に対してさまざまな操作をすることができるモジュール
    現在の日付・時刻を取得するにはdatetime.datetime . now ( )を使用
    現在の日付を取得するにはdatetime.date . today ( )を使用
    時刻を取得するにはtime.time( )を使用
    timedeltaオブジェクトは2つの日時の時間差や経過時間を表す
    strftime( )は日付や時間の情報を任意の書式フォーマットの文字列に変換
    strptime( )は日付や時刻を表す文字列からdatetimeオブジェクトを作成

datetimeを使用すれば簡単に日付や時刻を扱うことができるため、
この機会にしっかり理解を深めておくと良いでしょう。
"""
