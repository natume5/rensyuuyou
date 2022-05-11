class Goods:
    def __init__(self, name, price):
        self.__data = {"name": name, "price": price}

    def get_name(self):
        return self.__data["name"]

    def set_name(self, value):
        self.__data["name"] = value

    def get_price(self):
        price = self.__data["price"]
        price_str = f"{price:,}円"
        return price_str

    name = property(get_name, set_name)
    price = property(get_price)
