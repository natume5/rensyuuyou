"""2つのパラメーターを受け取る関数を書く。
この関数は、同じオブジェクトを渡されたらTrueを返し、
違ったらFalseを返す。"""


def compare(aly1, aly2):
    return aly1 is aly2


print(compare("a", "b"))
