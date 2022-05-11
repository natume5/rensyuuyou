# 学習結果の評価レポート
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
print(metrics.classification_report(y_test, predicted))
# precision(適合率)、recall(再現率)、f1-score(F値)、support(個数)
