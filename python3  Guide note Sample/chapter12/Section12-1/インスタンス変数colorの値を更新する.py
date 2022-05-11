# インスタンス変数colorの値を更新する


from car_class1 import Car
car1 = Car()
car2 = Car("red")
print(car1.color)    # 初期値の"white"が設定されている
print(car1.mileage)

# Car("red")で作ったcar2のインスタンス変数の値
print(car2.color)    # 引数で指定した"red"が設定されている
print(car2.mileage)

print(car1.color)    # colorには"white"が設定されている
car1.color = "green"    # "green"に設定し直す
print(car1.color)
