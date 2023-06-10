#5-8,5-9
available_users=['a','b','admin','c','d']
login_user =['b']
if login_user :
    for user in login_user:
        if user == 'admin':
            print(f"Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print(f"We need to find some users!")    

#5-10
current_users=['a','b','admin','c','d']
new_users = ['c','f','g','A','h']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"the name {new_user} was occupied, please choose another name.")
    else:
        print(f"name {new_user} is available.")

#5-11
number_lists=[1,2,3,4,5,6,7,8,9]
for number in number_lists:
    if number==1:
        print("1st")
    elif number==2:
        print("2nd")
    elif number==3:
        print("3rd")
    else:
        print(f"{number}th")
print("all listed")