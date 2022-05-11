# lambdaを使ってarea(w,h)と同じ機能の関数オブジェクトを作る
func = lambda w, h: w * h
# w, h   式の引数、w,* h   計算する式
num = func(3, 4)
print(num)
