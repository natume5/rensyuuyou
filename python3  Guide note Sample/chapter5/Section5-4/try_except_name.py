# 例外の種類によって例外処理を振り分ける
sum = 7600
while True:
    num = input("何人ですか？(qで終了)")
    if num == "q":
        print("終了しました。")
        break
    # 例外を振り分けて例外処理を行う
    try:
        price = round(sum / int(num))     # この式が例外を発生する可能性がある
        if price < 0:
            # マイナスの場合は無視
            continue
        print("1人当たりの金額", price)
    except ValueError:      # 数値に変換できなかった時
        print("数値を入れてください。")
    except ZeroDivisionError:         # ゼロの割り算を行ったとき
        print("0以外の数値を入れてください。")
