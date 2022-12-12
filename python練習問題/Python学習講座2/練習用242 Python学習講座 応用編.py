#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Pillowの使い方 ---")



print("--- Pillowとは？ ---")


"""
Python2時代、PythonにはPython Imaging Library（PIL）
という非常に強力な画像処理ライブラリがありました。
ですが、残念ながら2011以降更新が停止され、
Python3はサポートされていない状況です。
そんな中、Python3に対応したPILからフォークされたライブラリが誕生しました。
それがPillowです。
Pillowを使用すると、BMP、JPEG、PNG、PPM 、GIF、TIFF
といった代表的な画像形式に対し、サイズ変換、回転、クロッピング、合成等を
簡単に行うことができるようになります。
"""


print("--- Pillowのインストール ---")


"""
いつもどおりpipで一発です。

pip install Pillow
"""


print("--- Pillowを使った画像処理入門 ---")


"""
それでは、簡単な使い方について学習しましょう。
画像を開いて情報を取得する

まず、Image.open関数で画像を読み込み、
プログラム上で加工処理をするためのImageオブジェクトを生成します。
引数に画像のパスを指定します。
"""

from PIL import Image

image = Image.open('image_car.jpg')

"""
また、開いた画像の各種情報を取得する関数が用意されています。
"""

# ファイルフォーマットの取得
print(image.format)    # JPEG

# ピクセル形式("1", "L", "RGB", "CMYK."など)
print(image.mode)    # RGB

# 画像サイズ
print(image.size)    # (500, 180)


"""
画像を保存する

まだ画像を開いただけですが、加工したデータをsaveメソッドで保存することができます。
引数に出力先ファイル名を指定します。
"""

image.save('output.jpg')


"""
画像のリサイズ

それでは画像加工を行ってみましょう。
今回は以下の画像を使用します。
（写真は新川と佃島にかかる中央大橋から見える「メッセンジャー像」です。）

画像のリサイズはずばりそのままresizeメソッドを使用します。
引数にリサイズ後のタプルを指定します。
戻り値に新たなimageオブジェクトが返されます。
"""

image = Image.open('sample.jpg')

# リサイズする
resized_image = image.resize((400, 400))
print(image.size)    # (450, 800)
resized_image.save('resized.jpg')

"""
ただし、出力画像をご覧の通り、オリジナルの縦横比は無視されます。
もしオリジナルの縦横比を考慮したい場合は、
Pillow3.4以降に追加されたthumbnailメソッドを使用します。
なぜかthumbnailメソッドは破壊的に作用し、
元のオブジェクトを書き換えてしまうので注意してください。
"""

# サムネイル化する
image.thumbnail((400, 400))
print(image.size)    # (225, 400)
image.save('thumbnail.jpg')

"""
こんどは縦横比が考慮され、縦が400となっています。


クロッピング

画像の不要箇所を刈り取ることをクロッピング（cropping）と呼びます。
（トリミングと言う場合もあります。）
クロッピングする矩形を2点の座標のタプルで指定します。
例えば、像の上に止まった鳥を抽出したい場合、
以下のように座標を指定してクロッピングします。
"""

image = Image.open('sample.jpg')
rect = (1000, 1000, 1400, 1400)    # 領域を指定する(x0,y0), (x1,y1)
cropped_image = image.crop(rect)

"""
画像を回転、反転させる

画像を回転させるには、rotateを使用します。
引数に角度を指定します。
"""

# 回転
rotate_image = image.rotate(45)
rotate_image.save('rotated_image.jpg')

"""
この場合、回転して角がはみ出してしまいますが、
expandを指定すると回転させつつ枠内に収まるようにリサイズしてくれます。
"""

# 回転その2
rotated_image = image.rotate(45, expand=True)
rotated_image.save('rotated_image2.jpg')

"""
反転させたい場合はtransposeを使用します。
"""

# 反転
fliped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
fliped_image.save('fliped_image.jpg')

"""
画像の貼り付け

pasteメソッドで画像を貼り付けることができます。
第1引数に貼り付けるimageオブジェクトを、
第2引数に貼り付け先の座標を、
第3引数でマスク領域のimageオブジェクトを指定します。
もし、第3引数を省略すると、
透明部分がマスクされて黒く塗りつぶされることになります。
"""

# 画像の貼り付け
image.thumbnail((800, 800))
python_logo = Image.open('site-logo.png')
pasted_image = image.copy()
pasted_image.paste(python_logo, (0, 0), python_logo)
pasted_image.save('pasted_image.jpg')

"""
↓貼り付けたのは透明背景のロゴ画像です。
透明背景で白色フォントなのでサイトに添付すると見えなくなってしまいました(汗)。


テキストの挿入

テキストを挿入する場合はImageDrawをインポートしてtextを呼び出します。
"""

from PIL import Image, ImageFont, ImageDraw

image = Image.open('sample.jpg')
image.thumbnail((800, 800))
written_image = image.copy()

# 文字列の書き込み
font = ImageFont.truetype("arial.ttf", 42)
draw = ImageDraw.Draw(written_image)
draw.text((0, 0), "サンプル文字列", (255, 255, 255), font=font)
written_image.save('written_image.jpg')
 

"""
第1引数にテキストを記入する座標を、
第2引数にテキスト、font、fillでそれぞれフォントと色を指定することができます。

座標(0, 0)に白色でテキストが記入されたことが確認できます。
Pillowを使用すると簡単に画像加工を行うことができます。
上に挙げた処理以外にも様々な処理ができますので、
画像認識のための前捌きや、ECサイトのキャンペーン画像の自動生成等、
業務にも応用できそうですね。
https://pillow.readthedocs.io/en/latest/index.html
その他の機能は上記公式ドキュメントを参照してください。
"""
