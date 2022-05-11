# priceはリードオンリー


from goods_property import Goods
shoes = Goods("dream", 6800)
print(shoes.name)    # nameの値を調べる
shoes.name = "Dream 8"    # nameの値を更新する
# nameプロパティがあるように見える
print(shoes.name)
print(shoes.price)    # priceの値を調べる
shoes.price = 7200    # priceを更新しようとするとエラーになる
