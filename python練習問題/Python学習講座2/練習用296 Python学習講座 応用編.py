#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- NumPy入門 基本的な線形代数計算 その3 連立方程式 ---")


print("--- linalg.solve ---")


"""
NumPyのlinalgには連立方程式を解くsolveが用意されています。
引数に連立方程式の係数行列と定数の行列を指定します。

例えば、以下の連立方程式を解く場合を考えます。
\[
\begin{equation}
\begin{cases}
\; 3x+y= 9 \\
\; x+3y= 0
\end{cases}
\end{equation}
\] 連立方程式の変数x、yの係数の及び定数を行列で表すと
それぞれ以下のようになります。

\[
A = \left(
\begin{array}{ll}
3 & 1 \\
1 & 3
\end{array}
\right)
\]

\[
B = \left(
\begin{array}{ll}
9\\
0
\end{array}
\right)
\]

それでは実際にpythonのコードで連立方程式を解いてみましょう。
"""

import numpy as np

# 係数行列
coef = np.array([[3, 1], [1, 3]])
print(coef)

# 定数の行列
dep = np.array([9, 0])
print(dep)

# 連立方程式の解
ans = np.linalg.solve(coef, dep)
print(ans)

"""
[[3 1]
 [1 3]]

[9 0]

[ 3.375 -1.125]

念の為検算してみましょう。
"""

print(3 * ans[0] + 1 * ans[1])

print(1 * ans[0] + 3 * ans[1])

"""
9.0
0.0

正しい答えが得られていたことが確認できました。
"""
