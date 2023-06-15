#8-3
def make_shirt(size,print_message):
    """size and printing message on T-shirt"""
    print(f"The T-shirt is a size of {size} with message '{print_message}'.")

make_shirt(6,'I love China')
make_shirt(print_message='I love DG',size=7)

#8-4
def make_shirt(size,print_message='I love Python'):
    """size and printing message on T-shirt"""
    print(f"The T-shirt is a size of {size} with message '{print_message}'.")

make_shirt(6)
make_shirt(print_message='I love DG',size=7)

#8-5
def describe_city(city,province='GD'):
    """the city in province"""
    print(f"{city} is in {province}.")

describe_city('dongguan')
describe_city(city='foshan')
describe_city(city='wuhan',province='hubei')
