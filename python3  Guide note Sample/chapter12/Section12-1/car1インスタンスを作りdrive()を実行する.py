# car1インスタンスを作りdrive()を実行する
from car_class2 import Car
car1 = Car()    # car1インスタンスを作る
print(car1.drive(15))    # car1に対してインスタンスメゾットdrive()を実行
print(car1.drive(20))    # 総距離が加算されている
