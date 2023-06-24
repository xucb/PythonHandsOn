
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
        while time<=4:
            lucky_content= choice(self.contents)
            lucky_contents.append(lucky_content)
            #print(f"第{time}位中奖号码是{lucky_content}.")
            time +=1

#        for lucky_content in lucky_contents[:]:
#            print(f"中奖号码是{lucky_content}")
        #print(f"中奖号码是{lucky_contents}")
        return lucky_contents

def my_ticket():
    """每次购买彩票的号码"""    
    time = 1
    my_tickets=[]
    my_ticket =''
    while time<=4:
        my_ticket = choice(my_lottery.contents)
        my_tickets.append(my_ticket)
#        print(f"你购买的彩票第{time}位号码是{my_ticket}.")
        time +=1
    return my_tickets


my_lottery = Lottery()
print("中奖号码是：")
print(my_lottery.lucky_contents())
print(my_ticket())





cycle_time = 0
while my_lottery.lucky_contents() == my_ticket():
    print(f"你中奖了！！！，这是第{cycle_time}次循环。")
    my_ticket()
    cycle_time +=1

