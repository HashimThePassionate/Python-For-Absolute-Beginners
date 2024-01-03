#Using python as a calculator

# 1 NUMBERS..........

'''
We can use the interpreter to take an input and return an output!

Arithmetic Operators:
We have a whole bunch of opperators at our disposal
+ Addition
- Subtraction
* Multiplication
/ Division
// Floor division
% Modulus (remainder of x / y) | use divmod(a, b) 
** Exponentiation (power of) | can also use pow(x , y) instead of x**y

Assignment Opperators:
= Equals

Number Types:
int (2, 3, 458, 678)
float (2.2, 3.5, 5.666675678)

Build in Function:
round() Rounds a numbers with the specified number of 
decimals i.e. round(number, decimals) 
lastly, Python has a handy way of making big int's easier to read
4000000000 can be written as 
4_000_000_000
'''


#The basics
2 + 2 # simple addition
5 - 2 # simple subtraction
7 * 10 # simple multiplication

#Division and Modulus
10 / 4  # classic division returns a float
10 // 4  # floor division discards the fractional part
10 % 4 # the % operator returns the remainder of the division
round(10,4)

#Fancy sums
50 - 5*6 
(50 - 5*6) / 4
5 * 3 + 2  # floored quotient * divisor + remainder

#Exponentiation (power of)
5 ** 2  # 5 squared
2 ** 7  # 2 to the power of 7
pow(2,7)

#Using variables
width : int = 60
height : int = 3 * 7
width * height

#In interactive mode, the last printed expression is assigned to the variable _.
tax : int = 12.5 / 100
price : float = 100.50
price * tax #this is assigned to '_' and we use it in the next expression
price + _ #We reference '_' but this expression is now assigned to '_'
round(_, 2)

#NUMBERS END ...................................................................................



# 2 PYTHOM COMMENTS START .........................................................................

#Single-Line Comments
'''
This code is to show an example of a single-line comment  
'''
print( 'This statement does not have a hashtag before it' ) 
#Multi-Line Comments
'''
#use multi #tags
'''
# it is a  
# comment  
# extending to multiple lines  

#Using String Literals
'''
Because Python overlooks string expressions that aren't
allocated to a variable, we can utilize them as comments.
'''
'it is a comment extending to multiple lines'

#Python Docstring
'''
he strings enclosed in triple quotes that come immediately 
after the defined function are called Python docstring.
It's designed to link documentation developed for Python modules,
methods, classes, and functions together. It's placed just beneath
the function, module, or class to explain what they perform. 
The docstring is then readily accessible in Python
using the __doc__ attribute
'''
def add(x, y):  
    """This function adds the values of x and y"""  
    return x + y  
   
# Displaying the docstring of the add function  
print( add.__doc__ ) 

#PYTHON COMMENTS END......................................................................................




# 3 PYTHON LITERALS START...................................................................................

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
text1 : str = 'hello'

#a) Multi-line String -
'''
A piece of text that is written in multiple lines is known as multiple lines string.
There are two ways to create multiline strings:
'''
#b)1.1 Adding black slash at the end of each line.
text1 : str = ' hello\  user '    
print(text1)

#b)1.2 Using triple quotation marks:-
str2 : str = '''''welcome  
to  
SSSIT'''    
print(str2) 

#2Boolean literals:
'''
A Boolean literal can have any of the two values: True or False.
'''
x : bool = (1 == True)  
y : bool = (2 == False)  
z : bool = (3 == True)  
a : bool = True + 10  
b : bool = False + 10  
  
print("x is", x)  
print("y is", y)  
print("z is", z)  
print("a:", a)  
print("b:", b)

#PYTHON LITERALS END......................................................................................



# 4 PYTHON VARIABLES START...................................................................................

#Variables are containers for storing data values.
'''
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
'''
#Variable Assignment
n : int = 300
id(n)
print(n)

#Example
m : str = n
print("Value of m ",m)
print("id of m ",id(m))
print("Value of n ",n)
print("id of n ",id(n))

m : int = 400
print("Value of m ",m)
print("id of m ",id(m))
print("Value of n ",n)
print("id of n ",id(n))

n : str = "Hello"
print("Value of m ",m)
print("id of m ",id(m))
print("Value of n ",n)
print("id of n ",id(n))

#TYPE of Variable
a : int = 2
type(a)

#Same id to these objects
n : int = 10
m : str = "n"
print("n = :",id(n))
print("m = :",id(m))

'''
Camel case nOfStudent = "Hamza"
Pascal case NOfStudent = "Subhan"
Snake case  name_of_student = "Zeeshan"
'''

#-----------------------------------------------------------------------

# 4 Types of  Variable data 

#int 
a : int = 10 
b : int = -10

#float 
a : float = 10.1 
b : float = -10.1 

#string
name : str = " Farooq " 
#bool

a : bool = True
#----------------------------------------------------------------
#using Print()
name : str = "Hashim"
age  : int = 23
print('Age  is ',age)
print('name  is '+name)
#-----------------------------------------------------------------
#F-Strings (Formatted String Literals)
print(f'Age is {age} and Name is {name}')
#-----------------------------------------------------------------
#str.format() Method
print('Name : {} Age : {}'.format(name,age))
#-----------------------------------------------------------------
#Using % Formatting:
print('Age is %d and Name is %s'%(age,name))

#PYTHON VARIABLES END...................................................................................



#PYTHON OPERATORS START .................................................................................

