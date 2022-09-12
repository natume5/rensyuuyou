#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- Python入門　logging ログの階層---")


"""
ロガーの階層

前回の続きでロガーについてです。
ロガーオブジェクトにはそれぞれに名前が定義されているのですが、
この名前はドットをセパレータとした階層構造を定義できます。
例えば、carという名前のロガーはcar.engineというロガーの親となります。
前のページでも説明しましたが、ロガーの名前はgetLoggerの引数で指定することができます。
サンプルを見てみましょう。
"""

import logging

# ロガー1を取得
logger1 = logging.getLogger('parent')
logger1.setLevel(logging.DEBUG)

# ハンドラー1を作成する
h1 = logging.StreamHandler()
h1.setLevel(logging.DEBUG)

# ハンドラー１にフォーマッタを設定する
h1.setFormatter(logging.Formatter('フォーマット1 %(message)s'))

# ロガー1にハンドラー1を設定する
logger1.addHandler(h1)

# 2個目のロガー。ロガー2を取得。ハンドラーは設定しない
logger2 = logging.getLogger('parent.childe')

# 出力
logger2.error('エラーメッセージ')

"""
親子関係にあるロガー1とロガー2がありますが、ロガー2にはハンドラーを設定していないにもかかわらず、
ロガー1に設定したハンドラの設定が効いています。これはロガー1の名前がparentで、
ロガー2の名前がparent.childeで親子関係にあるためです。
また、子ロガーに対してaddHandlerすることにより、
特定モジュールの処理だけ重点的に別途ログ出力をすることができます。

ロガーの階層構造のトップは、ルートロガーと呼ばれ、ログ出力ではrootと表示されます。
ルートロガーを取得する場合はgetLoggerで空文字列を指定します。
(rootという名前でロガーを取得しても、ルートロガーは取得できないので注意してください。)
ルートロガーは全てのロガーの親なので、ここに設定した内容は全てのロガーに反映されます。
"""


print("--- Python入門　logging 設定ファイル---")


"""
ini形式による設定

ログの設定使用できる設定ファイルにはyaml形式(というか辞書形式)とini形式があります。
まずはini形式について説明します。
基本的な設定

設定ファイルには、フォーマッタ、ハンドラ、ロガーの設定を記述しますが、
考え方としてはコードに直接記述した時と同様、ロガーに対し、複数のハンドラーを設定し、
それぞれのハンドラーには1つのフォーマッタを設定するだけです。
まずはrootロガーを設定するサンプルを見てみましょう。

;logconf.ini


[loggers]
keys=root

[handlers]
keys=h1

[formatters]
keys=fmt1

; 以下、フォーマッター、ハンドラー、ロガーの個別設定

; フォーマッター
[formatter_fmt1]
format=%(asctime)s %(name)s %(levelname)s %(message)s
class=logging.Formatter

; ハンドラー
[handler_h1]
class=StreamHandler
level=DEBUG
formatter=fmt1
args=(sys.stdout,)

;ロガー
[logger_root]
level=NOTSET
handlers=h1

使用する側のPythonファイルは以下のようになります。


import logging.config


logging.config.fileConfig("logconf.ini")
logger = logging.getLogger(__name__)
logger.error('エラーが発生しました')


h1というハンドラーをrootロガーに設定しています。また、fmt1というフォーマッターをh1に設定しています。
なお、上のサンプルはあくまでも説明用なので、実運用では働きがわかるような名前を設定したほうが良いでしょう。
iniファイルのセクションは以下から構成されます。

セクション名 	                  内容
loggers 	                使用するロガーの名前をカンマ区切りで列挙
handlers 	                使用するハンドラーの名前をカンマ区切りで列挙
formatters 	                使用するフォーマッターの名前をカンマ区切りで列挙
logger_ロガー名 	            ロガーの個別設定。rootロガー以外はqualnameにてロガー名を設定。
handler_ハンドラー名 	        ハンドラーの個別設定。
                            classで使用するハンドラーのクラスを指定。
                            argsでハンドラー生成時の引数を指定。
formatter_フォーマッター名 	    フォーマッターの個別設定


複数のロガーを設定

では、もうひとつサンプルです。
今度は複数のロガーを設定して、標準出力とファイルの両方にログを出力してみます。
対象とするロガーの名前はsampleとしましょう。


import logging.config


logging.config.fileConfig("logconf.ini", 'r', encoding='utf-8')
logger = logging.getLogger('sample')
logger.error('エラーが発生しました')

"""

