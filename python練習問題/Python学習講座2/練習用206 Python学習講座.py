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


print("--- 複数モジュールに渡るログの設定 ---")


"""
モジュールが複数に渡る場合、
予め一箇所でbasicConfigを設定すると全体に設定が適用されるため、
後から他の場所でloggingを使う場合設定は不要です。
（より厳密にはロガーは階層構造で管理され、
basicConfigでルートのロガーに設定がなされている、という状況です。）
以下の２つのモジュールを準備して確認してみましょう。


# mod2.py
import logging

logger = logging.getLogger(__name__)


def sample():
    logger.error("エラー発生")


# sample3.py

import logging
import mod2

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

mod2.sample()

sample.pyからmod1.pyを呼び出します。
mod1.pyの方ではbasicConfigの設定を行っていませんが、
フォーマットされたログが出力されていることを確認することができます。
"""


print("--- ロガーごとに設定する ---")


"""
前述のとおりbasicconfigを使用するとロガー全体を設定することができるため、
大抵のアプリケーションではbasicconfigのみで設定が事足りるのではないでしょうか。
ですが、複雑なアプリケーションを構築する場合、
ロガーごとにもう少し細かい設定が必要となります。
ありがちな例として
「決済や個人情報を扱う処理の場合はシステムのログ以外に
監査部門に提出するため指定されたフォーマットの別ファイルでログ出力する」
といった要件が挙げられます。
ここからの説明で抑えていただきたいのが
「ロガーは複数のハンドラ（≒出力先）を持ち、ハンドラは1つのフォーマッタを持つ。」
という点です。実際に実装する際は多少順番が前後しますが、
概ね以下のフローで理解するとわかりやすいかと思います。

    ロガーを生成
    ハンドラーを生成
    フォーマッタを生成
    ハンドラーにフォーマッタを設定
    ロガーにハンドラーを設定

フォーマッタはFormatterでフォーマット文字列を指定して生成します。
"""

import logging


# 1.ロガーを取得する
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)    # 出力レベルを設定

# 2.ハンドラーを生成する
h = logging.StreamHandler()
h.setLevel(logging.DEBUG)    # 出力レベルを設定

# 3.フォーマッタを生成する
fmt = logging.Formatter('%(asctime)s - %(name)s -\
 %(levelname)s - %(message)s' )

# 4.ハンドラーにフォーマッタを設定する
h.setFormatter(fmt)

# 5.ロガーにハンドラーを設定する
logger.addHandler(h)

# ログ出力を行う
logger.info("ログを出力")
# 2022-11-01 14:20:08,627 - __main__ - INFO - ログを出力
# INFO:__main__:ログを出力

"""
出力レベルを2箇所で設定していますが、これには理由があります。
先ほど「ロガーは複数のハンドラを設定できる」
と書きましたがそれを念頭に以下のサンプルを見てみてください。
"""

import logging


# ロガーを取得する
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)    # 出力レベルを設定

# ハンドラー1を生成する
h1 = logging.StreamHandler()
h1.setLevel(logging.DEBUG)    # 出力レベルを設定

# ハンドラー2を生成する
h2 = logging.FileHandler('sample.log')
h2.setLevel(logging.ERROR)    # 出力レベルを設定

# フォーマッタを生成する
fmt = logging.Formatter('%(asctime)s - %(name)s -\
 %(levelname)s - %(message)s')

# ハンドラーにフォーマッタを設定する
h1.setFormatter(fmt)
h2.setFormatter(fmt)

# ロガーにハンドラーを設定する
logger.addHandler(h1)
logger.addHandler(h2)

# ログ出力を行う
logger.debug("debugログを出力")
logger.info("infoログを出力")
logger.warn("warnログを出力")
logger.error("errorログを出力")
# D:\テキストドキュメント１\IT・エンジニア・プログラミング\sublime text3関係\python練習問題\Python学習講座2\練習用206 Python学習講座.py:302: DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead
#   logger.warn("warnログを出力")
# 2022-11-01 14:36:36,085 - __main__ - WARNING - warnログを出力
# 2022-11-01 14:36:36,085 - __main__ - WARNING - warnログを出力
# WARNING:__main__:warnログを出力
# 2022-11-01 14:36:36,117 - __main__ - ERROR - errorログを出力
# 2022-11-01 14:36:36,117 - __main__ - ERROR - errorログを出力
# ERROR:__main__:errorログを出力

"""
1つのロガーにハンドラーを複数登録しています。
2つめのFileHandlerは指定したファイルにログを出力するハンドラーです。
ハンドラー1、ハンドラー2で設定されているレベルが異なる点に注意してください。
上のコードを実行してみると、標準出力ではDEBUG〜ERRORまで出力されますが、
ログファイル、つまりハンドラー2の方はERRORログしか出力されません。
また、5行目のロガーの出力レベルをERRORに変更すると、
標準出力もファイルの方もともにERRORログしか出力されなくなります。
ロガーの方の出力レベルは元栓を調整する感じですね。
"""
