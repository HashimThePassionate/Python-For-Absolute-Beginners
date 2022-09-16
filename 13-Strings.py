#Using python to manipulate string
'''
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
'''
#Syntax:
str = "Hi Python !"   
#Here, if we check the type of the variable str using a Python script
print(type(str))# then it will print a string (str)   

#Creating String in Python
'''
We can create a string by enclosing the characters in "single-quotes"
or "double- quotes". Python also provides "triple-quotes" to represent 
the string, but it is generally used for multiline string or 
"docstring|s.
'''
#Using single quotes  
str1 = 'Hello Python'  
print(str1)  
#Using double quotes  
str2 = "Hello Python"  
print(str2)  
#Using triple quotes  
str3 = '''''Triple quotes are generally used for  
    represent the multiline or 
    docstring'''   
print(str3)  

#Strings indexing and splitting
'''
Like other languages, the indexing of the Python strings starts 
from 0. For example, The string "HELLO" is indexed as given in the 
below figure.
str="HELLO"
 +---+---+---+---+---+
 | H | E | L | L | o | 
 +---+---+---+---+---+
   0   1   2   3   4      
  -5  -4  -3  -2  -1
str[0]='H'
str[1]='E'
str[2]='L'
str[3]='L'
str[4]='O'
Reverse
str[-1]='O'
str[-2]='L'
str[-3]='L'
str[-4]='E'
str[-5]='H'
'''
str = "HELLO"  
print(str[0])  
print(str[1])  
print(str[2])  
print(str[3])  
print(str[4]) 
print(str[-1])
print(str[-2])
print(str[-3])
print(str[-4])
print(str[-5])
# It returns the IndexError because 6th index doesn't exist  
print(str[6])  
'''
Strings have a bunch of methods available.
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
'''

#The basics
'spam eggs'  # single quotes
'doesn\'t'  # use \' to escape the single quote... "does't"
"doesn't"  # ...or use double quotes instead       "doesn't"
'"Yes," they said.'
"\"Yes,\" they said."

#New line
s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output

print(s)  # with print(), \n produces a new line

#Raw string
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote


#String literals
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")


#Concatenated
3 * 'un' + 'ium'
'Did' 'Coding'
text = ('Put several strings within parentheses '
        'to have them joined together.')
text
#This only works with two literals though, 
#not with variables or expressions:
prefix = 'Did'
prefix + 'Coding'

#Indexing
'''
 +---+---+---+---+---+---+---+---+---+
 | D | i | d | C | o | d | i | n | g |
 +---+---+---+---+---+---+---+---+---+
   0   1   2   3   4   5   6   7   8   
  -9  -8  -7  -6  -5  -4  -3  -2  -1
'''

word = 'Didcoding'
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
str = "JAVATPOINT"  
# Start Oth index to end  
print(str[0:])  
# Starts 1th index to 4th index  
print(str[1:5])  
# Starts 2nd index to 3rd index  
print(str[2:4])  
# Starts 0th to 2nd index  
print(str[:3])  
#Starts 4th to 6th index  
print(str[4:7])  

#changing strings
word[0] = 'P'
'P' + word[1:]
word[:2] + 'di'
'''
Traceback (most recent call last):
  File "12.py", line 2, in <module>
    str[0] = "h";
TypeError: 'str' object does not support item assignment
'''

#However, in example 1, the string str can be assigned completely 
# to a new content as specified in the following example.
str = "HELLO"    
print(str)    
str = "hello"    
print(str) 

#String length
s = 'bobby-didcoding'
len(s)

#Deleting the String
'''
As we know that strings are immutable. We cannot delete or remove the 
characters from the string.  But we can delete the entire string using 
the del keyword.
str = "JAVATPOINT"  
del str[1]  
Output:
TypeError: 'str' object doesn't support item deletion

'''
#Now we are deleting entire string.
str1 = "JAVATPOINT"  
del str1  
print(str1) 

