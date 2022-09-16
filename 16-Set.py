#Using python to manipulate sets
'''
A Python set is the collection of the "unordered items". 
Each element in the set must be "unique", "immutable", 
and the sets remove the duplicate elements. 
Sets are mutable which means we can modify it after its creation.

Unlike other collections in Python, there is no index attached 
to the elements of the set, i.e., we cannot directly access 
any element of the set by the index. However, we can print 
them all together, or we can get the list of elements by 
looping through the set.

a set is defined by a curly bracket. {}

Sets are mutable - this means that items can be changed.

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

#The basics
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)# show that duplicates have been removed

'orange' in basket # fast membership testing TRUE
'crabgrass' in basket # FALSE

#Example 1
Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}    
print(Days)    
print(type(Days))    
print("looping through the set elements ... ")    
for i in Days:    
    print(i)    
'''
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
It can contain any type of element such as integer, float, tuple etc.
But mutable elements (list, dictionary, set) can't be a member of set. 
Consider the following example.
'''
# Creating a set which have immutable elements  
set1 = {1,2,3, "JavaTpoint", 20.5, 14}  
print(type(set1))  
#Creating a set which have mutable element  
set2 = {1,2,3,["Javatpoint",4]}  
print(type(set2))  

'''
Output
<class 'set'>

Traceback (most recent call last)
<ipython-input-5-9605bb6fbc68> in <module>
      4 
      5 #Creating a set which holds mutable elements
----> 6 set2 = {1,2,3,["Javatpoint",4]}
      7 print(type(set2))

TypeError: unhashable type: 'list'

In the above code, we have created two sets, the set set1 have immutable 
elements and set2 have one mutable element as a list. While checking 
the type of set2, it raised an error, which means set can contain only 
immutable elements.

Creating an empty set is a bit different because empty curly {} braces 
are also used to create a dictionary as well. So Python provides the set() 
method used without an argument to create an empty set.
'''
# Empty curly braces will create dictionary  
set3 = {}  
print(type(set3))  
  
# Empty set using set() function  
set4 = set()  
print(type(set4))  
'''
Output
<class 'dict'>
<class 'set'>
'''

#Adding items to the set
'''
Python provides the add() method and update() method which can be used 
to add some particular item to the set. The add() method is used to add a 
single element whereas the update() method is used to add multiple elements 
to the set. Consider the following example.
'''
#Example
set = {"January","February"}
set.add(""March")
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
#Removing items from the set
'''
Python provides the discard() method and remove() method 
which can be used to remove the items from the set. The difference 
between these function, using discard() function if the item does not 
exist in the set then the set remain unchanged whereas remove() method 
will through an error
'''
months = {"January","February", "March", "April", "May", "June"}     
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
#Python Set Operations
'''
Set can be performed mathematical operation such as "union", 
"intersection", "difference", and "symmetric difference". 
Python provides the facility to carry out these operations
 with operators or methods. We describe these 
operations as follows.
'''
#Union of two Sets
'''The union of two sets is calculated by using the pipe (|) operator.
or the union() function The union of the two sets contains all 
the items that are present in 
both the sets.
'''
#Example 1: using union | operator
a = {"a", "b", "c", "d", "e"}
b = {"b", "d", "f", "a", "c"}
a|b
#{'f', 'c', 'e', 'd', 'a', 'b'} Output

#Intersection of two sets
'''
The intersection of two sets can be performed by the and & operator or 
the intersection() function. The intersection of the two sets is given as 
the set of the elements that common in both sets.
'''
Days1 = {"Monday","Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday","Tuesday","Sunday", "Friday"}    
print(Days1&Days2) # {'Monday', 'Tuesday'}

#Difference between the two sets
'''
The difference of two sets can be calculated by using the subtraction (-) 
operator or intersection() method. Suppose there are two sets A and B, and 
the difference is A-B that denotes the resulting set will be obtained that 
element of A, which is not present in the set B.
'''
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday", "Sunday"}    
print(Days1.difference(Days2)) 

#Symmetric Difference of two sets
'''
The symmetric difference of two sets is calculated by ^ operator or 
symmetric_difference() method. Symmetric difference of sets, it removes 
that element which is present in both sets. Consider the following example:
'''
a = {1,2,3,4}  
b = {1,2,9}  
c = a^b  
print(c)  #{3, 4, 9}

#Set comparisons
'''
Python allows us to use the comparison operators i.e., <, >, <=, >= , == 
with the sets by using which we can check whether a set is a subset, 
superset, or equivalent to other set. The boolean true or false is 
returned depending upon the items present inside the sets.
'''
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday"}    
Days3 = {"Monday", "Tuesday", "Friday"}    
    
#Days1 is the superset of Days2 hence it will print true.     
print (Days1>Days2)     
    
#prints false since Days1 is not the subset of Days2     
print (Days1<Days2)    
    
#prints false since Days2 and Days3 are not equivalent     
print (Days2 == Days3)   