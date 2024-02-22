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

A number is a mathematical object used to represent quantity. It can be used for counting, measuring, and labeling. There are different types of numbers, but they all share this basic function.
In Python, "number" isn't a specific definition but rather refers to numeric data types. These are fundamental building blocks used to store and manipulate numerical values. Here are the main three types:
<h4> 1.Integers (int)</h4>
Whole numbers without decimals, positive, negative, or zero.
Examples: 42, -10, 0.

```python

# Assign the integer value 10 to the variable x
x : int = 42
# Assign the integer value 4 to the variable y
y : int =  -10
# Assign the integer value 2 to the variable z
z : int = 0
# Print the value of x and its data type
print(x)
print(type(x))
# Print the value of y and its data type
print(y)
print(type(y))
# Print the value of z and its data type
print(z)
print(type(z))
```

<h4>2.Floats (float)</h4>:
Numbers with decimals, representing real numbers. 
Examples: 3.14159, -5.2, 1.0e6 (scientific notation for 1,000,000).

```python
# Define a float variable with decimal value
i = 3.14159
 j= -5.2
k = 1,000,000

# Print the variable and its data type
print(i)
print(type(i))
# Print the variable and its data type 
print(j)
print(type(j))
# Print the variable and its data type
print(k)
print(type(k))
```
<h4>3.Complex numbers (complex)</h4>:
Numbers with a real part and an imaginary part (denoted by j). Examples: 3+2j, 1j, -5.

```python
# Create two complex numbers
a = 1 + 2j
b = 3 - 4j

# Add the complex numbers
c = a + b

# Print the result
print(c)
print(type(c))

```
Another example
```python

real_part: float = 2.0
imaginary_part: float = 3.0

complex_num: complex = complex(real_part, imaginary_part)

Introduces complex numbers in programming.
```

Other concepts related to numbers in Python:

<h4>Arithmetic operations</h4>h4>: These are operations like addition, subtraction, multiplication, division, etc., that can be performed on numbers. Python supports these using standard operators (+, -, *, /, etc.).
For Example

```python


x: int = 5
y: int = 3

result_add: int = x + y
result_multiply: int = x * y
result_divide: float = y / x
result_power: int = x ** 2
result_modulo: int = x % 2
```
<h4>Increment/decrement</h4>
These are shorthand ways to increase or decrease the value of a variable by 1. Increment uses += (e.g., x += 1), and decrement uses -= (e.g., y -= 2).
For Example

```python

x: int = 5
y: float = 3.0

x += 1  # Increment x by 1
y -= 0.5  # Decrement y by 0.5

Shows how to increment and decrement variables.
```
<h4>Type conversion</h4>
This is the process of changing the data type of a value. Python provides functions like int(), float(), and complex() for type conversion.



```python
float_value: float = 3.75
int_value: int = 2

float_to_int: int = int(float_value)
int_to_float: float = float(int_value)

Illustrates converting between data types. 
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

<h4>1. String Literal</h4>
In Python, a string literal is a fixed sequence of characters enclosed within quotes. They are used to represent text data. Here are the different ways to define string literals with examples and their outputs:

**i. Single quotes (')**:

```Python
message : str= 'This is a string literal enclosed in single quotes.'
print(message)
```
**ii. Double quotes (")**:

```Python
message : str= "This is a string literal enclosed in double quotes."
print(message)
```
**iii. Triple quotes (''' or """)**:

Triple quotes allow you to create multi-line strings without the need for backslashes (\n) at the end of each line. They are useful for defining longer text blocks or poems.

```Python
message : str= """This is a string literal
enclosed in triple quotes,
which allows for multiple lines."""
print(message)  
```


<h4>2. Boolean Literals</h4>
Boolean literals in Python are used to represent truth or falsity. They are denoted by the keywords True and False.

```python 


is_true: bool = True
is_false: bool = False
```

Here are some examples of Boolean literals and their usage:
<pre>
Boolean         Literal	    Example	Output
True	         5 > 3	        True
False	         None	        False
False	          0	            False
True	        "hello"	        True
</pre>
Operations with Boolean literals:
<pre>
Operation	 Example	     Output
and	      True and False	 False
or	      True or False	     True
not	      not True	         False
</pre>


<h4>3. Numeric Literals</h4>
In Python, numeric literals are fixed values representing numbers used in your code. They come in three main types:

1. Integers (int):

Represent whole numbers without decimals and can be positive, negative, or zero.

Examples: 10, -5, 0, 1_000_000 (using underscores for readability).
2. Floats (float):

Represent numbers with decimals, holding real numbers.

Examples: 3.14, -5.2, 1.0e6 (scientific notation for 1,000,000).
3. Complex numbers (complex):

Numbers with a real and imaginary part (denoted by j).

Examples: 3+2j, 1j, -5.5+0.2j.
Simple examples:

```Python
age : int = 25  # Integer (int)
distance : float= 3.14159  # Float (float)
complex_number : complex = 1+2j  # Complex (complex)

print(f"Your age is: {age}") 
print(f"Distance: {distance}")  
print(f"Complex number: {complex_number}")  
```

<h4>String Concatenation</h4>
String concatenation in Python simply means joining two or more strings together to create a new string. Here's how you can do it:

1. Using the + operator:

This is the most common and straightforward way to concatenate strings. You just place the strings you want to join next to each other with a + sign in between.

```Python
first_name : str = "Alice"
last_name : str = "Smith"
full_name : str = first_name + " " + last_name

print(full_name) 
```
2. Using the str.join() method:

This method is useful when you have a sequence of strings (like a list or tuple) that you want to combine into a single string. You specify the sequence and an optional separator (the string inserted between each element).

```Python
words :list = ["Hello", "world", "!"]
sentence : str = " ".join(words)  # Join with a space

