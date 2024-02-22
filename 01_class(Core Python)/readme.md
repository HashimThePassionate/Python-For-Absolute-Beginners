# Comprehensive Guide to Programming Basics


This repository serves as a comprehensive guide to fundamental programming concepts using [programming language]. Whether you are a beginner or seeking a refresher, this README file covers essential topics.


## Table of Contents.

1. [Numbers](#1-numbers)
2. [Comments](#2-comments)
3. [Literals](#3-literals)
4. [Variables](#4-variables)
5. [Operators](#5-operators)
6. [User Input](#6-user-input)
7. [f-String](#7-f-String)
8. [Format](#8-Format)

# 1. Numbers

Numbers in programming are used for mathematical operations and storing numeric data. They can be integers or floating-point numbers. numbers in Python are essential for various programming tasks, from basic arithmetic operations to complex algorithms and data manipulation. They provide a flexible and powerful way to work with numerical data in the context of programming.


```python
Example 1: Integer

x : int = 5
temperature : float = 
Represents a whole number.
```

```python
Example 2: Floating-point
python
Copy code
y : float = 3.14
Represents a decimal or floating-point number.
```
```python
Example 3: Arithmetic Operations

x: int = 5
y: int = 3

result_add: int = x + y
result_multiply: int = x * y
result_divide: float = y / x
result_power: int = x ** 2
result_modulo: int = x % 2
```
```python

Example 4: Increment and Decrement
x: int = 5
y: float = 3.0

x += 1  # Increment x by 1
y -= 0.5  # Decrement y by 0.5

Shows how to increment and decrement variables.
```
```python
Example 5: Type Conversion

float_value: float = 3.75
int_value: int = 2

float_to_int: int = int(float_value)
int_to_float: float = float(int_value)

Illustrates converting between data types. 
```

```python
Example 6: Complex Numbers

real_part: float = 2.0
imaginary_part: float = 3.0

complex_num: complex = complex(real_part, imaginary_part)

Introduces complex numbers in programming.
```

# 2. Comments.

In Python, comments are lines of text in your code that are not executed as part of the program. They are meant for human readers to understand the code better. Python supports two types of comments: single-line comments and multi-line comments.

### 1. Single-line Comment

Single-line comments start with the # symbol and continue to the end of the line. Everything after # on that line is considered a comment and is ignored by the Python interpreter.


```python
# This is a single-line comment

print("Hello, World!")  # This is also a comment

Provides a brief comment on a single line.
```

### Multi-line Comments:

While Python doesn't have a built-in syntax for multi-line comments, you can use triple-quotes (''' or """) to create a multi-line string, and it's often used as a way to add multi-line comments. Although it's not ignored like a traditional comment, it serves the purpose of commenting out multiple lines.

```python
'''
This is a multi-line comment
spanning multiple lines.
'''
print("Hello, World!")

Demonstrates a comment spanning multiple lines.
```

# 3. Literals

In Python, literals are notations for representing fixed values in your source code. They are constants that represent data types directly, and their values are fixed and cannot be changed. Here are some common types of Python literals:

```python 
String Literal

message: str = "Hello, World!"
```
```python 
Boolean Literals

is_true: bool = True
is_false: bool = False
```
```python 
Numeric Literals

integer_literal: int = 42
float_literal: float = 3.14
```
```python 
String Concatenation

greeting: str = "Hello"
name: str = "John"
full_greeting: str = greeting + ", " + name + "!"
```
```python 
Boolean Expressions

x: int = 5
y: int = 3
greater_than: bool = (x > y)
equal_or_greater: bool = (x >= y)
not_equal: bool = (x != y)
```
```python 
Raw String Literal

file_path: str = r"C:\Users\username\Documents"
```

# 4. Variables

### The crucial use of Variables.

Variables are containers for storing data values. They are created using a variable name and assigned a value.

Variables facilitate the storage, retrieval, and manipulation of data during program execution. They serve as containers for values of different types, enabling dynamic and adaptable data handling.
Code Readability and Organization:

Variables play a pivotal role in creating flexible and modular code. They allow for dynamic values, function arguments, and the building of reusable components, fostering adaptability and maintainability in programming.

```python 
Example 1: Variable Assignment

age : int = 25
name : str = "Ahmed"
height : float = 5.5
quize : bool =  true

Assigns a value to a variable.
```

```python
Example 2: Variable Reassignment

age : str = age + 1
age : str = age * 2

Demonstrates changing the value of a variable.
```
```python 
Example 3: Multiple Assignments

a: int
b: int
c: int
a, b, c  : int = 1, 2, 3

Illustrates multiple assignments in a single line.
```
```python 
Example 4: Swapping Variables

x: int = 5
y: int = 10
temp: int = x
x = y
y = temp

Shows how to swap values between variables.
```
```python 
Example 5: Dynamic Typing

dynamic_variable : float= 3.14
dynamic_variable : str = "Hello"

Introduces dynamic typing in programming.
```
```python 
Example 6: Variable Naming Conventions

user_input_value : str = "example"

Follows a recommended naming convention for variables.
```



# 5. Operators

In Python, operators are symbols that perform operations on variables and values. They are fundamental components of expressions and statements, allowing you to manipulate and process data. Python supports various types of operators, which can be categorized as follows.

### 1. Arithmetic Operators:

Perform mathematical operations on numeric values.

Addition: +
Subtraction: -
Multiplication: *
Division: /
Floor Division: //
Modulus (Remainder): %
Exponentiation: **

```python
result_addition: int = 5 + 3
result_subtraction: int = 7 - 2
result_multiplication: int = 4 * 6
result_division: float = 10 / 2
result_floor_division: int = 17 // 3
result_modulus: int = 17 % 3
result_exponentiation: int = 2 ** 4
```

### 2. Assignment Operators:

Assign values to variables and perform operations in a concise way.

Assignment: =
Addition assignment: +=
Subtraction assignment: -=
Multiplication assignment: *=
Division assignment: /=
Modulus assignment: %=
Floor division assignment: //=
Exponentiation assignment: **=

```python
x: int = 5
x += 3  # Equivalent to x = x + 3
y: float = 10
y /= 2  # Equivalent to y = y / 2
```

### 3. Comparison Operators:

Compare two values and return a Boolean result (True or False).

Equal to: ==
Not equal to: !=
Greater than: >
Less than: <
Greater than or equal to: >=
Less than or equal to: <=

```python 
result_equal: bool = 5 == 5
result_not_equal: bool = 10 != 7
result_greater_than: bool = 8 > 3
result_less_than: bool = 6 < 9
result_greater_equal: bool = 5 >= 5
result_less_equal: bool = 3 <= 4
```
### 4. Logical Operators:

Perform logical operations on Boolean values.

Logical AND: and
Logical OR: or
Logical NOT: not

```python 
result_logical_and: bool = True and False
result_logical_or: bool = True or False
result_logical_not: bool = not True
```

### 5. Bitwise Operators:

Perform bitwise operations on integers.

Bitwise AND: &
Bitwise OR: |
Bitwise XOR: ^
Bitwise NOT: ~
Left shift: <<
Right shift: >>

```python 
result_bitwise_and: int = 0b1010 & 0b1100
result_bitwise_or: int = 0b1010 | 0b1100
result_bitwise_xor: int = 0b1010 ^ 0b1100
result_bitwise_not: int = ~0b1010
```
### 6. Membership Operators 

Check for membership in sequences.

In: in
Not in: not in

```python 
fruits: list[str] = ['apple', 'orange', 'banana']
result_in: bool = 'apple' in fruits
result_not_in: bool = 'grape' not in fruits
```
### 7. Identity Operators

Check if two objects have the same identity.

is
is not

```python
x_identity: list[int] = [1, 2, 3]
y_identity: list[int] = [1, 2, 3]
result_is: bool = x_identity is y_identity
result_is_not: bool = x_identity is not y_identity
```

# 6. User Input


```python 
Example 1: Basic User Input

Basic User Input  
user_name : str = input("Enter your name: ")  # Prompt user to enter their name
print("Hello, " + user_name + "!")  # Print a personalized greeting
```

```python 
Example 2: Numeric User Input , User Confirmation
user_age : int = int(input("Enter your age: "))  # Prompt user to enter their age and convert it to an integer
next_age = user_age + 1  # Calculate age for the next year
print("Next year, you'll be", next_age, "years old.")  # Print the calculated age
```
```python 
User Confirmation
confirmation : str = input("Are you sure? (yes/no): ")  # Ask for user confirmation
if confirmation.lower() == "yes":  # Check if the user confirmed (case-insensitive)
    print("Confirmed!")  # Print a confirmation message
else:
    print("Cancelled.")  # Print a cancellation message
```

# 7. f-String

In Python, an f-string (formatted string literal) is a way to embed expressions inside string literals, using curly braces {} and prefixed with the letter 'f' or 'F'. F-strings were introduced in Python 3.6 and provide a concise and readable syntax for string formatting.

### 1. Expression Inside Curly Braces:

You can include expressions inside curly braces {} within the string. These expressions will be evaluated at runtime and their values will be formatted into the string.

```python
name : str = "Ali Hamza"
age : int = 30
print(f"My name is {name} and I am {age} years old.")
```
### 2. Variable Substitution:

F-strings allow you to directly reference variables, making the code more readable and reducing the need for explicit conversions.

```python 
length : int = 5
width : int = 10
area = length * width
print(f"The area of a rectangle with length {length} and width {width} is {area}.")
```
### 3. Expressions and Functions:

You can use expressions, calculations, and even call functions within the curly braces.

```python 
x : int = 3
y : int = 4
print(f"The sum of {x} and {y} is {x + y}.")
```
### 4. Formatting Options:

F-strings support various formatting options, such as specifying the number of decimal places for floating-point numbers or formatting integers as binary, octal, or hexadecimal.

```python 
pi : float = 3.14159
print(f"Formatted Pi: {pi:.2f}")
```
### 5. Expressions with Braces:

If you need to include literal curly braces within the string, you can use double curly braces {{}}.

print(f"{{ This is a literal curly brace in an f-string }}")

```python 

print(f"{{ This is a literal curly brace in an f-string }}")
```

# 8. Foramt


In Python, the format() method is a built-in string method that allows you to format strings by replacing placeholders with values. This method provides a flexible and versatile way to create dynamic strings with variable content.

The basic syntax of the format() method is as follows:

```python 
formatted_string = "Some text with {} and {}".format(value1, value2)
```

### Example.

```python 
name : str = "Ali Hamza"
age : int = 30
result = "My name is {} and I am {} years old.".format(name, age)
print(result)
```

## Advanced Formatting:

The format() method supports more advanced formatting options, such as specifying the order of replacement, formatting numbers, and aligning text.

Index-Based Formatting:

```python
text : str = "{1} is a {0}".format("fruit", "Apple")
# Result: "Apple is a fruit"
```
Named Arguments:

```python 
text : str = "My name is {name} and I am {age} years old.".format(name="Bob", age=25)
# Result: "My name is Bob and I am 25 years old."
```
Number Formatting:

```python 
pi : str = 3.14159
formatted_pi = "Formatted Pi: {:.2f}".format(pi)
# Result: "Formatted Pi: 3.14"
```
Alignment:

```python
 formatted_table : str = "{:<10} {:^10} {:>10}".format("Left", "Center", "Right")
# Result: "Left       Center     Right"
```
 f-strings vs. format() method:

With the introduction of f-strings in Python 3.6, they have become the preferred way for string formatting due to their concise and readable syntax. However, the format() method is still widely used, especially in cases where dynamic string construction or advanced formatting options are required.

### Example.

Example with format():

```python 
name : str = "Saba"
age : int = 30
Formate_text = "My name is {} and I am {} years old.".format(name, age)
print(Formate_text)
```