"""
上のコードを実行してみると、sampleロガーにはrootロガーで設定したログが標準出力に、
sampleロガーで設定したログがファイルに、と2種類のログが出力されることが確認できます。


YAML形式による設定

前述の通りYAMLでも設定の記述が可能です。
最低限設定する必要がある項目は以下のとおりとなります。
ini形式との違いは、フォーマッター、ハンドラー、ロガーを別途列挙する必要が無いこと、
rootロガーの設定が必須であることが挙げられます。

項目 	                 説明
version 	        スキーマのバージョンを表す整数値に設定されます。現在有効な値は1だけです。
formatters 	        フォーマッターの設定を記述します。
handlers 	        ハンドラーの設定を記述します。
loggers 	        ロガーの設定を記述します。
root 	            rootロガーの設定を記述します。

YAML形式で使用するにはYAMLパーサが必要となります。以下でインストールしましょう。

pip install PyYAML


使用する側のPythonファイルは以下のようになります。
"""
"""

import yaml
from logging import config,getLogger

config.dictConfig(yaml.load(open("logconf.yml", encoding='UTF-8').read()))
logger = getLogger(__name__)
logger.error('エラーが発生しました')

"""

"""
yaml.loadでyaml形式を辞書型に変換して、config.dictConfigに読み込ませます。
上のコードでは、h1というハンドラーをrootロガーに、h2というハンドラーをsampleという名前のロガーに設定しています。
また、fmt1というフォーマッターをh1、h2に設定しています。
なお、上のサンプルはあくまでも説明用なので、実運用では働きがわかるような名前を設定したほうが良いでしょう。
なお、ロガーに複数のハンドラーを指定したい場合は、以下のようにカンマ区切りで列挙します。

handlers: [h1, h2]


JSON形式による設定

dictConfigで指定しているのは辞書型なので、
実はYAML形式以外であっても辞書型であれば何でも使用可能です。
あまり設定ファイルでJSONは使用しないかもしれませんが、
参考として上のコードをJSONに書きなおしたものも掲載します。
"""
"""
{
  "version": 1,
  "formatters": {
    "fmt1": {
      "format": "%(asctime)s %(name)s %(levelname)s %(message)s [fmt1]"
    }   
  },  
  "handlers": {
    "h1": {
      "class": "logging.StreamHandler",
      "level": "DEBUG",
      "formatter": "fmt1",
      "stream": "ext://sys.stdout"
    },
    "h2": {
      "class": "logging.StreamHandler",
      "level": "DEBUG",
      "formatter": "fmt1",
      "stream": "ext://sys.stdout"
    }
  },  
  "loggers": {
    "console": {
      "handlers": [
        "h2"
      ],  
      "level": "DEBUG",
      "qualname": "sample",
      "propagate": "no"
    }   
  },  
  "root": {
    "level": "DEBUG",
    "handlers": [
      "h1"
    ]   
  }
}

from logging import config,getLogger
import json

config.dictConfig(json.loads(open("logconf.json", encoding='UTF-8').read()))
logger = getLogger(__name__)
logger.error("エラーが発生しました")
"""


print("--- Python入門　unittest 単体テスト入門 その1 基本的な使い方---")


"""
基本的な使い方

unittestモジュールはpythonの組込みモジュールとして提供されている単体テストフレームワークです。
Javaの単体テストフレームワークであるJUnitに触発されたものであるため、使い方もJUnitとほぼ同様です。
まずは簡単なサンプルを通じて使い方を見てみましょう。

まずはテストされる側のモジュールを準備します。足し算をする関数と、
数値が正かどうかを判定する関数が記述されています。

次にテストをする側のコードです。
ファイル名は、test_テスト対象モジュール.pyとします。
また、テストクラスはテスト対象クラス名にTestをつけた名前を使用し、
unittest.TestCaseを継承します。また各テストケースに該当するテストメソッドは、
テスト対象関数・メソッド名の頭にtestをつけた名前を使用します。


テストの実行は以下の通りmオプションをつけてunittestモジュールを実行します。

D:\テキストドキュメント１\IT・エンジニア・プログラミング\sublime text3関係\python練習問題>python -m unittest
__init__.py: pkg1
..
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK

テストが実行され、結果が出力されました。上のコードで使用したassertEqualは、
検査値と期待値が等しいことをテストします。公式ドキュメントには引数の順序に関する言及はないのですが、
JUnitに習うならば期待値、検査値の順序で統一したほうがよいかもしれません。
assertTrue、assertFalseは検査値がそれぞれTrue、Falseであることをテストします。


検査用メソッド

ここからもう少しunittestモジュールについて細かく見ていきましょう。上の節でassertEqual、
assertTrue、assertFalseについて紹介しましたが、それ以外にTestCaseクラスで提供されている
代表的なテストメソッドには以下のようなものがあります。

メソッド                       確認事項
assertEqual(a, b)           a == b
assertNotEqual(a, b)        a != b
assertTrue(x)               bool(x) is True
assertFalse(x)              bool(x) is False
assertIs(a, b)              a is b
assertIsNot(a, b)           a is not b
assertIsNone(x)             x is None
assertIsNotNone(x)          x is not None
assertIn(a, b)              a in b
assertNotIn(a, b)           a not in b
assertIsInstance(a, b)      isinstance(a, b)
assertNotIsInstance(a, b)   not isinstance(a, b)


テスト用メソッド

ある程度規模のあるプログラムをテストする場合、テストの実行前や後に処理を追加したい場合が出てきます。
例えば、データベースに接続しテストデータを投入たり、テスト終了時にテストデータを削除したり
ロールバックすることが挙げられます。setUpClass()/tearDownClass()、setUp()/tearDown()、
skipTest()を紹介します。

setUpClass()/tearDownClass()、setUp()/tearDown()

setUpClass()/tearDownClass()は、テストクラス全体の前後処理を記述します。
setUp()/tearDown()は個別のテストメソッドの前後処理を記述します。

先ほどのサンプルにprint関数で文字出力を追記し、動作を確認してみましょう。

以下、実行時の出力です。

python -m unittest
__init__.py: pkg1
*** 全体前処理 ***
+ テスト前処理
test_add_num開始
test_add_num終了
+ テスト後処理
.+ テスト前処理
test_is_positive開始
test_is_positive終了
+ テスト後処理
.*** 全体後処理 ***

----------------------------------------------------------------------
Ran 2 tests in 0.032s

OK

テストの実行前後で処理が呼び出されていることが確認できます。


テストのスキップ

システム改修で修正中の機能が時など、
テストが通過しないことが予めわかっているため特定の機能だけスキップしたい場合が出てきますが、
そんな場合はskipデコレーターを使用します。引数に文字列を指定します。

最初のサンプルのメソッドの1つにデコーレーターをつけて実行してみましょう。

python -m unittest
__init__.py: pkg1
*** 全体前処理 ***
+ テスト前処理
test_add_num開始
test_add_num終了
+ テスト後処理
.s*** 全体後処理 ***

----------------------------------------------------------------------
Ran 2 tests in 0.009s

OK (skipped=1)

スキップされ、テストメソッドが実行されていないことが確認できます。
また、ここでは紹介しませんが、クラスデコレータを使用することによりテストクラス全体をスキップしたり、
skipIfデコレータを使用して条件付きでスキップすることができます。
"""


