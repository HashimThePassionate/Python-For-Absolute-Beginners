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
a: int =2
c : int= 0
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
x : int = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

'''
Traceback (most recent call last):
  File "<input>", line 4, in <module>
Exception: x should not exceed 5. The value of x was: 10
'''

#Example2
num : list= [3, 4, 5, 7]  
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
def square_root( Number: int )->None:  
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
def avg(scores : int)-> int:    
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
a : list = ["Python", "Exceptions", "try and except"]  
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
def reciprocal( num1 : int )-> None :  
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
'''
_____________________________________________________________________________________________________________________________________

# Examples of Error Handling

# Call by Value
# a : int = 5
# def abc(num : int ) -> None:
#     num = 6
#     print(id(num))
#     print(num)

# print(id(a))
# abc(a)
# print(a)

# Call by Reference
# l : list = [1,2,3,4,5]
# def myList(newList : list[int]) -> None:
#     print(newList)
#     print(id(newList))
#     newList.append(6)

# print(id(l))
# myList(l)
# print(l)


# a = int(input("Please Enter a Number\t"))
# b = int(input("Please Enter another Number\t"))

# res : int = (a/b)
# print(f"Value is {res}")


# a : int = 1
# while(True):
#     print(a)
#     a += a

# l: list[int] = [1,2,3]
# try:
#     # a = int(input("Please Enter a Number\t"))
#     # b = int(input("Please Enter another Number\t"))
#     # print(a/b)
#     print(k[3])
# except ZeroDivisionError:
#     print("You cannot Divide any number with zero")
# except IndexError:
#     print('List does not contain that index number')
# except NameError:
#     print('Variable name is not valid')
#     # pass


# Raising an Exception
# x : int = 10
# if x > 5:
#     raise Exception(f'x should not exceed 5. The value of x was: {x}')

# num = [3, 4, 5, 7]  
# if len(num) > 3:  
#     raise Exception( f"Length of the given list must be less than or equal to 3 but is {len(num)}" ) 

# Assertion Exception

_________________________________________________________________________________________________________________________________________________


def square_root( Number : int ) -> int:  
    assert ( Number < 0), "Give a positive number"
    return Number**(1/2)  
  
#Calling function and passing the values  
no1 : int = square_root(-36)
no2 : int = square_root(36)
print(no1)  
# print(no2) 

________________________________________________________________________________________________________________________________________________________

# Python Guide
# Table of Contents
# Pass by Reference vs Pass by Value
# Mutable and Immutable Variables
# Runtime Error Classes
# Try-Except-Else-Finally Block
# YouTube link
# 2 hour live session

# Pass by Reference vs Pass by Value
# In Python, the way variables are passed to functions can be thought of as "pass by object reference". This means that the function receives a reference to the object, not a copy of the object. However, the behavior can seem like "pass by value" or "pass by reference" depending on whether the object is mutable or immutable.

# Example: Pass by Value (with Immutable Types)
def modify_value(num: int)-> None:
    print("Inside function (before modification):", id(num))
    num = 10
    print("Inside function (after modification):", id(num))

x : int = 5
print("Before function call:", id(x))
modify_value(x)
print("After function call:", id(x))
# In this example, x is an integer (which is immutable). When we pass x to the function and modify it inside the function, the id (memory address) of num inside the function changes, indicating that a new integer object has been created. The id of x outside the function remains the same.

# Example: Pass by Reference (with Mutable Types)
def modify_list(lst: list)-> None:
    print("Inside function (before modification):", id(lst))
    lst.append(4)
    print("Inside function (after modification):", id(lst))

my_list : list= [1, 2, 3]
print("Before function call:", id(my_list))
modify_list(my_list)
print("After function call:", id(my_list))
# In this example, my_list is a list (which is mutable). When we pass my_list to the function and modify it inside the function, the id of lst inside the function remains the same, indicating that the same list object is being modified. The id of my_list outside the function also remains the same.

# Mutable and Immutable Variables
# Variables in Python can be either mutable or immutable.

# Mutable types can be changed after they are created. Examples include lists, dictionaries, and sets.
# Immutable types cannot be changed after they are created. Examples include integers, floats, strings, and tuples.
# Example: Mutable Type
my_list : list = [1, 2, 3]
print("Before modification:", my_list, "id:", id(my_list))
my_list.append(4)
print("After modification:", my_list, "id:", id(my_list))
# In this example, the list my_list is modified in place, and its id remains the same.

# Example: Immutable Type
my_string : str= "hello"
print("Before modification:", my_string, "id:", id(my_string))
my_string = my_string + " world"
print("After modification:", my_string, "id:", id(my_string))
# In this example, when we modify my_string, a new string object is created, and the id of my_string changes.

# Runtime Error Classes
# Python has several built-in error classes to handle runtime errors. Here are examples of some common runtime errors:

# IndexError
# Occurs when trying to access an index that is out of range.

try:
    my_list :list = [1, 2, 3]
    print(my_list[3])  # This will raise an IndexError
except IndexError as e:
    print("Caught an IndexError:", str(e))
ZeroDivisionError
# Occurs when dividing by zero.

try:
    result : int= 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print("Caught a ZeroDivisionError:", str(e))
# Try-Except-Else-Finally Block
# The try-except-else-finally block in Python is used for exception handling.

# The try block contains the code that may raise an exception.
# The except block contains the code that is executed if an exception is raised.
# The else block contains the code that is executed if no exceptions are raised.
# The finally block contains the code that is always executed, regardless of whether an exception is raised.
try:
    numerator :int = 10
    denominator : int = 2
    result = numerator / denominator
except ZeroDivisionError as e:
    print("Caught a ZeroDivisionError:", str(e))
else:
    print("Division successful:", result)
finally:
    print("This block is always executed")
    _________________________________________________________________________________________________________________________________________________
    
    
    #Python File Handling
'''
The file handling plays an important role when the data needs 
to be stored permanently into the file. A file is a named location
on disk to store related information. We can access the stored 
information (non-volatile) after the program termination.

