fruit = {"apple": 7, "orange": 5, "peach": 6}
while fruit:
    key = input("どのフルーツを取り出しますか？(qで終了)")
    if key == "":
        continue
    elif key == "q":
        print("終了しました。")
        break
    try:
        value = fruit.pop(key)
        print(f"{key}は{value}個")
    except KeyError:
        print(f"{key}はありません。")
    except Exception as error:
        print(error)
        beak
else:
    print("もう空っぽです。")
