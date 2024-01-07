from turtle import *
#get the instance of turtle
t=Turtle()
#select color
t.color('#4285F4','#4285F4') ## RBG value of color
#change the pen size
t.pensize(5)
#change the drawing speed
t.speed(3)

t.forward(120)
t.right(90)
t.circle(-150,50)  ## first circle for red color
t.color('#0F9D58')
t.circle(-150,100)
t.color('#F4B400')
t.circle(-150,60)
t.color('#DB4437','#DB4437')

t.begin_fill()
t.circle(-150,100)
t.right(90)
t.forward(50)
t.right(90)
t.circle(100,100)
t.right(90)
t.forward(50)
t.end_fill()

t.begin_fill()

## second circle for yellow color

t.color("#F4B400","#F4B400")
t.right(180)
t.forward(50)
t.right(90)

t.circle(100,60)
t.right(90)
t.forward(50)
t.right(90)
t.circle(-150,60)
t.end_fill()


# third circle of green color
t.right(90)
t.forward(50)
t.right(90)
t.circle(100,60)
t.color('#0F9D58','#0F9D58')
t.begin_fill()
t.circle(100,100)
t.right(90)
t.forward(50)
t.right(90)
t.circle(-150,100)
t.right(90)
t.forward(50)
t.end_fill()


##Draw last circle

t.right(90)
t.circle(100,100)
t.color('#4285F4','#4285F4')
t.begin_fill()
t.circle(100,25)
t.left(115)
t.forward(65)
t.right(90)
t.forward(42)
t.right(90)
t.forward(124)
t.right(90)
t.circle(-150,50)
t.right(90)
t.forward(50)

t.end_fill()
t.penup()


    
    
   