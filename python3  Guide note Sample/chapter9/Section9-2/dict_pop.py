# fruits辞書から指定のフルーツを取り出す
fruits = {"apple": 7, "orange": 5, "mango": 3, "peach": 6}
while fruits:      # fruitsが空でなければ繰り返す
    key = input("どのフルーツを取り出しますか？(qで終了):")
    if key == "":    # 何もタイプされずに入力された時は続行する
        continue
    elif key == "q":
        print("終了しました。")
        break
    try:
        value = fruits.pop(key)    # keyの値を取り出して要素を削除する
        print(f"{key}は{value}個")    # 取り出した値とキーを表示
    except KeyError:    # 入力されたキーが辞書になったらメッセージを表示
        print(f"{key}はありません。")
    except Exception as error:
        print(error)
        break
else:         # whileループの終了後に実行   fruitsがあ空になるとループは正常に終了
    print("もう空っぽです。")

