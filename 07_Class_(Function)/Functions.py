import re
from typing import Union
from typing import Callable, Tuple, Dict
# Python functions
'''
Think of a function as a little named container for a group 
of your code!
To run the code in a function, you must call the function.
A function can be called from anywhere after the function is defined. 

Syntax of Python Function
Code

def name_of_function( parameters : datatype ) -> return type(if they return something):  
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

3.We pass arguments to the defined function using parameters along with their datatypes,as code looks more professional. 
They are optional, though.

4.The function header is terminated by a colon (:).

5.We can use a documentation string called docstring 
in the short form to explain the purpose of the function.

6.The body of the function is made up of several valid Python
statements.The indentation depth of the whole code block must 
be the same (usually 4 spaces).

7.We can use a return expression to return a value from 
a defined function, it is also a professioal practice to define the return datatype.

example...
def demo_func(param:int) -> int :
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
of formal parameters along with their datatypes. The statements that form the body of 
the function start at the next line,and  be indented.

'''
# Basic Example of a User-Defined Function


def square(num: int) -> int:
    """ 
    This function computes the square of the number. 
    """
    return num**2


print(square.__doc__)
'''.__doc__(This line prints out the docstring associated with the square function.
 It accesses the docstring using the __doc__ attribute of the function.)'''

object_ = square(9)
print("The square of the number is: ", object_)

'''
Output
This function computes the square of the number.
The square of the number is:  81
'''

# Example 1


def demo_func(param: int) -> int:
    """This is just a demo
    function.
    """
    calc = param + 4
    return calc


demo_func(6)
print(demo_func(6))  # returns 10

# Example 2
# Defining a function


def a_function(string):
    "This prints the value of length of string"
    return len(string)


print("Length of the string Functions is: ", a_function("Muhammad Hashim"))
print("Length of the string Functions is: ", a_function("Functions"))
print("Length of the string Python is: ", a_function("Python"))

# Example 3
# Note: I will be defining a function to demo :)
# The basics


def number_play(x: int):
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

# Pass by Reference Vs Value
'''
In the Python programming language, all arguments are supplied by reference.
It implies that if we modify the value of an argument within a function, 
the change is also reflected in the calling function. For instance,
'''
# defining the function


def square(my_list):
    """This function will find the square of items in the list"""
    for i in range(len(my_list)):
        my_list[i] = my_list[i] ** 2
    return my_list


# calling the defined function
list_ = [1, 2, 4, 6, 8, 10]
print(f'Before: {list_}')
result = square(list_)
print(f"After: {list_}")

# Function Arguments
'''
The following are the types of arguments that we can use to 
call a function
1.  Default arguments
2.  Keyword arguments
3.  Required arguments
4.  Variable-length arguments
'''
# Default Arguments
'''
A default argument is a kind of parameter that takes input as a default 
value if no value is supplied to the argument when the function is 
called. Default arguments are demonstrated in the following instance.
'''
# Python code to demonstrate the use of default arguments
# defining a function


def function(num1=40, num2=40):
    print("num1 is: ", num1)
    print("num2 is: ", num2)


# Calling the function without argument
print("Passing without argument")
function()
# Calling the function and passing only one argument
print("Passing one argument")
function(10)
# Now giving two arguments to the function
print("Passing two arguments")
function(10, 30)

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

# Keyword Arguments
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


def function(num1: int, num2: int):
    print("num1 is: ", num1)
    print("num2 is: ", num2)


# Calling function and passing arguments without using keyword
print("Without using keyword")
function(50, 30)

# Calling function and passing arguments using keyword
print("With using keyword")
function(num2=50, num1=30)

'''
Without using keyword
num1 is:  50
num2 is:  30
With using keyword
num1 is:  30
num2 is:  50
'''

# Required Arguments
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


def function(num1: int, num2: int):
    print("num1 is: ", num1)
    print("num2 is: ", num2)


