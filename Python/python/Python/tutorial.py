# from turtle import*
# import colorsys
# bgcolor('black')
# tracer(10)
# pensize(5)
# h=0
# for i in range(300):
#     c= colorsys.hsv_to_rgb(h,1,1)
#     h += 3.140
#     pencolor(c)
#     fillcolor('black')
#     begin_fill()
#     for j in range(2):
#        fd(i*1.2)
#        rt(100)
#        fd(350)
#        rt(123)
#     rt(121)
#     end_fill()
# done()

from turtle import *
from time import sleep

bgcolor("black")
t = [Turtle(), Turtle()]
x = 6
colors = ["red", "yellow", "blue", "lime"]
for index, i in enumerate(t):
    i.speed(0)
    i.color("white")
    i.shapesize(0.3)
    i.width(3)
    i.pu()
    i.seth(90)
    i.fd(350)
    i.seth(-180)
    i.pd()
t[0].pu()

delay(0)
speed(0)
ht()
sleep(4)
for i in colors:
    color(i)
    for i in range(360):
        t[0].fd[x]
        t[0].lt(1)
        pu()
        goto(t[0].pos())
        pd()
        t[1].fd[2 * x]
        t[1].lt(2)
        goto(t[1].pos())
done()

























