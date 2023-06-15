def greet_user(username):
    """display a simple greeting"""
    print(f"Hello, {username.title()}!")

greet_user('bill')



def get_formatted_name(first_name,last_name):
    """return formatted name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("you may quit at any time if you input 'q'.\n")
    f_name = input("First Name: ")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name =='q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nHello, {formatted_name}!")    