print("Passing out of order arguments")
function(30, 20)

# Calling function and passing only one argument
print("Passing only one argument")
try:
    function(30)
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

# Variable-Length Arguments
'''
We can use special characters in Python functions to pass as many 
arguments as we want in a function. There are two types of characters
that we can use for this purpose:

1.  *args -These are Non-Keyword Arguments
2.  **kwargs - These are Keyword Arguments.

'''
# Python code to demonstrate the use of variable-length arguments
# Defining a function


def function(*args_list):
    ans = []
    for l in args_list:
        ans.append(l.upper())
    return ans


# Passing args arguments
object = function('Python', 'Functions', 'tutorial')
print(object)

# defining a function


def function(**kargs_list):
    ans = []
    for key, value in kargs_list.items():
        ans.append([key, value])
    return ans


# Passing kwargs arguments
object = function(First="Python", Second="Functions", Third="Tutorial")
print(object)
'''
Output
['PYTHON', 'FUNCTIONS', 'TUTORIAL']
[['First', 'Python'], ['Second', 'Functions'], ['Third', 'Tutorial']]
'''
# return Statement
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


def square(num: int) -> int:
    return num**2


# Calling function and passing arguments.
print("With return statement")
print(square(39))

# Defining a function without return statement


def square(num: int) -> int:
    num**2


# Calling function and passing arguments.
print("Without return statement")
print(square(39))

'''
Output
With return statement
1521
Without return statement
None
'''
# Printing Docstring using __doc__ method


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

# Namespace in python
'''

In Python, a namespace is a container that holds a set of identifiers (like variable names, function names, class names, etc.) and their corresponding objects (values, functions, classes, etc.). It provides a context for these identifiers, allowing Python to differentiate between them even if they have the same name but exist in different namespaces.

Here's a more detailed explanation of what a namespace is and how it works in Python:
Purpose of Namespaces:
Namespaces help avoid naming conflicts by keeping identifiers in different contexts separate. This is particularly useful in large projects where multiple developers might use the same variable or function names.

Types of Namespaces:
Global Namespace: This is the namespace associated with a module or script. It contains all globally defined identifiers.

Local Namespace: This is the namespace associated with a function or method. It contains identifiers defined within the function or method scope.

Built-in Namespace: This namespace includes Python's built-in functions and exceptions, like print, len, ValueError, etc.

Scope:
The concept of scope is closely related to namespaces. Scope defines where a namespace is accessible. The "global" scope is accessible throughout the module, while the "local" scope is typically accessible within a specific function or block.
Python follows the LEGB rule for scope resolution: Local, Enclosing, Global, Built-in. This determines the order in which Python looks up namespaces to resolve an identifier.

Namespace Operations:
You can view the contents of a namespace with functions like globals() for the global namespace and locals() for the local namespace.
Assignments and deletions of identifiers affect the current namespace. For example, x = 10 creates an identifier x in the current namespace.
'''

# Builtin Namespace:
# Using built-in functions
print("Hello, world!")  # 'print' is a built-in function
print(len([1, 2, 3]))   # 'len' is also built-in
# Using built-in types
my_list = list(range(5))  # 'list' and 'range' are built-in
# Handling built-in exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
# To check builtin namespace
print(dir(__builtins__))

# Global Namespace:
'''
In Python, the global namespace is a context that holds all the variables, functions, classes, and other objects defined at the top level of a module or script. It serves as a global scope, meaning that items defined within it are accessible throughout the module or script and from within any functions or classes defined in that module or script.
'''
x = 50  # Global variable


def mixed_example():
    x = 10  # Local variable
    print(f'Show the current local Namespace {dir()}')
    print("Local x:", x)  # Refers to the local variable within this function

    global y  # Declares 'y' as a global variable
    y = 30  # This modifies the global namespace


