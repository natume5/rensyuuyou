# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
●例題１－３
画面に "10を3で割ったときの商は" に続いて 10//310 // 310//3 の結果を，
"余りは" に続いて剰余 10%310 \% 310%3 を表示せよ．
整数除算の演算子は //，剰余の演算子は % である ．
普通の割り算 /// をすると小数（正確な用語は浮動小数点数）が表示される．

print("10を3で割ったときの商は", 10 //3 )
print("余りは", 10%3 )
print( 10/3 )

10を3で割ったときの商は 3
余りは 1
3.3333333333333335
"""

print("10を3で割った時の商は", 10 // 3)
print("余りは", 10 % 3)
print(10 / 3)
