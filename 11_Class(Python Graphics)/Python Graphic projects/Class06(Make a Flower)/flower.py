from turtle import *
title('Sixteen Petals Flower')
setworldcoordinates(-2000,-2000,2000,2000)

def draw_flower(x,y,tilt,radius):
    up()
    goto(x,y)
    down()
    seth(tilt-45)
    circle(radius,90)
    left(90)
    circle(radius,90)

for tilt in range(0,360,30):
    draw_flower(0,0,tilt,1000)
    
    done()
    
    
    
    
    
   