#Python Modules
'''
In Python we are able to write a long program and save as a module.
This is known as creating a script. We are able to import modules 
across modulesand into the Python interpreter. This negates the 
need to keep repeating ourselves.
DRY!....Don't repeat yourself
'''
import example
example.add(4,5.5)

#We can import a module by renaming it as follows:
# import module by renaming it

import example as m
print("The addition is ",example.add(4,5.5))

#Python import statement
# import statement example
# to import standard module math
import math
print("The value of pi is", math.pi)

#Python from...import statement
# import only pi from math module
from math import pi
print("The value of pi is", pi)






