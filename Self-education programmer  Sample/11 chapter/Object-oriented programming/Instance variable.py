class Orange:   # class[クラス名(クラス名の始めは必ず大文字)]:下段に[スイート]
    def __init__(self, w, c):   # __init__はinitialize(初期化)の略
        self.weight = w   # インスタンス変数をこの構文で定義している。
        self.color = c   # self.[変数名] = [値]
        print("Created!")

# Orangeオブジェクトを呼び出している[クラス名]([引数])
or1 = Orange(10, "dark orange")  # Orangeクラスをインスタンス化してる
# [オブジェクト名].[インスタンス変数名]でインスタンス変数の値を取得
print(or1)
