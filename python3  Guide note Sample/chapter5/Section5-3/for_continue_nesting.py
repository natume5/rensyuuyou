# ネスティングしている内側のfor文でcontinueを実行する
for i in range(4):
    for j in range(4):
        if i < j:
            print("." * j)
            continue     # スキップ
        print(f"i={i}, j={j}")
