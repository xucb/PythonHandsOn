prompt = "\nTell me something, and I will repeat it back for you:"
prompt +="\nEnter 'quit' to end the program. "
message = ""
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print (message)