# Welcome to Core Python
print("Welcome to Hello World")
#The basics
7 * 10 # simple multiplication

#Division and Modulus
5 / 4  # classic division returns a float
11 // 4  # floor division discards the fractional part
12 % 4 # the % operator returns the remainder of the division
round(8,4)

#Basic Division and Modulus:

dividend: int = 20
divisor: int = 3

quotient: int = dividend // divisor  # Integer division
remainder: int = dividend % divisor  # Modulus operation

print(f"{dividend} divided by {divisor} is {quotient} with a remainder of {remainder}.")

# Division with Floating-Point Result:

numerator: float = 15.0
denominator: float = 2.5

result: float = numerator / denominator  # Division with floating-point result

print(f"The result of {numerator} divided by {denominator} is {result}.")


#Fancy sums
30 - 5*6 
(60 - 5*6) // 4
5 * 3 + 2  # floored quotient * divisor + remainder


#Exponentiation (power of)-------------------------------------------------------------------------------------------------------------------

# Python's exponentiation operator is versatile and can handle both integer and floating-point exponents, making it a powerful tool for mathematical computations.
# In Python, the exponentiation operation, which calculates the power of a number, is performed using the ** operator.

5 ** 2  # 5 squared
2 ** 7  # 2 to the power of 7
pow(2,7)

# 1 Integer Exponentiation:
Number : int = 2
anoter_number : int = 3
result = Number ** exponent
print(f"{Number} raised to the power of {exponent} is {result}.")
# Output: 2 raised to the power of 3 is 8


# 2 Floating-Point Exponentiation:
base : float = 3.5
exponent : int = 2
result = base ** exponent
print(f"{base} raised to the power of {exponent} is {result}.")
# Output: 3.5 raised to the power of 2 is 12.25


# 3 Negative Exponentiation:

points : int = 4
credits : int = -2
result = points ** credits
print(f"{points} raised to the power of {credits} is {result}.")
# Output: 4 raised to the power of -2 is 0.0625

# 4 Exponentiation in Expressions:

x  : int = 2
y : int  = 3
z = x ** y + 1
print(f"{x} raised to the power of {y} plus 1 is {z}.")
# Output: 2 raised to the power of 3 plus 1 is 9
#---------------------------------------------------------------------------------------------------------------------------------------------


# Boolean literals:

# Boolean literals in Python represent the two truth values: True and False. These literals are used to perform logical 
# operations and make decisions in your code. Here are some key points about boolean literals in Python:


# Boolean literals
is_true: bool = True
is_false: bool = False

# Result of comparisons
result_greater_than: bool = (5 > 3)  # Result will be True
result_equal_or_greater: bool = (10 >= 5)  # Result will be True
result_not_equal: bool = (7 != 7)  # Result will be False

# Logical operations
condition1: bool = True
condition2: bool = False
result_logical_and: bool = condition1 and condition2  # Result will be False
result_logical_or: bool = condition1 or condition2  # Result will be True
result_logical_not: bool = not condition1  # Result will be False

# Boolean casting
number_value: int = 42
bool_value: bool = bool(number_value)  # Result will be True

# None type
variable: None = None
if variable is None:
    print("The variable is None.")

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
#----------------------------------------------------------------------------------------------------------------------------------------------

#Python Variables.

#Variables are containers for storing data values.
# In Python, a variable is a named storage location that holds a value. Variables provide a way to label and store data in the computer's memory,
# allowing you to manipulate and work with that data throughout your program. Here are key characteristics and points about variables in Python
'''
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
'''

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

saba: int = 2
aalia: int = 3
ans: int = saba ** aalia
print(f"{saba} raised to the power of {aalia} is {ans}.")
# Output: 2 raised to the power of 3 is 8

hamza: float = 3.5
nouman: int = 2
result: float = hamza ** nouman
print(f"{hamza} raised to the power of {nouman} is {result}.")
# Output: 3.5 raised to the power of 2 is 12.25

aalia: int = 4
hamza: int = -2
ans: float = aalia ** hamza
print(f"{aalia} raised to the power of {hamza} is {ans}.")
# Output: 4 raised to the power of -2 is 0.0625

nouman: int = 2
saba: int = 3
ans: int = nouman ** saba + 1
print(f"{nouman} raised to the power of {saba} plus 1 is {ans}.")
# Output: 2 raised to the power of 3 plus 1 is 9

width : int = 60
height : int = 3 * 7
width * height

#In interactive mode, the last printed expression is assigned to the variable _.
tax : int = 12.5 / 100
price : float = 100.50
price * tax #this is assigned to '_' and we use it in the next expression
price + _ #We reference '_' but this expression is now assigned to '_'
round(_, 2)


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

#id of Variable 

b : int = 5
print(id(b))

#megic Methods of Variable

caste : str = "malik"
print(dir(caste))


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
#---------------------------------------------------------------------------------------------------------------------------------------------------

#using Print()
name : str = "Hashim"
age  : int = 23
print('Age  is ',age)
print('name  is '+name)
#-----------------------------------------------------------------


#F-Strings (Formatted String Literals)

# Certainly! In Python, f-strings can be highlighted by using the f prefix before the string. Here's the same example with an emphasis on the f-string:

print(f'Age is {age} and Name is {name}')

name: str = "Shaan"
age: int = 30
height: float = 5.9

# The following string is an f-string
message: str = f"My name is {name}, I am {age} years old, and my height is {height:.2f} feet."
print(message)
#-------------------------------------------------------------------------------------------------------------------------------

#str.format() Method

# The format() method is a powerful tool that allows developers to create formatted strings by embedding variables and values into placeholders within a template string. This method offers a flexible and versatile way to construct textual output for a wide range of applications. Python string format() function has been introduced for handling complex string formatting more efficiently. Sometimes we want to make generalized print statements in that case instead of writing print statements every time we use the concept of formatting.

print('Name : {} Age : {}'.format(name,age))


name : str = "Shahmeer"
age : int = 22
message = "My name is {0} and I am {1} years \old. {1} is my favorite \ number.".format(name, age)
print(message)
#--------------------------------------------------------------------------------------------------------------------------------------------


#Using % Formatting:
print('Age is %d and Name is %s'%(age,name))



#PYTHON USERINPUT .............................................................................................................................

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




