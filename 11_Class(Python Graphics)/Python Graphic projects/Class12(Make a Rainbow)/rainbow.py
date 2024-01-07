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


