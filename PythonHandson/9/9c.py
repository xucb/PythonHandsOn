#9-6

class Restaurant:
    """describe a restaurant"""

    def __init__(self,name,cuisine_type):
        """restaurant name and type"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """restaurant info"""
        print(f"My restaurant name is {self.name} and cook food type is {self.cuisine_type}.")
        print(f"There are {self.number_served} been served.")

    def open_restaurant(self):
        """status of restaurant"""
        print(f"{self.name} is opening.\n")

    def set_number_served(self,numbers):
        """set number served """
        self.number_served = numbers

    def increment_number_served(self,increment_number):
        """increment number by each day"""
        self.number_served +=increment_number

class IceCreamStand(Restaurant):
    """icecream stand"""
    def __init__(self,name,cuisine_type):
        """icecream stand name and type"""
        super().__init__(name,cuisine_type)
        self.flavors = ['b','c','d']

    def display_icecream(self):
        """display the icecream flavors"""
        for flavor in self.flavors:
            print(f"We server below kinds of icecream {flavor}.")

my_restaurant = Restaurant('App','Chuan Food')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.number_served = 9
my_restaurant.describe_restaurant()

my_restaurant.set_number_served(100)
my_restaurant.describe_restaurant()

my_restaurant.increment_number_served(150)
my_restaurant.describe_restaurant()

my_icescreamstand = IceCreamStand('new ice cream','strange')
my_icescreamstand.describe_restaurant()
my_icescreamstand.open_restaurant()
my_icescreamstand.number_served = 99
my_icescreamstand.describe_restaurant()

my_icescreamstand.display_icecream()


#9-7
class User:
    """user class"""

    def __init__(self,first_name,last_name,age):
        """Users' attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """user's info"""
        print(f"The user is {self.first_name} {self.last_name} and is {self.age} years old.")

    def greet_user(self):
        """greeting"""
        if int(self.age) > 18:
            print(f"Hello, {self.first_name} {self.last_name}! you are older enough to vote.\n")
        else:
            print(f"Hello, {self.first_name} {self.last_name}! you are not older enough to vote.\n")
    
    def increment_login_attempts(self):
        """increase login attempts"""
        self.login_attempts +=1

    def reset_login_attempts(self):
        """reset login attempts to 0"""
        if self.login_attempts >=4:
            self.login_attempts = 0

class Admin(User):
    """describe admin rights"""
    def __init__(self,first_name,last_name,age):
        """Admin's attributes"""
        super().__init__(first_name,last_name,age)
        self.privileges = ['can add post','can delete post','can ban user']
    
    def show_privileges(self):
        """display admin's privileges"""
        for privilege in self.privileges:
            print(f"Admin {privilege}.")

first_user = User('Lucy', 'Wang',19)
second_user = User('William', 'Zhang',13)

first_user.describe_user()
first_user.greet_user()

print(first_user.login_attempts)
first_user.increment_login_attempts()

my_admin= Admin('bill','xu',55)
my_admin.describe_user()
my_admin.show_privileges()

#9-8
class User:
    """user class"""

    def __init__(self,first_name,last_name,age):
        """Users' attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """user's info"""
        print(f"The user is {self.first_name} {self.last_name} and is {self.age} years old.")

    def greet_user(self):
        """greeting"""
        if int(self.age) > 18:
            print(f"Hello, {self.first_name} {self.last_name}! you are older enough to vote.\n")
        else:
            print(f"Hello, {self.first_name} {self.last_name}! you are not older enough to vote.\n")
    
    def increment_login_attempts(self):
        """increase login attempts"""
        self.login_attempts +=1

    def reset_login_attempts(self):
        """reset login attempts to 0"""
        if self.login_attempts >=4:
            self.login_attempts = 0

class Privileges:
    """class of privileges"""
    def __init__(self,privileges=('can add user')):
        """initial privileges """
        self.privileges =  privileges
    
    def describe_privileges(self):
        """to describe admin privileges"""
        print(f"the privileges are {self.privileges}")


class Admin(User):
    """describe admin rights"""
    def __init__(self,first_name,last_name,age):
        """Admin's attributes"""
        super().__init__(first_name,last_name,age)
        self.privilege = Privileges()
    

my_admin= Admin('bill','xu',55)
my_admin.describe_user()
Privileges.describe_privileges()



#9-9
class Car:
    """一次模拟汽车的简单尝试。"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性。"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述信息。"""
        long_name=f"{self.year} {self.make} {self.model}"
 #       print(long_name.title())
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """
        将里程表读数设置为指定的值。
        禁止将里程表读数往回调。  
        """
        if mileage >=self.odometer_reading:
                self.odometer_reading = mileage
        else:
             print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
         """将里程表读数增加指定的量"""
         self.odometer_reading += miles

class Battery:
     """一次模拟电动汽车电瓶的简单尝试。"""

     def __init__(self,battery_size=75):
          """初始化电瓶的属性。"""
          self.battery_size = battery_size
     
     def describe_battery(self):
          """打印一条描述电瓶容量的消息"""
          print(f"This car has a {self.battery_size} - kwh battery.")

     def get_range(self):
          """打印一条消息，指出电瓶的续航里程"""
          if self.battery_size==75:
               range=260
          elif self.battery_size==100:
               range=315
          print(f"This car can go about {range} miles on a full charge.")

     def upgrade_battery(self):
          """给电池升级"""
          if self.battery_size <= 100:
               self.battery_size = 100

class ElectricCar(Car):
     """电动汽车的独特之处"""

     def __init__(self,make,model,year):
        """
        初始化父类的属性
        再初始化电动汽车特有的属性。
        """ 
        super().__init__(make,model,year)
  #      self.battery_size = 75
        self.battery = Battery()

  #   def describe_battery(self):
  #      """打印一条描述电瓶容量的消息"""
  #      print(f"This car has a {self.battery_size}-kwh battery.")
     

my_tesla = ElectricCar('tesla','model s',2019)

print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
