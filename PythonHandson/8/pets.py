
#位置实参
def describe_pet(animal_type,pet_name):
    """Display pets information"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog','willie')


#关键字实参
def describe_pet(animal_type,pet_name):
    """Display pets information"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry',animal_type='hamster')

#默认值
# def describe_pet(animal_type='dog',pet_name): <-- This is wrong, becaues the first parameter has default value
def describe_pet(pet_name,animal_type='dog'):  #<-- This is the correct sequ.
    """Display pets information"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry')
describe_pet(pet_name='willie',animal_type='cat')
# 使用默认值时，必须先在形参列表中列出没有默认值的形参，再列出有默认值的实参。这让Python依然能够正确地解读位置实参