The file-handling implementation is slightly lengthy or complicated in 
the other programming language, but it is easier and shorter in Python.

Hence, a file operation can be done in the following order.

1. Open a file
2. Read or write - Performing operation
3. Close the file

'''
#Opening a file
'''
Python provides an open() function that accepts two arguments, 
"file name" and "access mode" in which the file is accessed. 
Syntax:

file object = open(<file-name>, <access-mode>)  
e.g
path = 'C:\\Users\\DELL\\Desktop\\python-course-for-beginner\\Newfile.txt'
file = open (path, "r")
file.close()

SN	    Access mode     	Description
1	      r	             It opens the file to read-only mode. The file 
                            pointer exists at the beginning. The file is by 
                            default open in this mode if no access mode is 
                            passed.
2       	rb	             It opens the file to read-only in binary format.
                            The file pointer exists at the beginning of the 
                            file.
3       	r+	             It opens the file to read and write both. The 
                            file pointer exists at the beginning of the file.
4       	rb+	             It opens the file to read and write both in
                            binary format. The file pointer exists at the 
                            beginning of the file.
5          w	             It opens the file to write only. It overwrites 
                            the file if previously exists or creates a new 
                            one if no file exists with the same name. The 
                            file pointer exists at the beginning of the file.
6       	wb	             It opens the file to write only in binary format. 
                            It overwrites the file if it exists previously 
                            or creates a new one if no file exists. The file
                            pointer exists at the beginning of the file.
7       	w+	             It opens the file to write and read both. It is 
                            different from r+ in the sense that it overwrites 
                            the previous file if one exists whereas r+ doesn't 
                            overwrite the previously written file. It creates 
                            a new file if no file exists. The file pointer 
                            exists at the beginning of the file.
8	     wb+               It opens the file to write and read both in binary 
                            format. The file pointer exists at the beginning 
                            of the file.
9       	 a	             It opens the file in the append mode. The file 
                            pointer exists at the end of the previously 
                            written file if exists any. It creates a new 
                            file if no file exists with the same name.
10	      ab	             It opens the file in the append mode in binary 
                            format. The pointer exists at the end of the 
                            previously written file. It creates a new file 
                            in binary format if no file exists with the 
                            same name.
11	      a+	             It opens a file to append and read both. The 
                            file pointer remains at the end of the file if 
                            a file exists. It creates a new file if no file 
                            exists with the same name.
12	      ab+	             It opens a file to append and read both in 
                            binary format. The file pointer remains at the 
                            end of the file.

'''
#Example1 to open file Successfully
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
file = open(path,"r")  
print(file)  
if file:    
    print("file is opened successfully") 

'''
Output
file is opened successfully
'''

#The close() method
'''
Once all the operations are done on the file, we must close it through 
our Python script using the close() method. Any unwritten information 
gets destroyed once the close() method is called on a file object

Syntax
file.close()  
'''
#Example using close method
#opens the file in read mode    

#We should use the following method to overcome such type of problem.
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
try:    
   file = open(path)  
   print(file) 
   print("File Opened Successfully")
   # perform file operations  
finally:  
   file.close() 

#The with statement
'''
The with statement was introduced in python 2.5. The with statement 
is useful in the case of manipulating the files. It is used in the 
scenario where a pair of statements is to be executed with a block 
of code in between

with open(<file name>, <access mode>) as <file-pointer>:    
    #statement suite  

e.g
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
with open(path, "r") as file:
     Statement1
     statement2
     statement3



     statements

