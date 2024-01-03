# Welcome to Core Python
print("Welcome to Hello World")
#The basics
7 * 10 # simple multiplication

#Division and Modulus
5 / 4  # classic division returns a float
11 // 4  # floor division discards the fractional part
12 % 4 # the % operator returns the remainder of the division
round(8,4)

#Fancy sums
30 - 5*6 
(60 - 5*6) // 4
5 * 3 + 2  # floored quotient * divisor + remainder

#Exponentiation (power of)
5 ** 2  # 5 squared
2 ** 7  # 2 to the power of 7
pow(2,7)

#Using variables
width : int = 60
height : int = 3 * 7
width * height

#In interactive mode, the last printed expression is assigned to the variable _.
tax : int = 12.5 / 100
price : float = 100.50
price * tax #this is assigned to '_' and we use it in the next expression
price + _ #We reference '_' but this expression is now assigned to '_'
round(_, 2)

#2Boolean literals:
'''
A Boolean literal can have any of the two values: True or False.
'''
x : bool = (1 == True)  
y : bool = (2 == False)  
z : bool = (3 == True)  
a : bool = True + 10  
b : bool = False + 10  
  
print("x is", x)  
print("y is", y)  
print("z is", z)  
print("a:", a)  
print("b:", b)

# 4 PYTHON VARIABLES START...................................................................................

#Variables are containers for storing data values.
'''
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
'''
#Variable Assignment
n : int = 300
id(n)
print(n)

#Example
m : str = n
print("Value of m ",m)
print("id of m ",id(m))
print("Value of n ",n)
print("id of n ",id(n))

m : int = 400
print("Value of m ",m)
print("id of m ",id(m))
print("Value of n ",n)
print("id of n ",id(n))

n : str = "Hello"
print("Value of m ",m)
print("id of m ",id(m))
print("Value of n ",n)
print("id of n ",id(n))

#TYPE of Variable
a : int = 2
type(a)

#Same id to these objects
n : int = 10
m : str = "n"
print("n = :",id(n))
print("m = :",id(m))

'''
Camel case nOfStudent = "Hamza"
Pascal case NOfStudent = "Subhan"
Snake case  name_of_student = "Zeeshan"
'''

#-----------------------------------------------------------------------

# 4 Types of  Variable data 

#int 
a : int = 10 
b : int = -10

#float 
a : float = 10.1 
b : float = -10.1 

#string
name : str = " Farooq " 
#bool

a : bool = True
#----------------------------------------------------------------
#using Print()
name : str = "Hashim"
age  : int = 23
print('Age  is ',age)
print('name  is '+name)
#-----------------------------------------------------------------
#F-Strings (Formatted String Literals)
print(f'Age is {age} and Name is {name}')
#-----------------------------------------------------------------
#str.format() Method
print('Name : {} Age : {}'.format(name,age))
#-----------------------------------------------------------------
#Using % Formatting:
print('Age is %d and Name is %s'%(age,name))

#PYTHON USERINPUT ..............................................................................................

#Python User Input
'''
Python allows for user input.

That means we are able to ask the user for input.

The method is a bit different in Python 3.6 than Python 2.7.

Python 3.6 uses the input() method.

'''
username : str = input("Enter username:")
print("Username is:" + username)

#Example
name : str = input("Enter Your name:")
age : str = int(input("Enter your age"))
print("Your name is :",name,"Your age is",age)


