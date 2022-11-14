#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- logging 設定ファイル ---")


print("--- ini形式による設定 ---")


"""
ログの設定使用できる設定ファイルにはyaml形式(というか辞書形式)
とini形式があります。まずはini形式について説明します。

基本的な設定

設定ファイルには、フォーマッタ、ハンドラ、ロガーの設定を記述しますが、
考え方としてはコードに直接記述した時と同様、ロガーに対し、
複数のハンドラーを設定し、それぞれのハンドラーには1つのフォーマッタを
設定するだけです。
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
"""

"""
import logging.config

logging.config.fileConfig('logconf.ini', encoding="UTF-8")
logger = logging.getLogger(__name__)
logger.error('エラーが発生しました')
"""

"""
h1というハンドラーをrootロガーに設定しています。
また、fmt1というフォーマッターをh1に設定しています。
なお、上のサンプルはあくまでも説明用なので、
実運用では働きがわかるような名前を設定したほうが良いでしょう。
iniファイルのセクションは以下から構成されます。

セクション名 	            内容
loggers 	            使用するロガーの名前をカンマ区切りで列挙
handlers 	            使用するハンドラーの名前をカンマ区切りで列挙
formatters 	            使用するフォーマッターの名前をカンマ区切りで列挙
logger_ロガー名 	        ロガーの個別設定。rootロガー以外はqualnameにてロガー名を設定。
handler_ハンドラー名 	    ハンドラーの個別設定。
                        classで使用するハンドラーのクラスを指定。
                        argsでハンドラー生成時の引数を指定。
formatter_フォーマッター名 	フォーマッターの個別設定


複数のロガーを設定

では、もうひとつサンプルです。
今度は複数のロガーを設定して、
標準出力とファイルの両方にログを出力してみます。
対象とするロガーの名前はsampleとしましょう。

;logconf.ini


[loggers]
keys=root, sample

[handlers]
keys=h1, h2

[formatters]
keys=fmt1, fmt2

; 以下、フォーマッター、ハンドラー、ロガーの個別設定

; フォーマッター
[formatter_fmt1]
format=%(asctime)s %(name)s %(levelname)s %(message)s [fmt1]
class=logging.Formatter

[formatter_fmt2]
format=%(asctime)s %(name)s %(levelname)s %(message)s [fmt2]
class=logging.Formatter


; ハンドラー
[handler_h1]
; 標準出力
class=StreamHandler
level=DEBUG
formatter=fmt1
args=(sys.stdout,)

[handler_h2]
; ファイル出力
class=FileHandler
level=DEBUG
formatter=fmt2
args=('sample.log',)

;ロガー
[logger_root]
level=NOTSET
handlers=h1

[logger_sample]
level=NOTSET
handlers=h2
qualname=sample
"""

"""
import logging.config


logging.config.fileConfig('logconf2.ini')

logger = ogging.getLogger('sample')
logger.error('エラーが発生しました')
"""


"""
上のコードを実行してみると、
sampleロガーにはrootロガーで設定したログが標準出力に、
sampleロガーで設定したログがファイルに、
と2種類のログが出力されることが確認できます。
"""


print("--- YAML形式による設定 ---")


"""
前述の通りYAMLでも設定の記述が可能です。
最低限設定する必要がある項目は以下のとおりとなります。
ini形式との違いは、フォーマッター、ハンドラー、ロガーを
別途列挙する必要が無いこと、
rootロガーの設定が必須であることが挙げられます。

項目 	説明
version 	スキーマのバージョンを表す整数値に設定されます。現在有効な値は1だけです。
formatters 	フォーマッターの設定を記述します。
handlers 	ハンドラーの設定を記述します。
loggers 	ロガーの設定を記述します。
root 	rootロガーの設定を記述します。

YAML形式で使用するにはYAMLパーサが必要となります。
以下でインストールしましょう。

pip install PyYAML

ではサンプルです。


# logconf.yml
version: 1

formatters:
  fmt1:
    format: '%(asctime)s %(name)s %(levelname)s %(message)s [fmt1]'
    
handlers:
  h1:
    class: logging.StreamHandler    
    level: DEBUG
    formatter: fmt1 
    stream: ext://sys.stdout
  h2: 
    class: logging.FileHandler
    level: DEBUG
    formatter: fmt1
    filename: sample.log

loggers:     
  sample:
    handlers: [h2]
    level: DEBUG
    qualname: console
    propagate: no

root:
  level: DEBUG
  handlers: [h1]

使用する側のPythonファイルは以下のようになります。
"""

"""
import yaml
from logging import config, getLogger

config.dictConfig(yaml.load(open('logconf.yml', encoding='UTF-8').read()))
logger = getLogger(__name__)
logger.error('エラーが発生しました')
"""

"""
yaml.loadでyaml形式を辞書型に変換して、
config.dictConfigに読み込ませます。
上のコードでは、h1というハンドラーをrootロガーに、
h2というハンドラーをsampleという名前のロガーに設定しています。
また、fmt1というフォーマッターをh1、h2に設定しています。
なお、上のサンプルはあくまでも説明用なので、
実運用では働きがわかるような名前を設定したほうが良いでしょう。
なお、ロガーに複数のハンドラーを指定したい場合は、
以下のようにカンマ区切りで列挙します。

handlers: [h1, h2]
"""


print("--- JSON形式による設定 ---")


"""
dictConfigで指定しているのは辞書型なので、
実はYAML形式以外であっても辞書型であれば何でも使用可能です。
あまり設定ファイルでJSONは使用しないかもしれませんが、
参考として上のコードをJSONに書きなおしたものも掲載します。

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
"""

from logging import config, getLogger
import json

config.dictConfig(json.loads(open("logconf.json",
 encoding='UTF-8').read()))
logger = getLogger(__name__)
logger.error('エラーが発生しました')
