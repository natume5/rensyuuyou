"""簡単なレベルのアルゴリズム問題を３問解く"""
# 2問目 ２分探索(バイナリサーチ)アルゴリズム

"""バイナリーサーチ(二分探索とも呼ばれる)とは、
整列済みの要素を半分にして、目的のデータが前にあるのか、
後ろにあるのかを比べながら、目的のデータを見つけ出すアルゴリズム"""

"""線形探索リストの最大探索回数はN(Nはデータの個数分)で、平均探索回数はN/2

一方、二分探索アルゴリズムの
最大探索回数はlog2N＋1
平均探索回数はlog2N
になります

つまり、２分探索アルゴリズムで、100万個のデータを探索するとなると、最大で21回、
平均でも20回トランプをめくるだけですみます。

２分探索アルゴリズム、必ずデータが整列されていないと使えない
データが必ず、左側が一番小さく、右側にいけば大きくなるという条件があるから、
この２分探索アルゴリズムは成立します。"""

"""問題2 ハートのトランプ1~Kまでの内、10枚だけが昇順
(必ず小さいものから並べられている)で並べられています。
このとき、どこにハートの8のトランプがあるか答えなさい"""


# coding: utf-8
# Here your code !


def binary_search(card_list, card):
    low = 0
    high = len(card_list) - 1
    print(high)
    white liw <= high:
        mid = (low + high) // 2
        # print(mid)
        # print(card_list[mid])
        if card_list[mid] == card:
            print("{0}番目に{1}はあります".format(mid, card))
            return
        elif card_list[mid] < crad:
            low = mid + 1
        else:
            high = mid - 1
    return


if __name__ == '__main__':
    hrart_cards = [1, 2, 4, 5, 6, 8, 9, 10, 12, 13]
    heart_eight = 8
    binary_search(heart_cards, heart_eight)
