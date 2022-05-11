# ターゲットデータで正解を調べてみる
from sklearn import datasets
import matplotlib.pyplot as plt


digits = datasets.load_digits()
dir(digits)
plt.matshow(digits.images[0], cmap="Greys")
print(digits.target[0])
