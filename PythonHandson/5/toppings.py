requested_toppings=['a','b','c']
#requested_toppings=[]  #create an empty list 
if requested_toppings: #判断是否是空列表
    for requested_topping in requested_toppings:
        if requested_topping == 'b':
            print("Sorry, we are out of b right now.")
        else:
            print(f"Adding {requested_topping}")
    print("\nFinish make your pizza!")
else:
    print("Do you want a plain pizza?")



available_toppings = ['a','b','c','d','e','f']
requested_toppings = ['c','g','f']
for requestd_topping in requested_toppings:
    if requestd_topping in available_toppings:
        print(f"Adding {requestd_topping}")
    else:
        print(f"Sorry, we don't have {requestd_topping}")
print(f"\nFinished makeing your pizza!")