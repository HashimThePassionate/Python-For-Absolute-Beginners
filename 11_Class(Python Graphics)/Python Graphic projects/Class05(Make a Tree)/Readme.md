## Code structure
    ```python
    from turtle import *

speed(0)

# Blue Background
penup()
goto(0, -250)
pendown()
color("lightskyblue")
begin_fill()
circle(250)
end_fill()

# Tree Trunk
penup()
goto(-15, -50)
pendown()
color("brown")
begin_fill()
for i in range(2):
    forward(30)
    right(90)
    forward(40)
    right(90)
end_fill()

# Set the start position and the inital tree width
y = -50
width = 240
height = 25

# Green section of tree (add in the greater than symbol next to the 20 - YouTube doesn't allow me to put in pointy brackets).
while width > 20:
    width = width - 30 # Make the tree get smaller as it goes up in height
    x = 0 - width / 2 # Set the starting x-value of each level of the tree
    color("green")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

    y = y + height # Keep drawing the levels of the tree higher than the previous

# Star
penup()
goto(-15, 150)
pendown()
color("yellow")
begin_fill()
for i in range(5):
    forward(30)
    right(144)
end_fill()

# Message
penup()
goto(-130, -150)
color("red")
write("MERRY CHRISTMAS", font=("Arial", 20, "bold"))

hideturtle()
done()
   ``` 
    
   # Explaination:


## 1. Import and Setup:

- Imports the turtle module: from turtle import * for drawing graphics.
- Sets drawing speed: speed(0), fastest possible for a smoother experience.
## 2. Blue Background:

- Moves the turtle to position: penup(), goto(0, -250).
- Sets color: color("lightskyblue").
- Fills a circle as the background: begin_fill(), circle(250), end_fill().
- Image of light blue circular backgroundOpens in a new window
- light blue circular background
## 3. Tree Trunk:

- Moves to trunk position: penup(), goto(-15, -50).
- Sets color: color("brown").
- Draws a filled rectangle as the trunk: begin_fill(), forward(30), right(90), forward(40), right(90), end_fill().
- Image of brown rectangular trunk on the blue backgroundOpens in a new window

## 4. Green Tree Sections:

- Sets initial position and width: y = -50, width = 240, height = 25.
- Loop for multiple tree sections: while width > 20:
 Reduce width for each level: width = width - 30.
 Calculate starting x-position: x = 0 - width / 2.
- Set color: color("green").
- Move to starting position: penup(), goto(x, y).
- Draw a filled rectangle: begin_fill(), forward(width), left(90), forward(height), left(90), end_fill().
- Increment y-position for next level: y = y + height.
## 5. Star:

- Move to star position: penup(), goto(-15, 150).
- Set color: color("yellow").
- Draw a filled star: begin_fill(), for i in range(5): forward(30), right(144), end_fill().
- Image of yellow star on top of the treeOpens in a new window
## 6. Message:

- Move to message position: penup(), goto(-130, -150).
- Set color: color("red").
- Write the message: write("MERRY CHRISTMAS", font=("Arial", 20, "bold")).
- Image of text MERRY CHRISTMAS written in red below the treeOpens in a new window
## 7. Hide Turtle and Keep Window Open:

- Hide the turtle: hideturtle().
- Keep the window open until clicked: done().