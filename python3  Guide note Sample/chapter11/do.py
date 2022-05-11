def do(funk):
    funk()


def thanks():
    print("ありがとう")


def hi():
    print("やあ！")


condition = 1
if condition == 1:
    do(thanks)
else:
    do(hi)
