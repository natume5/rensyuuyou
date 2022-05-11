# enumerate()を使って要素を順に取り出す
import numpy as np


words = ["flower", "bird", "wind", "moon"]
for i, item in enumerate(words, 1):
    print(i, item)    # iには繰り返し回数が入る
