from sklearn import datasets
from sklearn import svm, metrics
import matplotlib.pyplot as plt


digits = datasets.load_digits()
X = digits.data
y = digits.target
n_train = len(X)*2//3

X_train, y_train = X[:n_train], y[:n_train]

X_test, y_test = X[n_train:], y[n_train]

clf = svm.SVC(gamma=0.001)
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(f"正答率{accuracy}")
predicted = clf.predict(X_test)
n_error = (y_test != predicted).sum()
print(f"誤った個数:{n_error}")


print("clssification report")
print(metrics.classification_report(y_test, predicted))
print("confusion matrix")
print(metrics.confusion_matrix(y_test, predicted))


imgs_yt_preds = list(zip(digits.images[n_train:], y_test, predicted))
for index, (image, y_t, pred) in enumerate(imgs_yt_preds[404:416]):
    plt.subplot(3, 4, index + 1)
    plt.axis('off')
    plt.tight_layout()
    plt.imshow(image, cmap="Greys", interpolation="nearest")
    plt.title(f't:{y_t} pre:{pred}', fontsize=12)
plt.show()
