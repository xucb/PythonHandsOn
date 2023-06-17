#8-9
messages=['1st msg','2nd msg','3rd msg']

def show_messages(messages):
    """show message"""
    for message in messages:
        print (f"\nThe message is {message}")

show_messages(messages)

#8-10
# messages.reverse()
def send_messages(messages,sent_messages):
    """move to sent_messages list and print it"""
    while messages:
        send_message = messages.pop()
        sent_messages.append(send_message)
    
    for sent_message in sent_messages:
        print (f"\nThe message is {sent_message}!")

messages=['1st msg','2nd msg','3rd msg']
sent_messages=[]


send_messages(messages,sent_messages)
print (sent_messages)
print (messages)


#8-11
messages=['1st msg','2nd msg','3rd msg']
sent_messages=[]


def send_messages(messages,sent_messages):
    """move to sent_message list"""
    while messages:
        message= messages.pop()
        sent_messages.append(message)

def show_sent_messages(sent_messages):
    """print sent_message"""
    
    for sent_message in sent_messages:
        print(f"\nThe message is {sent_message}")
    

send_messages(messages[:],sent_messages)
show_sent_messages(sent_messages)
print(messages)
