#Python control flows
'''
Python uses the usual flow control statements known 
from other languages, with some twists.
Perhaps the most well-known statement type is the 
'''
#if statement.
'''
Think of an if statement as a way to check to see if
conditions are met!
'''
num = int(input("enter the number?"))  
if num%2 == 0:  
    print("Number is even") 


#if else
'''
If a condition is met, do something...
else do something different!
'''
age = int (input("Enter your age? "))  
if age>=18:  
    print("You are eligible to vote !!");  
else:  
    print("Sorry! you have to wait !!");  


#elif 'elif' stands for 'else if'
'''
both elif and else are optional!
'''
number = int(input("Enter the number?"))  
if number == 10:  
    print("number is equals to 10")  
elif number == 50:  
    print("number is equal to 50");  
elif number == 100:  
    print("number is equal to 100");  
else:  
    print("number is not equal to 10, 50 or 100"); 

#Match statement

'''
Hot off the press in Python 3.10

A match statement takes an expression and compares 
its value to successive patterns given as one or 
more case blocks.

Note: We have a class in this demo. Don't get too caught 
up in how it
works! We have a class video in this course :)
'''

#basics
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

def http_error(status):
    match status:
        case 400 | 401 | 403 | 404:
            return "Not allowed"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

#Practise 
#when to know everything about tuple and class
#Patterns can look like unpacking assignments, and can be used to bind variables:
# point is an (x, y) tuple
def http_error(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")

point_tuple = (0,0)
point_tuple = (0,123)
point_tuple = (123,0)
point_tuple = (123,456)

#Match class
from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

where_is(Point(0, 0))
where_is(Point(0, 10))
where_is(Point(10, 0))
where_is(Point(10, 10))