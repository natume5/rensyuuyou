# 学習器SVMでが学習を行う
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn import svm


digits = datasets.load_digits()
print(dir(digits))
n_train = len(digits.data) * 2 // 3    # データの2/3の個数
x_train = digits.data[:n_train]    # dataの前半2/3(訓練用)
y_train = digits.target[:n_train]    # targetの前半2/3(訓練用)
x_test = digits.data[n_train:]    # dataの後半1/3(テスト用)
y_test = digits.target[n_train:]    # targetの後半1/3(テスト用)
print([d.shape for d in [x_train, y_train, x_test, y_test]])

clf = svm.SVC(gamma=0.001)    # 学習器
clf.fit(x_train, y_train)    # 訓練データと教師データで学習する
# fit(x_train, y_train)  訓練用のデータ
