#DayDayupQ4.py 工作日的努力
dayfactory_up = 0.01
dayfactory_down = 0.01
daydayup = 1
for i in range(365):
    if i%5 in [0,4]:
        daydayup = daydayup*(1-dayfactory_down)
    else :    
        daydayup = daydayup*(1+dayfactory_up)
print ("UP:{:.2f}".format(daydayup))



