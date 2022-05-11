# ポアゾン分布をヒストグラムで表示する
import matplotlib.pyplot as plt
import numpy as np


# ポアゾン分布(平均50、1000個)
data = np.random.poisson(lam=50, size=1000)
count, bins_eedges, patches = plt.hist(data, bins = 100)    # ヒストグラム
plt.grid()
plt.show()
