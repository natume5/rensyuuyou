class Color:
    def __init__(self, text="red"):
        self.text = text

    def __del__(self):
        print(str(self) + "が破棄されました")

color = Color()
print(color.text)
# インスタンス変数はクラスで定義しないでも使える
color.text_2 = "green"
print(color.text_2)
