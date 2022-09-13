#Python Literals
'''
Two Types of Literals:
1.String Literals
2.Boolean Literals
'''

#1. String literals:
'''
String literals can be formed by enclosing a text in the quotes.
We can use both single as well as double quotes to create a string.
'''
#Example:
"Aman" , '12345'  
#Types of Strings:
#There are two types of Strings supported in Python:
'''
a) Single-line String- Strings that are terminated within a single-line 
are known as Single line Strings.
'''
text1='hello'

#a) Multi-line String -
'''
A piece of text that is written in multiple lines is known as multiple lines string.
There are two ways to create multiline strings:
'''
#b)1.1 Adding black slash at the end of each line.
text1 = ' hello\   
ser '    
print(text1)

#b)1.2 Using triple quotation marks:-
str2='''''welcome  
to  
SSSIT'''    
print(str2) 

#2Boolean literals:
'''
A Boolean literal can have any of the two values: True or False.
'''
x = (1 == True)  
y = (2 == False)  
z = (3 == True)  
a = True + 10  
b = False + 10  
  
print("x is", x)  
print("y is", y)  
print("z is", z)  
print("a:", a)  
print("b:", b)  