#String Operator
'''

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
'''
#Consider the following example to understand the real use of 
# Python operators.
str = "Hello"     
str1 = " world"    
print(str*3) # prints HelloHelloHello    
print(str+str1)# prints Hello world     
print(str[4]) # prints o                
print(str[2:4]); # prints ll                    
print('w' in str) # prints false as w is not present in str    
print('wo' not in str1) # prints false as wo is present in str1.     
print(r'C://python37') # prints C://python37 as it is written    
print("The string str : %s"%(str)) # prints The string str : Hello  

#Python String Formatting
'''
Escape Sequence
Let's suppose we need to write the text as - 
They said, "Hello what's going on?"- the given statement can be written 
in single quotes or double quotes but it will raise the SyntaxError 
as it contains both single and double-quotes.
Example
Consider the following example to understand the real use of Python 
operators.
str = "They said, "Hello what's going on?""  
print(str)  
'''
str = "They said, "Hello what's going on?""  
print(str)  
#Solution:
str = '''"They said, "Hello what's going on?""'''  
print(str) 
'''
We can use the triple quotes to accomplish this problem but Python provides
the escape sequence.
The backslash(/) symbol denotes the escape sequence. The backslash can be 
followed by a special character and it interpreted differently. The single 
quotes inside the string must be escaped. We can apply the same as in the 
double quotes.
'''
#Example
# using triple quotes  
print('''''They said, "What's there?"''')  
  
# escaping single quotes  
print('They said, "What\'s going on?"')  
  
# escaping double quotes  
print("They said, \"What's going on?\"") 

'''
Sr.	Escape Sequence	        Description	        Example
1.	\newline	It ignores the new line.	print("Python1
\ Python2 
\ Python3") 
Output:
Python1 Python2 Python3

2.	\\	                Backslash	        print("\\")
Output:
\
3.     	\'	                Single Quotes	        print('\'')
Output:
'
4.	\\''	                Double Quotes	        print("\"")
Output:
"
5.	\a	                ASCII Bell	        print("\a")
6.	\b	             ASCII Backspace(BS)	print("Hello \b World")
Output:
Hello World
7.	\f	                ASCII Formfeed	        print("Hello \f World!")
Hello  World!
8.	\n	                ASCII Linefeed	        print("Hello \n World!")
Output:
Hello
 World!
9.	\r	             ASCII Carriege Return(CR)	print("Hello \r World!")
Output:
World!
10.	\t	              ASCII Horizontal Tab	print("Hello \t World!")
Output:
Hello 	 World!
11.	\v	                ASCII Vertical Tab	print("Hello \v World!")
Output:
Hello 
 World!
12.	\ooo           	Character with octal value	print("\110\145\154\154\157")
Output:
Hello
13	\xHH	             Character with hex value.	 print("\x48\x65\x6c\x6c\x6f")
Output:
Hello
'''
print("C:\\Users\\Hashim\\Python32\\Lib")  
print("This is the \n multiline quotes")  
print("This is \x48\x45\x58 representation") 
#We can ignore the escape sequence from the given string by using the 
#raw string. We can do this by writing r or R in front of the string.
#  Consider the following example.
print(r"C:\\Users\\Hamza\\Python32")  

#The format() method
'''
The format() method is the most flexible and useful method in formatting 
strings. The curly braces {} are used as the placeholder in the string 
and replaced by the format() method argument. Let's have a look at the 
iven an example:
'''
# Using Curly braces  
print("{} and {} both are the best friend".format("Hamza","Hashim"))  
#Positional Argument  
print("{1} and {0} best players ".format("Hashim","Hamza"))  
#Keyword Argument  
print("{a},{b},{c}".format(a = "Hashim", b = "Hamza", c = "Sir Farooq"))  

#Python String Formatting Using % Operator
'''
Python allows us to use the format specifiers used in C's printf 
statement. The format specifiers in Python are treated in the same 
way as they are treated in C. However, Python provides an additional 
operator %, which is used as an interface between the format specifiers 
and their values. In other words, we can say that it binds the format 
specifiers to the values.
'''
Integer = 10
Float = 1.290    
String = "Hamza"    
print("""Hi I am Integer ... My value is %d
Hi I am float ... My value is %f
Hi I am string ... My value is %s"""%(Integer,Float,String)) 
