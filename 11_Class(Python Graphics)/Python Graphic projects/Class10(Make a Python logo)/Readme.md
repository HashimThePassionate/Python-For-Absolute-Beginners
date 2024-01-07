## Code structure
 ```python
    from turtle import *

t = Turtle()
s = Screen()
s.bgcolor("black")
t.speed(10)
t.pensize(2)
t.pencolor("white")



def s_curve():
    for i in range(90):
        t.left(1)
        t.forward(1)

def r_curve():
    for i in range(90):
        t.right(1)
        t.forward(1)

def l_curve():
    s_curve()
    t.forward(80)
    s_curve()

def l_curve1():
    s_curve()
    t.forward(90)
    s_curve()

def half():
    t.forward(50)
    s_curve()
    t.forward(90)
    l_curve()
    t.forward(40)
    t.left(90)
    t.forward(80)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(120) #on test
    l_curve1()
    t.forward(30)
    t.left(90)
    t.forward(50)
    r_curve()
    t.forward(40)
    t.end_fill()

def get_pos():
    t.penup()
    t.forward(20)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.pendown()

def eye():
    t.penup()
    t.right(90)
    t.forward(160)
    t.left(90)
    t.forward(70)
    t.pencolor("black")
    t.dot(35)

def sec_dot():
    t.left(90)
    t.penup()
    t.forward(310)
    t.left(90)
    t.forward(120)
    t.pendown()

    t.dot(35)




t.fillcolor("#306998")
t.begin_fill()
half()
t.end_fill()
get_pos()
t.fillcolor("#FFD43B")
t.begin_fill()
half()
t.end_fill()

eye()
sec_dot()



def pause():
    t.speed(2)
    for i in range(100):
        t.left(90)
pause()


 
   ``` 
    
   # Explaination:

Here's a breakdown of the code's details:

Import and Setup:

Imports the turtle module: from turtle import *
Creates a turtle object and screen: t = Turtle(), s = Screen()
Sets background color to black: s.bgcolor("black")
Adjusts turtle speed and pen properties: t.speed(10), t.pensize(2), t.pencolor("white")
Curve Functions:

s_curve(): Creates a left-turning curve using a loop of small turns and forward steps.
r_curve(): Creates a right-turning curve using a similar loop.
l_curve(), l_curve1(): Combine s_curve() with forward movement for longer curves.
Half-Shape Drawing:

half(): Draws one half of the overall shape using s_curve(), l_curve(), forward movements, and turns.
Positioning and Filling:

get_pos(): Moves the turtle to the starting position for drawing the second half.
t.fillcolor("#306998"): Sets fill color to blue for the first half.
t.begin_fill(), half(), t.end_fill(): Draws and fills the first half.
t.fillcolor("#FFD43B"): Sets fill color to yellow for the second half.
t.begin_fill(), half(), t.end_fill(): Draws and fills the second half.
Eye and Dot:

eye(): Positions the turtle and draws a black dot as the eye.
sec_dot(): Positions the turtle and draws another black dot at a different location.
Pause:

pause(): Creates a visually appealing animation by repeatedly turning the turtle.
Key Points:

The code uses functions to create reusable blocks of code, making it more organized and readable.
It employs the turtle library's basic drawing commands and fill functions to create the shape.
It breaks down complex shapes into smaller, simpler curves for easier drawing.
It demonstrates basic animation techniques with the pause() function.
