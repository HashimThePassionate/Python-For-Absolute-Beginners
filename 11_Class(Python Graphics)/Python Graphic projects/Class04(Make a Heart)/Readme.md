## Code structure
    ```python
    from turtle import *
wn = Screen()
wn.setup(width=400, height=400)
red = Turtle()

def curve():
    for i in range(200):
        red.right(1)
        red.forward(1)

def heart():
    red.fillcolor('red')
    red.begin_fill()
    red.left(140)
    red.forward(113)
    curve()
    red.left(120)
    curve()
    red.forward(112)
    red.end_fill()

heart()
red.ht()
done()


   ``` 
    
   # Explaination:
 
## 1. Import and Setup:

- Imports the turtle module: from turtle import *
- Creates a screen object: wn = Screen()
- Sets screen dimensions: wn.setup(width=400, height=400)
- Creates a turtle object: red = Turtle()
## 2. Curve Function:

- Defines a function curve() to create a curved path:
- Loop for 200 steps: for i in range(200):
- Turn right by 1 degree: red.right(1)
- Move forward by 1 unit: red.forward(1)
## 3. Heart Function:

### Defines a function heart() to draw a heart shape:
- Set fill color to red: red.fillcolor('red')
- Start filling: red.begin_fill()
- Turn left by 140 degrees: red.left(140)
- Move forward by 113 units: red.forward(113)
### Call the curve() function to create the first curve: curve()
### Turn left by 120 degrees: red.left(120)
### Call curve() again for the second curve: curve()
### Move forward by 112 units: red.forward(112)
### End filling: red.end_fill()
## 4. Main Execution:

- Calls the heart() function to draw the heart: heart()
- Hides the turtle: red.ht()
- Keeps the window open until closed manually: done()
## In summary, the code uses the turtle library to create a red heart shape on a 400x400 window. It does this by:

- Defining functions for drawing curves and the heart shape.
- Using basic turtle commands (forward, left, right, fillcolor, begin_fill, end_fill) to create the shape.
- Employing a loop to create smooth curves.