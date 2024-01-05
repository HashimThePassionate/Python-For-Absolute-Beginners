

## Module Repository:
A module is a file containing Python definitions and statements.
A module is a file containing group of variables, methods, function and classes etc. 
They are executed only the first time the module name is encountered in an import statement.
The file name is the module name with the suffix .py appended. 
Ex:- mymodule.py

### Type of Modules:-
1. User-defined Modules
2. Built-in Modules
         


## Built In Module

Built-in modules in Python are collections of pre-written code that come as a part of the Python standard library. They provide a wide range of functionalities for various tasks, ready to be used in your programs without the need for external installations.

## Types of Built-In modules

Here are the major categories of built-in Python modules along with their purposes:

### Mathematical and Numerical Modules:


### Advanced functionalities:

 Are you curious about advanced functionalities like complex number operations, numerical precision control, or statistical distributions?

### 1. Math:
 
 Provides access to mathematical functions like trigonometric, logarithmic, exponential, and numerical operations.

```python
import math

# Trigonometric functions
def calculate_trigonometric() -> None:
    sin_result: float = math.sin(math.pi / 4)
    print(sin_result)  # Output: 0.7071067811865475

    cos_result: float = math.cos(math.pi)
    print(cos_result)  # Output: -1.0

    tan_result: float = math.tan(0)
    print(tan_result)  # Output: 0.0

# Logarithmic and exponential functions
def calculate_logarithmic_exponential() -> None:
    log_result: float = math.log10(100)
    print(log_result)  # Output: 2.0

    exp_result: float = math.exp(1)
    print(exp_result)  # Output: 2.718281828459045

# Rounding functions
def calculate_rounding() -> None:
    ceil_result: float = math.ceil(3.14)
    print(ceil_result)  # Output: 4.0

    floor_result: float = math.floor(3.99)
    print(floor_result)  # Output: 3.0

# Mathematical constants
def print_math_constants() -> None:
    pi_value: float = math.pi
    print(pi_value)  # Output: 3.141592653589793

    e_value: float = math.e
    print(e_value)  # Output: 2.718281828459045

# Example usage
calculate_trigonometric()
calculate_logarithmic_exponential()
calculate_rounding()
print_math_constants()


```

### 2. random:
 
 Generates random numbers and implements functions for random sampling and shuffling.

```python
from random import randint

def generate_random_number() -> int:
    return randint(1, 10)

# Example usage
random_number: int = generate_random_number()
print(random_number)

 

```

### 3. statistics:
 
 Calculates basic statistical measures like mean, median, mode, variance, standard deviation, and more.


## Data Handling Modules:


### 1. collections:

Offers specialized container data types like namedtuples, deques, counters, and OrderedDict.

```python
from collections import namedtuple

# Define the type for the namedtuple
class Person:
    def __init__(self, name: str, age: int, city: str) -> None:
        self.name = name
        self.age = age
        self.city = city

# Create an instance of the Person class
person: Person = Person(name='Alice', age=30, city='New York')

# Access attributes with type hints
print(person.name)
 

# Output: Alice

```

### 2. datetime: 

Handles dates and times, allowing operations like manipulation, formatting, and calculations.

```python
from datetime import datetime

# Define the type for the 'now' variable
now: datetime = datetime.now()

# Print the formatted date and time
print(now.strftime("%Y-%m-%d %H:%M:%S"))
 

# Output: e.g., 2024-01-05 15:35:00

```

### 3. json: 

Encodes and decodes JSON data, facilitating data exchange with web services.

### 4. re: 

Implements regular expression operations for pattern matching and text manipulation.

## System Interaction Modules:


### 1. os: 

Provides functions for interacting with the operating system, such as file system operations, environment variables, and process management.

```python
import os

# Get the current working directory
current_directory: str = os.getcwd()
print(current_directory)

# Create a new folder
new_folder_path: str = 'new_folder'
os.mkdir(new_folder_path)


# Create a new folder

```

### 2. sys: 

Accesses system-specific parameters and functions, including command-line arguments and interpreter information.


```python
import sys
print(sys.argv)  # Access command-line arguments
#Output:['c:/Users/hp/Desktop/a/ab.py']
```

### 3. Platform: 

Provides information about the current platform and operating system.


## File I/O Modules:

### 1. io: 

Offers a core set of tools for working with various types of I/O, including files, streams, and buffers.

```python
from typing import TextIO

# Open a file and write to it
file_path: str = 'my_file.txt'
with io.open(file_path, 'w', encoding='utf-8') as file:  # type: TextIO
    file.write('Hello, world!')

#Output:PS C:\Users\hp\Desktop\a> & C:/Users/hp/AppData/Local/Programs/Python/Python311/python.exe c:/Users/hp/Desktop/a/ab.py

```

### 2. OS.path: 

Manipulates file paths and names, handling path manipulations and directory operations.


## Concurrency Modules:


### 1. Threading: 

Enables multithreaded programming for concurrent execution of tasks.

```python
import threading

def worker() -> None:
    print("Hello from a thread!")

# Create a thread with the specified target function
thread: threading.Thread = threading.Thread(target=worker)

# Start the thread
thread.start()

#output:Hello from a thread!
```

### 2. Multiprocessing: 

Utilizes multiple processes for parallel execution across multiple cores.


## Networking Modules:


### 1. Socket: 

