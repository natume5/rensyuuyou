# 教師データ(ターゲット)
from sklearn import datasets


iris = datasets.load_iris()
dir(iris)
X = iris.data    # 計測データ
Y = iris.target    # ターゲットデータ
print(Y)
"""
0=setosa,1=versicolor,2=virginca
"""