# Call the function to demonstrate the interaction of namespaces
mixed_example()
print(f'Show the Global Namespace {dir()}')
print("Global x:", x)  # Still refers to the global 'x' (Output: 50)
# Refers to the global 'y' defined in the function (Output: 30)
print("Global y:", y)


# Local Namespace:
def local_example():
    local_variable = 10  # This is in the local namespace of the function
    print("Local variable:", local_variable)


# Call the function to see the local variable in action
local_example()

# Trying to access a local variable outside its scope results in an error
try:
    print(local_variable)  # This raises a NameError
except NameError:
    print("Local variable is not accessible outside its function")


# Non Local Variable and LEGE Rule:
def outer():
    value = 10  # Enclosing scope

    def inner():
        nonlocal value  # References the variable in the enclosing scope
        value += 5  # Modifies the variable in the enclosing scope

    inner()
    print("Value after calling inner:", value)  # Output: 15


outer()

# LEGB Rule
'''
The LEGB rule in Python stands for the order of namespace resolution: Local, Enclosing, Global, Built-in. It describes the order in which Python looks up variable names to determine which scope they belong to when they're used in a program.
'''
# Global scope
x = 10  # Global variable


def outer():
    # Enclosing scope
    x = 20  # Variable in enclosing scope

    def inner():
        # Local scope
        x = 30
        print("Global scope (x):", x)      # Global variable

    inner()  # Calling the nested function


# Call the outer function, which calls the inner function
outer()

# Function as Alais
'''
In Python, you can create an alias for a function by assigning it to a new name. This allows you to refer to the same function using a different name, which can be useful for various reasons, including code readability, shorter syntax, or context-specific naming. When you create an alias, both the original function name and the alias refer to the same function object in memory, meaning any changes to the function affect both references.
'''


def original_function():
    return "Hello, world!"


# Creating an alias for the function
alias_function = original_function

# Calling the function using the alias
print(alias_function())  # Output: "Hello, world!"


# Every Python Function is an object
'''

In Python, everything is an object, including functions. This concept is fundamental to understanding Python's flexibility and expressiveness. Let's explore what it means for functions to be objects, how functions behave as objects, and what capabilities this provides.
'''

# Functions as Objects


def multiply(a, b):
    return a * b


multiply.description = "Multiplies two numbers."
print(multiply.description)  # Output: "Multiplies two numbers."

# Using a function's attributes to modify its behavior
multiply.factor = 2


def multiply_with_factor(x):
    return multiply(x, multiply.factor)


print(multiply_with_factor(3))  # Output: 6 (3 * 2)


# Function that takes another function as a parameter
def apply_twice(func, x):
    return func(func(x))
# Applying a function twice


def double(x):
    return x * 2


print(apply_twice(double, 3))

# Storing Functions in Data Structure
# Storing functions in a list
operations = [double, lambda x: x + 10, lambda x: x ** 2]
# Applying each function to a number
results = [func(5) for func in operations]
print(results)  # Output: [10, 15, 25]
# Storing functions in a dictionary
operations_dict = {
    'double': double,
    'add_ten': lambda x: x + 10,
    'square': lambda x: x ** 2
}
print(operations_dict)  # Output: 16

# Closure in python
'''
A closure in Python is a function that retains access to its enclosing scope, even after the scope has exited. Closures allow inner functions to capture variables from their enclosing context, enabling them to carry those captured variables wherever they go, even when the outer function has finished execution.
'''


def outer():
    def inner():
        x = 200  # Local variable within 'inner'
        return x  # Return the value of 'x'

    return inner()  # Call 'inner' and return its result


print(outer())  # Output: 200

# Closure Example


def outer():
    def inner():
        x = 200  # Local variable within 'inner'
        return x  # Return the value of 'x'

    return inner  # Call 'inner' and return its result


inner = outer()
print(inner)
print(inner())


def outer():
    def inner():
        x = 200
        return x
    return inner()


print(outer())

# Higher-order Functions


def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)


