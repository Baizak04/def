import turtle
pen = turtle.Turtle()
pen.speed(10)
pen.up()
pen.setposition(-100,-100)
pen.down()

def rightMNOG(n,dlina):
    sumAngle = (n-2)*180
    if sumAngle%n==0:
        baizak = sumAngle//n
        for i in range(n):
            pen.forward(100)
            pen.left(180-baizak)

for i in range(3,11):
    rightMNOG(i,50)
