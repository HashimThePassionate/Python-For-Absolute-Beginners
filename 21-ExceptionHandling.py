#What is exception handling
'''
Exception handling is the process of responding to unwanted 
or unexpected events when a computer program runs. Exception 
handling deals with these events to avoid the program or 
system crashing, and without this process, 
exceptions would disrupt the normal operation of a program.

a=1
while a:
    a=a+1
    print(a)
    
''' 
#Python Exceptions
'''
A Python program terminates as soon as it encounters an error. 
In Python, an error can be a "syntax error" or an "exception".
'''
'''
Syntax errors: Also known as parsing errors, are perhaps the 
most common kind of complaint you get while you are still 
learning Python.

Exceptions: This type of error occurs whenever syntactically 
correct Python code results in an error. The last line of 
the message indicated what type of exception error you ran into.

Here are all of Pythons built-in exception
1.ArithmeticError Raised when an error occurs in numeric calculations
2.AssertionError Raised when an assert statement fails
3.AttributeError Raised when attribute reference or assignment fails
4.Exception Base class for all exceptions
5.EOFError Raised when the input() method hits an "end of file" 
condition (EOF)
6.FloatingPointError Raised when a floating point calculation fails
7.GeneratorExit Raised when a generator is closed (with the close() 
method)
8.ImportError Raised when an imported module does not exist
9.IndentationError Raised when indentation is not correct
10.IndexError Raised when an index of a sequence does not exist
11.KeyError Raised when a key does not exist in a dictionary
12.KeyboardInterrupt Raised when the user presses Ctrl+c, Ctrl+z or 
Delete
13.LookupError Raised when errors raised cant be found
14.MemoryError Raised when a program runs out of memory
15.NameError Raised when a variable does not exist
16.NotImplementedError Raised when an abstract method requires 
an inherited class to override the method
17.OSError Raised when a system related operation causes an error
18.OverflowError Raised when the result of a numeric calculation is 
too large
19.ReferenceError Raised when a weak reference object does 
not exist
20.RuntimeError Raised when an error occurs that do not belong 
to any specific expections
21.StopIteration Raised when the next() method of an iterator 
has no further values
22.SyntaxError Raised when a syntax error occurs
23.TabError Raised when indentation consists of tabs or spaces
24.SystemError Raised when a system error occurs
25.SystemExit Raised when the sys.exit() function is called
26.TypeError Raised when two different types are combined
27.UnboundLocalError Raised when a local variable is referenced 
before assignment
28.UnicodeError Raised when a unicode problem occurs
29.UnicodeEncodeError Raised when a unicode encoding problem occurs
30.UnicodeDecodeError Raised when a unicode decoding problem occurs
31.UnicodeTranslateError Raised when a unicode translation problem 
occurs
32.ValueError Raised when there is a wrong value in a specified 
data type
33.ZeroDivisionError Raised when the second operator in a 
division is zero
'''

#Syntax error
'''
a=2
a++ #Error 
a=a+1
a
'''
#ZeroDivisionError 
a=2
c=0
d=a/c
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
"ZeroDivisionError: division by zero"
'''
#The Raising an Exception
'''
We can use raise to throw an exception if a condition occurs. 
The statement can be complemented with a custom exception.

If a condition does not meet our criteria but is correct according to 
the Python interpreter, we can intentionally raise an exception using 
the raise keyword

If you want to throw an error when a certain condition occurs 
using raise, you could go about it like this:
'''
#Example1
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

'''
Traceback (most recent call last):
  File "<input>", line 4, in <module>
Exception: x should not exceed 5. The value of x was: 10
'''

#Example2
num = [3, 4, 5, 7]  
if len(num) > 3:  
    raise Exception( f"Length of the given list must be less than or equal to 3 but is {len(num)}" ) 
'''
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
Exception: Length of the given list must be less than or equal to 3 but is 4
'''

#The AssertionError Exception
'''
The simplest way to understand an assertion to check the condition.
If it finds that the condition is true, it moves to the next line of 
code, and If not, then stops all its operations and throws an error.
It points out the error in the code.
assert Expressions[, Argument]

If this condition turns out to be True, then that is excellent! 
The program can continue. If the condition turns out to be False, 
you can have the program throw an AssertionError exception.
'''
#Example1
def square_root( Number ):  
    assert ( Number < 0), "Give a positive integer"  
    return Number**(1/2)  
  
#Calling function and passing the values  
print( square_root(-36))  
print( square_root(36)) 

'''
Output
(3.6739403974420594e-16+6j)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in square_root
AssertionError: Give a positive integer)
'''
#Example2
def avg(scores):    
    assert len(scores) != 0,"The List is empty."    
    return sum(scores)/len(scores)    
scores2 = [67,59,86,75,92]    
print("The Average of scores2:",avg(scores2))    
scores1 = []    
print("The Average of scores1:",avg(scores1))   

'''
The Average of scores2: 75.8

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in avg
AssertionError: The List is empty.
'''

#The try and except Block
'''
In Python, we catch exceptions and handle them using try and except 
code blocks. The try clause contains the code that can raise an 
exception, while the except clause contains the code lines that handle 
the exception. Let's see if we can access the index from the array, 
which is more than the array's length, and handle the resulting 
exception.
'''
#Example
a = ["Python", "Exceptions", "try and except"]  
try:  
    #looping through the elements of the array a, choosing a range that goes beyond the length of the array  
     for i in range( 4 ):  
        print( "The index and element from the array is", i, a[i] )  
#if an error occurs in the try block, then except block will be executed by the Python interpreter       
except:  
    print ("Index out of range")  
'''

Output
The index and element from the array is 0 Python
The index and element from the array is 1 Exceptions
The index and element from the array is 2 try and except
Index out of range

'''
#Try with Else Clause
'''
If there is no exception, this code block will be executed by 
the Python interpreter 
'''
def reciprocal( num1 ):  
    try:  
        reci = 1 / num1  
    except ZeroDivisionError:  
        print( "We cannot divide by zero" )  
    else:  
        print ( reci )  
# Calling the function and passing values  
reciprocal( 4 )  
reciprocal( 0 )

'''
0.25
"We cannot divide by zero" 
'''

#Finally Keyword in Python
'''
The finally keyword is available in Python, and it is always used 
after the try-except block. The finally code block is always executed 
after the try block has terminated normally or after the try block 
has terminated for some other reason.
'''
# Python code to show the use of finally clause  

try:  
    div = 4 / 0    
    print( div )  
# this block will handle the exception raised  
except ZeroDivisionError:  
    print( "Attepting to divide by zero" )  
# this will always be executed no matter exception is raised or not  
finally:  
    print( 'This is code of finally clause' )  

'''
Output
Atepting to divide by zero
This is code of finally clause

# Custom Exception in python using Custom Class
class InvalidAgeError(Exception):
    pass


no: int = 18
try:
    input_user: int = int(input('Please Enter Your Age!'))
    if input_user < no:
        raise InvalidAgeError
    else:
        print('You Are Eligible For Vote')
except InvalidAgeError:
    print('Exception occurred : You are not Eligible for Vote ')
'''
