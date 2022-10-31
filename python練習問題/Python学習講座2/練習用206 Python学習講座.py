#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- logging 基本的な使い方 ---")


print("--- loggingの基本的な使い方 ---")


"""
loggingモジュールは使用方法が少し難しいのですが、
基本的にはログの設定　→　ロガーの生成　→　ロガーを使用して
ログ出力という流れになります。
ログの設定方法にも色々あるのですが、
最初のうちはbasicConfigを使用する方法がわかりやすいかと思います。
"""

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.error('エラーが発生しました')

"""
上のサンプルの解説です。
3行目のbasicConfigでログの設定を行えますが、
今回はデフォルトなので何も指定していません。
4行目でロガー、つまりログを出力する機能をもったオブジェクトを生成しています。
ロガーには名前を定義でき、
特にこだわりがない場合はモジュール名が格納された__name__を使用しますが、
監査や調査等、役割に応じた名称を設定することがあります。
"""


print("--- ログの設定 ---")


"""
ログが難しい点は、アプリケーションの構成や運用に合わせて
様々な設定が必要であるという点ではないでしょうか。
ここから基本的な設定項目について解説していきます。

ログレベル

一般的なプログラムにはログには用途に応じたレベルが用意されています。
Pythonのログには代表的なものとして以下のレベルが用意されています。
以下は公式ドキュメントからの抜粋となります。

レベル 	                    用途 	メソッド
DEBUG 	    おもに問題を診断するときにのみ関心があるような、詳細な情報。 	debug
INFO 	    想定された通りのことが起こったことの確認。 	                info
WARNING 	想定外のことが起こった、または問題が近く起こりそうである 
            (例えば、’disk space low’) ことの表示。 	            warning
ERROR 	    より重大な問題により、ソフトウェアがある機能を実行できないこと。 	error
CRITICAL 	プログラム自体が実行を続けられないことを表す、重大なエラー。 	critical


では様々なレベルのログを出力してみましょう。
先程のデフォルトの設定ではwarning以上のレベルのログしか出力されませんので
basicConfigでログのレベルを指定します。
"""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.debug('調査用ログ')
logger.info('処理を開始します')
logger.warning('1件の警告があります。')
logger.error('エラーが発生しました。')

"""
以下のようにINFO以上のログが出力されます。
一方、DEBUGは出力されていないことが確認できます。

INFO:__main__:処理を開始します。
WARNING:__main__:1件の警告があります。
ERROR:__main__:エラーが発生しました。

--- ログの設定 ---
WARNING:__main__:1件の警告があります。
ERROR:__main__:エラーが発生しました。


フォーマット

実際に運用でログを使用する場合、エラー等が起こった時刻が知りたいですね。
また、頻繁にエラーの分析が必要なシステムでは区切り文字を変えたりして
可読性をあげたほうがよいかもしれません。
さらに、マルチプロセスやマルチスレッドの場合は
プロセスIDやスレッドIDを参照する必要が出てくるかもしれません。
こういった要求を満たすため、
一般的なプログラミング言語ではログのフォーマットを整える機能がついており、
Pythonにも当然ログのフォーマットを整える機能があります。
basicConfigのformat引数でログのフォーマットを指定します。
"""

import logging

logging.basicConfig(format='%(asctime)s - %(name)s -\
 %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('処理を開始します。')
# 2022-10-30 14:46:22,482 - __main__ - INFO - 処理を開始します。

"""
以下のように出力されます。

2021-10-09 20:54:12,448 - __main__ - INFO - 処理を開始します。

フォーマット文字列の%()sで囲まれた部分で何を出力するかを指定します。
asctimeが時間、nameがloggerの名称、
(loggerについては後ほど説明します。)levelnameがログレベルの名称、
messageがメッセージとなります。その他、以下のものが用意されています。
標準ライブラリのlogging/__init__.pyのコメントから抜粋しました。

%(name)s 	        logger名
%(levelno)s 	ログレベル番号
%(levelname)s 	ログレベル名
%(pathname)s   （利用可能であれば）ソースファイルのフルパス
%(filename)s 	ソースファイル名
%(module)s 	    モジュール名
%(lineno)d 	   （利用可能であれば）行番号
%(funcName)s 	関数、メソッド名
%(created)f 	Time when the LogRecord was created (time.time()return value)
%(asctime)s 	ログレコードが作成された時間のテキスト形式
%(msecs)d 	    Millisecond portion of the creation time
%(relativeCreated)d 	Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded (typically at application startup time)
%(thread)d 	   （利用可能であれば）スレッドID
%(threadName)s 	（利用可能であれば）スレッド名
%(process)d 	（利用可能であれば）プロセスID
%(message)s 	 メッセージ


ログメッセージへの変数埋め込み

変数出力する場合は以下のようにstrのフォーマットを使用することができます。

logger.error('引数の値に%s と %sが指定されました', 'aaaa', 'bbbb')


ハンドラとファイル出力

標準出力やファイル等、指定された箇所にログを出力するものをハンドラと呼びます。
ハンドラには様々な種類があるのですが、大抵は以下2つで事足りるかと思います。

    logging.StreamHandler:標準出力に出力する
    logging.FileHandler:ファイルに出力する

ファイルハンドラの生成では引数にファイルパスを指定します。
basicConfigのhandlers引数で複数のハンドラをリストで
指定することができます。
"""

import logging

sth = logging.StreamHandler()
flh = logging.FileHandler('sample.log')

logging.basicConfig(format='%(asctime)s - %(name)s -\
 %(levelname)s - %(message)s', level=logging.INFO,
  handlers=[sth, flh])
logger = logging.getLogger(__name__)
logger.info('処理を開始します。')

"""
なお余談ですが、2021年10月時点でPyCharmで
このhandlersを記述をするとUnexpected argument(s)
という警告が出力されます。
これはPyCharm側の不具合のようです。
"""

















