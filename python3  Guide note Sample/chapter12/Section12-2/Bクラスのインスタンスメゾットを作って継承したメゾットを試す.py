# スーパークラスにするAクラス定義
class A:    # Aクラス
    def hello(self):    # Aクラスのインスタンスメゾット
        print("ハロー")


# Aクラスを継承したBクラス
class B(A):    # Aクラスを継承したBクラス
    def bye(self):    # Bクラスのインスタンスメゾット
        print("グッバイ")


# Bクラスのインスタンスメゾットを作って継承したメゾットを試す
obj = B()    # Bクラスのインスタンスを作る
print(obj.hello())    # Aクラスから継承したインスタンスメゾットを実行
print(obj.bye())    # Bクラスのインスタンスメゾットを実行
