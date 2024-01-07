

#                                                                Draw a Shape


### I'll break down the Python turtle code right(90) forward(100) left(90) backward(100) and explain what it does, accompanied by visuals:

### Code
```python
right(90)
forward(100)
left(90)
backward(100)
```
## Explaination

### 1. right(90):

- Turns the turtle 90 degrees to the right (clockwise).

### 2. forward(100):

- Moves the turtle forward 100 units in its current direction, drawing a line as it goes.

### 3. left(90):

- Turns the turtle 90 degrees to the left (counterclockwise).

### 4. backward(100):

- Moves the turtle backward 100 units in its current direction, drawing a line as it goes.

### Combined effect:

When executed together, these commands create a right-angled hook shape, as shown below:

### Key points:

- The turtle starts facing towards the right of the screen.
- Angles are measured in degrees, with 0 degrees pointing towards the right and 90 degrees pointing upwards.
- The distance moved by forward and backward is measured in pixels (or other units you might have set).

### Output:

```python

See output in your Python Environment.

```



### Draw a Square:

```python
from turtle import *
fd(100)
rt(90)
fd(100)
rt(90)
fd(100)
rt(90)
fd(100)
```
### Output:

```python

See output in your Python Environment.

```




## Draw a Square:

```python
from turtle import *
pen = Turtle()
pen.circle(50)  
done()   
```
### Output:

```python

See output in your Python Environment.

```





## Change the Screen Color

```python

from turtle impurt *
bgcolor("purple")

```

### Output:

```python

See output in your Python Environment.

```


## Explaination

### Available colors:

- You can use common color names like "red", "blue", "green", "yellow", "orange", "pink", "purple", "black", and "white".
- For more specific colors, use RGB values in a tuple: screen.bgcolor((255, 100, 0)) for a bright orange.










## Changing the  Screen Title

```python
from turtle import *
title("Turtle in the Sunshine Meadow")

```

### Output:

```python

See output in your Python Environment.

```

- In this example, the screen title will be "My Awesome Turtle Drawing". You can replace this with any text you like.



## Changing the  Turtle Size

```python
from turtle import *
shapesize(1,5,10)
shapesize(10,5,1)
shapesize(1,10,5)
shapesize(10,1,5)

```

### Output:

```python

See output in your Python Environment.

```


## Explaination


The shapesize function lets you adjust the size and outline thickness of your  It takes three arguments:

- stretch_wid: This controls the width of the turtle shape, relative to its default size. A value of 1 leaves the width unchanged, while higher values stretch it horizontally.
- stretch_len: This controls the length of the turtle shape, relative to its default size. A value of 1 leaves the length unchanged, while higher values stretch it vertically.
- outline: This controls the thickness of the turtle's outline. A value of 1 leaves the outline unchanged, while higher values make it thicker.
Now, let's see how each of your commands affects the turtle:

- shapesize(1,5,10): This stretches the turtle vertically by a factor of 5 and horizontally by a factor of 10, with the outline thickness remaining unchanged. Imagine a tall, skinny rectangle for the turtle's shape. 




## Changing the Pen Size

```python
from turtle import *


# Set pen size to 5
pensize(5)

# Draw the square
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)

# Keep the window open
done()

```

### Output:

```python

See output in your Python Environment.

```


## Explaination


Here are some things to know about pensize(5):

- Effects: Thicker lines can create bolder drawings, but they can also obscure details in smaller drawings.
- Combined with other commands: You can use pensize in conjunction with other turtle commands like forward, backward, circle, and penup to draw various shapes and lines with different thicknesses.
- Default value: The default pen size is usually 1.
- Visual impact: You can imagine the pen like a marker with adjustable tip size. A pen size of 5 would be like using a thicker marker compared to a thinner one with a size of 1.








## Changing the Turtle and Pen Color

### 1. Pen Color:

- Using pencolor: This function takes either a color name ("red", "blue", etc.) or an RGB tuple (e.g., (255, 0, 0) for red).

```python
from turtle import *


# Using color name
pencolor("green")

# Using RGB tuple
pencolor((0, 255, 0))  # Green

done()

```



### Output:

```python

See output in your Python Environment.

```
Using color: This function is more versatile, allowing you to set both the pen and fill color simultaneously. It also accepts keywords like "brown", "gold", and "teal".

```python

color("yellow", "purple")  # Yellow pen, purple fill

```
### 2. Turtle Color:

- Using turtlecolor: This function sets the turtle's shell and body color. It works similarly to pencolor and color.

```python
from turtle import *
turtlecolor("orange")

```
### Output:

```python

See output in your Python Environment.

```


### 3. Combined Effects:

You can mix and match these functions to create unique effects. For example:

```python
from turtle import *
pencolor("blue")
turtlecolor("yellow")
circle(50) 

```
### Output:

```python

See output in your Python Environment.

```




## Filling the Shape

### 1. Set the fill color:

