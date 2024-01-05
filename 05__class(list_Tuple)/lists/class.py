#Using python to manipulate lists
'''
A list in Python is used to store the sequence of various 
types of data. Python lists are mutable type.

Python knows a number of compound data types, 
used to group together other values. The most
versatile of which is a list.
Others include:
tuple
set
dictionary
Lists are written as a list of comma-separated 
values (items) between square brackets []

Lists are mutable - this means that items can be changed

List have a bunch of methods available.
append() Adds an element at the end of the list
clear()	Removes all the elements from the list
copy() Returns a copy of the list
count()	Returns the number of elements with the specified value
extend() Add the elements of a list (or any iterable), to the end of the 
current list
index() Returns the index of the first element with the specified value
insert() Adds an element at the specified position
pop() Removes the element at the specified position
remove() Removes the first item with the specified value
reverse() Reverses the order of the list
sort() Sorts the list
'''
#A list can be define as below
# Creating lists with mixed types
L1: List[Union[str, int, str]] = ["John", 102, "USA"]
L2: List[int] = [1, 2, 3, 4, 5, 6]

print(type(L1))
print(type(L2))
'''
If we try to print the type of L1, L2, and L3 using type() function 
then it will come out to be a "list".
''' 

#lets check the list are same objects equal or not
from typing import List, Union

a: List[Union[int, str, float]] = [1, 2, "Peter", 4.50, "Ricky", 5, 6]
b: List[Union[int, str, float]] = [1, 2, "Peter", 4.50, "Ricky", 5, 6]

print(a is b)  # Output: False
print(id(a))
print(id(b))

b = a

print(a is b)  # Output: True
print(id(a))
print(id(b))

##Let's check the first statement that lists are the ordered.

a: List[Union[int, float, str]] = [1, 2, "Peter", 4.50, "Ricky", 5, 6]
b: List[Union[int, float, str]] = [1, 2, "Peter", 4.50, "Ricky", 5, 6]

result: bool = a == b
print(result)


'''
Both lists have consisted of the same elements, but the second list 
changed the index position of the 5th element that violates the order 
of lists. When compare both lists it returns the false.

Lists maintain the order of the element for the lifetime. That's why it 
is the ordered collection of objects.
'''

a: List[Union[int, float, str]] = [1, 2, "Peter", 4.50, "Ricky", 5, 6]
b: List[Union[int, float, str]] = [1, 2, "Peter", 4.50, "Ricky", 5, 6]

result: bool = a == b
print(result)

# The basics
squares: List[int] = [1, 4, 9, 16, 25]
print(squares)
#Indexing
'''
 +---+---+---+---+---+
 | 1 | 4 | 9 | 16 | 25|
 +---+---+---+---+---+
   0   1   2   3    4     
  -5  -4  -3  -2   -1  
'''

squares[0]  # indexing returns the item 1
squares[-1] # 25
squares[-3:]  # slicing returns a new list [9,16,25]

#Create a list copy
squares[:] # [1, 4, 9, 16, 25]

#Concatenation (glue together)
squares + [36, 49, 64, 81, 100] 
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Alter items
cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value


#list methods
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7


#Length

letters: List[str] = ['a', 'b', 'c', 'd']
length: int = len(letters)

print(length)


#Nesting
# Type hints for variables
a: List[str] = ['a', 'b', 'c']
n: List[int] = [1, 2, 3]
x: List[List[Union[str, int]]] = [a, n]

# Alternatively, you can directly provide type hints to the lists
# x: List[List[Union[str, int]]] = [['a', 'b', 'c'], [1, 2, 3]]

print(x)
print(x[0])
print(x[0][1])
print(x[1][2])

#nesting 2nd
# Type hints for variables
a: List[str] = ['a', 'b', 'c', 'd']
b: List[int] = [1, 2, 4, 5]
c: List[Union[int, str]] = [1, 'abc', 3, 4]
d: List[List[Union[str, int, List[Union[int, str]]]]] = [a, b, c]

print(d)
'''
output [['a', 'b', 'c', 'd'], [1, 2, 4, 5], [1, 'abc', 3, 4]]
'''
d[0][3] #d
d[2][1] #abc
'''
output 'd'
'''
d[1][2]
'''
output 4
'''
d[3][1]
'''
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
IndexError: list index out of range
'''
d[2][1]
'''
output 'abc'
'''

#Let's have a look at the list example in detail.

# Static type hints for variables
student: List[Union[str, int]] = ["Hamza", 21, "Spartan300"]
Field1: List[Union[str, int]] = ["Wp full stack", 1]
Field2: List[Union[str, int]] = ["Mern Stack", 2]
HOD_Field1: List[Union[int, str]] = [10, "Sr. Farooq"]
HOD_Field2: List[Union[int, str]] = [11, "Mr. Hamza"]

