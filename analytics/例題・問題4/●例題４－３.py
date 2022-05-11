# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
●例題４－３
ifブロックの中に別のifブロックがあるプログラムを作ってみよう．
else の後に if 文を入れたい場合には，elif: とあわせて書くことができる．
 これを使うと，不必要な字下げ（インデント）をしないで済むようになるので綺麗に書ける．

if 条件文1:
　　条件文1が真のときに実行される文のブロック
elif 条件文2:
    条件文1が偽で条件文2が真のときに実行される文のブロック
else:
    条件文1が偽で条件文2も偽のときに実行される文のブロック

入力した整数が正の場合はpositiveと表示して，
 さらに100以上の場合は100以上，100未満の場合は100未満と表示する．
また，入力した整数が正でない場合，0の場合はzero，負の場合はnegativeと表示する．

x = int(input("Please enter an integer:"))
if x > 0 :
    print("positive")
    if x >= 100 :
        print("100以上")
    else :
        print("100未満")
elif x == 0 :
    print ("zero")
else :
    print ("negative")

positive
100以上

条件文には，様々な論理式を入れることができる．
論理式とは真(True)か偽(False)に and（かつ）
や or（または） や not などの論理演算子を適用した式のことであり， 必ず真か偽になる．

たとえば，「xが 1 または yが6でない」ということは，

x==1 or y!=6

という論理式で書ける．

同様に「xが4未満でなく かつyが6未満」は

not(x<4) and y<6

と書ける．
"""

A = int(float(input("整数を入力して下さい。:")))
if A > 0:
    print("positive")
    if A >= 100:
        print("100以上")
    else:
        print("100未満")
elif A == 0:
    print("zero")
else:
    print("negative")
