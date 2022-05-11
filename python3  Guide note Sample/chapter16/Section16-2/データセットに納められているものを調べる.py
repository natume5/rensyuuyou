# データセットに納められているものを調べる
from sklearn import datasets


digits = datasets.load_digits()
print(dir(digits))
"""
'DESCR'   データセットの説明文
'data'   画像データ(特徴量:訓練とテスト用のデータ)
'images'   画像データを8行8列にしたもの
'target'   画像データに対応する数字(ターゲット:教師と検証用のデータ)
'target_names'   targetデータの名前(書いた数字の種類)
"""
