#7-1
lease_car=input("Which brand of car you want to lease? ")
print(f"Let me see if I can find you a {lease_car}.")

#7-2
order_seats=input("How many seats do you want to order? ")
order_seats=int(order_seats)
if order_seats>8:
    print(f"Sorry, we don't have enough seats.")
else:
    print(f"Welcome!")

#7-3
number_10 = input("输入一个数，我可以判断它是不是10的整数倍：")
number_10=int(number_10)  
if number_10 % 10 == 0:
    print (f"数字{number_10}是10的整数倍。")
else:
    print(f"数字{number_10}不是10的整数倍。")