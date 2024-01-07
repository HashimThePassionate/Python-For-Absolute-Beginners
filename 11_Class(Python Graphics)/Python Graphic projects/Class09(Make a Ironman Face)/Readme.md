## Code structure
    ```python
    from turtle import *

canvas1 = [[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10),
           (-40, -20), (0, -20)],
          [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),
           (40, 120), (0, 120)]]
canvas2 = [[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210),
           (-80, -230), (-64, -210), (0, -210)],
          [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40),
           (100, -46), (50, -40), (40, -30), (0, -30)]]
canvas3 = [[(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250),
           (0, -250)],
          [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240), (60, -220),
           (0, -220)]]

hideturtle()
bgcolor('#ba161e')  # Dark Red
setup(500, 600)
title("I AM IRONMAN")
canvas1Goto = (0, 120)
canvas2Goto = (0, -30)
canvas3Goto = (0, -220)
speed(2)


def logo(a, b):
    penup()
    goto(b)
    pendown()
    color('#fab104')  # Light Yellow
    begin_fill()

    for i in range(len(a[0])):
        x, y = a[0][i]
        goto(x, y)

    for i in range(len(a[1])):
        x, y = a[1][i]
        goto(x, y)
    end_fill()


logo(canvas1, canvas1Goto)
logo(canvas2, canvas2Goto)
logo(canvas3, canvas3Goto)
hideturtle()
done()


    
    
  
   ``` 
    
   # Explaination:
 
## 1. Import:

- nImports the turtle module for drawing graphics.
- Defines lists of coordinates (canvas1, canvas2, canvas3) representing shapes to be drawn.
## 2. Sets up the drawing environment:
- Hides the turtle cursor (hideturtle()).
- Sets background color to dark red (bgcolor('#ba161e')).
- Creates a 500x600 pixel window (setup(500, 600)).
- Sets the window title to "I AM IRONMAN" (title("I AM IRONMAN")).
- Defines starting positions for each shape (canvas1Goto, canvas2Goto, canvas3Goto).
- Sets turtle drawing speed to 2 (speed(2)).
## 3. Logo Drawing Function:

## 3. logo(a, b):
- Takes a list of coordinates (a) and a starting position (b) as input.
- Moves the turtle to the starting position without drawing (penup(), goto(b), pendown()).
- Sets the drawing color to light yellow (color('#fab104')).
- Begins filling the shape (begin_fill()).
- Iterates through the coordinates in a[0] and a[1], moving the turtle to each point (goto(x, y)).
- Ends filling the shape (end_fill()).
## 4. Main Execution:

- Calls the logo function to draw each shape: logo(canvas1, canvas1Goto), logo(canvas2, canvas2Goto), logo(canvas3, canvas3Goto).
- Hides the turtle cursor again (hideturtle()).
- Keeps the drawing window open until clicked (done()).
## 5. Key Points:

The code uses lists of coordinates to define shapes, making it easier to modify their appearance.
It employs a function (logo) to reuse the drawing logic for different shapes, promoting code organization.
The turtle library's basic commands (penup, pendown, goto, color, begin_fill, end_fill) are used to create and fill the shapes.
The code sets up a custom background color and title for the drawing window