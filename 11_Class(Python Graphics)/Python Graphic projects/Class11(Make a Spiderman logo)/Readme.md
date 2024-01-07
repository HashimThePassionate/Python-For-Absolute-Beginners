## Code structure
```python
    
from time import  *
from turtle import *
bgcolor('red')
pensize(10)
fillcolor('black')
begin_fill()
circle(20)
end_fill()
penup()
right(90)
forward(5)
pendown()
fillcolor('black')
begin_fill()
right(60)
for i in range(6):
    forward(50)
    left(60)
end_fill()
penup()
left(150)
forward(39)
left(90)
forward(9)
pendown()
forward(25)
right(60)
forward(15)
left(60)
forward(25)
penup()
backward(25)
right(60)
back(15)
left(60)
backward(25)
left(60)
pendown()
backward(35)
left(120)
forward(80)
penup()
left(40)
forward(30)
left(140)
pendown()
forward(110)
left(60)
forward(40)
right(60)
forward(7)
right(60)
forward(20)
left(60)
forward(40)
penup()
goto(0,0)
left(90)
forward(39)
right(90)
forward(9)
pendown()
forward(25)
left(60)
forward(15)
right(60)
forward(25)
penup()
backward(25)
left(60)
back(15)
right(60)
backward(25)
right(60)
pendown()
backward(35)
right(120)
forward(80)
penup()
right(40)
forward(30)
right(140)
pendown()
forward(110)
right(60)
forward(40)
left(60)
forward(7)
left(60)
forward(20)
right(60)
forward(40)
sleep(30)
done()






   ``` 
    
   # Explaination:
 
## 1. Imports:

- from time import *: Imports the time module for pausing the execution later.
- from turtle import *: Imports the turtle module for drawing graphics.
## 2. Background and Head:

- bgcolor('red'): Sets the background color to red.
- pensize(10): Sets the pen thickness to 10 pixels.
- fillcolor('black'): Sets the fill color to black.
- begin_fill(): Starts a filled shape.
- circle(20): Draws a black circle with a radius of 20 pixels (the head).
- end_fill(): Ends the filled shape.
## 3. Body:

- penup(): Lifts the pen to move without drawing.
- right(90), forward(5): Moves the turtle slightly to the right and up.
- pendown(): Puts the pen down to start drawing again.
- fillcolor('black'): Sets the fill color to black again.
- begin_fill(): Starts another filled shape.
- right(60): Turns the turtle 60 degrees right.
- for i in range(6): ...: Repeats the following code 6 times:
- forward(50): Draws a side of the body.
- left(60): Turns 60 degrees left to prepare for the next side.
- end_fill(): Ends the filled shape, completing the hexagonal body.
## 4. Left Arm:

- penup(), left(150), forward(39), left(90), forward(9): Positions the turtle for drawing the left arm.
- pendown(): Starts drawing.
A series of forward, right, left, and backward movements create the arm's shape.
## 5. Left Hand:

- More movements draw the fingers and hand.
## 6. Right Arm and Hand:

Similar code blocks, positioned differently, create the right arm and hand.
## 7. Pause and Exit:

- sleep(30): Pauses the execution for 30 seconds.
- done(): Keeps the turtle graphics window open until it's closed manually.
## 8. Key Points:

- The code uses basic turtle commands to draw a simple robot with a head, body, and arms.
- It employs the fill function to create solid shapes.
- The sleep() function pauses the drawing for a visual effect.



