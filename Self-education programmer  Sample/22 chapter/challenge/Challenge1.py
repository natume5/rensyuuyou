"""簡単なレベルのアルゴリズム問題を３問解く"""
# １問目 線形探索アルゴリズム(もしくは逐次探索アルゴリズム)

"""一枚一枚まっすぐにめくっていくことから逐次探索と呼ばれ、
途中で一枚飛ばしたり、途中からめくり始めたりせず、
最初から最後まで目的のデータが見つかるまで探索を続けることから
線形探索と呼ばれています。"""

"""ハートのトランプが1~Kまで13枚ランダムに並べられています。
このとき、どこにハートの7のトランプがあるか答えなさい"""


# coding: utf-8
# Here your code !


def linear_search(card_list, card):
    for i, element in enumerate(card_list):
        if element == card:
            print("{0}番目に{1}はあります".format(card))
            return
    print("{0}はありませんでした".format(card))
    return

if __name__ == '__main__':
    heart_cards = ["h-5", "h-J", "h-2", "h-9", "h-1",
                   "h-7", "h-K", "h-4", "h-10", "h-3",
                   "h-6", "h-8", "h-Q"]
    heart_king = "h-k"
    linear_search(heart_cards, heart_king)
