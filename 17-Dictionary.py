#Using python to manipulate dictionary
'''
Python Dictionary is used to store the data in a "key-value" pair 
format.The dictionary is the data type in Python, which can 
simulate the real-life data arrangement where some specific 
value exists for some particular key. It is the mutable 
data-structure. The dictionary is defined into element 
"Keys" and "values".

1.Keys must be a single element
2.Value can be any type such as list, tuple, integer, etc.

In other words, we can say that a dictionary is the collection of key-value 
pairs where the value can be any Python object. In contrast, the keys are 
the immutable Python object, i.e., Numbers, string, or tuple.

Dictionaries are used to store data values in key:value pairs.

some_dict = {
    'a_key': 'a_value',
    'a_key_2': 'a_value_2',
    'a_key_3': ['a_list', 'as', 'a value'],
    'a_key_4': {'a_dict': 'as a value'}
}

Dictionaries are mutable - this means that item values can be changed

Dictionaries have a bunch of methods available.
clear() Removes all the elements from the dictionary
copy() Returns a copy of the dictionary
fromkeys() Returns a dictionary with the specified keys and value
get() Returns the value of the specified key
items() Returns a list containing a tuple for each key value pair
keys() Returns a list containing the dictionary's keys
pop() Removes the element with the specified key
popitem() Removes the last inserted key-value pair
setdefault() Returns the value of the specified key. If the key does not exist: 
insert the key, with the specified value
update() Updates the dictionary with the specified key-value pairs
values() Returns a list of all the values in the dictionary
'''

#The basics
some_dict = {
    'a_key': 'a_value',
    'a_key_2': 'a_value_2',
    'a_key_3': ['a_list', 'as', 'a value'],
    'a_key_4': {'a_dict': 'as a value'}
}
some_dict


some_dict[0]  # this will return an error as you need to ref the key by name
some_dict['a_key']
some_dict['a_key_4']

#Basic
Employee = {"Name": "Hamza", "Age": 20, "salary":250000,"Company":"GOOGLE"}    
print(type(Employee))    
print("printing Employee data .... ")    
print(Employee)   

#Accessing the dictionary values
'''
the values can be accessed in the dictionary by using the keys as 
keys are unique in the dictionary.
'''
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}  
print(type(Employee))  
print("printing Employee data .... ")  
print("Name : %s" %Employee["Name"])  
print("Age : %d" %Employee["Age"])  
print("Salary : %d" %Employee["salary"])  
print("Company : %s" %Employee["Company"])  

'''
Output
<class 'dict'>
printing Employee data .... 
Name : John
Age : 29
Salary : 25000
Company : GOOGLE
'''
#Adding dictionary values
'''
he value can be updated along with key Dict[key] = value. The update() 
method is also used to update an existing value.
'''
# Creating an empty Dictionary   
Dict = {}   
print("Empty Dictionary: ")   
print(Dict)   

#example 1    
# Adding elements to dictionary one at a time   
Dict[0] = 'Peter'  
Dict[2] = 'Joseph'  
Dict[3] = 'Ricky'  
print("\nDictionary after adding 3 elements: ")   
print(Dict)   
# Adding set of values    
# with a single Key   
# The Emp_ages doesn't exist to dictionary  
Dict['Emp_ages'] = 20, 33, 24  
print("\nDictionary after adding 3 elements: ")   
print(Dict)       
# Updating existing Key's Value   
Dict[3] = 'JavaTpoint'  
print("\nUpdated key value: ")   
print(Dict)  

'''
Output
Empty Dictionary: 
{}

Dictionary after adding 3 elements: 
{0: 'Peter', 2: 'Joseph', 3: 'Ricky'}

Dictionary after adding 3 elements: 
{0: 'Peter', 2: 'Joseph', 3: 'Ricky', 'Emp_ages': (20, 33, 24)}

Updated key value: 
{0: 'Peter', 2: 'Joseph', 3: 'JavaTpoint', 'Emp_ages': (20, 33, 24)
'''
#Example 2
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
print(type(Employee))    
print("printing Employee data .... ")    
print(Employee)    
print("Enter the details of the new employee....");    
Employee["Name"] = input("Name: ");    
Employee["Age"] = int(input("Age: "));    
Employee["salary"] = int(input("Salary: "));    
Employee["Company"] = input("Company:");    
print("printing the new data");    
print(Employee)    

'''
<class 'dict'>
{'Name': 'John', 'Age': 29, 'salary': 25000, 'Company': 'GOOGLE'}
Enter the details of the new employee....
Name: Muhammad Hashim
Age: 22
Salary: 50000
Company:Google
printing the new data
{'Name': 'Muhammad Hashim', 'Age': 22, 'salary': 50000, 'Company': 'Google'}
'''

#Deleting elements using del keyword
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
print(type(Employee))    
print("printing Employee data .... ")    
print(Employee)    
print("Deleting some of the employee data")     
del Employee["Name"]    
del Employee["Company"]    
print("printing the modified information ")    
print(Employee)    
print("Deleting the dictionary: Employee");    
del Employee    
print("Lets try to print it again ");    
print(Employee) 

'''
Output
<class 'dict'>
printing Employee data .... 
{'Name': 'John', 'Age': 29, 'salary': 25000, 'Company': 'GOOGLE'}
Deleting some of the employee data
printing the modified information 
{'Age': 29, 'salary': 25000}
Deleting the dictionary: Employee
Lets try to print it again 
NameError: name 'Employee' is not defined
'''
#Iterating Dictionary using for loop
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
for x in Employee:    
    print(x)  
'''
Output
Name
Age
salary
Company
'''

#for loop to print all the values of the dictionary
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
for x in Employee:    
    print(Employee[x])  
'''
Output
John
29
25000
GOOGLE
'''

#for loop to print the items of the dictionary by using items() method.
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
for x in Employee.items():    
    print(x)  
'''
Output
('Name', 'John')
('Age', 29)
('salary', 25000)
('Company', 'GOOGLE')
'''


#show all keys and values
some_dict.keys()
some_dict.values()


#Dict comprehension
{x: x**2 for x in (2, 4, 6)}

#built-in function dict()
x = dict(a=1, b=2, c=3, d=4)# creates a dictionary object
x