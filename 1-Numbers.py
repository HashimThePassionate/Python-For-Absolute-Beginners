#Using python as a calculator

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

# In this example, static type hints are provided for integer, float, and complex variables. The code also demonstrates basic arithmetic
# operations, working with sequences (a list of integers), iterating over the list, and generating a random number. Remember that these type 
# hints are optional and for documentation purposes, but they can be used by static analysis tools


#The basics
5 + 2 # simple addition
8 - 2 # simple subtraction
5 * 10 # simple multiplication

#Division and Modulus
12 / 3  # classic division returns a float
15 // 4  # floor division discards the fractional part
15 % 4 # the % operator returns the remainder of the division..
round(15,4)

#Fancy sums
50 - 5*6 
(50 - 5*6) / 4
5 * 3 + 2  # floored quotient * divisor + remainder..

#Exponentiation (power of)
10 ** 2  # 5 squared
5 ** 7  # 2 to the power of 7
pow(5,7)

#Using variables
width : int = 60
height : int = 3 * 7
width * height

#In interactive mode, the last printed expression is assigned to the variable _.
tax = 12.5 / 100
price = 100.50
price * tax #this is assigned to '_' and we use it in the next expression
price + _ #We reference '_' but this expression is now assigned to '_'
round(_, 2)


num1: int = 42

# Example 2: Float
num2: float = 3.14

# Example 3: Complex
num3: complex = 2 + 3j

# Example 4: Integer
count: int = 100

# Example 5: Float
pi: float = 3.14159

# Example 6: Complex
imaginary_number: complex = 1j

# Example 7: Integer
quantity: int = 25

# Example 8: Float
price: float = 49.99



# Example 2: Arithmetic operations with floats
float1: float = 3.14
float2: float = 2.5
result_division: float = float1 / float2
result_power: float = float1 ** 2

# Example 3: Using numbers in sequences (list of integers)
numbers_list: List[int] = [1, 2, 3, 4, 5]
sum_of_numbers: int = sum(numbers_list)

# Example 4: Iterating over a range of integers
for i in range(5):
    print(f"Index: {i}")

# Example 5: Indexing a string (sequence of characters)
word: str = "Python"
first_char: str = word[0]

# Example 6: Random number generation
import random
random_number: int = random.randint(1, 100)

# Example 7: Mathematical functions with the math module
import math
square_root: float = math.sqrt(25)
sin_value: float = math.sin(math.radians(30))

# Example 8: Complex numbers
complex_num1: complex = 2 + 3j
complex_num2: complex = 1 - 2j
result_complex_addition: complex = complex_num1 + complex_num2




