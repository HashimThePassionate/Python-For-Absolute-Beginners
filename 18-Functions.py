#Python functions
'''
Think of a function as a little named container for a group 
of your code!
To run the code in a function, you must call the function.
A function can be called from anywhere after the function is defined. 

Syntax of Python Function
Code

def name_of_function( parameters ):  
    """This is a docstring"""  
    # code block  

The following elements make up define a function, as seen above.
1.The beginning of a function header is indicated by a keyword 
called def.

2.name_of_function is the function's name that we can use 
to separate it from others. We will use this name to call 
the function later in the program. The same criteria 
apply to naming functions as to naming variables 
in Python.

3.We pass arguments to the defined function using parameters. 
They are optional, though.

3.The function header is terminated by a colon (:).

4.We can use a documentation string called docstring 
in the short form to explain the purpose of the function.

5.The body of the function is made up of several valid Python
statements.The indentation depth of the whole code block must 
be the same (usually 4 spaces).

6.We can use a return expression to return a value from 
a defined function.

example...
def demo_func(param:int):
    """This is just a demo
    function.
    """
    calc = param + 4
    return calc

>>>demo_func(6)
10

Functions can return a value using a return statement. Functions are 
a common feature among all programming languages

The keyword def introduces a function definition. It must 
be followed by the function name and the parenthesized list 
of formal parameters. The statements that form the body of 
the function start at the next line, 
and must be indented.

def demo_func(param:int):
    """This is just a demo
    function.
    """
    calc = param + 4
    return calc
'''
#Basic Example of a User-Defined Function
def square( num ):  
    """ 
    This function computes the square of the number. 
    """  
    return num**2 
     
print(square.__doc__) #.__doc__
object_ = square(9)  
print( "The square of the number is: ", object_ ) 

'''
Output
This function computes the square of the number.
The square of the number is:  81
'''

#Example 1
def demo_func(param:int):
    """This is just a demo
    function.
    """
    calc = param + 4
    return calc

demo_func(6)

#Example 2
# Defining a function  
def a_function( string ):  
    "This prints the value of length of string"  
    return len(string)  
print( "Length of the string Functions is: ", a_function("Muhammad Hashim") )
print( "Length of the string Functions is: ", a_function( "Functions" ) )  
print( "Length of the string Python is: ", a_function( "Python" ) )

#Example3
#Note: I will be defining a function to demo :)
#The basics
def number_play(x):
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

number_play(-1)
number_play(0)
number_play(1)
number_play(2)

'''
Negative changed to zero
Zero
Single
More
'''
  

#Pass by Reference Vs Value
'''
In the Python programming language, all arguments are supplied by reference.
It implies that if we modify the value of an argument within a function, 
the change is also reflected in the calling function. For instance,
'''
# defining the function  
def square( my_list ):  
    '''''This function will find the square of items in list'''  
    squares = []  
    for l in my_list:  
        squares.append( l**2 )  
    return squares  
  
# calling the defined function  
list_ = [1, 2, 4, 6, 8, 10]
result = square( list_ )  
print( "Squares of the list is: ", result )  

#Function Arguments
'''
The following are the types of arguments that we can use to 
call a function
1.  Default arguments
2.  Keyword arguments
3.  Required arguments
4.  Variable-length arguments
'''
#Default Arguments
'''
A default argument is a kind of parameter that takes as input a default 
value if no value is supplied for the argument when the function is 
called. Default arguments are demonstrated in the following instance.
'''
# Python code to demonstrate the use of default arguments  
# defining a function  
def function( num1 = 40, num2 = 40 ):  
    print("num1 is: ", num1)  
    print("num2 is: ", num2)  
    
# Calling the function without argument  
print( "Passing without argument" )  
function()
# Calling the function and passing only one argument  
print( "Passing one argument" )  
function(10)  
# Now giving two arguments to the function  
print( "Passing two arguments" )  
function(10,30)  

'''
Passing without argument
num1 is:  40
num2 is:  40
Passing one argument
num1 is:  10
num2 is:  40
Passing two arguments
num1 is:  10
num2 is:  30
'''

#Keyword Arguments
'''
The arguments in a function called are connected to keyword arguments. 
If we provide keyword arguments while calling a function, the user uses 
the parameter label to identify which parameters value it is.

Since the Python interpreter will connect the keywords given to link 
the values with its parameters, we can omit some arguments or 
arrange them out of order. The function() method can also be 
called with keywords in the following manner:
'''
# Python code to demonstrate the use of keyword arguments  
  
