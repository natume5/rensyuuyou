class Color:
    def __init__(self, text="red"):
        self.text = text

    def __del__(self):
        print(str(self) + "が破棄されました")
