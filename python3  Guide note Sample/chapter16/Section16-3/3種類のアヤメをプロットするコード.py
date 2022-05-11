# 3種類のアヤメをプロットするコード
from sklearn import datasets
import matplotlib.pyplot as plt


iris = datasets.load_iris()
dir(iris)
X = iris.data    # 計測データ
Y = iris.target    # ターゲットデータ
for i, cl, mk, lb in zip([0, 1, 2], 'rgb', 'o+x', iris.target_names):
    plt.scatter(X[Y==i][:, 0], X[Y==i][:, 1], color=cl, marker=mk, label=lb)

# X[100:, 0], X[100:, 1]  0列目(がく片の長さ)、1列目(がく片の幅)
plt.title("Iris Plans Database")
plt.xlabel('sepal length(cm)')
plt.ylabel('petal length(cm)')
plt.legend()
plt.show()