#Python Operators
'''
The operator can be defined as a symbol which is responsible 
for a particular operation between two operands.
'''
#Arithmetic operators
'''
#Operator	                Description
+ (Addition)             	It is used to add two operands. For example, if a = 20, b = 10 => a+b = 30
- (Subtraction)	            It is used to subtract the second operand from the first operand. If the first operand is less than the second operand, the value results negative. For example, if a = 20, b = 10 => a - b = 10
/ (divide)	                It returns the quotient after dividing the first operand by the second operand. For example, if a = 20, b = 10 => a/b = 2.0
* (Multiplication)	        It is used to multiply one operand with the other. For example, if a = 20, b = 10 => a * b = 200
% (reminder)	            It returns the reminder after dividing the first operand by the second operand. For example, if a = 20, b = 10 => a%b = 0
** (Exponent)	            It is an exponent operator represented as it calculates the first operand power to the second operand.
// (Floor division)	        It gives the floor value of the quotient produced by dividing the two operands.
'''
# Comparison operators
'''
Operator	                Description
==	                        If the value of two operands is equal, then the condition becomes true.
!=	                        If the value of two operands is not equal, then the condition becomes true.
=	                        If the first operand is less than or equal to the second operand, then the condition becomes true.
>=	                        If the first operand is greater than or equal to the second operand, then the condition becomes true.
>	                        If the first operand is greater than the second operand, then the condition becomes true.
<	                        If the first operand is less than the second operand, then the condition becomes true.
'''
# Assignment Operators
'''
Operator	                Description
=	                        It assigns the value of the right expression to the left operand.
+=	                        It increases the value of the left operand by the value of the right operand and assigns the modified value back to left operand. For example, if a = 10, b = 20 => a+ = b will be equal to a = a+ b and therefore, a = 30.
-=                     	    It decreases the value of the left operand by the value of the right operand and assigns the modified value back to left operand. For example, if a = 20, b = 10 => a- = b will be equal to a = a- b and therefore, a = 10.
*=	                        It multiplies the value of the left operand by the value of the right operand and assigns the modified value back to then the left operand. For example, if a = 10, b = 20 => a* = b will be equal to a = a* b and therefore, a = 200.
%=	                        It divides the value of the left operand by the value of the right operand and assigns the reminder back to the left operand. For example, if a = 20, b = 10 => a % = b will be equal to a = a % b and therefore, a = 0.
*=	                        a**=b will be equal to a=a**b, for example, if a = 4, b =2, a**=b will assign 4**2 = 16 to a.
//=                         A//=b will be equal to a = a// b, for example, if a = 4, b = 3, a//=b will assign 4//3 = 1 to a.
'''
# Logical Operators
'''
Operator	                Description
and	                        If both the expression are true, then the condition will be true. If a and b are the two expressions, a → true, b → true => a and b → true.
or	                        If one of the expressions is true, then the condition will be true. If a and b are the two expressions, a → true, b → false => a or b → true.
not	                        If an expression a is true, then not (a) will be false and vice versa
'''
# Bitwise Operators
'''
Operator	                Description
& (binary and)         	    If both the bits at the same place in two operands are 1, then 1 is copied to the result. Otherwise, 0 is copied.
| (binary or)          	    The resulting bit will be 0 if both the bits are zero; otherwise, the resulting bit will be 1.
^ (binary xor)          	The resulting bit will be 1 if both the bits are different; otherwise, the resulting bit will be 0.
~ (negation)	            It calculates the negation of each bit of the operand, i.e., if the bit is 0, the resulting bit will be 1 and vice versa.
<< (left shift)	            The left operand value is moved left by the number of bits present in the right operand.
>> (right shift)       	    The left operand is moved right by the number of bits present in the right operand.
'''
# Membership Operators
'''
Python membership operators are used to check
the membership of value inside a Python data structure. 
If the value is present in the data structure, 
then the resulting value is true otherwise it returns false.
Operator	                Description
in	                        It is evaluated to be true if the first operand is found in the second operand (list, tuple, or dictionary).
not in                 	    It is evaluated to be true if the first operand is not found in the second operand (list, tuple, or dictionary).
'''
# Identity Operators
'''
The identity operators are used to decide whether an element certain class or type.
Operator	                Description
is	                        It is evaluated to be true if the reference present at both sides point to the same object.
is not	                    It is evaluated to be true if the reference present at both sides do not point to the same object.
'''
#Operator Precedence
'''
Operator	                Description
**	                        The exponent operator is given priority over all the others used in the expression.
~ + -	                    The negation, unary plus, and minus.
* / % //	                The multiplication, divide, modules, reminder, and floor division.
+ -	                        Binary plus, and minus
>> <<	                    Left shift. and right shift
&	                        Binary and.
^ |	                        Binary xor, and or
<= < > >=	                Comparison operators (less than, less than equal to, greater than, greater then equal to).
<> == !=               	    Equality operators.
= %= /= //= -= +=#*= **=  	Assignment operators
is is not	                Identity operators
in not in              	    Membership operators
not or and	                Logical operators
'''




#PYTHON USERINPUT ..............................................................................................

#Python User Input
'''
Python allows for user input.

That means we are able to ask the user for input.

The method is a bit different in Python 3.6 than Python 2.7.

Python 3.6 uses the input() method.

'''
username : str = input("Enter username:")
print("Username is:" + username)

#Example
name : str = input("Enter Your name:")
age : str = int(input("Enter your age"))
print("Your name is :",name,"Your age is",age)


