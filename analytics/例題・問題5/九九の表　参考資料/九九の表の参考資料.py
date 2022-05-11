# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題5－14　■問題5－15　等の参考資料
参考　pythonで九九の表を完成させたい　より
"""

# コード1
nums = range(1, 10)
print("***九九の表***")
print("-------------")
for a in range(1, 10):
    for b in nums:
        answer = a * b
        print(answer, end=" ")
    print(" ")


# コード2
size = range(1, 10)
muls = [[f'{(x * y):2}' for x in size] for y in size]

line_width = 3 * len(size)
print('九九の表'.center(line_width - 4))
print("-" * line_width)
[print(*row) for row in muls]


# コード3　表に罫線を加える例:
size = range(1, 10)
muls = [[f'{(x * y):2}' for x in size] for y in size]

line_width = 3 * len(size)
print('九九の表'.center(line_width - 4))
print(" | " + " ".join(muls[0]))
print("-+" + "-" * line_width)
[print(str(row[0][1]) + "|", * row) for row in muls]


# コード4　sizeをnumsに変更
nums = range(1, 10)
print("***九九の表***")
print('  |' + ' '.join(map(str, list(nums))))
print("-------------")
for a in nums:
    print(str(a) + '|', end=" ")
    for b in nums:
        answer = a * b
        print(answer, end=" ")
    print(" ")


# コード5
nums = range(1, 10)
print("***九九の表***")
print("-------------")
for a in range(1, 10):
    print('???', end=" ")    # ここで何の段かを出力
    for b in nums:
        answer = a * b
        print(answer, end=" ")
    print(" ")