result = apply(lambda x: x ** 2, 5)
print(result)


# Recursion

def factorial(x: int) -> int:
    """This is a recursive function
    to find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 5
print("The factorial of", num, "is", factorial(num))

# Python Lambda Functions
'''
Lambda Functions in Python are anonymous functions, 
implying they don't have a name. The def keyword is needed to create 
a typical function in Python, as we already know. We can also use 
the "lambda" keyword in Python to define an unnamed function.

Syntax of Python Lambda Function
lambda arguments: expression 
'''
# Example1
# Code to demonstrate how we can use a lambda function
def add(num): return num + 4


print(add(6))
'''
Output
10
'''
# Example2


def reciprocal(num):
    return 1 / num


def lambda_reciprocal(num): return 1 / num


print("Lambda keyword: ", lambda_reciprocal(6))
print("Def keyword: ", reciprocal(6))
'''
Output
Def keyword:  0.16666666666666666
Lambda keyword:  0.16666666666666666
'''
# Example3 Lambda Function with filter()
# Code to filter odd numbers from a given list
list_ = [34, 12, 64, 55, 75, 13, 63]
odd_list = list(filter(lambda num: (num % 2 != 0), list_))
print(odd_list)
'''
Output
[55, 75, 13, 63]
'''
# Example4 Lambda Function with map()
# Code to calculate the square of each number of a list using the map()
# function
numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]
squared_list = list(map(lambda num: num ** 2, numbers_list))
print(squared_list)
'''
Output
[4, 16, 25, 1, 9, 49, 64, 81, 100]
'''

# Example5 Lambda Function with List Comprehension and For Loop
# Code to calculate square of each number of list using list comprehension
squares = [lambda num=num: num ** 2 for num in range(0, 11)]
for square in squares:
    print(square(), end=" ")
'''
Output
0 1 4 9 16 25 36 49 64 81 100 
'''

# Example 6 Lambda Function with if-else


def Minimum(x, y): return x if (x < y) else y


print(Minimum(35, 74))
'''
Output
35
'''

# Example 7 Printing number tables with functions


def demo_func(param: int):
    res: int = demo_func(10)


print(f"The result is {res}")
print(param)
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def TableFun(tableNo: int, limit: int) -> None:
    for i in range(1, len(l)):
        print(f"{tableNo} * {i} = {tableNo*i}")

    TableFun(5, 11)
    print(TableFun(5, 11))
    TableFun(4, 11)
    print()
    TableFun(2, 11)
    print()
    TableFun(11, 11)

# Example 8 Functions with Exceptions

    # Raising an Exception
x: int = 10
if x > 5:
    raise Exception(f'x should not exceed 5. The value of x was: {x}')

num = [3, 4, 5, 7]
if len(num) > 3:
    raise Exception(
        f"Length of the given list must be less than or equal to 3 but is {len(num)}")

# Assertion Exception


def square_root(Number: int) -> int:
    assert (Number < 0), "Give a positive number"
    return Number**(1/2)


# Calling function and passing the values
no1: int = square_root(-36)
no2: int = square_root(36)
print(no1)
#  print(no2)

# Example 9 calling functions by arguments,values and errors in functions

# Call by Value
a: int = 5


def abc(num: int) -> None:
    num = 6
    print(id(num))
    print(num)


print(id(a))
abc(a)
print(a)

# Call by Reference
l: list = [1, 2, 3, 4, 5]


def myList(newList: list[int]) -> None:
    print(newList)
    print(id(newList))
    newList.append(6)


print(id(l))
myList(l)
print(l)


a = int(input("Please Enter a Number\t"))
b = int(input("Please Enter another Number\t"))

res: int = (a/b)
print(f"Value is {res}")


a: int = 1
while (True):
    print(a)
    a += a

l: list[int] = [1, 2, 3]
try:
    # a = int(input("Please Enter a Number\t"))
    # b = int(input("Please Enter another Number\t"))
    # print(a/b)
    print(k[3])
except ZeroDivisionError:
    print("You cannot Divide any number with zero")
except IndexError:
    print('List does not contain that index number')
except NameError:
    print('Variable name is not valid')
    # pass

# Example 9 Arithmetic operations with Functions

    def display(a: int, b: int) -> int:
    return a + b

a = display(10, 20)
print(a)


def add_two_numbers(num1: int, num2: int) -> int:
    print(f"num1 value is {num1} and num 2 value is {num2}")
    return num1 + num2


x: int = add_two_numbers(7, 20)
print(f"The sum is {x}")


def a(num1, num2): return num1 + num2


sum: Callable[[int, int], int] = lambda no1, no2: no1 + no2
print(sum(2, 5))
a(7, 8)

# Example 10 Squaring a list and shortlisting it's even and odd numbers


def square(no): return 2 * no + str(2)


print(square('Name'))
data: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                   10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

d1 = list(map(lambda x: x**2, data))
even: list[int] = list(filter(lambda x: x % 2 == 0, data))
odd: list[int] = list(filter(lambda x: x % 2 == 1, data))


print(data)
print('--------------------')
print(d1)
print(even)
print(odd)

# Example 11 Generator Function
# Generator Function


def my_range(start: int, end: int, step: int = 1):
    for i in range(start, end+1, step):
        yield i  # Generator fucntion


a = my_range(1, 10)
print(next(a))
print(next(a))
print(next(a))
print("Hello World")
print(next(a))
print(next(a))
print(next(a))
print(10)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print("Hello World")

# Example 12 Greeting Function

# List Items


def abc(*names: Tuple[str, ...]) -> None:
    """
    This function greets all persons in the names tuple.
    """
    for name in names:
        print("Hello", name)


a = abc('Muhammad Mowahid', 'Abdullah Sobadar', 'Ahmed NotesWala',
        'Ishaque Londonwala', 'Butt Khamoshi Wala')
print(abc.__doc__)
print(a)

# Dictionary Items


def greet(**greeting: Dict[str, str]) -> None:
    print(f'Hey {greeting}')


greet(a="Mowahid", b='Sobadar')

# Example 11 Functions with Class Callable and Decorator Functions


def my_decorator(func: Callable[[], None]) -> Callable[[], None]:
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


def validate_cnic_format(cnic: str) -> bool:
    """
    Validates the format of a CNIC when passed as a string.
    Format should be "*****-*******-*" where * represents any digit.
    """
    pattern = r'^\d{5}-\d{7}-\d{1}$'
    return bool(re.match(pattern, cnic))


def format_cnic(cnic: str) -> str:
    """
    Formats the CNIC string by inserting hyphens after the first five digits and the next seven digits.
    """
    return f"{cnic[:5]}-{cnic[5:12]}-{cnic[12:]}"


def CNIC(cnic: Union[int, str]) -> Union[int, str]:
    """
    Validates and returns the CNIC.
    If passed as a string, automatically formats the CNIC string with hyphens if it doesn't match the desired format.
    """
    if isinstance(cnic, int):
        return cnic
    elif isinstance(cnic, str):
        if validate_cnic_format(cnic):
            return cnic
        else:
            formatted_cnic = format_cnic(cnic)
            print(f'Without format {cnic}')
            print(f"Automatically formatted CNIC: {formatted_cnic}")
            return formatted_cnic
    else:
        raise TypeError("CNIC must be either an integer or a string")


# Test cases
try:
    sum_result = CNIC(1430138428791)
    print(f'Your CNIC is {sum_result}')
except ValueError as e:
    print(e)

try:
    sum_result = CNIC("14301-3842879-1")
    print(f'Your CNIC is {sum_result}')
except ValueError as e:
    print(e)

try:
    sum_result = CNIC("1430138428791")
    print(f'Your CNIC is {sum_result}')
except ValueError as e:
    print(e)
