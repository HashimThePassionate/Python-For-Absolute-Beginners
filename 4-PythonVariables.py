#Variables are containers for storing data values.
'''
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
'''
#Variable Assignment
n = 300
id(n)
print(n)

#Example
m = n
print("Value of m ",m)
print("id of m ",id(m))
print("Value of n ",n)
print("id of n ",id(n))

m=400
print("Value of m ",m)
print("id of m ",id(m))
print("Value of n ",n)
print("id of n ",id(n))

n = "Hello"
print("Value of m ",m)
print("id of m ",id(m))
print("Value of n ",n)
print("id of n ",id(n))

#TYPE of Variable
a = 2
type(a)

#Same id to these objects
n = 10
m = n
print("n = :",id(n))
print("m = :",id(m))

'''
Camel case nOfStudent = "Hamza"
Pascal case NOfStudent = "Subhan"
Snake case  name_of_student = "Zeeshan"
'''

#Types of  Variable data 
#int 
a = 10 
b = -10
#float 
a = 10.1 
b = -10.1 
#string
name = " Farooq " 
#bool
a = True
#----------------------------------------------------------------
#using Print()
name = "Hashim"
age = 23
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




