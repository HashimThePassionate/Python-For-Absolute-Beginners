## Code structure
    ```python
    from  turtle import *
from  colorsys import *

def draw_one_color_arc(x,y,r,pensize,color):
    up()
    goto(x+r,y)
    down()
    seth(90)
    pensize(pensize)
    pencolor(color)
    circle(r,180)


speed(0)
hideturtle()
bgcolor('light blue')
title('Rainbow In Python Turtle')
setup(700,700)
num_colors = 49

radius = 300
penwidth = 20*7/num_colors
hue = 0

for i in range(num_colors):
    (r,g,b) = hsv_to_rgb(hue,1,1)
    draw_one_color_arc(0,-100,radius,penwidth,(r,g,b))
    radius -= (penwidth-1)
    hue += 0.9/num_colors

done()



   ``` 
    
   # Explaination:

## 1. Import Modules:

- from turtle import *: Imports the turtle library for graphics.
- from colorsys import *: Imports the colorsys library for color conversions.
## 2. Define a Function to Draw Arcs:

- draw_one_color_arc(x, y, r, pensize, color):
- Moves the turtle to position (x + r, y).
- Sets the heading to 90 degrees (upwards).
- Sets the pen size and color.
- Draws a semicircle with radius r and angle 180 degrees.
## 3. Set Up Turtle Canvas:

- speed(0): Sets the turtle's drawing speed to fastest.
- hideturtle(): Hides the turtle cursor.
- bgcolor('light blue'): Sets the background color.
- title('Rainbow In Python Turtle'): Sets the window title.
- setup(700, 700): Sets the window size to 700 pixels by 700 pixels.
## 4. Initialize Variables:

- num_colors = 49: Specifies the number of colors in the rainbow.
- radius = 300: Initializes the starting radius of the arcs.
- penwidth = 20 * 7 / num_colors: Calculates the pen width for each arc.
- hue = 0: Initializes the hue value for color generation.
## 5. Draw Rainbow Arcs:

- for i in range(num_colors):: Loops through each color.
- (r, g, b) = hsv_to_rgb(hue, 1, 1): Converts HSV color (hue, saturation, value) to RGB (red, green, blue).
- draw_one_color_arc(0, -100, radius, penwidth, (r, g, b)): Draws an arc with the calculated color.
-  radius -= (penwidth - 1): Decrements the radius for the next arc.
- hue += 0.9 / num_colors: Increments the hue for the next color.
## 6. Keep Window Open:

- done(): 
Keeps the turtle graphics window open until manually closed.
## 7. Key Points:

- The code utilizes a function to create modular and reusable code for drawing arcs.
- It employs the colorsys library to generate a smooth spectrum of colors based on hue values.
- It adjusts the radius and pen width for each arc to create the overlapping rainbow effect.
- The turtle library provides the fundamental graphics commands for drawing shapes and setting colors.
