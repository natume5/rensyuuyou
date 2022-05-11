# finallyブロックがあるtry文
num = 0      # numが0の場合の結果を確かめる
try:
    value = 120 / num       # numが0の時例外発生
    print(value)
except:
    print("エラーになりました。")
finally:
    print("計算終了。")     # 例外が発生してもしなくても最後に実行
