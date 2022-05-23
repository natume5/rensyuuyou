#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- Python入門　__pycache__と.pycファイル---")


"""
Pythonのバイトコード

自前のPythonモジュールをimportすると自動的に__pycache__というディレクトリが作成され、
配下に.pycファイルが作成されます。これは実行時にコンパイルした結果のバイトコードのキャッシュです。
なお、__pycache__ディレクトリの生成はPython3.2以降の仕様で、
それ以前のバージョンの場合は同じ階層に.pycファイルが配置されます。


__pycache__と.pycファイルを生成させない

実行時にBオプションを指定すると、このキャッシュ機能をOFFにすることができます。
たとえば、run.pyという名前のスクリプトを実行する場合、以下のように実行します。

python -B run.py
"""


print("--- Python入門　モジュールの実行と__name__---")


"""
変数__name__と"__main__"
変数__name__に格納されているもの
まず、__name__という特別な変数ですが、これには現在実行中のモジュールの完全修飾名が格納されます。
ただし、いつでもモジュール名が格納されるわけではなく、実行時のトップレベル（いわゆるエントリーポイント）
のモジュールの場合は"__main__"という文字列が格納されます。
つまり、そのモジュールがスクリプトのエントリーポイントとして実行されたかどうかはこの
__name__が__main__かどうかで判定することが可能、ということです。
したがって、スクリプトとして実行された場合の挙動は冒頭のif文の後に記述すれば良いわけです。

ただし、__name__に格納される値については他にも例外があります。
代表的なものとして、パッケージの__init__.pyが挙げられます。
このモジュールの__name__にはパッケージ名が格納されます。
ここまでの説明が飲み込めない方も多いと思いますが、次のサンプルを実行してみると理解が深まると思います。

理解を深めるためのサンプル
カレントディレクトリにsample1.pyとpkg1パッケージが配置されているものとします。
また、pkg1配下には__init__.pyとmod1.pyが配置されているものとします。
"""

"""

.
├── pkg1
│   ├── __init__.py
│   └── mod1.py
└── sample.py
それぞれ以下のコードを記述します。

sample.py


# sample.py
from pkg1 import mod1

def func1():
    print('sample.py : ' + __name__)
    mod1.func1()

if __name__ == '__main__':
    func1()
pkg1/__init__.py


# __init__.py
print('__init__.py : ' + __name__)
pkg1/mod1.py


# pkg1/mod1.py
 
def func1():
    print('pkg1/mod1.py : ' + __name__)
 
 
if __name__ == '__main__':
    func1() 

コードの解説です。カレントディレクトリのsample1.pyを実行すると、
パッケージとそのモジュールmod1.pyを読み込みます。
それぞれのpythonファイルは__name__の値を表示するだけのプログラムです。
また、パッケージ配下のmod1モジュールは実行可能となっています。

それではまず、カレントディレクトリのsample1.pyを実行してみましょう。


$ python sample1.py
__init__.py : pkg1
sample1.py : __main__
pkg1/mod1.py : pkg1.mod1

いかがでしょうか。まず、トップレベルのモジュールである
sample1.pyの__name__の値は"__main__"であることが確認できます。
また、モジュールのmod1の名前はモジュールの完全修飾名（パッケージ名を含んでいる）が格納されています。
そして、__init__.pyの__name__にはパッケージ名が格納されています。

一方、mod1.pyを実行してみます。


$ python pkg1/mod1.py
pkg1/mod1.py : __main__

先ほどモジュールの完全修飾名が格納されていましたが、
こんどは"__main__"が格納されていることが確認できます。
"""


"""
-mオプション 実行可能パッケージ __main__.py

さて、if ...で実行可能なスクリプトを作成することができましたが、実はパッケージに対しても可能です。
パッケージ配下に__main__.pyという名前のモジュールを作成し、
pythonコマンド実行時に-mオプションを付与します。
先ほどのpkg1パッケージに以下のように__main__.pyを作成してみましょう。


# pkg/__main__.py
import pkg1.mod1
pkg1.mod1.func1()
-mオプションをつけて実行してみます。


$ python -m pkg1
__init__.py : pkg1
pkg1/mod1.py : pkg1.mod1
__main__.pyが実行されたことが確認できました。
"""


