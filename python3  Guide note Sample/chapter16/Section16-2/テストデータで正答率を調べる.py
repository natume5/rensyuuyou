# テストデータで正答率を調べる
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn import svm


digits = datasets.load_digits()
print(dir(digits))
n_train = len(digits.data) * 2 // 3
x_train = digits.data[:n_train]
y_train = digits.target[:n_train]
x_test = digits.data[n_train:]
y_test = digits.target[n_train:]
print([d.shape for d in [x_train, y_train, x_test, y_test]])

clf = svm.SVC(gamma=0.001)
clf.fit(x_train, y_train)
print(clf.score(x_test, y_test))
# score(x_test, y_test)  テスト用のデータ
