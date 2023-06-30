#Generating a random code 
#By @ammmerzougui

import random

def genCode(length):
	s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
	a=random.sample(s,length)
	print(a)
	return "".join(a)
   
l=input("Enter the length of the random code: ")
print(genCode(int(l)))

s=[[i for i in range(3)] for j in range(4)]
print(s)

