# 画像データから手書き文字を復元する
from sklearn import datasets
import matplotlib.pyplot as plt


digits = datasets.load_digits()
dir(digits)
plt.matshow(digits.images[0], cmap="Greys")
# images[0]    # 1文字目のデータを画像にする
plt.show()
