# 0~9の配列を作る
import numpy as np


print(np.arange(10))
"""
 書式:範囲から配列を作る　　numpy.arange(start,stope,dtype=None)
引数のうち省略できないものはstopだけで、
startを省略すると0、stepを省略すると1となる。
dtypeは数値の型を指定するが、省略するとstert、stop、stepに合わせて型が選ばれる。
"""
