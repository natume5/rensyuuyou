# 文字列を挿入すると最長の文字列に合わせた長さで切れる
import numpy as np


words = np.array(["dog", "cat", "bird"])
# "bird"  文字数の上限は最長の"bird"に合わせて4文字になる
new_words = np.insert(words, 0, "snake")
print(new_words)    # 4文字で"snake"が切れる
