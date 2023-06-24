#9-4

class Restaurant:
    """descript a restaurant"""

    def __init__(self,name,cuisine_type):
        """restaurant name and type"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """restaurant info"""
        print(f"My restauranta name is {self.name} and cook food type is {self.cuisine_type}.")
        print(f"There are {self.number_served} benn served.")

    def open_restaurant(self):
        """status of restaurant"""
        print(f"{self.name} is opening.\n")

    def set_number_served(self,numbers):
        """set number served """
        self.number_served = numbers

    def increment_number_served(self,increment_number):
        """increment number by each day"""
        self.number_served +=increment_number

my_restaurant = Restaurant('App','Chuan Food')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.number_served = 9
my_restaurant.describe_restaurant()

my_restaurant.set_number_served(100)
my_restaurant.describe_restaurant()

my_restaurant.increment_number_served(150)
my_restaurant.describe_restaurant()


#9-5

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

first_user = User('Lucy', 'Wang',19)
second_user = User('William', 'Zhang',13)

first_user.describe_user()
first_user.greet_user()

print(first_user.login_attempts)
first_user.increment_login_attempts()
print(first_user.login_attempts)
first_user.increment_login_attempts()
print(first_user.login_attempts)
first_user.increment_login_attempts()
print(first_user.login_attempts)
first_user.increment_login_attempts()
print(first_user.login_attempts)

first_user.reset_login_attempts()
print(first_user.login_attempts)