It is always suggestible to use the with statement in the case of files 
because, if the break, return, or exception occurs in the nested block 
of code then it automatically closes the file, we don't need to write
the close() function. It doesn't let the file to corrupt. 

'''
#Example "with" Statement
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
with open(path,'r') as file:    
    content = file.read();    
    print(content)  

#Writing the file
'''
w: It will overwrite the file if any file exists. The file pointer is 
at the beginning of the file.

a: It will append the existing file. The file pointer is at the end of 
the file. It creates a new file if no file exists.

'''
#Using Write Example
# open the file.txt in append mode. Create a new file if no such file exists.  
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
with open(path, "w") as file:  
     file.write("""Python is the modern day language. It makes things so simple. 
It is the fastest-growing programing language""")  

#using Append Example 
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
with open(path, "a") as file:  
     file.write("""\nPython has an easy syntax and user-friendly interaction.""")
    
#Reading text from file using read() method
'''
The syntax of the read() method is given below.

Syntax:

content= file.read(10) #<count> read only first 10 characters
or
content1= file.read() #read complete text

'''
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
with open(path, "r") as file:
     content = file.read(10)
     print(type(content)) 
     print("print first 10 letters")
     print(content)    

with open(path, "r") as file:
     content = file.read()
     print("print everything to the end")
     print(content)

#Read file through for loop
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
print("\nPrint Through For Loop\n")
with open(path, "r") as file:
     for i in file:    
         print(i) 

#Read Line of the file
'''
Python facilitates to read the file line by line by using a function 
readline() method. The readline() method reads the lines of the file 
from the beginning, i.e., if we use the readline() method two times, 
then we can get the first two lines of the file.
'''
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
with open(path, "r") as file:
     content1 = file.readline() 
     content2 = file.readline()
     #it will print two lines bcz we use two times
     print(content1)
     print(content2)

# Reading Lines Using readlines() function that reads everyline
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
with open(path, "r") as file:
     content = file.readlines()
     print(content)
'''
Output
['Python is the modern day language. It makes things so simple. \n', 
'It is the fastest-growing programing language\n', 
'Python has an easy syntax and user-friendly interaction']

'''

#Creating a new file
'''
x: it creates a new file with the specified name. It causes an error a 
file exists with the same name.

a: It creates a new file with the specified name if no such file exists. 
It appends the content to the file if the file already exists with the 
specified name.

w: It creates a new file with the specified name if no such file exists. 
It overwrites the existing file