print(sentence)  # Output: Hello world!
```
3. Using f-strings (formatted string literals):

Introduced in Python 3.6, f-strings offer a more readable way to embed variables and expressions directly within strings.

```Python
name : str = "Bob"
age : int = 30

message : str  = f"Hi, my name is {name} and I am {age} years old."

print(message)
```

<h4>Boolean Expressions</h4>

In Python, Boolean expressions are used to evaluate conditions and return either True or False. They play a crucial role in controlling program flow and decision making.
Example:

```Python
age : int = 18
has_license : bool = True

# Check if both age is 18 and has_license is True
can_drive : bool = age == 18 and has_license

# Check if either age is above 16 or has_license is True
can_rent_car : bool = age > 16 or has_license

# Check if age is not equal to 21
not_of_legal_drinking_age = age != 21

print(can_drive) 
print(can_rent_car)  
print(not_of_legal_drinking_age)  
```

<h4>Raw String Literal</h4>
In Python, a raw string literal, denoted by an r or R before the quotes, is a string where backslashes () are treated literally instead of escape sequences. This is useful when you want to include backslashes in your string without them having special meanings.

Here's a simple example:

```Python
# Regular string (backslash is interpreted as newline)
regular_string : str = "This is a regular string.\nIt interprets backslashes like \n for newlines."

# Raw string (backslash is preserved)
raw_string : str = r"This is a raw string literal.\nIt preserves backslashes like \n and \"."

file_path: str = r"C:\Users\username\Documents"
print(regular_string)
print(raw_string)
print(file_path)
```


# 4. Variables

In Python, a variable is simply a named container that holds a value. It acts like a label you stick on a box to remember what's inside. You can use the variable name to access and manipulate the stored value throughout your program.

Here's a breakdown of key points:

What they do:

Store and manage data of different types (numbers, text, lists, etc.).
Make your code more readable and maintainable by using meaningful names.
Allow you to easily change values without modifying the entire code.
How to define them:

There's no strict "define" command. Simply assign a value to a name using the equal sign (=):


```python
age = 25
name = "Alice"
is_happy = True

```
Another example are given below
```python
# Define variables
my_number = 10
fruit = "apple"

# Use variables in calculations
total = my_number * 2
message = "I have " + str(total) + " " + fruit + "s!"

# Print the result
print(message)  # Output: I have 20 apples!
```

 <h3>Variable Assignment</h3>
 
```python 
Example 1:

age : int = 25
name : str = "Ahmed"
height : float = 5.5
quize : bool =  true
```
 <h3>Variable Reassignment</h3>

```python
Example 2: 

age : str = age + 1
age : str = age * 2

Demonstrates changing the value of a variable.
```
<h3>Multiple Assignments</h2>

```python 
Example 3: 

a: int
b: int
c: int
a, b, c  : int = 1, 2, 3

Illustrates multiple assignments in a single line.
```
<h2> Swapping Variables</h3>

Swapping variables in Python can be done in several ways, each with its advantages and applications. eg;
```python 
Example 4:

x: int = 5
y: int = 10
temp: int = x
x = y
y = temp

Shows how to swap values between variables.
```
Here are some common methods:

1. Using a temporary variable:

This is the most basic and straightforward method, suitable for beginners. It involves storing the value of one variable in a temporary variable, then assigning the other variable's value to the first, and finally assigning the original value from the temporary variable to the second.

```Python
a : int = 5
b : int = 10

temp = a
a = b
b = temp

print("a:", a)   # Output: 10
print("b:", b)   # Output: 5
```
2. Using tuple unpacking:

This method leverages Python's ability to unpack tuples. It's concise and readable for simple swaps.

```Python
a : int = 5
b : int = 10

a, b = b, a

print("a:", a)   # Output: 10
print("b:", b)   # Output: 5
```
3. Using arithmetic operators (for numbers only):

This method relies on arithmetic operations like addition and subtraction, but it's only applicable to numeric values.

```Python
a : int = 5
b : int = 10

a  = a + b
b  = a - b
a  = a - b

print("a:", a)   # Output: 10
print("b:", b)   # Output: 5
```
4. Using the XOR bitwise operator (for integers only):

This method uses the bitwise XOR operator (^) to achieve the swap in a single line. However, it's less intuitive and might be harder to understand for beginners.

```Python
a : int = 5
b : int = 10

a  = a ^ b
b  = a ^ b
a  = a ^ b

print("a:", a)   # Output: 10
print("b:", b)   # Output: 5
```


<h3>Dynamic Typing</h3>
Dynamic Typing simply means that the data type of a variable is determined at runtime, not during declaration. Unlike static typing, where you explicitly specify the type beforehand, dynamic languages like Python let the variable "discover" its type based on the value assigned.

```python 


dynamic_variable : float= 3.14
dynamic_variable : str = "Hello"

Introduces dynamic typing in programming.
```
<h3>Variable Naming Conventions</h3>
Variable names are crucial for code readability and maintainability.
General Principles:

- Meaningful: Describe the variable's purpose, e.g., customer_age not x.
- Consistent: Use the same style throughout your code.
- Readable: Avoid abbreviations unless widely understood.
- Case-sensitive: Choose one style (e.g., camelCase or snake_case) and stick to it.
Popular Styles:

- CamelCase: Capitalize the first letter of each word, e.g., customerName, totalCost.
- Snake_case: Use underscores to separate words, e.g., customer_name, total_cost.
- PascalCase: Similar to camelCase but capitalize all words, e.g., CustomerName, TotalCount.
```python 
 
Python


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
