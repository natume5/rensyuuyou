# 例外になったら、エラー情報を表示して処理を続行する
sum = 7600
while True:
    num = input("何人ですか？(qで終了)")
    if num == "q":
        print("修了しました。")
        break
    # 例外を処理する
    try:
        price = round(sum / int(num))
    except Exception as error:
        print("エラーになりました。")
        print(error)      # エラー情報を出力する
    else:
        if price < 0:
            # マイナスの場合は無視
            continue
        print("1人当たりの金額", price)
