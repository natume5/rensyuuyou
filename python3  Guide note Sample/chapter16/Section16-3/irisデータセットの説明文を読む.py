# irisデータセットの説明文を読む
from sklearn import datasets


iris = datasets.load_iris()
dir(iris)
print(iris.DESCR)
