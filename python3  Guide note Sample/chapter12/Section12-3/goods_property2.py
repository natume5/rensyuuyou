# 2個のプロパティをproperty()で定義したGoodsクラス


class Goods:
    # 初期化メゾット
    def __init__(self, name, price):
        # 非公開の__dataインスタンス変数(辞書)
        self.__data = {"name":name, "price":price}


    # nameプロパティ―のゲッター
    def name(self):
        return self.__data["name"]


    # nameプロパティ―のセッター
    @name.setter
    def name(self, value):
        self.__data["name"] = value


    # priceプロパティのゲッター
    def price(self):
        price = self.__data["price"]
        price_str = f"{price:,}円"
        return price_str


    # プロパティの設定
    name = property(get_name, set_name)
    # nameプロパティのゲッター/セッターを設定
    price = property(get_price)    # priceプロパティのゲッターを設定
