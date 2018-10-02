#DayDayupQ2.py 
dayfactory = 0.01
daydayup = pow(1+dayfactory,365)
daydaydown= pow(1-dayfactory,365)
print ("UP:{:.2f}, DOWN:{:.2f}".format(daydayup,daydaydown))

