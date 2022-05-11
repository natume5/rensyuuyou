class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")


or1 = Orange(10, "dark orange")
or1.weight = 100   # インスタンス変数の値を変更している
or1.color = "light orange"   # インスタンス変数の値を変更している
# [オブジェクト名].[インスタンス変数名] = [新しい値]
print(or1.weight)
print(or1.color)
