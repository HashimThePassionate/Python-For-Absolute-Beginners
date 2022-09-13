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