# Print Student data
print("printing Student data...")
print("Name : %s, ID: %d, Team: %s" % (student[0], student[1], student[2]))

# Print Fields of Expert
print("printing Fields of Expert...")
print("Field 1:\nName: %s, ID: %d\nField 2:\nName: %s, ID: %s" % (Field1[0], Field1[1], Field2[0], Field2[1]))

# Print HOD Details
print("HOD Details ....")
print("HOD Name: %s, Id: %d" % (HOD_Field1[1], HOD_Field1[0]))
print("HOD Name: %s, Id: %d" % (HOD_Field2[1], HOD_Field2[0]))

# Print types
print(type(student), type(Field1), type(Field2), type(HOD_Field1), type(HOD_Field2))

'''
Output
printing Student data...
Name : Hamza, ID: 21, Team: Spartan300
printing Fields of Expert...
Field 1:
Name: Wp full stack, ID: 1
Field 2:
Name: Mern Stack, ID: 2
HOD Details ....
HOD Name: Sr. Farooq, Id: 10
HOD Name: Mr. Hamza, Id: 11
<class 'list'> <class 'list'> <class 'list'> <class 'list'> <class 'list'>
'''

#Updating List values
'''
Lists are the most versatile data structures in Python since they 
are mutable, and their values can be updated by using the slice 
and assignment operator.
'''
# Static type hint for the list
my_list: List[int] = [1, 2, 3, 4, 5, 6]

# Print the initial list
print(my_list)

# Assign a value to the second index
my_list[2] = 10
print(my_list)

# Adding multiple elements
my_list[1:3] = [89, 78]
print(my_list)

# Add a value at the end of the list
my_list[-1] = 25
print(my_list)

'''
Output
[1, 2, 3, 4, 5, 6]
[1, 2, 10, 4, 5, 6]
[1, 89, 78, 4, 5, 6]
[1, 89, 78, 4, 5, 25]
'''

#Python List Operations
'''
The concatenation (+) and repetition (*) operators work 
in the same way as they were working with the strings.
'''

# Static type hints for the lists
l1: List[int] = [1, 2, 3, 4]
l2: List[int] = [5, 6, 7, 8]

# Print the result of expressions
print(l1 * 2 + l2)
print(l1 + l2)
print(len(l1))

#Iterating a List
# Static type hint for the list
my_list: List[str] = ["John", "David", "James", "Jonathan"]

# Iterate over the list and print each element
for i in my_list:
    print(i)


#Adding elements to the list
#Declaring the empty list  
my_list: List[int] = [] 
#Number of elements will be entered by the user    
n = int(input("Enter the number of elements in the list:"))  
# for loop to take the input  
for i in range(0,n):     
    # The input is taken from the user and added to the list as the item  
    l.append(input("Enter the item:"))     
print("printing the list items..")   
# traversal loop to print the list items    
for i in l:   
    print(i, end = "  ")  

'''
Output
Enter the number of elements in the list:5
Enter the item:25
Enter the item:46
Enter the item:12
Enter the item:75
Enter the item:42
printing the list items
25  46  12  75  42
'''

#Removing elements from the list
'''
Python provides the remove() function which is used to remove the 
element from the list. Consider the following example to understand 
this concept.
'''
my_list: List[int] = [0, 1, 2, 3, 4]
  
print("printing original list: ");    
for i in list:    
    print(i,end=" ")    
my_list.remove(2)    
print("\nprinting the list after the removal of first element...")    
for i in list:    
    print(i,end=" ") 

'''
Output
printing original list: 
0 1 2 3 4 
printing the list after the removal of first element...
0 1 3 4
'''

#List comprehension
'''
Python is known for helping us produce code that is elegant, simple to 
write, and reads almost as well as plain English. List comprehension 
is one of the language's most distinguishing features, allowing us to 
develop sophisticated functionality with just one line of code. On 
the other hand, many Python writers struggle to fully utilize the 
more complex aspects of list comprehension. Sometimes programmers 
may overuse them, resulting in much less efficient and 
difficult-to-read code.
Using List Comprehension
newlist = [expression for item in iterable if condition == True]  
'''
#Example
numbers: List[int] = [3, 5, 1, 7, 3, 9]
num: List[int] = []
for n in numbers:  
    num.append(n**2)  
print(num)  
#All of this can be accomplished with only single line of code using 
# list comprehension.
#newlist = [expression for item in iterable if condition == True]  
numbers = [3, 5, 1, 7, 3, 9]  
num = [n**2 for n in numbers]
print(num)




