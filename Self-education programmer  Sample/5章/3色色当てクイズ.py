colors = ["purple", "orange", "green"]

guess = input("何色でしょう？(入力して下さい。):")

if guess in colors:
    print("当たり！")
else:
    print("ハズレ！また挑戦してね。")
