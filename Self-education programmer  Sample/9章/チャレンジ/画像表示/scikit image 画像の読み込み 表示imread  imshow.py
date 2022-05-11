# -*- coding: utf-8 -*-
from skimage import io


def main():
    # CSVファイルを取得
    img = io.imread('index.jpg')
    io.imshow(img)

if __name__ == "__main__":
    main()

"""画像の読み込み・表示

Scikit-imageでは、skimage.io.imreadメソッドで画像を読み込むことができます。
また、skimage.io.imshowメソッドで画像を表示できます。

    【書式】
    img = skimage.io.imread(画像ファイル名)
    io.imshow(img)
"""
