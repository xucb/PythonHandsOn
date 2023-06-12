#7-4
prompt="Please let me know what do you need,"
prompt+="\nenter 'quit' when you finish.\n"
message = ""
while message !='quit':
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(f"ok, we will add {message}.")

#7-5
prompt="Please let me know your age:\n"
return_message = "please pay "
your_age =''
while  your_age!='quit':
    your_age = input(prompt)
    if your_age == 'quit':
        break
    else:
        your_age_number = int(your_age)
        if your_age_number < 3:
            fee = 0
        elif your_age_number >12:
            fee = 15
        else:
            fee = 10
    print(f"{return_message} {fee} dollar.")

#7-6

