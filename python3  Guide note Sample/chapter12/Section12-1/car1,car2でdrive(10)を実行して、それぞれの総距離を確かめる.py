# car1,car2でdrive(10)を実行して、それぞれの総距離を確かめる
from car_class2 import Car
car1 = Car()
car2 = Car("red")    # car2インスタンスを作る
print(car1.drive(15))    # car1に対してインスタンスメゾットdrive()を実行
print(car1.drive(20))    # 総距離が加算されている
print(car2.drive(10))    # car2に対してインスタンスメゾットdrive()を実行
# car1とcar2では総距離が個別に保持される
print(car1.drive(10))
