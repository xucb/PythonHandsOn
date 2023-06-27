
#10-7
def input_number():
    """用户输入数字"""
    while True:
        usernumber = input('Please enter a number: ')
        try:
            usernumber = int(usernumber)
            break
        except ValueError:
            print(f"This is not a valid number, please input a valid number.")
        continue
    return usernumber

while True:
    number1 = input_number()
    number2 = input_number()
    print(f"{number1} + {number2} = {number1 + number2} \n") 
    print("Do you want to continue? Enter 'q' to quit.")
    again = input("")
    if again == 'q':
        break


"""
# 另外一种方式,复杂.
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
print(f"the sum of your input is {sum}.")
"""



