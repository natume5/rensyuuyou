class ParentClass:
    parent_static_val = "親の静的変数"
    def __init__(self, parent_self_val = "親のインスタンス変数"):
        print("親のコンストラクタ")
        self.parent_self_val = parent_self_val
    def func_parent(self):
        print("親のメゾット")
# ()内にParentClassと書き継承する
class ChildClass(ParentClass):
        child_static_val = "子の静的変数"
        def __init__(self, child_self_val = "子のインスタンス変数"):
            print("子のコンストラクタ")
            self.child_self_val = child_self_val
        def func_child(self):
            print("子のメゾット")


# ParentClassを継承しているChildClassのインスタンス
childClass = ChildClass()
print(ParentClass.parent_static_val)
print(ChildClass.child_static_val)
# メゾット
childClass.func_child()
# 親のクラスのメゾット
childClass.func_parent()
# 静的変数
print(childClass.child_static_val)
# 親クラスの静的変数
print(childClass.parent_static_val)
# インスタンス変数
print(childClass.child_self_val)
# 親クラスのインスタンス変数
print(childClass.parent_self_val)



