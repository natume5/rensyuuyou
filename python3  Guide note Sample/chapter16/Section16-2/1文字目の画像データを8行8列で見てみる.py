# 1文字目の画像データを8行8列で見てみる
from sklearn import datasets


digits = datasets.load_digits()
dir(digits)
print(digits.images[0])
