#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説---")
print("--- 文字コードの基本（エンコードやバイナリーなど）  ---")


"""
文字コードとは「それぞれの文字に与えられた番号」のことです。
文字コードを正しく扱うことができないと、文字化けを引き起こすので注意が必要です。
ここでは「文字コードって何？」「エンコードやデコードはどうやって使うの？」
「バイナリデータを扱いたい」といった方へ、文字コードやエンコード・デコードについて解説します。
"""


print("--- 文字コードとは？  ---")


"""
世の中には日本語や英語をはじめ、中国語、イタリア語、ヘブライ語など、様々な言語が存在します。
それらの言語をコンピュータ上で扱うために、それぞれの文字に対して番号が割り振られています。
それが「文字コード」です。
文字コードにはいくつか種類があり、文字コードが変われば文字に割り当てられる番号も変わります
（なので、システムが想定していない文字コードだったときに「文字化け」が発生します）。
代表的な文字コードを見ていきましょう。

ASCII

最も基本的な文字コードで、a〜z, A~Z, 0〜9, 記号などの128の文字から成り立っています。
1つの文字に対して1バイト使用するので「シングルバイト文字」の一種です。
今でも英語圏ではよく使われています。

UTF-8

最もポピュラーな文字コードで、半角英数字や記号だけでなく、
日本語を含めた世界中の様々な言語に対応しています。
元々Python2ではASCIIが標準の文字コードでしたが、
Python3からはUTF-8が標準に変更されました。
そのおかげで一々日本語を扱う際に文字コードを指定する必要がなくなり、楽になったという経緯があります。
1文字に対して1〜4バイト使用しているので「マルチバイト文字」と呼ばれています。

Shift-JIS

日本語に対応した文字コードです。
1文字に対して2バイト固定で割り振られているので「マルチバイト文字」です。
PythonではUTF-8で日本語を扱えるのであまり使いませんが、参考程度に覚えておきましょう。
"""


print("--- エンコードとデコード  ---")


"""
次にエンコードとデコードについて見ていきましょう。
エンコードとは「文字を決められた規則によって、他の形に変換すること」です。
デコードはその反対で「エンコードされて変換された文字を、元の形に戻す」処理です。
Pythonでは文字をエンコードするとバイト列に変換されます。
その後デコードをすると元の文字に戻すことができます。
実際にやってみましょう。
"""

str = 'こんにちは！'

sjis_byte = str.encode('shift_jis')    # shift_jisのルールでバイト列に変換する
print(sjis_byte)    # b'\x82\xb1\x82\xf1\x82\xc9\x82\xbf\x82\xcd\x81I'

utf8_byte = str.encode('utf-8')    # utf-8のルールでバイト列に変換する
print(utf8_byte)
# b'\xe3\x81\x93\xe3\x82\x93\xe3\x81\xab\xe3\x81\xa1\xe3\x81\xaf\xef\xbc\x81'

sjis_str = sjis_byte.decode('shift_jis')    # shift_jisのルールでデコードする
print(sjis_str)    # こんにちは！

utf8_str = utf8_byte.decode('utf-8')    # utf-8のルールでデコードする
print(utf8_str)    # こんにちは！

"""
SHIFT-JIS、UTF-8を使って、それぞれのバイト列に変換した後、デコードして元の文字列に直しています。
SHIFT-JISとUTF-8それぞれでバイト列が異なっています。
これはエンコードのルールが文字コードによって異なるからです。
なので、例えばSHIFT-JISでエンコードしたバイト列をUTF-8でデコードしようとするとエラーになります。

str = "こんにちは！"

sjis_byte = str.encode("shift_jis") #shift_jisのルールでバイト列に変換する
print(sjis_byte)

utf8_str = sjis_byte.decode("utf-8") #utf-8のルールでデコードする
print(utf8_str)

[出力結果]

UnicodeDecodeError: 'utf-8' codec can't decode byte 0x82 in position 0: invalid start byte

PythonはUTF-8がデフォルトなので、基本的にエンコードは必要ありませんが、
参考程度に覚えておくと良いでしょう。
"""


print("--- base64とは？  ---")


"""
base64とはエンコード方法の一つで、
主にメールに添付されるファイルをエンコードしたりするときに使われています。
Pythonでもbase64でのエンコード・デコードに対応しているので、
例えば画像ファイルをbase64でエンコードして文字列として保存したり、
base64で保存した画像ファイルをデコードして画像に戻したりすることができます。
実際にやってみましょう。まずは画像ファイルをエンコードして文字列にします。
画像ファイルのパスは環境によって変わりますので、適宜変更してください。
また、Google Colabで、Googleドライブ上に画像を保存する想定になります。
"""

import base64

image_file = 'fmworld_10_lowerbnr_781_270.png'
saved_file = 'image.txt'
with open(image_file, 'rb') as f:
	data = f.read()
encode_txt = base64.b64encode(data)
with open(saved_file, 'wb') as f:
	f.write(encode_txt)

"""
image.txtというファイルの中に、Python.pngをbase64でエンコードした文字列を書き込みました。
最初のwith openで画像ファイルを読み込み、それをb64encode()に渡して、
画像をbase64のルールでエンコードしています。
保存されたimage.txtの中身は以下のようになっています。
（※巨大なテキストファイルになるので、開く場合は重たくなるかもしれないので注意してください。）
今度は反対にエンコードしたテキストから画像ファイルを復元しましょう。
次のように書きます。
"""

import cv2
import base64
import numpy as np


#エンコードした画像が入っているファイル
encoded_txt = 'image.txt'
# デコードしたファイルのファイル名
decoded_image_file = 'decode.png'

# エンコードした文字列を取得
with open(encoded_txt, 'rb') as f:
	encoded_image = f.read()

# 文字列をデコードしてバイナリデータを取得
binary = base64.b64decode(encoded_image)
png = np.frombuffer(binary, dtype = np.uint8)

# 画像ファイルに変換して保存する
img = cv2.imdecode(png, cv2.IMREAD_COLOR)
cv2.imwrite(decoded_image_file, img)

"""
decode.pngというファイル名で、エンコードしたテキストを画像ファイルに復元しました。
画像ファイルを扱うにはcv2が必要になります。
もしインストールしていない場合は「pip install opencv-python」でインストールできます。
"""
