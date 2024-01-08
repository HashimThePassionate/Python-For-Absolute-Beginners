## String Formatting and Definitions in Python with Static Typing

## Table of Contents

- [String Definitions](#string-definitions)
- [String Formatting](#string-formatting)
  - [Basic Techniques](#basic-techniques)
  - [Advanced Techniques](#advanced-techniques)
- [Naming Conventions](#naming-conventions)

## String Definitions
Python can be used to manipulate strings, which can 
be expressed in several ways.

They can be enclosed in single quotes ('...') 
or double quotes ("...")

'\' can be used to escape quotes

or triple quotes (""" ...
.
.
""")
Python strings cannot be changed — "they are immutable".
We will also look at the built in function called len()
This function returns the length of a string as a integer value:

## syntax
```python
  strr : str = "Hi Python !"
```

Here, if we check the type of the variable str using a Python script

```python
  print(type(strr))# then it will print a string (str)   
```
## Creating String in Python

We can create a string by enclosing the characters in "single-quotes"
or "double- quotes". Python also provides "triple-quotes" to represent 
the string, but it is generally used for multiline string or 
"docstring|s.

### Single Quotes

You can define a string with single quotes.

```python
my_string: str = 'Hello, World!'
```

### Double Quotes

Alternatively, you can define a string with double quotes.

```python
my_string: str = "Hello, World!"
```

### Triple Single Quotes

Triple single quotes allow for string definitions that span multiple lines.

```python
my_string: str = '''Hello,
World!'''
```

### Triple Double Quotes

Like triple single quotes, triple double quotes also allow for multi-line string definitions.

```python
my_string: str = """Hello,
World!"""
```

## Strings indexing and splitting
Like other languages, the indexing of the Python strings starts 
from 0. For example, The string "HELLO" is indexed as given in the 
below figure.

```python
strr : str ="HELLO"
 +---+---+---+---+---+
 | H | E | L | L | o | 
 +---+---+---+---+---+
   0   1   2   3   4      
  -5  -4  -3  -2  -1
strr[0]='H'
strr[1]='E'
strr[2]='L'
strr[3]='L'
strr[4]='O'
Reverse
strr[-1]='O'
strr[-2]='L'
strr[-3]='L'
strr[-4]='E'
strr[-5]='H'

```
```python
strr : str = "HELLO"  
print(strr[0])  
print(strr[1])  
print(strr[2])  
print(strr[3])  
print(strr[4]) 
print(strr[-1])
print(strr[-2])
print(strr[-3])
print(strr[-4])
print(strr[-5])
# It returns the IndexError because 6th index doesn't exist  
print(strr[6])  
```
## Strings have a bunch of methods available.

```python
capitalize() Converts the first character to upper case
casefold() Converts string into lower case
center() Returns a centered string
count() Returns the number of times a specified value occurs in a string
encode() Returns an encoded version of the string
endswith() Returns true if the string ends with the specified value
expandtabs() Sets the tab size of the string
find() Searches the string for a specified value and returns the position of where it was found
format() Formats specified values in a string
format_map() Formats specified values in a string
index() Searches the string for a specified value and returns the position of where it was found
isalnum() Returns True if all characters in the string are alphanumeric
isalpha() Returns True if all characters in the string are in the alphabet
isascii() Returns True if all characters in the string are ascii characters
isdecimal() Returns True if all characters in the string are decimals
isdigit() Returns True if all characters in the string are digits
isidentifier() Returns True if the string is an identifier
islower() Returns True if all characters in the string are lower case
isnumeric() Returns True if all characters in the string are numeric
isprintable() Returns True if all characters in the string are printable
isspace() Returns True if all characters in the string are whitespaces
istitle() Returns True if the string follows the rules of a title
isupper() Returns True if all characters in the string are upper case
join() Converts the elements of an iterable into a string
ljust() Returns a left justified version of the string
lower() Converts a string into lower case
lstrip() Returns a left trim version of the string
maketrans() Returns a translation table to be used in translations
partition() Returns a tuple where the string is parted into three parts
replace() Returns a string where a specified value is replaced with a specified value
rfind()	 Searches the string for a specified value and returns the last position of where it was found
rindex() Searches the string for a specified value and returns the last position of where it was found
rjust() Returns a right justified version of the string
rpartition() Returns a tuple where the string is parted into three parts
rsplit() Splits the string at the specified separator, and returns a list
rstrip() Returns a right trim version of the string
split() Splits the string at the specified separator, and returns a list
splitlines() Splits the string at line breaks and returns a list
startswith() Returns true if the string starts with the specified value
strip() Returns a trimmed version of the string
swapcase() Swaps cases, lower case becomes upper case and vice versa
title() Converts the first character of each word to upper case
translate() Returns a translated string
upper() Converts a string into upper case
fill() Fills the string with a specified number of 0 values at the beginning

```
### The basics
```python
'spam eggs'  # single quotes
'doesn\'t'  # use \' to escape the single quote... "does't"
"doesn't"  # ...or use double quotes instead       "doesn't"
'"Yes," they said.'
"\"Yes,\" they said."
```
### New line

```python
s : str = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output

print(s)  # with print(), \n produces a new line
```
### Raw string

```python
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

```
### String literals

```python
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```
### Concatenated

```python
3 * 'un' + 'ium'
'Did' 'Coding'
text = ('Put several strings within parentheses '
        'to have them joined together.')
text
```
This only works with two literals though,not with variables or expressions:

```python
prefix = 'Did'
prefix + 'Coding'

```
### Indexing
```python
 +---+---+---+---+---+---+---+---+---+
 | D | i | d | C | o | d | i | n | g |
 +---+---+---+---+---+---+---+---+---+
   0   1   2   3   4   5   6   7   8   
  -9  -8  -7  -6  -5  -4  -3  -2  -1
```

```python
word : str  = 'Didcoding'
word[0]    # character in position 0 print D
word[5]    # character in position 5 print d
word[0:2]  # characters from position 0 (included) to 2 (excluded)
word[2:5]  # characters from position 2 (included) to 5 (excluded)
word[:2]   # character from the beginning to position 2 (excluded)
word[4:]   # characters from position 4 (included) to the end
word[-2:]  # characters from the second-last (included) to the end
word[::-1] #Characters from start to end but reverse in order
word[:2] + word[2:] #Complete
word[:4] + word[4:] #Complete

# Given String  
strr : str = "JAVATPOINT"  
# Start Oth index to end  
print(strr[0:])  
# Starts 1th index to 4th index  
print(strr[1:5])  
# Starts 2nd index to 3rd index  
print(strr[2:4])  
# Starts 0th to 2nd index  
print(strr[:3])  
#Starts 4th to 6th index  
print(strr[4:7])  


```
### changing strings

```python
word[0] = 'P'
'P' + word[1:]
word[:2] + 'di'
```
```python
Traceback (most recent call last):
  File "12.py", line 2, in <module>
    str[0] = "h";
TypeError: 'str' object does not support item assignment
```
However, in example 1, the string str can be assigned completely to a new content as specified in the following example.

```python
strr : str = "HELLO"    
print(strr)    
strr : str = "hello"    
print(strr) 

```
### String length
```python
s : str = 'bobby-didcoding'
len(s)
```
### Deleting the String
As we know that strings are immutable. We cannot delete or remove the 
characters from the string.  But we can delete the entire string using 
the del keyword.

```python
strr : str = "JAVATPOINT"  
del strr[1]  
```
### Output
```python
TypeError: 'str' object doesn't support item deletion
```

Now we are deleting entire string.

```python
str1 : str = "JAVATPOINT"  
del str1  
print(str1) 

```
### String Operator
```python
Operator	Description
+	It is known as concatenation operator used to join the strings 
        given either side of the operator.
*	It is known as repetition operator. It concatenates the multiple 
        copies of the same string.
[]	It is known as slice operator. It is used to access the sub-strings 
        of a particular string.
[:]	It is known as range slice operator. It is used to access the 
        characters from the specified range.
in	It is known as membership operator. It returns if a particular 
        sub-string is present in the specified string.
not in	It is also a membership operator and does the exact reverse of in. 
        It returns true if a particular substring is not present in the 
        specified string.
r/R	It is used to specify the raw string. Raw strings are used in the 
        cases where we need to print the actual meaning of escape characters such as "C://python". To define any string as a raw string, the character r or R is followed by the string.
%	It is used to perform string formatting. It makes use of the 
        format specifiers used in C programming like %d or %f to map 
        their values in python. We will discuss how formatting is 
        done in python.


```
Consider the following example to understand the real use of Python operators.

```python
strr : str = "Hello"     
str1 : str = " world"    
print(strr*3) # prints HelloHelloHello    
print(strr+str1)# prints Hello world     
print(str[4]) # prints o                
print(str[2:4]); # prints ll                    
print('w' in str) # prints false as w is not present in str    
print('wo' not in str1) # prints false as wo is present in str1.     
print(r'C://python37') # prints C://python37 as it is written    
print("The string str : %s"%(strr)) # prints The string str : Hello  

```
### Python String Formatting
Escape Sequence
Let's suppose we need to write the text as - 
They said, "Hello what's going on?"- the given statement can be written 
in single quotes or double quotes but it will raise the SyntaxError 
as it contains both single and double-quotes.

### Example
Consider the following example to understand the real use of Python 
operators.
```python
strr : str = "They said, "Hello what's going on?""  
print(strr)    
```

We can use the triple quotes to accomplish this problem but Python provides
the escape sequence.
The backslash(/) symbol denotes the escape sequence. The backslash can be 
followed by a special character and it interpreted differently. The single 
quotes inside the string must be escaped. We can apply the same as in the 
double quotes.

```python
print("C:\\Users\\Hashim\\Python32\\Lib")  
print("This is the \n multiline quotes")  
print("This is \x48\x45\x58 representation") 
```
We can ignore the escape sequence from the given string by using the 
raw string. We can do this by writing r or R in front of the string.
Consider the following example.

### The format() method
The format() method is the most flexible and useful method in formatting 
strings. The curly braces {} are used as the placeholder in the string 
and replaced by the format() method argument.

### Using Curly braces  
```python
print("{} and {} both are the best friend".format("Hamza","Hashim"))  
```

### Positional Argument
```python
print("{1} and {0} best players ".format("Hashim","Hamza"))  
```
### Keyword Argument 
```python
print("{a},{b},{c}".format(a = "Hashim", b = "Hamza", c = "Sir Farooq"))  
```
### Python String Formatting Using % Operator

Python allows us to use the format specifiers used in C's printf 
statement. The format specifiers in Python are treated in the same 
way as they are treated in C. However, Python provides an additional 
operator %, which is used as an interface between the format specifiers 
and their values. In other words, we can say that it binds the format 
specifiers to the values.
```python
Integer : int = 10
Float : float = 1.290    
String : str = "Hamza"    
print("""Hi I am Integer ... My value is %d
Hi I am float ... My value is %f
Hi I am string ... My value is %s"""%(Integer,Float,String)) 
```




## String Formatting

### Basic Techniques

#### Using `%s` and `%d`

You can use `%s` for string and `%d` for integers.

```python
name: str = "Alice"
age: int = 30
print("My name is %s and I am %d years old." % (name, age))
```

#### Using `.format()`

The `.format()` method is another way to format your strings.

```python
name: str = "Alice"
age: int = 30
print("My name is {} and I am {} years old.".format(name, age))
```

#### Using f-string (Python 3.6+)

f-strings provide a concise and readable way to include the value of Python expressions inside strings.

```python
name: str = "Alice"
age: int = 30
print(f"My name is {name} and I am {age} years old.")
```

### Advanced Techniques

#### f-string Expressions

You can include Python expressions within f-strings.

```python
x: int = 10
y: int = 20
print(f"The sum of {x} and {y} is {x+y}.")
```

#### f-string with Format Specification

You can format numbers using f-strings.

```python
pi: float = 3.14159
print(f"Value of pi to 2 decimal places: {pi:.2f}")
```

## Naming Conventions

### Variables

- Use `snake_case` for variable names.
  
```python
my_variable: int = 10
```

### Constants

- Use `UPPER_SNAKE_CASE` for constants.

```python
PI: float = 3.14159
```
