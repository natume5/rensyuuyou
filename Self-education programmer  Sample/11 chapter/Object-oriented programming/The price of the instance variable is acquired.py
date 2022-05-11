class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")


or1 = Orange(10, "dark orange")
print(or1.weight)  # インスタンス変数の値を取得
print(or1.color)  # [オブジェクト名].[インスタンス変数]
