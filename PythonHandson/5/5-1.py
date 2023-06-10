cars=['subaru','bmw','Audi']
car='sabaru'
if car =='sabaru':
    print (f"Is car=='subaru'? I predict True.")
    print(f"car == {car}")
else:
    print (f"no, it is {car}")

alien_color='green'
if alien_color == 'green':
    print("your score is 5!")

alien_color="yellow"
if alien_color=='green':
    print("your score is 5")
else:
    print("the color is not green, you don't have score!")


alien_color = 'yellow'
if alien_color =='green':
    print("your score is 5") 
else:
    print("your score is 10")   


alien_colors=['green','yellow','red']
alien_color = "red"

if alien_color =="green":
    score=5
elif alien_color=="yellow":
    score=10
elif alien_color=="red":
    score=15
else:
    score = 0
print(f"alien_color is {alien_color}, your score is {score}")

age=3.5
if age <2:
    print(f"your age is {age}, you are infant!")
elif age>=2 and age<4:
    print(f"your age is {age}, you are kid!")
else:
    print(f"your age is {age}, you are old enough!")


fruits=['a','b','c']
if 'a' in fruits:
    print(f"you really like a!")
if 'd' in fruits:
    print ("you really like d!")
if 'b' in fruits:
    print(f"you really like b!")
if 'c' in fruits:
    print(f"you really like c!") 