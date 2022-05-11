numbers = [21, 32, 43, 15, 5]

while True:
    answer = input("数字を入力するか、qで終了します。")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("数字入力を続けるか、qで終了します。")
    if answer in numbers:
        print("正解です！")
    else:
        print("間違いです！")
