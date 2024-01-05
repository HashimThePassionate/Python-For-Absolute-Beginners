## Using python to manipulate tuples

Python Tuple is used to store the sequence of immutable Python 
objects. 

Tuples are written as a list of "comma-separated"
```python
values (items) between parentheses. ()
```

Tuples are immutable - this means that items can not be changed. 
However,a tuple can contain mutable objects.

### Tuple has 2 methods available.

1. count()	Returns the number of elements with the specified value
2. index() Returns the index of the first element with the specified value


### The basics - tuple packing
```python
t = 12345, 54321, 'hello!'
t[0]
t
type(t)

T1 = (101, "Peter", 22)    
T2 = ("Apple", "Banana", "Orange")     
T3 = 10,20,30,40,50  
  
print(type(T1))  
print(type(T2))  
print(type(T3)) # Class Tuple

```
The tuple which is created without using parentheses is also known as tuple packing.
```python
a = 'abc', 2, 4, 'd'
print(type(a)) # Class Tuple

```
### An empty tuple can be created as follows.
```python
T4 = ()
```

### Creating a tuple with single element is slightly different.

 We will need to put comma after the element to declare the tuple

```python
tup1 = ("JavaTpoint")  #String
print(type(tup1))  
#Creating a tuple with single element   
tup2 = ("JavaTpoint",) #Tuple  
print(type(tup2)) 

```
## Output
```python
<class 'str'>
<class 'tuple'>

```
### Example 1
```python
tuple1 = (10, 20, 30, 40, 50, 60)    
print(tuple1)    
count = 0    
for i in tuple1:    
    print("tuple1[%d] = %d"%(count, i))   
    count = count+1  

```
### Output
```python
(10, 20, 30, 40, 50, 60)
tuple1[0] = 10
tuple1[1] = 20
tuple1[2] = 30
tuple1[3] = 40
tuple1[4] = 50
tuple1[5] = 60

```

### Example 2
```python
tuple1 = tuple(input("Enter the tuple elements ..."))  
print(tuple1)    
count = 0    
for i in tuple1:    
    print("tuple1[%d] = %s"%(count, i))   
    count = count+1  


```
### Output
```python
Enter the tuple elements ...123456
('1', '2', '3', '4', '5', '6')
tuple1[0] = 1
tuple1[1] = 2
tuple1[2] = 3
tuple1[3] = 4
tuple1[4] = 5
tuple1[5] = 6

```
### indexing
```python
tuple = (1,2,3,4,5,6,7)
```  
### element 1 to end 
```python#
print(tuple[1:])  

``` 
### element 0 to 3 element   
```python
print(tuple[:4])
```  
#### element 1 to 4 element  
```python
print(tuple[1:5])   

```
### element 0 to 6 and take step of 2  
```python
print(tuple[0:6:2])  

```
### Output
```python
(2, 3, 4, 5, 6, 7)
(1, 2, 3, 4)
(1, 2, 3, 4)
(1, 3, 5)

```

### Negative Indexing
```python
tuple1 = (1, 2, 3, 4, 5)    
print(tuple1[-1])    
print(tuple1[-4])    
print(tuple1[-3:-1])  
print(tuple1[:-1])  
print(tuple1[-2:])  

```
### Output
```python
5
2
(3, 4)
(1, 2, 3, 4)
(4, 5)

```
### Deleting Tuple

Unlike lists, the tuple items cannot be deleted by using the del keyword 
as tuples are immutable. To delete an entire tuple, we can use the del 
keyword with the tuple name.

```python
tuple1 = (1, 2, 3, 4, 5, 6)    
print(tuple1)    
del tuple1[0]    
print(tuple1)    
del tuple1    
print(tuple1) 

```
### Output
```python
(1, 2, 3, 4, 5, 6)

```
```python
Traceback (most recent call last):
  File "tuple.py", line 4, in <module>
    print(tuple1)
NameError: name 'tuple1' is not defined

```

### Python Tuple inbuilt functions

SN	Function	Description
```python

1	cmp(tuple1, tuple2)	It compares two tuples and returns true
                 if tuple1 is greater than tuple2 otherwise false.
2	len(tuple)	It calculates the length of the tuple.
3	max(tuple)	It returns the maximum element of the tuple
4	min(tuple)	It returns the minimum element of the tuple.
5	tuple(seq)	It converts the specified sequence to the tuple.

```

### Where use tuple?
```python
1. Using tuple instead of list gives us a clear idea that tuple data 
is constant and must not be changed.
2. Tuple can simulate a dictionary without keys. Consider the following 
nested structure, which can be used as a dictionary.
[(101, "John", 22), (102, "Mike", 28),  (103, "Dustin", 30)]  

```

### Tuples may be nested:
```python
v = ([1, 2, 3], [3, 2, 1])
u = v, (1, 2, 3, 4, 5)
u

```

 