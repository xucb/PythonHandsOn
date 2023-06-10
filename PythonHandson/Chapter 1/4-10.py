mylist = list(range(1,11))
print(mylist)

print(f"The first three items in the list are: {mylist[0:3]}")
print(f"Three itmes from the middel of the list are: {mylist[3:6]}")
print(f"The last three items in the list are: {mylist[-3:]}")


my_pizza=['abc','bcd','cde']
for name in my_pizza:
    print (f"I like {name} pizza.")
print("I really love pizza!")

print(f"\n\n")
friend_pizzas = my_pizza[:]

print(f"My favorite pizzas are: {my_pizza}")

friend_pizzas = my_pizza[:]
my_pizza.append('new_mypizza')
friend_pizzas.append('new_friendpizza')

print(f"my pizza are: ")
s=""
for v in my_pizza:
    s+=v+","
s=s[:-1]
print(f"my pizza are: {s}")


print(f"my friend pizza are:")
for pizza in friend_pizzas:
    print(pizza)

