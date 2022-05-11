# スーパークラスにするAクラス定義
class A:    # Aクラス
    def hello(self):    # Aクラスのインスタンスメゾット
        print("ハロー")


# Aクラスを継承したBクラス
class B(A):    # Aクラスを継承したBクラス
    def bye(self):    # Bクラスのインスタンスメゾット
        print("グッバイ")
