# 追加したインスタンスメゾットを実行する
# Simpleクラスに動的にクラスメゾットgreetingを追加する


class Simple:    # Simpleクラス定義
    pass    # Simpleクラスにはメンバーはいない

# 動的にインスタンスメゾットを追加する
obj1 = Simple()
obj2 = Simple()


def drum(beat="トコトコ"):
    print(beat)


def sax(phrase="ブーブー"):
    print(phrase)

obj1.play = drum    # obj1にplay()を追加
obj2.play = sax    # obj2にplay()を追加

# 追加したインスタンスメゾットを実行
print(obj1.play())    # obj1のplay()ではdrum()が実行
print(obj2.play())    # obj2のplay()ではsax()が実行

print(obj1.play("ドンドコ"))
print(obj1.play())
print(obj2.play())
