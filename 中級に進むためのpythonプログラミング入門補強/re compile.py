import re


sentence = """\
    電話番号は0120-0000-0000だったかな
    あっ、でも0120-0-0000かも
    いやいや確か0120-000-0000だった\
    """
pattern = "0120-[0-9]{2,4}-[0-9]{4}"
re_comp = re.compile(pattern)


match_list = re_comp.findall(sentence)
print("【文字列】\n" + sentence)
print("【正規表現】\n" + pattern + "\n【結果】")
if len(match_list) > 0:
    for match_str in match_list:
        print(match_str)
else:
    print("正規表現と一致しませんでした")
