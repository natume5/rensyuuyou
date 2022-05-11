# 学習済みモデルが誤って分類した個数を調べる
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
[d.shape for d in [x_train, y_train, x_test, y_test]]

clf = svm.SVC(gamma=0.001)
clf.fit(x_train, y_train)
clf.score(x_test, y_test)
predicted = clf.predict(x_test)    # 分類結果を取り出す
print((y_test != predicted).sum())    # 正解と分類結果が一致しなかった数を合計する
