# average()だけで呼び出せるようにインポートする
from mylib.judgement import average    # average()だけで呼び出せるようにする
# mylib.judgement   パッケージ.モジュールで指定する

result = average(56, 67, 46, 81, 76)    # average())だけで呼び出せる
print(result)