'''

#Using x
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
with open(path, "x") as file:
     print(file)    
     if file:    
        print("File created successfully")  

'''
Output
File Already Exists thats why error show
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileExistsError: [Errno 17] File exists: r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
'''
______________________________________________________________________________________________________________________________________________________




# Python Error Handling and File Handling Guide
# This guide provides an overview of error handling techniques in Python, including creating custom errors and dynamic error handling. It also covers file handling with various access modifiers and reading files of different types such as CSV, PDF, Excel, and audio files.

# YouTube link
# 2 hour live session

# Table of Contents
# Error Handling
# Try-Except-Else
# Multiple Except Blocks
# Creating Custom Errors
# Dynamic Error Handling
# File Handling with Access Modifiers
# Read Mode (r)
# Read and Write Mode (r+)
# Write Mode (w)
# Write and Read Mode (w+)
# Append Mode (a)
# Append and Read Mode (a+)
# Binary Read Mode (rb)
# Reading Files
# Reading CSV Files
# Reading PDF Files
# Reading Excel Files
# Reading Audio Files
# Error Handling
# Try-Except-Else
# Using try, except, and else blocks allows you to handle errors gracefully and execute code when no errors occur.

def divide(a: float, b: float) -> float:
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return 0.0
    else:
        print("Division successful")
        return result
# Multiple Except Blocks
# You can handle different types of exceptions using multiple except blocks.

def convert_to_int(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        print("Invalid integer!")
        return 0
    except TypeError:
        print("Value must be a string!")
        return 0
# Creating Custom Errors
# You can create custom error classes by inheriting from the base Exception class.

class NegativeValueError(Exception):
    def __str__(self) -> str:
        return "Value cannot be negative"

def sqrt(value: float) -> float:
    if value < 0:
        raise NegativeValueError()
    return value ** 0.5
# Dynamic Error Handling
# You can handle errors dynamically by capturing the exception and analyzing it.

def dynamic_error_handling(value: str) -> int:
    try:
        return int(value)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 0
# File Handling with Access Modifiers
# Read Mode (r)
# Opens a file for reading.

with open('file.txt', 'r') as f:
    content = f.read()
    print(content)
# Read and Write Mode (r+)
# Opens a file for reading and writing.

with open('file.txt', 'r+') as f:
    content = f.read()
    print(content)
    f.write("New line")
# Write Mode (w)
# Opens a file for writing, creates the file if it does not exist, and truncates the file if it exists.

with open('file.txt', 'w') as f:
    f.write("Hello, World!")
# Write and Read Mode (w+)
# Opens a file for writing and reading.

with open('file.txt', 'w+') as f:
    f.write("Hello, World!")
    f.seek(0)
    content = f.read()
    print(content)
# Append Mode (a)
# Opens a file for appending, creates the file if it does not exist.

with open('file.txt', 'a') as f:
    f.write("Appending line")
# Append and Read Mode (a+)
# Opens a file for appending and reading.

with open('file.txt', 'a+') as f:
    f.write("Appending line")
    f.seek(0)
    content = f.read()
    print(content)
# Binary Read Mode (rb)
# Opens a file in binary read mode.

with open('file.txt', 'rb') as f:
    content = f.read()
    print(content)
# Reading Files
# Reading CSV Files
# You can use the csv module to read CSV files.

import csv

with open('file.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# Reading PDF Files
# You can use the PyPDF2 library to read PDF files.

# import PyPDF2

with open('file.pdf', 'rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    text = reader.getPage(0).extractText()
    print(text)
# Reading Excel Files
# You can use the openpyxl library to read Excel files.

from typing import openpyxl

wb = openpyxl.load_workbook('file.xlsx')
sheet = wb.active
cell = sheet['A1']
print(cell.value)
# Reading Audio Files
# You can use the pydub library to read audio files.

from typing import pydub , AudioSegment

audio = AudioSegment.from_file("file.mp3")
print("Channels:", audio.channels)
print("Sample Width:", audio.sample_width)
print("Frame Rate:", audio.frame_rate)
print("Frame Width:", audio.frame_width)
print("Length (ms):", len(audio))
print("Frame Count:", audio.frame_count())
# Remember to install the necessary libraries before running the code examples.

# pip install PyPDF2 openpyxl pydub
# This README provides a comprehensive guide on various error handling and file handling techniques in Python, along with examples of reading different file types. Feel free to modify and extend it as per your project's requirements.
# _________________________________________________________________________________________________________________________________________________

# Examples of Try Except Else 
# def avg(scores):    
#     assert len(scores) != 0,"The List is empty."    
#     return sum(scores)/len(scores)    
# scores2 = [67,59,86,75,92]    
# print("The Average of scores2:",avg(scores2))    
# scores1 = []    
# print("The Average of scores1:",avg(scores1))   

# def square_root( Number ):  
#     assert ( Number < 0), "Give a positive integer"  
#     return Number**(1/2)  
  
# #Calling function and passing the values  
# print( square_root(-36))  
# print( square_root(36)) 

a : list[str] = ["A","B","C"]
# a  : list = "usman"
# print(a)
# a  : list = "USMAN"
# print(a)

# print(a[3])
# try:
#     print(a[3])
# except IndexError:
#     print("Index does not assign")

# a = ["Python", "Exceptions", "try and except"]  
# try:  
#     #looping through the elements of the array a, choosing a range that goes beyond the length of the array  
#      for i in range( 4 ):  
#         print( "The index and element from the array is", i, a[i] )  
# #if an error occurs in the try block, then except block will be executed by the Python interpreter       
# except:  
#     print ("Index out of range")  


# def reciprocal( num1 ):  
#     try:  
#         reci = 1 / num1  
#     except ZeroDivisionError:  
#         print( "We cannot divide by zero" )  
#     else:  
#         print ( reci )  
# Calling the function and passing values  
# reciprocal( 4 )  
# reciprocal( 0 )

# class SobadarError(Exception):
#     def __str__(self) -> str:
#         return "We cannot divide by zero"
    
# def rep(value : int ) -> int:
#     if value==0:
#         raise SobadarError()
#     return 1 / value 

# a : int = rep(10)
# b : int = rep(0)
# print(a)
# print(b)

# def dynamic_error_handling(value:int) -> int:
#     try:
#         return [i**2 for i in value]
#     except Exception as e:
#         print(f"An error occurred: str({e})")
#         return 0

class NotFound(Exception):
    def __str__(self) -> str:
        return "This username is not found in DB"
    
def check(value : str) -> str:
    # student : list = {'M': 'mowahid', 'A': 'abdullah', 'R': 'raheem', 'N': 'nadia', 'B': 'butt', 'M': 'maaz'}
    student : list = ['mowahid','ahmed','nadia','abdullah']
    for i in student:
        if i == value:
            return value
    raise NotFound() 
    
name : str = input("Please Enter Your Name!")
string : str = check(name)
print(f'Username {string} is found in Database')


# a : list = dynamic_error_handling([1,2,3,4,5,6,7,9])
# print(a)
