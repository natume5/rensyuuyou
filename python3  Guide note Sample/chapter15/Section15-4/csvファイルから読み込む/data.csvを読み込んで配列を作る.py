# data.csvを読み込んで配列を作る
import numpy as np


data = np.loadtxt("data.csv", delimiter=",", skiprows=1)
"""
delimiter=","  カンマの区切りを読み込む
skiprows=1  1行目を読み込みません
"""
print(data)
