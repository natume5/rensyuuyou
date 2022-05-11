# irisデータセットに納められているものを調べる
from sklearn import datasets


iris = datasets.load_iris()
print(dir(iris))
