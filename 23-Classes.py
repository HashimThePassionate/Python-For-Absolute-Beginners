# Python classes
'''
Everything in Python is an object. An object has a state and 
behaviors. To create an object, you define a class first. 
And then, from the class, you can create one or more 
objects. The objects are instances of a class.

Classes provide a means of bundling data and functionality together. 
Creating a new class creates a new type of object, allowing new 
instances of that type to be made.

The simplest form of class definition looks like this:
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>

Class definitions, like function definitions (def statements) 
must be executed before they have any effect.

'''
#Define a class
'''
To define a class, you use the class keyword followed by 
the class name. For example, the following defines a Person class:

Since the Person class is incomplete; you need to use the pass 
statement to indicate that you’ll add more code to it later.
'''
class Person:
    pass
print(Person)
print(id(Person))
'''

To create an object from the Person class, you use the class name 
followed by parentheses (), like calling a function:

An object is a container that contains data and functionality
the data of an object is called the "state". 
Python uses attributes to model the state of an object.
'''
p = Person()

#Define instance attributes
'''
Python is dynamic. It means that you can add an attribute to an 
instance of a class dynamically at runtime.

For example, the following adds the name attribute to the person
object:
'''
p.name = 'Hashim'
'''
To define and initialize an attribute for all instances of a class, 
you use the __init__ method also known as constructor. The following 
defines the Person class with two instance 
attributes "name" and "age":
'''
#Parameterized Constructor
class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age
#The following creates a Person object named person:
'''
When you create a Person object, Python automatically calls 
the __init__ method to initialize the instance attributes. 
In the __init__ method, the self is the instance of the 
Person class.

self represents the instance of the class. By using the “self”  
we can access the attributes and methods of the class in python. 
It binds the attributes with the given arguments

Self is always pointing to Current Object.
'''
p = Person("Hashim",22)
'''
The p object now has the name and age attributes. 
To access an instance attribute, you use the dot notation. 
For example, the following returns the value of the name 
attribute of the person object
'''
p.name
p.age

#Non-parameterized Constructor
#it is clearly seen that self and obj is referring to the same object
class check:
	def __init__(self):
		print("This is non parametrized constructod id =  ",id(self))

obj = check()
print("Address of class object = ",id(obj))
'''
Output
This is non parametrized constructod id = =  2175972664240
Address of class object =  2175972664240
'''
#Define Class Attribute
'''
Unlike instance attributes, class attributes are shared by all 
instances of the class. They are helpful if you want to define 
class constants or variables that keep track of the number of 
instances of a class.

For example, the following defines the "counter" class attribute 
in the Person class:
'''
class Person:
    counter = 0 #Attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter+=1
    def great(self):
        return f"Hi, it's {self.name}."

#The following creates two instances of the Person class and 
#shows the value of the counter:

p1 = Person('Hashim', 22)
p1.great()
p2 = Person('Hamza', 20)
p2.great()
print(Person.counter)
Person.counter=10
print(Person.counter)
print("The First  object counter value is ",p1.counter)
print("The Second  object counter value is ",p2.counter)
'''
"Hi, it's Hashim."
"Hi, it's Hamza."
2
10
The First  object counter value is  10
The Second  object counter value is  10
'''
#Define instance methods
'''
If we use "instance variables" inside a method, 
such methods are called instance methods.

The "instance method" performs a set of actions on 
the data/value provided by the "instance variables".

To work with an instance method, we use the "self" keyword. 
We use the "self" keyword as the "first parameter" to a method. 
The "self" refers to the current object.
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def great(self):
        return f"Hi, it's {self.name}."

p1 = Person('Hashim', 22)
print(p.great())
p2 = Person('Hamza', 20)
print(p.great())

'''
Note:

Inside any instance method, we can use "self" to access any "data" or 
method that reside in our class. We are unable to access it 
without a self parameter.

An instance method can freely access attributes and even modify 
the value of "attributes" of an object by using the "self" parameter.

'''
#Let’s create the instance method update() method 
#to modify the Person age and roll number
class Person:
    def __init__(self, roll_no, name, age):
        self.roll_no = roll_no
        self.name = name
        self.age = age
    # instance method access instance variable
    def show(self):
        print('Roll Number:', self.roll_no, 'Name:', self.name, 'Age:', self.age,)
    # instance method to modify instance variable
    def update(self, roll_number,name, age):
        self.roll_no = roll_number
        self.name = name
        self.age = age

# create object
s = Person(2, "Hashim", 21)
print(Person.counter)
# call instance method
s.show()

# Modify instance variables
s.update(1,"Hamza", 20)
s.show()

#Define class method
'''
inside an instance method, we use the self keyword to access or modify the 
instance variables. Same inside the class method, we use the cls keyword as 
a first parameter to access class variables

The class method can only access the class attributes, not the instance attributes

'''
from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year):
        # calculate age an set it as a age
        # return new object
        return Person(name, date.today().year - birth_year)

    def show(self):
        print(self.name + "'s age is: " + str(self.age))

a = Person('Hashim', 21)
a.show()

# create new object using the factory method
'''
The calculate_age() method takes Person class (cls) as a first 
parameter and returns constructor by calling 
Person(name, date.today().year - birthYear), 
which is equivalent to Person(name, age).
'''
b = Person.calculate_age("Hamza", 2001)
b.show()

#Another Class Method Example
class Person:
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def show(self):
        return f"Hi, it's {self.name}."

    @classmethod
    def create_anonymous(cls):
        return Person('Hashim', 22)  

a = Person("Hamza", 20)
a.show()
b = Person.create_anonymous()
print(b.name)  # Anonymous

#Static Method 
'''
A static method is bound to the class and not the 
object of the class. Therefore, we can call it 
using the class name.
'''
class Person:
    @staticmethod
    def sample(x):
        print('Inside static method', x)

# call static method
Person.sample(10)

#Another Example of static method
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9 * c / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5 * (f - 32) / 9
print(TemperatureConverter.celsius_to_fahrenheit(30))  # 86.0

#Single inheritance
'''
A class can reuse another class by inheriting it. When a child class 
inherits from a parent class, the child class can access the 
attributes and methods of the parent class.

Syntax
class derived-class(base class):  
    <class-suite>  
'''
class Animal:  
    def speak(self):  
        print("Animal Speaking") 
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak()  

#Python Multi-Level inheritance
'''
Multi-Level inheritance is possible in python like other object-oriented languages. 
Multi-level inheritance is archived when a derived class inherits another derived class. 
There is no limit on the number of levels up to which, the multi-level inheritance is 
archived in python.

Syntax
class class1:  
    <class-suite>   
class class2(class1):  
    <class suite>  
class class3(class2):  
    <class suite>  
'''

class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#The child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
#The child class Dogchild inherits another child class Dog  
class DogChild(Dog):  
    def eat(self):  
        print("Eating bread...")  
d = DogChild()  
d.bark()  
d.speak()  
d.eat()  

#Python Multiple inheritance
'''
Syntax
class Base1:  
    <class-suite>  
  
class Base2:  
    <class-suite>  
.  
.  
.  
class BaseN:  
    <class-suite>  
  
class Derived(Base1, Base2, ...... BaseN):  
    <class-suite>  
'''
class Calculation1:  
    def Summation(self,a,b):  
        return a+b
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b
d = Derived()  
print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20))  






