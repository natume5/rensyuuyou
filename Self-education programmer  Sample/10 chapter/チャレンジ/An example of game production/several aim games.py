import random
answer_num_ary = []


while len(answer_num_ary) < 4:
    # ランダムな4桁の数値を生成し、answer_num_aryに同じ値があれば
    # 追加しない。同じ値が無ければanswer_num_aryに追加する。
    random_num = random.randint(0, 9)
    append_flg = True   # answer_num_aryに追加するかのどうかのフラグ。
    # Trueならば追加しFalseなら追加しない

    for ary_element in answer_num_ary:
        if ary_element == random_num:
            append_flg = False   # すでに同じ値があるならappend_flgをFalseにする
            break
    if append_flg is True:
        answer_num_ary.append(random_num)
        append_flg = True

    print(answer_num_ary)