"""
実行可能な組込みモジュール例
モジュールとして実行可能なパッケージですが、
標準ライブラリには便利なツールとして実行可能なパッケージがいくつか提供されています。
例えば、json.toolなんかが有名ですね。
これは引数で指定したjson文字列を読みやすくダンプしてくれます。
実行例を見てみましょう。sample.jsonというファイルにjson文字列が格納されているものとします。
-mオプションを指定して実行すると以下のように出力されます。


$ python -m json.tool sample.json
{
    "key1": 100,
    "key2": [
        1,
        2,
        3,
        4
    ],
    "key3": {
        "key4": 100,
        "key5": 200
    }
}
"""


print("--- Python入門　datetimeモジュールとdatetime型---")


"""
datetimeモジュール
datetimeモジュールには日付、時間データを様々な方法で操作する方法が提供されています。
まずは代表的な4種類のオブジェクトを紹介します。

型   説明
date型   日付 (年、月、および日) を表します。
time型   ローカル時刻を表します。
datetime型   dateオブジェクトおよび timeオブジェクトの全ての情報が入っている単一のオブジェクトです。
timedelta型  経過時間、つまり2つの日付や時刻間の差を表します。
datetime型
それではdatetimeモジュールのdatetime型から説明します。
モジュール名と型の名前が一緒ですが混同しないように注意してください。
(import文で混乱されている方はこちらで復習してください。)

datetime型変数の生成
datetime型の変数を生成する際は、
引数に年、月、日、自、分、秒、マイクロ秒を順に指定します。
以下のサンプルは、2018-01-02 03:04:05を表すdatetime型の変数を生成しています。
"""

from datetime import datetime, timedelta

# datetimeオブジェクトの生成
dt_obj = datetime(2018, 1, 2, 3, 4, 5, 000000)
print(dt_obj)    # 2018-01-02 03:04:05


"""
現在日時の取得

datetimeのnowメソッドを使用すると、現在時刻のdatetime型変数を得ることができます。
"""

# from datetime import datetime

# 現在時刻の取得
dt_obj_now = datetime.now()
print(dt_obj_now)    # 現在時刻が表示される


"""
日付、時刻要素の取得
datetime型の変数から年、月、日、自、分、秒などの要素を取得することができます。
下記の通りそれぞれに対応した属性を使用します。
"""

# form datetime import datetime, timedelta

dt_obj = datetime(2018, 1, 2, 3, 4, 5, 000000)
print(dt_obj)     # 2018-01-02 03:04:05
print(dt_obj.year)    # 2018
print(dt_obj.month)    # 1
print(dt_obj.day)    # 2
print(dt_obj.hour)    # 3
print(dt_obj.minute)    # 4
print(dt_obj.second)    # 5
print(dt_obj.microsecond)    # 0


"""
文字列からdatetimeへ変換
strptimeメソッドを使用すると、文字列からdatetime型に変換することができます。
第1引数に日付時刻の文字列を、第2引数にフォーマット文字列を指定します。
"""

# from datetime import datetime

# 文字列からdatetimeへ(strptimeメゾットの利用)
dt_str = '2017-04-01 12:32:05'
dt_obj = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
print(type(dt_obj))    # <class 'datetime.datetime'>

"""
上のサンプルの年月日の区切りはハイフンですが、
例えばスラッシュを使用したい場合はフォーマット文字列に'%Y/%m/%d %H:%M:%S'を指定します。


datetimeから文字列への変換
strftimeメソッドを使用すると、さきほどとは逆にdatetimeから文字列に変換することも可能です。
引数に文字列フォーマットを指定します。
"""

# from datetime import datetime

# 文字列からdatetimeへ変換
dt_str = '2017-04-01 12:32:05'
dt_obj = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')


# datetimeから文字列に変換(strftimeメゾットの利用)
dt_str2 = dt_obj.strftime('%Y/%m/%d %H:%M:%S')
print(dt_str2)    # 2017/04/01 12:32:05


"""
datetimeの加減算

日時の計算にはtimedelta型を使用します。
引数に週(weeks)、日(days)、時(hours)、分(minutes)、秒(seconds)、
ミリ秒(milliseconds)、マイクロ秒(microseconds)を指定できます。
必要なものだけキーワード引数を指定します。
"""

# form datetime import datetime, timedelta

dt_obj = datetime(2018, 1, 2, 3, 4, 5, 000000)
print(dt_obj)     # 2018-01-02 03:04:05

delta = timedelta(days=1)    # 1日分の間隔

dt_obj2 = dt_obj + delta    # 1日分足す
print(dt_obj2)    # 2018-01-03 03:04:05

