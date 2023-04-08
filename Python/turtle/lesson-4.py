import turtle, random, time
def starFill(n,dlina):
    bai.left(random.randint(10,350))
    bai.begin_fill()
    if n % 2!=0:
        for i in range(n):
            bai.forward(dlina)
            angle = n // 2 * 360 / n
            bai.left(angle)
    bai.end_fill()
window = turtle.Screen()
window.bgcolor('black')
window.setup(700,500)

bai = turtle.Turtle()
bai.speed(0)
bai.color('yellow')
bai.hideturtle()
for i in range(6):
    x = random.randint(-320,320)
    y = random.randint(-220,220)
    bai.up()
    bai.setposition(x,y)
    bai.down()
    siz = random.randint(10,20)
    vershina = random.choice([5,7,9,11,13,15])
    starFill(vershina,siz)
def move(x,y):
    bai.up()
    bai.setposition(x,y)
    bai.down()
    siz = random.randint(10,20)
    vershina = random.choice([5,7,9])
    starFill(vershina,siz)
window.onclick(move)
window.listen()
window.mainloop()
# 2)

# import turtle as t
# import time
# t.pen()
# t.bgcolor("black")
# colors = ["red", "green", "yellow", "blue", "gray", "purple", "aqua", "brown"]
# name =t.textinput("Введите  ваше имя:", "Введите  ваше имя:")
# s=int(t.numinput("количество сторон","сколько сторон вы хотите(1-20)", 10,1,20))
# for i in range(100):
#     t.pencolor(colors[i%s%10])
#     t.penup()
#     t.forward(i*5)
#     t.pendown()
#     t.write(name, font=("", int((i*2+4)/4),"bold"))
#     t.left(360/s+4)

# time.sleep(2)





# # import turtle
# # import random
# # colors=['blue' , 'red', 'orange', 'purple']
 
# # def cpolygon(n, size, colors):
# #     angle = 360/n
# #     for i in range(n):
# #         turtle.pencolor(random.choice(colors)) 
# #         turtle.forward(100)
# #         turtle.left(angle)
# #     turtle.mainloop()
 
# # cpolygon(8, 100, colors)