# Simpleクラスに動的クラス変数xを追加する
class Simple:    # Simpleクラス定義
    pass    # Simpleクラスにはメンバーはいない

Simple.x = 100    # クラス変数xを追加する
print(Simple.x * 2)
