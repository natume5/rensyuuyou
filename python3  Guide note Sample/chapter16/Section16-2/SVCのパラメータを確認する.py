# SVCのパラメータを確認する
from sklearn import svm


clf = svm.SVC(gamma=0.001)
print(clf)
