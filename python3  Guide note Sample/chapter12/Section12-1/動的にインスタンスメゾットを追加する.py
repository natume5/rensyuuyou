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
