# digigitsデータセットの説明文を読む
from sklearn import datasets


digits = datasets.load_digits()
dir(digits)
print(digits.DESCR)