Provides access to the underlying socket API for network communication.

```python
from typing import Optional

# Make the request and read the response content
url: str = 'https://www.example.com'
response: urllib.request.Response = urllib.request.urlopen(url)  # type: Optional[urllib.request.Response]

# Check if the response is not None before reading
if response is not None:
    response_content: bytes = response.read()
    print(response_content)

# Output: PS C:\Users\hp\Desktop\a> & C:/Users/hp/AppData/Local/Programs/Python/Python311/python.exe c:/Users/hp/Desktop/a/ab.py

```

### 2. urllib: 

Offers functions for working with URLs and retrieving data from the web.

### 3. http.client: 

Implements a client-side HTTP protocol for connecting to web servers.

## Other Useful Modules:


### 1. Itertools: 

Provides functions for working with iterators and generating efficient sequences.

### 2. Functools: 

Offers high-order functions and tools for working with functions and callable objects.

### 3. operator: 

Contains a collection of built-in operators as functions for convenient manipulation.

##  Benefits of Built-In modules:
1. Ready-to-use functionality:

Provide a vast range of functions and classes for common tasks, saving you time and effort from writing code from scratch.
Cover various domains, including:
Math (math, random)
Data structures (collections, array)
File I/O (os, shutil, pathlib)
Data manipulation (csv, json, xml)
Web interactions (urllib, http)
System interactions (sys, os, platform)
Date and time (datetime)
Regular expressions (re)
And many more!

2.  Enhanced code reusability:

Promote code reuse across different projects, leading to:
More efficient development
Reduced code duplication
Increased consistency

3. Improved code readability:

Organize code into logical units, making it easier to understand and maintain.
Abstract away complex details, allowing you to focus on the higher-level logic of your program.

4. Reduced development time:

Eliminate the need to search for, install, and learn external libraries for common tasks.
Streamline development by providing a wide range of ready-to-use tools.

5. Quality and consistency:

Built-in modules are meticulously tested and maintained by the Python community, ensuring reliability and compatibility.
Offer consistent interfaces and behavior across different Python environments.

6. Cross-platform compatibility:

Work seamlessly on different operating systems, without requiring platform-specific modifications.
Facilitate the development of portable applications.

7. Access to core language features:

Provide essential functionalities that are integral to the Python language itself, such as:
Object introspection (the inspect module)
Debugging and profiling (the pdb module)
Code execution (the exec module)
Dynamic code generation (the code module)


## User defined module

1. They are Python files (with a .py extension) that you create yourself to organize and reuse code.
2. They can contain functions, classes, variables, and other Python elements.
3. They promote modularity, code reusability, and better project structure.
### Example of user defined module
### cal.py
```python
def square(myList:list) -> list:
    return [i**2 for i in myList]


def info(**what:dict)->None:
    for key, value in what.items():
        print(f"{key} is {value}")

def add(a : int, b: int) ->int:
    return a+b
``` 
     
### error.py
This file handles errors:
```python
def zeroError(a : int) -> str:
    if (a == 0):
        raise "Zero Division Error"
    else:
      return "You nailed it!"
```      
### msg.py

This file contains a multiline message:
```python
message: str: Welcome message with a Python programming theme.
line: str: A simple line.
```
### main.py

This example demonstrates the usage of functions from the other files:
```python
from typing import List, Dict

from msg import message as M, line as L
from cal import square as s, add as a, info as i
from error import zeroError as e

# Access variables
print(L)  # Assuming line is a string
print(M)  # Assuming message is a string
print(L)  # Assuming line is a string

# Use functions with static typing
lt: List[int] = s([1, 2, 3, 4, 5, 6])  # Assuming square returns a list of integers
add: int = a(10, 5)  # Assuming add returns an integer
dt: Dict[str, int] = i(name="Umer", age=1)  # Assuming info returns a dictionary

# Example of using the zeroError function
try:
    e(0)
except ValueError as error:
    print("Error:", error)

```
### Example Output
```python
THANK YOU
Welcome to Our
    Python Programming
                        World
Python is not For Innocent People
THANK YOU
{'name': 'Umer', 'age': 16}
THANK YOU
[1, 4, 9, 16, 25, 36]
THANK YOU
15
THANK YOU
You nailed it!
THANK YOU
```

## Benefits of user-defined modules:
1. Code organization: Break down large programs into smaller, more manageable modules.
2. Reusability: Use the same code in multiple scripts without duplication.
3. Maintainability: Easier to update and test code in separate modules.
4. Namespace management: Avoid naming conflicts by keeping code in separate modules.

## Package Repository:
 This repository contains a Python package that demonstrates basic usage and organization of a package. ###Step-by-Step Guide: ##Create the Package:

Create a directory named MyPythonPackage. Inside it, create a subdirectory named mypackage. In mypackage, create two files:

init.py: An empty file to mark the directory as a package.

module_inside_package.py: Content of this file should be:

### mypackage/module_inside_package.py
### Example
```python
def multiply(a:int, b:int)->int:
    return a * b
##Create the Main Script:

create a file named main_package.py with the following content:

# main_package.py

# Import the multiply function from mypackage
from mypackage.module_inside_package import multiply

if __name__ == "__main__":
    # Use the imported function
    result = multiply(3, 5)
    print("Result:", result)
```    
### output:
```python
Result: 15
```


        

        
