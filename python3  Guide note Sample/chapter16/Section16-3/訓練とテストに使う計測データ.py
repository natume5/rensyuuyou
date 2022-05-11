# 訓練とテストに使う計測データ
from sklearn import datasets


iris = datasets.load_iris()
dir(iris)
X = iris.data
print(X)