print("--- Python入門　unittest 単体テスト入門 その2 テストパッケージとテストスイート---")


"""
プロジェクト構成とテストの実行

Pythonに限らずプロジェクトの構成として、アプリケーションのソースコードとテストのソースコードは
別パッケージとしてディレクトリを分けることが一般的です。
以下のような構成の場合の実行方法について考えてみましょう。

.                        # プロジェクトディレクトリ(ここで実行する)
├── sample_lib        # アプリケーションのパッケージ
│   ├── __init__.py
│   ├── mod1.py
│   └── mod2.py
└── test              # テストのパッケージ
    ├── __init__.py
    ├── test_mod1.py
    └── test_mod2.py

mod1.py、mod2.pyというコードに対するテストコードが用意されているものとします。
これらのテストを実行する際、プロジェクトディレクトリ直下で以下のように
-mオプションでunittestモジュールを実行し、相対パスでテストスクリプトを指定します。

$ python -m unittest test/test_mod1.py 
test_add_num
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

$ python -m unittest test/test_mod2.py 
test_is_positive
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

それぞれのテストスクリプトにif __name__ == '__main__':をつけて実行する方法もあるのですが、
その場合はエントリーポイントがtestディレクトリ配下になってしまいますので、
予めPYTHON_PATHをエクスポートするなどの措置が必要になります。


テストスイート（テストのグループ化）

上のプロジェクトの場合テストスクリプトがたった2つなので順番にpythonコマンドを実行しても良いのですが、
プロジェクトによってはこれが数十、数百になることも考えられます。
こういった時のためPythonはunittestをグループ化してまとめて実行することが可能です。
（一般的にテストスイートと呼ばれています。）

テストスイートの作成方法

さっそくテストスイートを作成してみましょう。runner.pyという名前でテストクラスを作成します。

.
├── sample_lib
│   ├── __init__.py
│   ├── mod1.py
│   └── mod2.py
└── test
    ├── __init__.py
    ├── runner.py        # テストスイートクラス
    ├── test_mod1.py
    └── test_mod2.py

unittest.TestSuite()オブジェクトを生成し、addTestでテストクラスを指定します。
TextTestRunner().run()が呼び出されるとaddしたテストクラスが実行されます。

今までと同様に-mオプションをつけ、テストスイートクラスを指定すると、
addしたテストケースが実行されていることが確認できます。


discover（テストスイート作成の自動化）

上のテストスイートではaddTestで1つ1つ追加していきましたが、
これもモジュール数が多いと管理が大変そうですね。
このため、ディレクトリ単位でテストモジュールを探索し、
自動でテストスイートを作成してくれる仕組みがあります。これをdiscoverと呼びます。

実はテストモジュールを指定せずに以下のように打ち込むと、
プロジェクト全体を走査してテストを見つけ実行してくれます。

python -m unittest

ですが、サブプロジェクト単位でテストスイートを実行したい場合などは、
上で作成したrunnerに自分でdiscoveryを記述してカスタマイズすることが可能です。
上のrunner.pyをdiscoverを使用したものに修正してみましょう。

discoverの引数にはディレクトリを指定します。
ローカルでテストを実行する場合は、機能単位でテストをする等をして時間を節約することが可能です。
"""
