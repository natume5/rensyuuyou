# ジェネレータ関数を使って単語当てクイズを作る


def word_quiz(word):    # word_quizジェネレータの定義
    hint = ""
    for letter in word:    # 引数で受け取った文字列から1文字ずつ取り出す
        hint += letter    # 先に取り出した文字に連結していく
        yield hint    # ヒントを返す
        # yield   これまでに取り出した分を次の値として返す

# 出題する
ans = "Python"    # 正解
quiz = word_quiz(ans)    # ジェネレータを作る
while True:
    try:
        hint = next(quiz)    # ヒントを取り出す
        print(hint)
        word = input("この単語は何？:")
        if ans.lower() == word.lower():    # 大文字小文字を区別しないで比較
            point = len(ans) - len(hint)
            print(f"正解です！得点:{point}")
            break
        else:
            print("違います。")
    except:
        print("終了。得点:0")
        break
