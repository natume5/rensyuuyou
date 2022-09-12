#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説 ---")
print("--- ログ出力のライブラリ（logging） ---")


"""
loggingは「ログを出力するためのライブラリ」です。
システム開発中はIDEのデバッグ機能等を使えばデバッグ可能ですが、
システムをリリースする場合や、デバッグ機能が使えない環境での開発時、
ログの出力はとても役に立ってくれます。
ここでは「ログとは？」「loggingの使い方は？」「見やすいようにログを出力する方法が知りたい」
といった方へ、loggingの使い方を解説します。
"""


print("--- ログとは ---")


"""
ログとは「システムがどう動いたのかを記録したもの」です。
一般的には.logという拡張子のテキストファイルに保存し、
システムがいつ、どのように動いたのかを、動いている間に記録し続けます。
例えばif分岐で予期しない動作を見せた場合などに、
条件に使った変数の値と一緒にログに記録するようプログラムを組んでおくことで、
なぜそんな動きをしたのかのヒントになります。
システムが使われているうちはもちろん、開発中でもデバッグ目的でよく使われる手法です。
"""


print("--- ログレベルとは ---")


"""
ログにはログレベルというものがあり、それぞれのレベルに応じて重要度が変わってきます。

ログレベル	                              説明
CRITICAL	    データの破損やシステム自体が停止した場合などに使う。
ERROR	        正常に動いているが、予期しない動作をした場合などに使う。
WORNING	        エラーにするほどではないが、予期しない動作をした場合などに使う。
INFO	        単純なシステム動作中のログ。正常動作時に使う。
DEBUG	        より詳細なログ。変数内のデータ解析などに使う。

それぞれのログレベルを適切に使うことで、その問題の大きさを把握できるようになります。
"""


print("--- loggingの使い方 ---")


"""
では実際にloggingを使ってログを出力してみましょう。
"""

import logging

logging.basicConfig(
	filename='test.log',
)
logging.error('エラーが発生しました。')    # ERROR:root:エラーが発生しました。

"""
このプログラムは「test.logテキストに『エラーが発生しました。』ログを出力」しています。
loggingは import logging でインポートして使います。
次にbasicConfigのfilename引数にログファイルのファイル名を指定しています。
これだけでtest.logが存在しない場合はファイルを作成し、存在する場合は上書きしてくれます。
最後にlogging.error()でエラーログを出力しています。
出力されたログを見てみると、ちゃんとERRORレベルのログが出力されていることがわかります。

ちなみに、rootというのはプログラムで一番はじめに実行されるPythonファイルを指しています。
1つのファイルでログ出力をしているので、今回はrootになりました。


出力できるログレベルを変更する

先ほどのlogging.error()の部分をlogging.warning()やinfo()
に変えるとそれぞれのレベルのログを出力できますが、
デフォルトではWORNING以上のレベル(CRITICAL、ERROR、WORNING)のログしか出力されません。
INFO以下のレベルのログも出力できるようにするためには
basicConfigのlevel引数を変更する必要があります。
"""

import logging

logging.basicConfig(
	filename='test.log',
	level=logging.INFO,
)
logging.info('infoレベルは出力されます。')    # INFO:root:infoレベルは出力されます。
logging.debug('debugレベルは出力されません。')

"""
level引数に logging.INFO を設定したことで、INFOレベルのログが出力されるようになりました。
一方で、DEBUGはINFOよりも下位レベルのログなので、DEBUGのログは出力されませんでした。
"""


print("--- loggingのフォーマット ---")


"""
ここまで出力したログは[ログレベル]:[実行ファイル]:[ログメッセージ]というフォーマットでしたが、
これではいつ出力されたログなのかが判断できません。
loggingにはログ出力時のフォーマットの設定も可能なので、
実際に使うときはしっかりとフォーマットを設定することをおすすめします。
"""

import logging

logging.basicConfig(
	filename='test.log',
	format='[%(asctime)s](%(levelname)s) filename=%(filename)s(%(lineno)s):%(message)s',
	datefmt='%Y%m%d %H:%M:%S',
)
logging.error('ログを出力しました。')


"""
formatでフォーマットを設定しています。

例えば %(asctime)s は発生時刻、 %(levelname)s 
はログレベルの名称などを出力してくれます。
またdatefmtで時刻のフォーマットを指定しています。
これは %(asctime)s に関係する引数になっています。
最後によく使われる各フォーマットの一覧を載せておきます。
個人的には上の組み合わせがおすすめですが、
それぞれのシステムに合ったフォーマットを設定しましょう。


フォーマット	            説明
%(asctime)s	        発生時刻
%(filename)s	    ファイル名
%(funcName)s	    関数名
%(levelname)s	    レベル名
%(levelno)s	        レベルNo（ERROR:40, WARNING:30 等）
%(lineno)d	        行番号
%(message)s	        ログメッセージ
%(module)s	        モジュール名
%(pathname)s	    ファイルの完全パス
"""
