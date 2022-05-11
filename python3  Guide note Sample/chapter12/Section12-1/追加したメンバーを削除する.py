class Simple:    # Simpleクラス定義
    pass    # Simpleクラスにはメンバーはいない

Simple.x = 100    # クラス変数xを追加する

# 動的にインスタンスメゾットを追加する
obj1 = Simple()
obj2 = Simple()


# 追加したメンバーを削除する
obj1.a = None
obj1.play = None
del Simple.x

print(obj1.a)
print(obj1.play)
print(Simple.x)
