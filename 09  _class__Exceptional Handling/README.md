# Exceptional-Handling And File_Handling

## Exception Handling: 
In Python is a way to deal with errors that might occur during the execution of a program. It allows you to gracefully manage unexpected situations that could cause your program to crash. The `try`, `except`, `finally`, and `raise` keywords are used to implement exception handling in Python.

Here's a basic example:

```python
def divide_numbers() -> None:
    try:
        # Code block where an exception might occur
        result: float = 10 / 0  # This will raise a ZeroDivisionError
    except ZeroDivisionError as e:
        # Handle the specific exception
        print("Error:", e)
    else:
        # This block is executed if no exception is raised in the try block
        print("No errors occurred.")
    finally:
        # This block is always executed, regardless of whether an exception occurred
        print("Execution complete.")

# Example usage
divide_numbers()

```

In this example:
- The code inside the `try` block is executed.
- If an exception of type `ZeroDivisionError` occurs, it's caught in the `except` block, and a message is printed.
- If no exception occurs, the `else` block is executed.
- Finally, the `finally` block is executed whether an exception occurred or not. It's commonly used for cleanup tasks.

You can also create custom exceptions using the `raise` statement:

```python
def validate_age(age: int) -> None:
    if age < 0 or age > 120:
        raise ValueError("Invalid age!")
    else:
        print("Age is valid.")

try:
    validate_age(150)  # This will raise a ValueError
except ValueError as e:
    print("Error:", e)

```

This code defines a function `validate_age` that raises a `ValueError` if the age is not within a certain range.

Remember, handling exceptions is important for writing robust code, but it's also crucial to handle them appropriately based on the context and potential errors that might arise.

 ## Types Of Error:
In Python, errors can be categorized into three main types:

### Syntax Errors: 
These occur when the code doesn't follow the correct syntax of the Python language. It's often detected by the interpreter when the code is being compiled. For example, missing colons, incorrect indentation, or using an invalid keyword.

### Runtime Errors (Exceptions): 
These occur during the execution of the program. They can happen due to various reasons such as division by zero, trying to access an undefined variable, or attempting to open a file that doesn't exist.

### Semantic Errors (Logical Errors):
These errors don’t cause the program to crash, but they lead to incorrect behavior. The code runs without throwing an error, but it doesn’t produce the expected output due to faulty logic or incorrect algorithms. These errors can be the trickiest to identify since they don’t generate error messages.

Python provides a wide range of built-in exceptions that cover various types of errors. Some common built-in exceptions include SyntaxError, TypeError, NameError, ValueError, ZeroDivisionError, FileNotFoundError, and more. You can handle these exceptions using try-except blocks to gracefully manage errors and prevent the program from crashing.

File handling in Python involves working with files: creating, reading, writing, and manipulating their contents. Python provides built-in functions and methods to perform these operations.

### Opening a File
You can open a file using the open() function, specifying the file path and the mode ('r' for reading, 'w' for writing, 'a' for appending, and more).


### Open a file for reading
```python
file = open('filename.txt', 'r')
```

### Open a file for writing
```python
file = open('filename.txt', 'w')
```

### Open a file for appending
```python
file = open('filename.txt', 'a')
```
Reading from a File
To read the contents of a file, you can use various methods like read(), readline(), or readlines().


### Read the entire file
```python
content = file.read()
```

### Read one line at a time
```python
line = file.readline()
```

### Read all lines into a list
```python
lines = file.readlines()
```
### Writing to a File
To write content to a file, use the write() method. Remember to open the file in write or append mode.
```python

file.write("This is some text.")
```

# To write multiple lines
```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file.writelines(lines)
```
### Closing a File
After performing operations on a file, it's essential to close it using the close() method.
```python
file.close()
```
Using 'with' Statement (Context Manager)
A cleaner way to handle files is by using the with statement. It automatically closes the file once the block is exited.
```python
with open('filename.txt', 'r') as file:
    content = file.read()
```

### File automatically closed outside the block
Error Handling
Handle file-related errors using try and except blocks to ensure graceful handling of exceptions.

```python
from typing import TextIO

def read_file_content(file: TextIO[str]) -> str:
    return file.read()

try:
    with open('filename.txt', 'r') as file:
        content = read_file_content(file)
        # Perform operations on the content
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")
except Exception as e:
    print("An unexpected error occurred:", e)

```
Remember to handle file paths carefully and be cautious while performing write operations as they can overwrite existing content.
