# リンゴと言われて思い浮かぶ4つの属性を考える。
# その4つの属性をインスタンス変数に持つ、appleクラスを定義する。


class Apple:
    def __init__(self, c, p, s, k):
        # Producing center→産地,size→大きさ,kind→品種,color→色
        self.color = c
        self.producing = p
        self.size = s
        self.kind = k
