# データセットに納められているものを調べる
from sklearn import datasets


boston = datasets.load_boston()
print(dir(boston))