dt_obj3 = dt_obj - delta    # 1日分引く
print(dt_obj3)    # 2018-01-01 03:04:05

"""
また、datetime型の変数同士を演算することも可能です。
引き算するとその間隔のtimedelta型変数を取得することができます。
"""

# form datetime import datetime, timedelta

# 2018-01-02 03:04:05
dt_obj1 = datetime(2018, 1, 2, 3, 4, 5, 000000)

# 2018-02-03 04:05:06
dt_obj2 = datetime(2018, 2, 3, 4, 5, 6, 000000)

# 日時の間隔を求める
delta = dt_obj2 - dt_obj1
print(delta)    # 32 days, 01:01:01

"""
このサンプルでは２つの日時の間隔を引き算で求めています。
 
次回は日付と時間を表すdate型、time型について解説します
"""


print("--- Python入門　datetimeモジュールとdate型/time型---")


"""
datetime.date

datetimeモジュールのdate型は日付を表す型です。

date型変数の生成

date型変数を生成する場合、引数に順に年月日を指定します。
以下のサンプルは、2017/01/02を表すdate型の変数を生成しています。
"""

from datetime import date

d = date(2017, 1, 2)
print(d)

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
print(d)


"""
現在日付の取得

date.todayを使用するか、datetimeから変換する方法があります。
"""

# from datetime import datetime, date

# todayを使用する場合
today = date.today()

# 現在日時から日付に変換する場合
dt_obj_now = datetime.now()
today = dt_obj_now.date()
print(today)


"""
日数の計算

datetimeと同様、timedeltaを使用します。
"""

from datetime import timedelta, date

d1 = date(2017, 1, 2)
delta = timedelta(days=3)
d2 = d1 + delta    # 3日加算
print(d2)     # 2017-01-05

"""
また、引き算により日付の間隔を算出することが可能です。
"""

# from datetime import timedelta, date

d1 = date(2016, 12, 22)    # 2016-12-22
d2 = date(2017, 1, 2)    # 2017-01-02
delta = d2 - d1     # 日付の間隔を取得する
print(delta)    # 11 days, 0:00:00


"""
datetime.time

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


print("--- Python入門　jsonモジュール JSONのエンコードとデコード---")


"""
dict型からJSON文字列に変換

dumpsによる辞書からJSONへの変換

json.dumpsを使用すると、dict型からJSONに変換することができます。
また、引数にindentを指定すると指定した数だけスペースでインデントをつけた見やすい形に整形してくれます。
"""

import json

# dict型からJson文字列に変換する
dict_data = {"items": [{"id": 1, "name": "pen"}, {"id": 2, "name": "apple"}, 
{"id": 3, "name": "painapple"}], "status": "sell"}

# JSONの文字列形式
json_str = json.dumps(dict_data)
print(json_str)

# インデントをつける
json_str = json.dumps(dict_data, indent=2)
print(json_str)


"""
ASCIIエンコード

また、デフォルトではASCIIにエンコードされますので、
ASCIIエンコードしない場合はensure_ascii=Falseを指定します。
"""

# import json

# 日本語が格納された辞書
dict_data = {"items": [{"id": 1, "name": "ペン"}, {"id": 2, 
"name": "アップル"}, {"id": 3, "name": "パイナップル"}], "status": "sell"}

# asciiエンコードする場合
json_str = json.dumps(dict_data, ensure_ascii=True)    
# 日本語部分が\u30da\u30f3のように出力される
print(json_str)

# asciiエンコードしない場合
json_str = json.dumps(dict_data, ensure_ascii=False)
print(json_str)


"""
loads JSON文字列から辞書に変換

今度は逆にJSON文字列から辞書に変換してみましょう。json.loadsを使用します。
"""

# import json

# JSON文字列から辞書に変換する
json_str = '{"items": [{"id": 1, "name": "ペン"}, {"id": 2, "name": "アップル"}, \
{"id": 3, "name": "パイナップル"}], "status": "sell"}'

dict_data = json.loads(json_str)
print(type(dict_data))     # <class 'dict'> dict型に変換できたことが確認


"""
load JSONファイルからdict型に変換

また、JSONファイルの場合はread()で一旦文字列に変換しなくても
loadを使用することでファイルオブジェクトから辞書に変換することが可能となります。

"""

# import json

# JSONファイルから辞書に変換する
f = open('json_file.txt', 'rb')
d_d = json.load(f)
print(type(d_d))    # <class 'dict'> 辞書に変換できたことが確認

