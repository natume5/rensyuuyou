#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- chardet 文字コードを判定する ---")


"""
日本語サイトのスクレイピング等でマルチバイト文字を含んだ
バイナリ文字列データを扱う場合、
デコードのために文字コード（正確にはエンコーディングですが）
が何なのかを事前に把握する必要がなります。
ですが、Webサイト等ではそれがわからない場合も往々にしてあります。
そんなとき便利なのが今回学習するchardetという文字コード判定ライブラリです。
"""


print("--- 基本的な使い方 ---")


"""
detectメソッドにバイナリ文字列データを指定します。
以下のサンプルでは、yahooのサイトの文字コードを判定しています。
webサイトのデータ取得はurllibモジュールを使用しています。
"""

import chardet
from urllib.request import urlopen

r = urlopen('http://yahoo.co.jp/')
rawdata = r.read()
print(chardet.detect(rawdata))
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

"""
結果は辞書形式で、encodingが文字コード、
confidenceが判定結果の信頼性を表します。
"""


print("--- 応用的な使い方 ---")


"""
文字列判定時、比較的大きなサイズのデータで判定をすると時間がかかります。
そんな場合、UniversalDetectorを利用しfeedメソッドで少しずつ判定を行い、
信頼性がある一定以上になればそこで判定を終わる、という方法があります。
サンプルを見てみましょう。
"""

from chardet.universaldetector import UniversalDetector
from urllib.request import urlopen

detector = UniversalDetector()

r = urlopen('http://yahoo.co.jp/')
for line in r:
	detector.feed(line)
	if detector.done:
		break

detector.close()
print(detector.result)
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

"""
detector.doneは、信頼性が一定を超えるとTrueを返します。
detector.resultで結果を取得できますが、
その前にclose()メソッドを呼び出す必要があるので注意してください。
"""
