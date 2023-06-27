
#10-7
def input_number():
    """用户输入数字"""
    while True:
        usernumber = input('Please enter a number, input "q" if you want to quit: ')
        if usernumber == 'q':
            break
        else:
            try:
                usernumber = int(usernumber)
            break
        except ValueError:
        print(f"This is not a valid number, please input a valid number.")
        continue
    return usernumber

times = 0
numbers =[]
while True:
    number = input_number()
    times +=1
    print (f"the {times} number is {number}.")
    numbers.append(number)
    if times ==2:
        break

sum = 0
for number in numbers:
    sum += int(number)
print(f"the sum of your inputer is {sum}.")



