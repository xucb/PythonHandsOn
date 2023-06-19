#9-1 and 9-2

class Restaurant:
    """descript a restaurant"""

    def __init__(self,name,cuisine_type):
        """restaurant name and type"""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """restaurant info"""
        print(f"My restauranta name is {self.name} and cook food type is {self.cuisine_type}.")
    
    def open_restaurant(self):
        """status of restaurant"""
        print(f"{self.name} is opening.")


my_restaurant = Restaurant('App','Chuan Food')
big_restaurant = Restaurant('BigRestaurant','YueFood')
small_restaurant = Restaurant('smallRestaurant','LuFood')

print(f"My restaurant is {my_restaurant.name}, the type is {my_restaurant.cuisine_type}.")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print(f"Big restaurant is {big_restaurant.name}, the type of it is {big_restaurant.cuisine_type}.")
big_restaurant.describe_restaurant()
big_restaurant.open_restaurant()


small_restaurant.describe_restaurant()
small_restaurant.open_restaurant()


#9-3

class User:
    """user class"""

    def __init__(self,first_name,last_name,age):
        """Users' attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        """user's info"""
        print(f"The user is {self.first_name} {self.last_name} and is {self.age} years old.")

    def greet_user(self):
        """greeting"""
        if int(self.age) > 18:
            print(f"Hello, {self.first_name} {self.last_name}! you are older enough to vote.\n")
        else:
            print(f"Hello, {self.first_name} {self.last_name}! you are not older enough to vote.\n")

first_user = User('Lucy', 'Wang',19)
second_user = User('William', 'Zhang',13)


first_user.describe_user()
first_user.greet_user()
second_user.describe_user()
second_user.greet_user()
