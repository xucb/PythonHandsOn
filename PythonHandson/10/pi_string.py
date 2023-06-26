"""

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
#    pi_string += line.rstrip() #只删除了右边的空格
    pi_string +=line.strip() #删除了全部空格
print(pi_string)
print(len(pi_string))

"""

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
#    pi_string += line.rstrip() #只删除了右边的空格
    pi_string +=line.strip() #删除了全部空格

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
    print(f"It appears from {pi_string.find(birthday)}th.")
else:
    print("Your birthday does not appear in the first million digits of pi.")


print(f"{pi_string[:55]}...")
print(len(pi_string))
