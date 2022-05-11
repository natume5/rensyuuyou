# モデルclfを使って訓練データで学習する
from sklearn import datasets
from sklearn import svm


iris = datasets.load_iris()     # アヤメのデータセットを読み込む
X = iris.data    # データ
Y = iris.target     # ターゲット
n_train = len(X) // 2    # データの半分の個数
X_train, X_test = X[:n_train], X[n_train:]    # 訓練データ
"""
正答率の低い原因は
n_train = len(X) // 2　と
X_train, X_test = X[:n_train], X[n_train:]　の訓練データにある
3種類のアヤメのデータを2つに分けて前半のデータを訓練用に後半のデータをテスト用にしたので
訓練データにはvirginicaのデータは1個もない為
"""
Y_train, Y_test = Y[:n_train], Y[n_train:]    # 訓練データ
clf = svm.SVC()    # モデルを作る
clf.fit(X_train, Y_train)    # 学習する
print(clf.score(X_test, Y_test))
