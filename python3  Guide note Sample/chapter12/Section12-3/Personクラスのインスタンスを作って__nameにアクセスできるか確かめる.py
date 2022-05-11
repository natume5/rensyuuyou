# Personクラスのインスタンスを作って__nameにアクセスできるか確かめる
from person import Person

man = Person("宇佐美")
print(man.who())    # インスタンスメゾットを介して__nameの値を調べることはできる
man.__name    # 直接アクセスするとエラーになる
