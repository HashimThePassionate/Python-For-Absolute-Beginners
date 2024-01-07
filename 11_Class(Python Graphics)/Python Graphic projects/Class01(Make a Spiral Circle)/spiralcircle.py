# Import the turtle library for
# drawing the required curve
from turtle  import *

# Set the background color as black,
# pensize as 2 and speed of drawing
# curve as 10(relative)
Screen().bgcolor('black')
pensize(2)
speed(10)

# Iterate six times in total
for i in range(6):

	# Choose your color combination
	for color in ('red', 'magenta', 'blue',
				'cyan', 'green', 'white',
				'yellow'):
		color(color)

		# Draw a circle of chosen size, 100 here
		circle(100)

		# Move 10 pixels left to draw another circle
		left(10)

	# Hide the cursor(or turtle) which drew the circle
	hideturtle()
done()


