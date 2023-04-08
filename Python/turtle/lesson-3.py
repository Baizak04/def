import turtle,time

bai=turtle.Turtle()

def startFill(n, dlina):
    bai.begin_fill()
    start(n,dlina)
    bai.end_fill()

def start(n,dlina):
    if n % 2 != 0:
        for i in range(n):
            bai.forward(100)
            asy = n//2 * 360 / n
            bai.left(asy)
for i in range(5,16,2):
    bai.speed(10)
    startFill(9,150)
    time.sleep(1)
    bai.reset()