# データの構造を調べる
from sklearn import datasets


iris = datasets.load_iris()
dir(iris)
X = iris.data    # 計測データ
Y = iris.target    # ターゲットデータ
print(X.shape)
print(Y.shape)
