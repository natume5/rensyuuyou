# がく片の長さと幅の値で3種類のアヤメをプロットする
from sklearn import datasets
import matplotlib.pyplot as plt


iris = datasets.load_iris()
dir(iris)
X = iris.data    # 計測データ
Y = iris.target    # ターゲットデータ
# setosa:0~49, versicolor:50~99, virginica:100~149
plt.scatter(X[:50, 0], X[:50, 1], color='r', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='g', marker='+',  label='versicolor')
plt.scatter(X[100:, 0], X[100:, 1], color='b', marker='x', label='virginica')
# X[100:, 0], X[100:, 1]  0列目(がく片の長さ)、1列目(がく片の幅)
plt.title("Iris Plans Database")
plt.xlabel('sepal length(cm)')
plt.ylabel('petal length(cm)')
plt.legend()
plt.show()
