# Python Sets and Dictionary

In Python, sets and dictionaries are fundamental data structures designed to facilitate efficient and flexible data organization.
sets and dictionaries in Python offer distinct advantages for managing and manipulating data efficiently. Whether it's ensuring uniqueness, performing set operations, or establishing key-value associations, these data structures enhance the flexibility and speed of various programming tasks.

1. [Sets](#1-Sets)
2. [Dictionary](#2-Dictionary)


# 1. Sets

A set is an unordered collection of unique elements. It is commonly used when the order of elements doesn't matter, and the presence of distinct values is essential. Sets offer efficient membership testing and provide operations such as union, intersection, and difference, making them useful for various mathematical and logical operations.


## Using python to manipulate sets

A Python set is the collection of the "unordered items". 
Each element in the set must be "unique", "immutable", 
and the sets remove the duplicate elements. 
Sets are mutable which means we can modify it after its creation.

Unlike other collections in Python, there is no index attached 
to the elements of the set, i.e., we cannot directly access 
any element of the set by the index. However, we can print 
them all together, or we can get the list of elements by 
looping through the set.

## Sets are mutable - this means that items can be changed.

Set has a whole bunch of methods available.
add() Adds an element to the set
clear() Removes all the elements from the set
copy() Returns a copy of the set
difference() Returns a set containing the difference between two or more sets
difference_update() Removes the items in this set that are also included in another, specified set
discard() Remove the specified item
intersection() Returns a set, that is the intersection of two or more sets
intersection_update() Removes the items in this set that are not present in other, specified set(s)
isdisjoint() Returns whether two sets have a intersection or not
issubset() Returns whether another set contains this set or not
issuperset() Returns whether this set contains another set or not
pop() Removes an element from the set
remove() Removes the specified element
symmetric_difference() Returns a set with the symmetric differences of two sets
symmetric_difference_update() Inserts the symmetric differences from this set and another
union() Return a set containing the union of sets
update() Update the set with another set, or any other iterable
'''

## Python Sets Basics

```python
a set is defined by a curly bracket. {}
```
```python
# Static datatype declaration for a set of integers
numbers: set[int] = {1, 2, 3, 4, 5}
Set of Integers:
```
```python
# Static datatype declaration for a set of strings
names: set[str] = {"hamza", "Babar", "Maaz"}
Set of Strings:
```
```python
# Static datatype declaration for a set of floats
prices: set[float] = {19.99, 29.95, 39.99}
Set of Floats:
```
```python
# Static datatype declaration for a set with mixed types (int and str)
mixed_set: set[Union[int, str]] = {1, "apple", 3, "orange"}
Mixed-Type Set:
```
```python
# Static datatype declaration for an empty set of booleans
flags: set[bool] = set()
Empty Set of Booleans:
```

```python
#Example 1
Days : set[str] = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}    
print(Days)    
print(type(Days))    
print("looping through the set elements ... ")    
for i in Days:    
    print(i)  

    Output
{'Friday', 'Tuesday', 'Monday', 'Saturday', 'Thursday', 'Sunday', 'Wednesday'}
<class 'set'>
looping through the set elements ... 
Friday
Tuesday
Monday
Saturday
Thursday
Sunday
Wednesday
'''  
'''
```
It can contain any type of element such as integer, float, tuple etc.
But mutable elements (list, dictionary, set) can't be a member of set. 
Consider the following example.

```python
# Creating a set which have immutable elements  
set1 : set [int, str, float] = {1,2,3, "JavaTpoint", 20.5, 14}  
print(type(set1))  
#Creating a set which have mutable element  
set2 = {1,2,3,["Javatpoint",4]}  
print(type(set2))  

'''
Output
<class 'set'>
```


```python
Traceback (most recent call last)
<ipython-input-5-9605bb6fbc68> in <module>
      4 
      5 #Creating a set which holds mutable elements
----> 6 set2 : set[int,str] = {1,2,3,["Javatpoint",4]}
      7 print(type(set2))

TypeError: unhashable type: 'list'
```
In the above code, we have created two sets, the set set1 have immutable 
elements and set2 have one mutable element as a list. While checking 
the type of set2, it raised an error, which means set can contain only 
immutable elements.

# Empty Sets

Creating an empty set is a bit different because empty curly {} braces 
are also used to create a dictionary as well. So Python provides the set() 
method used without an argument to create an empty set.
```python
'''
# Empty curly braces will create dictionary  
set3 = {}  
print(type(set3))  
```

```python
# Empty set using set() function  
set4 = set()  
print(type(set4))  
'''
Output
<class 'dict'>
<class 'set'>
```

### Adding items to the set

Python provides the add() method and update() method which can be used 
to add some particular item to the set. The add() method is used to add a 
single element whereas the update() method is used to add multiple elements 
to the set. Consider the following example.


```python
#Example
set = {"January","February"}
set.add(""March"")
set.update({"April", "May", "June"})
for i in set:    
    print(i)  

'''
Output
March
May
February
April
June
January
'''
```

### Removing items to the set

'''
Python provides the discard() method and remove() method 
which can be used to remove the items from the set. The difference 
between these function, using discard() function if the item does not 
exist in the set then the set remain unchanged whereas remove() method 
will through an error
'''

```python
#Removing items from the set

months : set[str] =  {"January","February", "March", "April", "May", "June"}     
print(months)    
print("\nRemoving some months from the set...")
months.discard("January")
months.discard("April")
months.remove("August")
'''
{'March', 'May', 'February', 'April', 'June', 'January'}
{'March', 'May', 'February', 'June'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'August'
'''
```

## Python Set Operations

Set can be performed mathematical operation such as "union", 
"intersection", "difference", and "symmetric difference". 
Python provides the facility to carry out these operations
 with operators or methods. We describe these 
operations as follows.

## Union of two Sets

The union of two sets is calculated by using the pipe (|) operator.
or the union() function The union of the two sets contains all 
the items that are present in 
both the sets.

```python
#Example 1: using union | operator
a : set[str] = {"a", "b", "c", "d", "e"}
b : set[str] = {"b", "d", "f", "a", "c"}
a|b
#{'f', 'c', 'e', 'd', 'a', 'b'} Output
```

```python
set1: Set[int] = {2, 4, 5, 6}
set2: Set[int] = {4, 6, 7, 8}
set3: Set[int] = {7, 8, 9, 10}
 
# union of two sets
print("set1 U set2 U set3 :", set1.union(set2).union(set3))
 
# union of three sets
print("set1 U set2 U set3 :", set1.union(set2, set3))
Output: 


```

##  Intersection of two sets

The intersection of two sets can be performed by the and & operator or 
the intersection() function. The intersection of the two sets is given as 
the set of the elements that common in both sets.

```python
Days1 : Set[str] = {"Monday","Tuesday", "Wednesday", "Thursday"}    
Days2 : Set[str] = {"Monday","Tuesday","Sunday", "Friday"}    
print(Days1&Days2) # {'Monday', 'Tuesday'}
```

## Difference of two sets

The difference of two sets can be calculated by using the subtraction (-) 
operator or intersection() method. Suppose there are two sets A and B, and 
the difference is A-B that denotes the resulting set will be obtained that 
element of A, which is not present in the set B.

```python
#Difference between the two sets
'''
Days1 : Set[str] = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 : Set[str] = {"Monday", "Tuesday", "Sunday"}    
print(Days1.difference(Days2)) 
```
## Symmetric Difference of two sets

The symmetric difference of two sets is calculated by ^ operator or 
symmetric_difference() method. Symmetric difference of sets, it removes 
that element which is present in both sets. Consider the following example:

```python
a : Set[int] = {1,2,3,4}  
b : Set[int] = {1,2,9}  
c = a^b  
print(c)  #{3, 4, 9}
```
```python
a: Set[int] = {1, 2, 3, 4, 5}
b: Set[int] = {4, 5, 6, 7, 8}

# Symmetric difference of sets
symmetric_difference_result: Set[int] = a.symmetric_difference(b)
```

## Super Sets

```python
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday"}    
Days3 = {"Monday", "Tuesday", "Friday"}    
```
```python
#Days1 is the superset of Days2 hence it will print true.     
print (Days1>Days2)   
```
```python
#prints false since Days1 is not the subset of Days2     
print (Days1<Days2)    
    
```
```python
#prints false since Days2 and Days3 are not equivalent     
print (Days2 == Days3) 
```

# 2. Dictionary  


Dictionaries, on the other hand, are collections of key-value pairs. They enable the association of values with unique keys, providing a way to store and retrieve information using meaningful identifiers. Dictionaries are particularly valuable when there is a need for fast data access and retrieval based on specific keys. They are versatile and widely used in scenarios where data needs to be stored and accessed in a structured manner.

## Python Static Typing for Dictionaries

This guide demonstrates the creation of dictionaries in Python using static typing. We'll explore dictionaries with different hashable key types and values of type Any, Optional, and Union. Additionally, we'll use dictionary comprehensions and demonstrate swapping keys and values.

## Table of Contents

3. [Setting up Static Typing ](#Setting-up-Static-Typing)
4.  [Creating Dictionaries ](#Creating-Dictionaries)






```python
```
```python
```
```python
```