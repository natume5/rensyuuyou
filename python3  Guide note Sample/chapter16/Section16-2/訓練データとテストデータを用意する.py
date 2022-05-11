# 訓練データとテストデータを用意する
from sklearn import datasets
import matplotlib.pyplot as plt


digits = datasets.load_digits()
print(dir(digits))
n_train = len(digits.data) * 2 // 3    # データの2/3の個数
x_train = digits.data[:n_train]    # dataの前半2/3(訓練用)
y_train = digits.target[:n_train]    # targetの前半2/3(訓練用)
x_test = digits.data[n_train:]    # dataの後半1/3(テスト用)
y_test = digits.target[n_train:]    # targetの後半1/3(テスト用)
