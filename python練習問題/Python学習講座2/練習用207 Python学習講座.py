#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- logging ログの階層 ---")


print("--- ロガーの階層 ---")


"""
前回の続きでロガーについてです。
ロガーオブジェクトにはそれぞれに名前が定義されているのですが、
この名前はドットをセパレータとした階層構造を定義できます。
例えば、carという名前のロガーはcar.engineというロガーの親となります。
前のページでも説明しましたが、
ロガーの名前はgetLoggerの引数で指定することができます。
サンプルを見てみましょう。
"""

import logging


# ロガー1を取得
logger1 = logging.getLogger('parent')
logger1.setLevel(logging.DEBUG)

# ハンドラー1を作成する
h1 = logging.StreamHandler()
h1.setLevel(logging.DEBUG)

# ハンドラー1にフォーマッタを設定する
h1.setFormatter(logging.Formatter('フォーマット1 %(message)s'))

# ロガー1にハンドラー1を設定する
logger1.addHandler(h1)

# 2個目のロガー。ロガー2を取得。ハンドラーは設定しない。
logger2 = logging.getLogger('parent.childe')

# 出力
logger2.error('エラーメッセージ')

"""
親子関係にあるロガー1とロガー2がありますが、
ロガー2にはハンドラーを設定していないにもかかわらず、
ロガー1に設定したハンドラの設定が効いています。
これはロガー1の名前がparentで、
ロガー2の名前がparent.childeで親子関係にあるためです。
また、子ロガーに対してaddHandlerすることにより、
特定モジュールの処理だけ重点的に別途ログ出力をすることができます。

ロガーの階層構造のトップは、ルートロガーと呼ばれ、
ログ出力ではrootと表示されます。
ルートロガーを取得する場合はgetLoggerで空文字列を指定します。
(rootという名前でロガーを取得しても、
ルートロガーは取得できないので注意してください。)
ルートロガーは全てのロガーの親なので、
ここに設定した内容は全てのロガーに反映されます。
"""


















