# ShuffleSplitを使って学習データを分割する
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import ShuffleSplit


iris = datasets.load_iris()     # アヤメのデータセットを読み込む
X = iris.data    # データ
Y = iris.target     # ターゲット

# データを分割するインデックスを作る
iris_ss = ShuffleSplit(train_size=0.6, test_size=0.4, random_state=0)
train_index, test_index = next(iris_ss.split(X))    # 分割するインデックス番号
# データを分割する
X_train, Y_train = X[train_index], Y[train_index]    # 訓練データ
X_test, Y_test = X[test_index], Y[test_index]    # テストデータ

# モデルを作る
clf = svm.SVC()
clf.fit(X_train, Y_train)    # 訓練する
print(clf.score(X_test, Y_test))
