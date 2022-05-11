# インスタンス変数milageの値を更新する


from car_class1 import Car
car1 = Car()
car2 = Car("red")

print(car1.mileage)     # mileageの現在の値は45
car1.mileage = 45    # 45に設定
print(car1.mileage)     # mileageの現在の値は45
car1.mileage = 100    # 100に設定
print(car1.mileage)     # 100になっている
