## Code structure
```python
from turtle import *

bat = Turtle()


bat.turtlesize(1, 1, 1)
bat.pensize(3)


wn = Screen()
wn.bgcolor("white")
wn.title("BATMAN")


bat.color("yellow", "black")


bat.begin_fill()

bat.left(90)   
bat.circle(50, 85) 
bat.circle(15, 110)
bat.right(180)

bat.circle(30, 150)
bat.right(5)
bat.forward(10) #draw forward line of 10 units

bat.right(90)
bat.circle(-70, 140)
bat.forward(40)
bat.right(110)

bat.circle(100, 30)
bat.circle(30, 100)
bat.left(50)
bat.forward(50)
bat.right(145)

bat.forward(30)
bat.left(55)
bat.forward(10)


bat.forward(10)
bat.left(55)
bat.forward(30)


bat.right(145)
bat.forward(50)
bat.left(50)
bat.circle(30, 100)
bat.circle(100, 30)

bat.right(90)
bat.right(20)
bat.forward(40)
bat.circle(-70, 140)

bat.right(90)
bat.forward(10)
bat.right(5)
bat.circle(30, 150)

bat.left(180)
bat.circle(15, 110)
bat.circle(50, 85)

bat.end_fill()

done()
```
# Explaination:


## 1. Import and Setup:

Imports the turtle module: from turtle import *
Creates a turtle object: bat = Turtle()
Sets turtle size and pen size: bat.turtlesize(1, 1, 1), bat.pensize(3)
Creates and customizes the screen: wn = Screen(), wn.bgcolor("white"), wn.title("BATMAN")
Sets turtle color: bat.color("yellow", "black") (outline: yellow, fill: black)
## 2. Drawing the Batman Logo:

Begins fill: bat.begin_fill()
Turn 1:
Rotates left 90 degrees: bat.left(90)
Draws two circles: bat.circle(50, 85), bat.circle(15, 110)
Rotates right 180 degrees: bat.right(180)
Turn 2:
Draws a circle and moves forward: bat.circle(30, 150), bat.right(5), bat.forward(10)
Turn 3:
Draws a circle and moves forward: bat.right(90), bat.circle(-70, 140), bat.forward(40)
Rotates right 110 degrees: bat.right(110)
Turn 4:
Draws two circles, moves forward, and rotates: bat.circle(100, 30), bat.circle(30, 100), bat.left(50), bat.forward(50), bat.right(145)
Turn 5:
Moves forward and turns: bat.forward(30), bat.left(55), bat.forward(10)
Reverse (repeating steps for symmetry):
... (same commands as Turn 4 and Turn 5, but in reverse order)
End fill: bat.end_fill()
Keeps the window open: done()
## 3.Key Points:

- The code leverages the turtle library for simple visual drawing.
- It uses basic turtle commands like forward, left, right, and circle to create shapes.
- The begin_fill() and end_fill() functions enable filling shapes with color.
- The code carefully coordinates turns and movements to construct the Batman logo's recognizable shape.
- By reversing the steps, it ensures symmetry in the final drawing.