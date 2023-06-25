#9-13 骰子

from random import randint

class Die:
    """一个简单的骰子类"""
    def __init__(self,sides=6):
        """包含6面的骰子"""
        self.sides = sides

    def roll_die(self):
        """掷出骰子"""
        times = 1
        while times <= 10:
            print(f"这是第{times}次,本次掷出结果是{randint(1,self.sides)}.")
            times +=1

my_die = Die(20)
print(f"骰子有{my_die.sides}面.\n")
my_die.roll_die()

#9-14
from random import choice

class Lottery:
    """一个彩票类"""
    def __init__(self,contents=['1','2','3','4','5','6','7','8','9','0','a','b','c','d']):
        """彩票的组成"""
        self.contents = contents

    def lucky_contents(self):
        """中奖的彩票号码"""
        time = 1
        lucky_contents=[]
        while time<=4:
            lucky_content= choice(self.contents)
            lucky_contents.append(lucky_content)
            print(f"第{time}位中奖号码是{lucky_content}.")
            time +=1

#        for lucky_content in lucky_contents[:]:
#            print(f"中奖号码是{lucky_content}")
        print(f"中奖号码是{lucky_contents}")
        return lucky_contents
    
my_lottery = Lottery()
my_lottery.lucky_contents()

 


#9-15
from random import choice

class Lottery:
    """一个彩票类"""
    def __init__(self,contents=['1','2','3','4','5','6','7','8','9','0','a','b','c','d']):
        """彩票的组成"""
        self.contents = contents

    def lucky_contents(self):
        """中奖的彩票号码"""
        time = 1
        lucky_contents=[]
        while time<=5:
            lucky_content= choice(self.contents)
            lucky_contents.append(lucky_content)
            #print(f"第{time}位中奖号码是{lucky_content}.")
            time +=1

#        for lucky_content in lucky_contents[:]:
#            print(f"中奖号码是{lucky_content}")
        #print(f"中奖号码是{lucky_contents}")
        return lucky_contents


my_lottery = Lottery()
print("中奖号码是：")
lucky_number = my_lottery.lucky_contents()[:]
print(lucky_number)
#print(my_ticket())


my_last_ticket=[] 
cycle_time = 0

while True:
    my_last_ticket=my_lottery.lucky_contents()[:]
    cycle_time +=1
    if lucky_number==my_last_ticket:
        break
   
    
print(f"lucky number is {lucky_number}, your ticket number is {my_last_ticket}")

print(f"你中奖了！！！，这是第{cycle_time}次循环。")
