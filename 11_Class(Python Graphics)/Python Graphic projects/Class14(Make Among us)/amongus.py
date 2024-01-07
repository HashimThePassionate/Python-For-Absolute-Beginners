from turtle import *

BODY_COLOR = 'red'
BODY_SHADOW = ''
GLASS_COLOR = 'grey'
GLASS_SHADOW = ''

s = getscreen()
tur = Turtle()

tur.speed(10)

def body():
    tur.pensize(20)
    tur.fillcolor(BODY_COLOR)
    tur.begin_fill()

    tur.right(90)
    tur.forward(50)
    tur.right(180)
    tur.circle(40, -180)
    tur.right(180)
    tur.forward(200)
    tur.right(180)
    tur.circle(100, -180)
    tur.backward(20)
    tur.left(15)
    tur.circle(500, -20)
    tur.backward(20)
    tur.circle(40, -180)
    tur.left(7)
    tur.backward(50)

    tur.up()
    tur.left(90)
    tur.forward(10)
    tur.right(90)
    tur.down()
    tur.right(240)
    tur.circle(50, -70)

    tur.end_fill()

def glass():
    tur.up()
    tur.right(230)
    tur.forward(100)
    tur.left(90)
    tur.forward(20)
    tur.right(90)
    tur.down()

    tur.fillcolor(GLASS_COLOR)
    tur.begin_fill()

    tur.right(150)
    tur.circle(90, -55)
    tur.right(180)
    tur.forward(1)
    tur.right(180)
    tur.circle(10, -65)
    tur.right(180)
    tur.forward(110)
    tur.right(180)
    tur.circle(50, -190)
    tur.right(170)
    tur.forward(80)
    tur.right(180)
    tur.circle(45, -30)

    tur.end_fill()

def backpack():
    tur.up()
    tur.right(60)
    tur.forward(100)
    tur.right(90)
    tur.forward(75)

    tur.fillcolor(BODY_COLOR)
    tur.begin_fill()

    tur.down()
    tur.forward(30)
    tur.right(255)
    tur.circle(300, -30)
    tur.right(260)
    tur.forward(30)

    tur.end_fill()

body()
glass()
backpack()
tur.screen.exitonclick()






