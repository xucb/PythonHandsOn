
#10-7
def input_number():
    """用户输入数字"""
    a=0
    while True:
        usernumber = input('Please enter a number: ')
        try:
            usernumber = int(usernumber)
            break
        except ValueError:
            print(f"This is not a valid number, please input a valid number.")
#            continue
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


#10-8 Cat and Dog
filenames = ['cat.txt','dog.txt']

for filename in filenames:
    try:
        with open(filename,encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        print(f"The file {filename} is:")
        print(contents)
#        print('\n')


#10-9 Slient Cat and Dog
filenames = ['cat.txt','dog.txt']

for filename in filenames:
    try:
        with open(filename,encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f"The file {filename} is:")
        print(contents)
#        print('\n')


#10-10 Count words


def count_word(contents,word):
    """计算一个单词在文章中出现了多少次"""
    word_repeat=contents.count(word)
    return word_repeat

filename = 'alice.txt'
with open (filename,encoding='utf-8') as f:
    contents = f.read().lower()

word = input("The word you want to count is:")
word_repeat= count_word(contents,word.lower())
print(f"The word {word} in file {filename} appears {word_repeat} times.")
