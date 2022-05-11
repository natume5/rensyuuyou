# 画像イメージと分類結果(404~415の12文字を表示)
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import metrics
import matplotlib.pyplot as plt


digits = datasets.load_digits()
dir(digits)
n_train = len(digits.data) * 2 // 3
x_train = digits.data[:n_train]
y_train = digits.target[:n_train]
x_test = digits.data[n_train:]
y_test = digits.target[n_train:]
[d.shape for d in [x_train, y_train, x_test, y_test]]

clf = svm.SVC(gamma=0.001)
clf.fit(x_train, y_train)
clf.score(x_test, y_test)
predicted = clf.predict(x_test)
metrics.classification_report(y_test, predicted)
imgs_yt_preds= list(zip(digits.images[n_train:], y_test, predicted))
# digits.images[n_train:]  画像データ、y_test  正解、predicted  分類結果
for index, (image, y_t, pred) in enumerate(imgs_yt_preds[404:416]):
    plt.subplot(3, 4, index + 1)    # 3x4で表示する
    plt.axis('off')
    plt.tight_layout()
    plt.imshow(image, cmap="Greys", interpolation="nearest")    # 画像を表示
    plt.title(f'{y_t} pre:{pred}', fontsize=12)    # 正解と分類結果
    # {y_t} pre:{pred}  画面上のタイトル

plt.show()
