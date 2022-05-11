# 正解の数値が入ったターゲットデータを確かめる
from sklearn import datasets


digits = datasets.load_digits()
dir(digits)
print(digits.data)
print(digits.target)
