"""
第一种导入类的方法
from car import Car, ElectricCar

my_beetle = Car('volkswagen','beetle',2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2020)
print(my_tesla.get_descriptive_name())

"""
"""导入整个模块"""
import car

my_beetle = car.Car('volkswagen','beetle',2019)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla','roadster',2020)
print(my_tesla.get_descriptive_name())


"""导入模块中的所有类，不推荐
from module_name import *
建议使用上述第二种方法
"""

