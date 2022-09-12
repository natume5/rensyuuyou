#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説 ---")
print("--- 画像処理ライブラリの使い方（Pillow） ---")


"""
Pillowは「Pythonで画像処理を行うためのライブラリ」です。

画像処理を行うライブラリといえば有名なのがOpenCVですが、
PillowはOpenCVよりもシンプルに扱うことができるので、
トリミングやカラーの変更など単純な画像処理をするだけであればPillowがおすすめです。
ここでは「Pillowとは？」「Pillowで画像加工をする方法は？」といった初心者の方へ向けて、
Pillowについて解説します。
"""


print("--- Pillowのインストール ---")


"""
まずはインストールです。以下のコードを叩いてライブラリをインストールしてください。

$ pip install Pillow
"""


print("--- Pillowのモジュール読み込み ---")


"""
Pillowを使うには次のようにモジュールを読み込む必要があります。

from PIL import Image, ImageFilter

この時、PillowではなくPILなので注意してください。
PILとはPython Imaging Libraryの略称で、
Pillow以前に画像処理の為に使われていたライブラリです。
PIL自体の開発は2011年に終了し後継のPillowが登場、現在も開発されていますが、
このPillowも互換性の観点からモジュールを読み込む際はPILと打つことになっています。
今回はとりあえず『Pillowの旧verなんだな』くらいに捉えていただいて構いません。
"""


print("--- 画像の読み込み ---")


"""
ではここから具体的にPillowを使って画像処理を行っていきましょう。
まずは処理する画像を読み込みます。

今回使うのはこの画像（みゃふのイラスト画像）です。
"""

from PIL import Image, ImageFilter

img = Image.open('myafu.jpg')
print(type(img))
img.show()
# <class 'PIL.JpegImagePlugin.JpegImageFile'>

"""
Image.open()で画像の読み込みを行い、
取得したJpegImageFileのshow()メソッドで画像のプレビューが表示されます。
"""


print("--- 画像の情報を取得する ---")


"""
次に読み込んだ画像のサイズやフォーマット、色などの情報を取得してみましょう。
format()で画像のフォーマットを、size()は画像サイズをそれぞれ取得できます。
また、getpixel()はタプルを渡すことで、その座標の色情報を取得することができます。
今回はフォーマット、サイズ、カラーの順で画像の情報を取得してみましょう。
"""

from PIL import Image, ImageFilter

img = Image.open('myafu.jpg')
print(img.format)    # JPEG
print(img.size)    # (220, 220)
print(img.getpixel((100, 100)))     # (91, 99, 162)

"""
なお出力されたサイズの読み方は（縦幅、横幅）の順。カラーはRGB形式となっています。
"""


print("--- 画像を回転させる ---")


"""
画像を回転させるにはrotate()を使います。
正の引数で左回転を、負（-）で右回転をします。
今回は左に90°回転させてみましょう。
"""

from PIL import Image, ImageFilter

img = Image.open('myafu.jpg')
new_img = img.rotate(90)
new_img.show()

"""
rotate()の引数に90を指定することで90度回転した画像が表示されました。
なお、rotate()は回転させた画像を戻り値として渡すので、新しく変数に格納する必要があります。
"""


print("--- 画像のカラーモードを変更する ---")


"""
画像のカラーモードを変更するにはconvert()を使います。
今回は画像の色を白黒にしてみましょう。白黒画像へ変換するにはconvert()にLを指定します。
"""

from PIL import Image, ImageFilter

img = Image.open('myafu.jpg')
new_img = img.convert('L')
new_img.show()

"""
カラー画像が白黒になって出力されました。
この他グレースケールはもちろん『全体的に白っぽくさせる』『横のグラデーションをつける』
など応用的に様々な変更が可能です。
興味がある方は調べてみてください。
"""


print("--- 画像の明度を変える ---")


"""
画像の明度を調整するにはpoint()を使います。
"""

from PIL import Image, ImageFilter

img = Image.open('myafu.jpg')
new_img = img.point(lambda x: x * 2.0)
new_img.show()

"""
lambda式の2.0を1以下にすることで暗くすることも可能です。
"""


print("--- 画像のリサイズをする ---")


"""
リサイズするにはresize()を使います。
resize()では第一引数にサイズ、第二引数にリサイズフィルタを指定します。
"""

from PIL import Image, ImageFilter

img = Image.open('myafu.jpg')
new_img = img.resize((64, 64), Image.LANCZOS)
new_img.show()

"""
リサイズフィルタはいくつか種類がありますが、LANCZOSが最も品質が優れています
（その分パフォーマンスが悪い）。
リサイズフィルタを指定しない場合はデフォルトでNEARESTが指定されます
（品質は悪いがパフォーマンスが良い）。
"""


print("--- 画像をトリミングする ---")


"""
リサイズ同様、画像を任意の座標でトリミングすることも可能です。ト
リミングしたい場合はcrop()を使いましょう。
タプルの要素はそれぞれ(left, upper, right, under)、
つまり(左,上, 右, 下)を表します。
今回はみゃふの顔をクローズアップした画像を生成してみます。
"""

from PIL import Image, ImageFilter

img = Image.open('myafu.jpg')
new_img = img.crop((20, 70, 220, 160))
new_img.show()

"""
cropにタプルを渡すことで、引数にあったトリミングが可能です。
"""


print("--- 画像の上に画像を貼り付ける ---")


"""
画像の上に画像を貼り付けるにはpaste()を使います。
今回はまずresize()を使って小さい画像を作り、
それをオリジナルの画像へ貼り付ける処理をしてみましょう。
paste()のタプルで指定するのは（左のX座標,右のY座標）です。
"""

from PIL import Image, ImageFilter

img = Image.open('myafu.jpg')
new_img = img.resize((64, 64), Image.LANCZOS)
img.paste(new_img, (75, 155))
img.show()

"""
今回は既存の画像をリサイズしましたが、
もちろん全く異なる2つの画像をopenしてpaste()することも可能です。
"""


print("--- 画像の保存 ---")


"""
最後に画像を保存する方法の紹介です。画像の保存ではsave()を使います。
save()の第一引数に保存したいパスを指定することで、
元の画像に処理を加えた画像を保存できます。
ここでは本稿で紹介してきた関数をいくつか使って画像処理を施し、
更にその加工後の画像を保存してみましょう。
"""

from PIL import Image, ImageFilter

img = Image.open('myafu.jpg')
# トリミングして暗めに、更にグレイスケールに変更
new_img = img.crop((30, 70, 210, 160)).point(lambda x: x * 0.7).convert('L')
new_img.save('myafu_gray.jpg', quality=95)

"""
quality引数は1〜100までの数値を任意に設定することで、
保存される画像のクオリティ（＝解像度）を上げたり下げたりできます。
しかし、95よりも大きい値は品質が向上せずただ容量の大きいファイルができあがるだけなので、
クオリティを最大にしたい場合は95を設定するのが良いでしょう
（デフォルトは75です）解像度を優先するか、
ファイルサイズを考慮すべきかは画像処理の目的やファイル数にも依るので、
適宜ケースバイケースで判断することをオススメします。
"""


print("--- Pillowで色々な画像処理を試そう ---")


"""
今回はPythonの画像処理ライブラリ・Pillowのインストールから
具体的な加工方法までまとめて紹介しました。
処理の種類が沢山ありますが、
これらを組み合わせたり他のライブラリも使ってみたりすることで
画像処理の業務効率を劇的に改善することも可能です。
是非慣れていってみてください。
"""





