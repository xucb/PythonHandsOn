#pySquare.py
import turtle as t
t.setup (650,350)
t.penup()
t.pensize(1)
t.pencolor("black")
t.goto(-100,-100)
t.pendown()
# 绝对角度
for i in range(4):
    t.fd(50)
    ### angle = 90*(i+1)
    t.seth(90*(i+1))  ###*i)
### t.done()

#相对角度
t.pencolor ("red")
for i in range(4):
    t.fd(100)
    t.left(90)

#六边形
t.pencolor (1,0.39,0.28)
t.penup()
t.goto(100,-110)
t.pendown()
for i in range(6):
    t.fd(100)
    t.left(60)