# Defining a function  
def function( num1, num2 ):  
    print("num1 is: ", num1)  
    print("num2 is: ", num2)  
  
# Calling function and passing arguments without using keyword  
print( "Without using keyword" )  
function( 50, 30)     
      
# Calling function and passing arguments using keyword  
print( "With using keyword" )  
function( num2 = 50, num1 = 30)

'''
Without using keyword
num1 is:  50
num2 is:  30
With using keyword
num1 is:  30
num2 is:  50
'''

#Required Arguments
'''
The arguments given to a function while calling in a pre-defined 
positional sequence are required arguments. The count of required 
arguments in the method call must be equal to the count of arguments 
provided while defining the function.

We must send two arguments to the function function() in the correct 
order,or it will return a syntax error, as seen below.
'''
# Python code to demonstrate the use of default arguments  
  
# Defining a function  
def function( num1, num2 ):  
    print("num1 is: ", num1)  
    print("num2 is: ", num2)  

print( "Passing out of order arguments" )  
function( 30, 20 )     
  
# Calling function and passing only one argument  
print( "Passing only one argument" )  
try:  
    function( 30 )  
except:  
    print("Function needs two positional arguments") 

'''
Output
Passing out of order arguments
num1 is:  30
num2 is:  20
Passing only one argument
Function needs two positional arguments
'''

#Variable-Length Arguments
'''
We can use special characters in Python functions to pass as many 
arguments as we want in a function. There are two types of characters
that we can use for this purpose:

1.  *args -These are Non-Keyword Arguments
2.  **kwargs - These are Keyword Arguments.

'''
# Python code to demonstrate the use of variable-length arguments     
# Defining a function  
def function( *args_list ):  
    ans = []  
    for l in args_list:  
        ans.append( l.upper() )  
    return ans  
# Passing args arguments  
object = function('Python', 'Functions', 'tutorial')  
print( object )  
  
# defining a function  
def function( **kargs_list ):  
    ans = []  
    for key, value in kargs_list.items():  
        ans.append([key, value])  
    return ans  
# Paasing kwargs arguments  
object = function(First = "Python", Second = "Functions", Third = "Tutorial")  
print(object)  
'''
Output
['PYTHON', 'FUNCTIONS', 'TUTORIAL']
[['First', 'Python'], ['Second', 'Functions'], ['Third', 'Tutorial']]
'''
#return Statement
'''
We write a return statement in a function to leave a function and give 
the calculated value when a defined function is called.

Syntax:
return < expression to be returned as output >  
An argument, a statement, or a value can be used in the return statement, 
which is given as output when a specific task or function is completed. 
If we do not write a return statement, then None object is returned by a 
defined function.
Here is an example of a return statement in Python functions.
'''
# Python code to demonstrate the use of return statements  
  
# Defining a function with return statement  
def square( num ):  
    return num**2  
   
# Calling function and passing arguments.  
print( "With return statement" )  
print( square( 39 ) )  
  
# Defining a function without return statement   
def square( num ):  
     num**2   
  
# Calling function and passing arguments.  
print( "Without return statement" )  
print( square( 39 ) )  

'''
Output
With return statement
1521
Without return statement
None
'''
#Printing Docstring using __doc__ method
def my_function():
    """Demonstrates triple double quotes
    docstrings and does nothing really."""
   
    return None
  
print("Using __doc__:")
print(my_function.__doc__)
  
print("Using help:")
help(my_function)

'''
Output
Using __doc__:
Demonstrates triple double quotes
    docstrings and does nothing really.
Using help:
Help on function my_function in module __main__:

my_function()
    Demonstrates triple double quotes
    docstrings and does nothing really.
'''

'''
As guidance:

Use positional-only if you want the name of the parameters to not 
be available to the user. This is useful when parameter names have 
no real meaning, if you want to enforce the order of the arguments 
when the function is called or if you need to take some positional 
parameters and arbitrary keywords.

Use keyword-only when names have meaning and the function definition 
is more understandable by being explicit with names or you want to 
prevent users relying on the position of the argument being passed.

For an API, use positional-only to prevent breaking API changes if 
the parameter’s name is modified in the future.
'''

