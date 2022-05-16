import re


sentence = """\
    電話番号は0120-0000-0000だったかな
    あっ、でも0120-0-0000かも
    いやいや確か0120-000-0000だった\
    """
pattern = "0120-[0-9]{2, 4}-[0-9]{4}"
match = re.search(pattern, sentence)
print("【文字列】\n" + sentence)
print("【正規表現】\n" + pattern + "\n 【結果】")
if match is not None:
    print("group():{0}".format(match.group()))
    print("start():{0}".format(match.start()))
    print("end():{0}".format(match.end()))
    print("span():{0}".format(match.span()))
else:
    print("正規表現と一致しませんでした")
