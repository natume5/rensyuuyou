class Greet():
    def hello(self):
        print("やあ！")

    def bye(self):
        print("さよなら")


class Greet2(Greet):
    def hello(self, name=None):
        if name:
            print(name + "さん、こんにちは！")
        else:
            super().hello()
