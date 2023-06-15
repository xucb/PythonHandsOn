# print number between 1 to 20

for mynumber in range(1,21):
    print(mynumber)

# create a list of 1-1000 , use for to print them
mylist=list(range(1,1_000_001))
#for value in mylist:
#    print (value)

print(f"The min of list mylist is: {min(mylist)}")
print(f"The max of list mylist is: {max(mylist)}")
print (f"The sum of list mylist is: {sum(mylist)}")


#odd number and even number
myoddnumber = list(range(1,20,2))
for value in myoddnumber:
    print (value)

for value in list(range(2,21,2)):
    print (value)

#3-30中3的整数倍
trinumber = list(range(3,30,3))
for value in list(trinumber):
    print (value)

#cube
number = list(range(1,11))
for value in number:
    print (value**3)

for value in list(range(1,11)):
    print (value**3)


cubenumber = [value**3 for value in range(1,11)]
print(cubenumber)