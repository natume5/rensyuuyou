# 数字毎に正解数と読み違えた数字を調べる
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import metrics


digits = datasets.load_digits()
dir(digits)
n_train = len(digits.data) * 2 // 3
x_train = digits.data[:n_train]
y_train = digits.target[:n_train]
x_test = digits.data[n_train:]
y_test = digits.target[n_train:]
[d.shape for d in [x_train, y_train, x_test, y_test]]

clf = svm.SVC(gamma=0.001)
clf.fit(x_train, y_train)
clf.score(x_test, y_test)
predicted = clf.predict(x_test)
metrics.classification_report(y_test, predicted)
print(metrics.confusion_matrix(y_test, predicted))
