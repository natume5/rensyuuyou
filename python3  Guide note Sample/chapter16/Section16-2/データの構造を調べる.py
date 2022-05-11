# データの構造を調べる
from sklearn import datasets


digits = datasets.load_digits()
dir(digits)
digits.DESCR
print(digits.data.shape)    # 1797x64の2次元配列
print(digits.target.shape)    # 要素が1797個の1次元配列
