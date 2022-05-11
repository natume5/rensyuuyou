# ループカウンタを付けて表示する
names = ["鈴木", "田中", "栗林", "山岡"]
for i, who in enumerate(names, 1):        # iにカウンタの値、whoの名前が入る
    print(f"{i}:{who}さん")