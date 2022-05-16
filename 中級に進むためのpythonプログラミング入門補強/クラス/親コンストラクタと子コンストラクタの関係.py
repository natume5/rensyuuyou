class ParrentClass:
    parent_static_val =  "親の静的変数"
    def __init__(self, parent_self_val = "親のインスタンス変数"):
        print("親のコンストラクタ")
        self.parent_self_val = parent_self_val
        self.__pri_val = pri_val
    def func_parent(self):
        print("親のメゾット")
    # ()内にParentClassと書き継承する
    class ChildClass(ParentClass):
        child_static_val = "子の静的変数"
        def __init__(self, child_self_val = "子のインスタンス変数")

test = Test()
print(test.pub_val)

print(test.get_pri_val())
test.set_pri_val("PRI")
print(test.get_pri_val())

