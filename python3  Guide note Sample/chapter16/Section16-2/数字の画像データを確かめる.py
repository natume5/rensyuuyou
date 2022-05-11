# 数字の画像データを確かめる
from sklearn import datasets


digits = datasets.load_digits()
dir(digits)
print(digits.data)
