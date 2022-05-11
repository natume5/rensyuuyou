# 最後の要素を削除した配列を作る
import numpy as np


words = np.array(["dog", "cat", "bird"])
new_words = np.delete(words, len(words)-1)
# len(words)-1  要素数から1を引くと最後のインデックス番号になる
print(new_words)
