"""
#整个文件读取
file_path = 'C:\\Python\\PythonHandOn\\PythonHandson\\10\\pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip())
"""

"""
#一行行读取
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
"""

#读取到列表
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print(lines)

