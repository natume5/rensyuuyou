# fruits辞書からフルーツを取り出す
fruits = {"apple": 7, "orange": 5, "mango": 3, "peach": 6}
while fruits:     # fruitsが空でなければ繰り返す
    ans = input("フルーツを取り出しますか？(y/n):")
    if ans =="y":
        key, value = fruits.popitem()    # 任意の要素を取り出す
        print(f"{key}は{value}個")
    elif ans == "n":
        print("終了しました。")
        break
else:     # whileループの終了後に実行
    print("もう空っぽです。")
