from turtle import *


myCar = Turtle()


# code for drawing rectangular upper body
myCar.color('black')
myCar.fillcolor('yellow')
myCar.penup()
myCar.goto(0,0)
myCar.pendown()
myCar.begin_fill()
myCar.forward(370)
myCar.left(90)
myCar.forward(50)
myCar.left(90)
myCar.forward(370)
myCar.left(90)
myCar.forward(50)
myCar.end_fill()


# code for drawing window and roof
myCar.penup()
myCar.goto(100, 50)
myCar.pendown()
myCar.setheading(45)
myCar.forward(70)
myCar.setheading(0)
myCar.forward(100)
myCar.setheading(-45)
myCar.forward(70)
myCar.setheading(90)
myCar.penup()
myCar.goto(200, 50)
myCar.pendown()
myCar.forward(49.50)


# code for drawing two tyres
myCar.penup()
myCar.goto(100, -10)
myCar.pendown()
myCar.color('black')
myCar.fillcolor('black')
myCar.begin_fill()
myCar.circle(20)
myCar.end_fill()
myCar.penup()
myCar.goto(300, -10)
myCar.pendown()
myCar.color('black')
myCar.fillcolor('black')
myCar.begin_fill()
myCar.circle(20)
myCar.end_fill()


myCar.hideturtle()

done()





# ###### readme
