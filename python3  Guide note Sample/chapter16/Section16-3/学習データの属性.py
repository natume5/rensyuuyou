# 学習データの属性
from sklearn import datasets


iris = datasets.load_iris()
dir(iris)
X = iris.data
print(iris.feature_names)
"""
sepal width(がく片の長さ)、petal length(花弁の長さ)、
petal width(がく片の幅)、sepal length(花弁の幅)
"""