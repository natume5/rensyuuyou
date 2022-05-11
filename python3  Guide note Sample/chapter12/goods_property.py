class Goods:
    def __init__(self, name, price):
        self.__data = {"name": name, "price": price}

    @property
    def name(self):
        return self.__data["name"]

    @name.setter
    def name(self, value):
        self.__data["name"] = value

    @property
    def price(self):
        price = self.__data["price"]
        price_str = f"{price:,}円"
        return price_str
