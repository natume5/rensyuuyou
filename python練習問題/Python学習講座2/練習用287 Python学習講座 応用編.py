#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- NumPy入門 型と型変換 ---")


print("--- NumPyの型 ---")


"""
以下URLから基本的な演算でよく使用するものを抜粋しました。
https://docs.scipy.org/doc/numpy-dev/user/basics.types.html

型 	     説明
bool 	真偽型
int8 	8ビット符号付き整数
int16 	16ビット符号付き整数
int32 	32ビット符号付き整数
int64 	64ビット符号付き整数
uint8 	8ビット符号なし整数
uint16 	16ビット符号なし整数
uint32 	32ビット符号なし整数
uint64 	64ビット符号なし整数
float16 	16ビット浮動小数点
float32 	32ビット浮動小数点
float64 	64ビット浮動小数点
complex64 	64ビット複素数
complex128 	１２８ビット複素数

上記以外にも、C言語と互換の型などがあります。
詳細はリンク先を参照してください。
"""


print("--- 型の指定 ---")


"""
ここでも少し説明しましたが、
配列の生成時にdtypeで型を指定することができます。
配列全ての要素が同じ型になります。
型を指定する場合は文字列か、nu.型名で指定します。
"""

import numpy as np

# 文字列で指定
x = np.array([1, 2, 3], dtype='int64')
print(x)    # [1 2 3]

# np.で指定
x = np.array([1, 2, 3], dtype=np.int64)
print(x)    # [1 2 3]


print("--- 型変換 ---")


"""
作成後の配列に対してastypeを使用して型変換を行うことができます。
例えばint32からfloat32に型を変える場合は以下のようにします。
"""

import numpy as np

x = np.array([1, 2, 3, 4, 5], dtype='int32')
y = x.astype('float32')
print(y)    # [1. 2. 3. 4. 5.]

"""
元のインスタンスは破壊されない点に注意してください。
"""
