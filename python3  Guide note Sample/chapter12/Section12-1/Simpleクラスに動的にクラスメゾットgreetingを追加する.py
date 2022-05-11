# Simpleクラスに動的にクラスメゾットgreetingを追加する
class Simple:    # Simpleクラス定義
    pass    # Simpleクラスにはメンバーはいない

Simple.x = 100    # クラス変数xを追加する
print(Simple.x * 2)


def hello(msg="ハロー"):    # helloメゾット定義
    print(msg)

Simple.greeting = hello    # greetingクラスメゾットを追加
print(Simple.greeting("おはよう！"))    # 実行
