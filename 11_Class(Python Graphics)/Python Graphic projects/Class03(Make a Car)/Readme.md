## -Code structure

 ```python
# from turtle import *


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
```

Explaination :

## 1. Import Turtle Module:

- from turtle import *: Imports the turtle graphics library for drawing shapes and animations.
## 2. Create Turtle Object:

- myCar = Turtle(): Creates a turtle object named myCar, which will act as the "pen" to draw the car.
## 3. Draw Rectangular Upper Body:

### Set colors:
- myCar.color('black'): Sets the outline color of the car to black.
- myCar.fillcolor('yellow'): Sets the fill color of the car to yellow.
### Position the turtle:
- myCar.penup(): Lifts the pen so it doesn't draw while moving.
- myCar.goto(0, 0): Moves the turtle to the starting position (bottom-left corner of the car).
m- yCar.pendown(): Puts the pen down to start drawing.
### Draw the rectangle:
- myCar.begin_fill(): Starts filling the shape with the chosen fill color.
- myCar.forward(370), myCar.left(90), myCar.forward(50), etc.: These commands draw the four sides of the rectangle.
- myCar.end_fill(): Finishes filling the shape.
## 4. Draw Window and Roof:

### Position the turtle:
- myCar.penup(), myCar.goto(100, 50), myCar.pendown(), etc.: These commands move the turtle to the appropriate starting position for the window and roof.
### Draw the window and roof:
- myCar.setheading(45), myCar.forward(70), etc.: These commands draw the slanted lines for the window and the top of the roof.
- myCar.forward(49.50): Draws the horizontal line dividing the window.
## 5. Draw Tyres:

### Position the turtle and set colors:
- myCar.penup(), myCar.goto(100, -10), myCar.pendown(), etc.: Move the turtle to the positions for the two tyres.
- myCar.color('black'), myCar.fillcolor('black'): Set both outline and fill color to black for the tyres.
### Draw the tyres:
- myCar.begin_fill(), myCar.circle(20), myCar.end_fill(): These commands create two filled black circles for the tyres.
## 6. Hide Turtle and Keep Window Open:

- myCar.hideturtle(): Hides the turtle so it's not visible in the final drawing.
- done(): Keeps the turtle graphics window open until it's manually closed.
