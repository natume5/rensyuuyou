# 条件式をorを使って書いた場合:どちらか片方でもTrueならば合格
# randomモジュールのrandint関数を読み込む
from random import randint
size = randint(5, 20)
weight = randint(20, 40)
# 判定(どちらか片方でもTrueならば合格)
if (size >= 10) or (weight >= 25):
    result = "合格"
else:
    result = "不合格"

# 結果の出力
text = f"サイズ{size}、重量{weight}:{result}"
print(text)
