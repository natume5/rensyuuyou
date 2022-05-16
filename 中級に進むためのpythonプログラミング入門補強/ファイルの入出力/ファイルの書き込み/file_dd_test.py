# -*-coding:utf-8-*-
import sys


print(sys.argv)
for arg in sys.argv:
    print(arg)
print("-" * 20)
# インデックス0番目は実行pyパスが入るので
# [1:]を付けインデックス1番目よりループ
for arg in sys.argv[1:]:
    print(arg)



