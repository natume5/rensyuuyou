# 1文字目の画像データ
from sklearn import datasets


digits = datasets.load_digits()
dir(digits)
print(digits.data[0])
print(digits.images[0])
