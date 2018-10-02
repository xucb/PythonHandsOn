#DayDayupQ4.py 工作日的努力

def dayUP(df):
    dayup = 1
    for i in range (365):
        if i%7 in [6,0]:
            dayup = dayup*(1-0.01)
        else:
            dayup = dayup*(1+df)
    return dayup
dayfactory = 0.01
while dayUP(dayfactory)<37.78:
      dayfactory +=0.001
      print ("When day factory is: {:.3f}, the day up is {:.3f}".format(dayfactory,dayUP(dayfactory)))



