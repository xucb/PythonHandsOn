def greet_users(names):
    """send simple hello to each user in list"""
    for name in names:
        msg=f"Hello, {name.title()}!"
        print (msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)