Choose the desired color for your shape using either fillcolor("color_name") or color("pen_color", "fill_color").

### 2. Begin filling:

Before drawing your shape, use begin_fill(). This tells Turtle to remember the starting point and start filling any enclosed area you draw afterwards.

### 3. Draw your shape:

Use the usual Turtle commands like forward, backward, circle, turn, etc., to draw the desired shape. Ensure all sides connect to properly enclose the area.

### 4. End filling:

After drawing the last side of your shape, use end_fill(). This signals that the enclosed area is complete and tells Turtle to fill it with the chosen color.

### Example:

Here's how to draw and fill a blue square:

```python
from turtle import *
# Set fill color
fillcolor("blue")

# Begin filling
begin_fill()

# Draw the square
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)

# End filling
end_fill()

# Keep the window open
done()

```
### Output:
```python

See output in your Python Environment.

```

- This code will draw a blue square with a solid blue fill. You can adjust the fill color, shape, and drawing commands to create different filled shapes.








## Changing the Shape

### 1.Predefined Shapes:

#### - Turtle comes with a set of built-in shapes you can easily switch to:

- arrow
- circle
- square
- triangle
- classic (may vary depending on your system)

```python
from turtle import *

shape("square")
forward(100)  # Now the turtle draws a square instead of a line

shape("circle")
forward(100)  # Now the turtle draws a circle instead of a square

```
### Output:

```python

See output in your Python Environment.

```

### 2. Custom Shapes:

#### - Create your own unique shapes using images (typically GIFs):
-Save your image file in a valid format like GIF.
-Use the register_shape("shape_name", "image_filename") function to register your custom image as a new shape:


```python
from turtle import *

register_shape("star", "star.gif")
shape("star")
forward(100)  # Now the turtle draws a star instead of a circle


```
### Output:

```python

See output in your Python Environment.

```


## 2. Changing the Pen Speed 


There are two primary ways to change the pen speed in Python Turtle:

### 1. Using the speed() function:

- This function takes a numeric argument (1-10) representing the desired speed level.
- Higher values represent faster drawing, while lower values (including 0) represent slower or no animation at all.

```python
from turtle import *
# Set slow speed
speed(3)

# Draw slowly
forward(100)

# Set fast speed
speed(8)

# Draw quickly
circle(50)

```
### Output:

```python

See output in your Python Environment.

```

### 2. Disabling animation:

You can completely disable animation using tracer(False).
- This will instantly draw all commands without any visual transition, effectively making the pen "infinitely fast."
- Remember to call update() afterward to show the final drawing on the screen.

```python
from turtle import *
# Disable animation
tracer(False)

# Draw everything instantly
forward(100)
right(90)
circle(50)

# Show the results
update()
done()
```
### Output:

```python

See output in your Python Environment.

```






## Customizing in One Line

Customizing in one line can be a fun challenge and depends heavily on the context and what needs to be customized. Here are a few examples to get you started:

##### Python Turtle:

- Change turtle shape and color: shape("star").pencolor("purple")
- Draw and fill a square: begin_fill().forward(100).right(90).forward(100).right(90).forward(100).right(90).forward(100).end_fill().speed


```python
from turtle import *
pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
begin_fill()
circle(90)
end_fill()
done()
```

### Output:

```python

See output in your Python Environment.

```







## Picking the Pen Up and Down

Picking the pen up and down in Python Turtle is essential for controlling which parts of your drawing get traced and which don't. Here are two key functions to remember:

1. penup(): This function lifts the pen off the ground, preventing it from drawing any lines as you move the  Think of it like picking up a real pen.

2. pendown(): This function puts the pen back down on the ground, allowing it to draw lines as you move the  Think of it like putting down the real pen.

Here's how you can use these functions in your code:


```python
from turtle import *
# pendown()

# Draw a square
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)

# Pick up the pen and move to a new location
penup()
forward(200)
left(90)

# Put the pen down and draw a circle
pendown()
circle(50)

# Keep the window open
done()
```

### Output:

```python

See output in your Python Environment.

```






## Clearing the Screen

#### 1. Clear all drawings and reset the turtle:

Use clear(): This removes all turtle drawings, sets the pen color and position back to initial values, and keeps the window open.

```python
from turtle import *
clear()
# Turtle has no drawings and is back in its initial state.
```
### Output
```python

See output in your Python Environment.

```

#### 2. Clear only drawings but keep turtle state:

- Use turtle.clearscreen(): This erases all drawings but maintains the turtle's current position, heading, and pen settings.


```python
from turtle import *
clearscreen()
# Turtle remains at its current location and retains its settings.
```
### Output
```python

See output in your Python Environment.

```

#### 3. Clear the screen and close the window:

- Use turtle.bye(): This removes all drawings, resets the turtle, and closes the Turtle graphics window.

```python
from turtle import *
urtle.bye()
# The Turtle window closes completely.
```
### Output
```python

See output in your Python Environment.

```
