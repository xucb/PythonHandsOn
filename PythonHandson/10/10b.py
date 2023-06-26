#10-3

guest = input("Hi, please enter your name: ")
filename = 'guest.txt'
with open(filename,'w') as file_object:
    file_object.write(guest)
	
	
#10-4
filename = 'guest_book.txt'
prompt = "\nTell me your name,"
prompt +="\nEnter 'q' to end the program: "
while True:
    guest=input(prompt)                
    if guest == 'q':
        break
    else:
        print(f'Welcome, {guest}!')
        with open(filename,'a') as file_object:
            file_object.write(f"{guest}\n")

    