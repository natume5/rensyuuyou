# スーパークラスGreetのhello()をサブクラスでオーバーライドする
# スーパークラス


class Greet():
    def hello(self):
        print("やあ！")

    def bye(self):
        print("さよなら")


# サブクラス
class Greet2(Greet):    # Greet  Greetクラスを継承
    # スーパークラスのメゾットをオーバーライドする
    def hello(self, name=None):    # Greetクラスのhello()をオーバーライド
        if name:
            print(name + "さん こんにちは！")
        else:
            super().hello()
            # スーパークラスのhello()→def hello(self):をそのまま使う
