import re


sentence = """\
    電話番号は0120-0000-0000だったかな
    あっ、でも0120-0-0000かも
    いやいや確か0120-000-0000だった\
    """
pattern = "0120-[0-9]{2,4}-[0-9]{4}"
re_comp = re.compile(pattern)

rep_word = "[フリーダイヤル]"

res = re.sub(pattern, rep_word, sentence)
print("【文字列】\n" + sentence)
print("【正規表現】\n" + pattern)
print("【置換文字列】\n" + rep_word + "\n【結果】")


print(res)
