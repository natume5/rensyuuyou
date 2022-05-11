# !/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    list = [1, 3, 4, 9, 6, 2, -1]
    # ソート前の配列
    print('ソート前 :{}'.format(list))
    # 調べる範囲の開始する位置を一つずつ後ろへ移動していく繰り返し
    for i in range(len(list) - 1):
        # 後から前へ小さい値を移動させていく
        for j in range(len(list) - 1, i, -1):
            if list[j] < list[j - 1]:
                tmp = list[j]
                list[j] = list[j - 1]
                list[j - 1] = tmp

    print('ソート後 :{}'.format(list))
if __name__ == '__main__':
    main()
