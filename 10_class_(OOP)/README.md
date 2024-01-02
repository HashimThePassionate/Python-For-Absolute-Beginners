Explains the basic concepts of Object-Oriented Programming (OOP) in Python, including classes, methods, attributes, class variables, and inheritance. It also includes examples of an `Employee` class and its subclasses `Designer` and `Developer`, demonstrating the use of `super().__init__()` to initialize the parent class.

---

# Object-Oriented Programming in Python

## Table of Contents
1. [OOP Basic Concepts](#oop-basic-concepts)
2. [Classes, Methods, and Attributes](#classes-methods-and-attributes)
3. [Class Variables](#class-variables)
4. [Inheritance](#inheritance)
5. [Example: Employee, Designer, and Developer](#example-employee-designer-and-developer)


## OOP Basic Concepts
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data and code that manipulates that data. Objects are instances of classes, which can hold both data (attributes) and code (methods).

## Classes, Methods, and Attributes
- **Class**: A blueprint for creating objects.
- **Method**: A function defined inside a class.
- **Attribute**: A variable that belongs to an object.

## Python classes
Everything in Python is an object. An object has a state and 
behaviors. To create an object, you define a class first. 
And then, from the class, you can create one or more 
objects. The objects are instances of a class.
Classes provide a means of bundling data and functionality together. 
Creating a new class creates a new type of object, allowing new 
instances of that type to be made.

The simplest form of class definition looks like this:
```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```
## Define a class
To define a class, you use the class keyword followed by 
the class name. For example, the following defines a Person class:

Since the Person class is incomplete; you need to use the pass 
statement to indicate that you’ll add more code to it later.

```python
 class Person:
    pass
print(Person)
print(id(Person))
```
To create an object from the Person class, you use the class name 
followed by parentheses (), like calling a function:

An object is a container that contains data and functionality
the data of an object is called the "state". 
Python uses attributes to model the state of an object.
```python
p : Person = Person()
```
## Define instance attributes
Python is dynamic. It means that you can add an attribute to an 
instance of a class dynamically at runtime.

For example, the following adds the name attribute to the person
object:
```python
p.name = 'Hashim'
```
To define and initialize an attribute for all instances of a class, 
you use the __init__ method also known as constructor. The following 
defines the Person class with two instance 
attributes "name" and "age":


```python
 #Parameterized Constructor
class Person:
    def __init__(self, name : str, age : int) -> None:
        self.name = name  
        self.age = age
```
When you create a Person object, Python automatically calls 
the __init__ method to initialize the instance attributes. 
In the __init__ method, the self is the instance of the 
Person class.

self represents the instance of the class. By using the “self”  
we can access the attributes and methods of the class in python. 
It binds the attributes with the given arguments

Self is always pointing to Current Object.


```python
p : Person = Person("Hashim",22)
```
The p object now has the name and age attributes. 
To access an instance attribute, you use the dot notation. 
For example, the following returns the value of the name 
attribute of the person object
p.name
p.age
```python
p.name
p.age
```
it is clearly seen that self and obj is referring to the same object
## Example
```python
class check:
	def __init__(self)-> None:
		print("This is non parametrized constructod id =  ",id(self))

obj : check = check()
print("Address of class object = ",id(obj))
```
## Output
```python
This is non parametrized constructod id = =  2175972664240
Address of class object =  2175972664240
```
## Define Class Attribute
Unlike instance attributes, class attributes are shared by all 
instances of the class. They are helpful if you want to define 
class constants or variables that keep track of the number of 
instances of a class.
## Example defines the "counter" class attribute 
For example, the following defines the "counter" class attribute 
in the Person class:
```python
class Person:
    counter : int = 0 #Class Attribute
    def __init__(self, name : str, age : int):
        self.name = name
        self.age = age
        Person.counter+=1
    def great(self):
        return f"Hi, it's {self.name}."
```
The following creates two instances of the Person class and 
shows the value of the counter:
```python
p1 : Person = Person('Hashim', 22)
p1.great()
p2 : Person = Person('Hamza', 20)
p2.great()
print(Person.counter)
Person.counter=10
print(Person.counter)
print("The First  object counter value is ",p1.counter)
print("The Second  object counter value is ",p2.counter)
```
## output
```python
"Hi, it's Hashim."
"Hi, it's Hamza."
2
10
The First  object counter value is  10
The Second  object counter value is  10
```
## Note:
Inside any instance method, we can use "self" to access any "data" or 
method that reside in our class. We are unable to access it 
without a self parameter.

An instance method can freely access attributes and even modify 
the value of "attributes" of an object by using the "self" parameter.


### Example: Creating a Simple Class
```python
class Cat:
    def __init__(self, name : str, age:int)-> None:
        self.name = name  # Attribute
        self.age = age    # Attribute
    
    def bark(self)->None:       # Method
        print("Woof!")
```
## Class Variables
Class variables are shared by all instances of a class. They are set by prefixing a variable with the name of the class.

### Example: Using Class Variables
```python
class Dog:
    species : str = "Canis familiaris"  # Class variable
    
    def __init__(self, name : str, age : int)-> None:
        self.name = name
        self.age = age
    
    def bark(self)-> None:
        print("Woof!")
```

This is just Simple Example How we relate in real world Shopping Cart Ecommerce Website don't be confuse we can cover everything in very detail
```python
from typing import List

class Product:
    def __init__(self, product_id: int, name: str, price: float) -> None:
        self.product_id: int = product_id
        self.name: str = name
        self.price: float = price

    def __str__(self) -> str:
        return f"{self.name} - ${self.price:.2f}"


class ShoppingCart:
    def __init__(self) -> None:
        self.items: List[dict] = []

    def add_item(self, product: Product, quantity: int = 1) -> None:
        self.items.append({"product": product, "quantity": quantity})

    def remove_item(self, product: Product) -> None:
        self.items = [item for item in self.items if item["product"] != product]

    def calculate_total(self) -> float:
        total: float = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

    def __str__(self) -> str:
        cart_str: str = "Shopping Cart:\n"
        for item in self.items:
            cart_str += f"{item['product']} x{item['quantity']}\n"
        cart_str += f"Total: ${self.calculate_total():.2f}"
        return cart_str


class Customer:
    def __init__(self, name: str, email: str) -> None:
        self.name: str = name
        self.email: str = email
        self.shopping_cart: ShoppingCart = ShoppingCart()

    def add_to_cart(self, product: Product, quantity: int = 1) -> None:
        self.shopping_cart.add_item(product, quantity)

    def remove_from_cart(self, product: Product) -> None:
        self.shopping_cart.remove_item(product)

    def checkout(self) -> None:
        total: float = self.shopping_cart.calculate_total()
        print(f"Thank you, {self.name}! Your total is ${total:.2f}.")
        self.shopping_cart = ShoppingCart()

# Sample usage
# Create some products
product1: Product = Product(1, "T-shirt", 15.99)
product2: Product = Product(2, "Jeans", 29.99)
product3: Product = Product(3, "Sneakers", 49.99)

# Create a customer
customer: Customer = Customer("Alice", "alice@example.com")

# Add products to the customer's cart
customer.add_to_cart(product1, 2)
customer.add_to_cart(product2)
customer.add_to_cart(product3)

# Display the cart contents and total
print(customer.shopping_cart)

# Checkout
customer.checkout()

```
## Output


```python
Shopping Cart:
T-shirt - $15.99 x2
Jeans - $29.99 x1
Sneakers - $49.99 x1
Total: $111.96
Thank you, Alice! Your total is $111.96.
```
## Define class method
inside an instance method, we use the self keyword to access or modify the 
instance variables. Same inside the class method, we use the cls keyword as 
a first parameter to access class variables

The class method can only access the class attributes, not the instance attributes
## Example
```python
from datetime import date
class Person:
    def __init__(self, name : str, age : int)-> None:
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name : str, birth_year : int)-> int:
        # calculate age an set it as a age
        # return new object
        return Person(name, date.today().year - birth_year)

    def show(self)-> None:
        print(self.name + "'s age is: " + str(self.age))

a = Person('Hashim', 21)
a.show()
```
## Output


```python
Hashim's age is: 21
```
The calculate_age() method takes Person class (cls) as a first 
parameter and returns constructor by calling 
Person(name, date.today().year - birthYear), 
which is equivalent to Person(name, age).

## This is an Class Method Example 
```python
class Car:
    num_wheels : int = 4  # Class variable shared among all instances

    def __init__(self, color : str, make : str, model : str)-> None:
        self.color = color  # Instance variable
        self.make = make    # Instance variable
        self.model = model  # Instance variable

# Creating car instances
car1 : Car = Car("Red", "Toyota", "Camry")
car2 : Car = Car("Blue", "Honda", "Civic")

# Accessing class variable
print(car1.num_wheels)  # Outputs: 4
print(car2.num_wheels)  # Outputs: 4

# Changing class variable
Car.num_wheels = 3

# All instances reflect the change
print(car1.num_wheels)  # Outputs: 3
print(car2.num_wheels)  # Outputs: 3
```
## Static Method 
A static method is bound to the class and not the 
object of the class. Therefore, we can call it 
using the class name.

## Example

```python
class Person:
    @staticmethod
    def sample(x : int):
        print('Inside static method', x)

# call static method
Person.sample(10)

#Another Example of static method
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c : int):
        return 9 * c / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f : int):
        return 5 * (f - 32) / 9
print(TemperatureConverter.celsius_to_fahrenheit(30))  # 86.0
```
##  Example of Class, Instance and Static Level Methods and Attributes
```python
from typing import List

class IAJK:
    admin: str = "Administrator Tasks"
    university: str = "COMSTATS UNIVERSITY ISLAMABAD"
    library: str = "Books"
    Sports: List[str] = ["Cricket", "Hockey", "Football"]

    def __init__(
        self,
        facultyMember: int,
        noOfStudents: int,
        departmentName: str,
        courseSubjects: int,
        noOfGrounds: int,
        admissions: int,
        courseDuration: str,
        courseName: str,
        courseTeacher: str,
    ) -> None:
        self.facultyMember: int = facultyMember
        self.noOfStudents: int = noOfStudents
        self.departName: str = departmentName
        self.courseSubjects: int = courseSubjects
        self.noOfGrounds: int = noOfGrounds
        self.admissions: int = admissions
        self.courseDuration: str = courseDuration
        self.courseName: str = courseName
        self.courseTeacher: str = courseTeacher

    @classmethod
    def uniInfo(cls) -> None:
        print(f'{cls.admin}')
        print(f'{cls.university}')
        print(f'{cls.library}')
        print(f'{cls.Sports}')

    def Show(self) -> None:
        print(f'Total Faculty Members are : {self.facultyMember}')
        print(f'Your Department Name is : {self.departName}')
        print(f'Number of Students are : {self.noOfStudents}')
        print(f'Total Courses offers are : {self.courseSubjects}')
        print(f'Sports Grounds are  : {self.noOfGrounds}')
        print(f'Total  Admissions : {self.admissions}')
        print(f'Course Durations : {self.courseDuration}')
        print(f'Teacher Name  : {self.courseTeacher}')

    @staticmethod
    def iajkboy() -> None:
        fileshandle: List[str] = ["Document Print", "Files Racking"]
        refreshment: List[str] = ["Juice", "Cake"]


fm = int(input("Please Enter Total Faculty member"))
ns = int(input("Please Enter Number of Studentsr"))
dp = input("Please your Department Name")
UIIT : IAJK = IAJK(fm,ns,dp,10,1,100,"6 Months","DevOPS","Ehtisham")
IAJK.uniInfo()
UIIT.Show()
IAJK.iajkboy()
```

```python
Please Enter Total Faculty member10
Please Enter Number of Studentsr5
Please your Department Namephysic
Administrator Tasks
COMSTATS UNIVERSITY ISLAMABAD    
Books
['Cricket', 'Hockey', 'Football']
Total Faculty Members are : 10
Your Department Name is : physic
Number of Students are : 5
Total Courses offers are : 10
Sports Grounds are  : 1
Total  Admissions : 100
Course Durations : 6 Months
Teacher Name  : Ehtisham
['Document Print', 'Files Racking']
['Water', 'Quette Chai']
```

## Inheritance
Inheritance allows a class to inherit attributes and methods from another class.

## Single inheritance
A class can reuse another class by inheriting it. When a child class 
inherits from a parent class, the child class can access the 
attributes and methods of the parent class.

## Syntax
```python
class derived-class(base class):  
    <class-suite> 
```
## Example
```python
class father:
    pocketMoney : int = 1000
    def show(self)-> None:
        print("Parent Class Instance Method")
    @classmethod
    def showMoney(cls)-> None:
        print(cls.pocketMoney)
class Son(father):
    def display(self)-> None:
        print("Child Class Instance Method")

child : Son = Son()
child.show()
child.showMoney()
child.display() 
```
## Output
```python
Parent Class Instance Method
1000
Child Class Instance Method
```
## Constructor in Single Inheritance
```python
class father:
    def __init__(self,money:str)-> None:
        self.money = money
    def show(self)-> None:
        print("Parent Class Instance Method")
class Son(father):
    def display(self)-> None:
        print("Child Class Instance Method",self.money)
s : Son = Son(500)
print(s.money)
s.show()
s.display()
```
## Output 
```python
500
Parent Class Instance Method
Child Class Instance Method 500
```
## Constructor Overriding

 If we write constructor in both classes, parent class and child class then the parent
    class constructor will not available to the child class
    In this case only child class constructor only accessible which means child class 
    constructor is replacing parent class constructor.
    Constructor ovveriding is used when the programmer want to modify the existing behaviour
    of a constructor.
```python
class Father:
    def __init__(self):
        self.money = 1000
        print("Father Class Constructor")
    def show(self):
        print("Parent Class Instance Method")
class Son(Father):
    def __init__(self):
        self.money = 5000
        self.car = "BMW"
        print("Son Class Constructor", self.money, self.car)
    def disp(self):
        print("Parent Class Instance Method")
S = Son()
```
```python
Son Class Constructor 5000 BMW
```
## Constructor With Supper() Method
    If we write constructor in both classes, parent class and child class then the parent
    class constructor will not available to the child class
    In this case only child class constructor only accessible which means child class 
    constructor is replacing parent class constructor.
    Super() Method is used to call parent class constructor from the child class

```python
class Father:
    def __init__(self,money: str)-> None:
        self.money = money
        print("Father Class Constructor",self.money)
    def show(self)-> None:
        print("Parent Class Instance Method")
class Son(Father):
    def __init__(self,money: str ,car : str)-> None:
        super().__init__(3000)
        self.money = money
        self.car = car
        print("Son Class Constructor", self.money, self.car)
    def disp(self)-> None:
        print("Parent Class Instance Method")
S:Son = Son(700000,"Mercendes")
```
```python
Father Class Constructor 3000
Son Class Constructor 700000 Mercendes
```
## Python Multi-Level inheritance
Multi-Level inheritance is possible in python like other object-oriented languages. 
Multi-level inheritance is archived when a derived class inherits another derived class. 
There is no limit on the number of levels up to which, the multi-level inheritance is 
archived in python.

## Syntax
```python
class class1:  
    <class-suite>   
class class2(class1):  
    <class suite>  
class class3(class2):  
    <class suite>
```
## Example of Multi-Level inheritance
```python
class Father:
    def __init__(self, name : str)-> None:
        self.name = name
        print("Father Class Constructor")
    def showFather(self):
        print("Father Name:", self.name)
class Son(Father):
    def __init__(self, father_name: str, son_name : str)-> None:
        super().__init__(father_name)
        self.son_name = son_name
        print("Son Class Constructor")
    def showSon(self)-> None:
        print("Son Name:", self.son_name)
class GrandSon(Son):
    def __init__(self, father_name:str, son_name:str, grandson_name:str)-> None:
        super().__init__(father_name, son_name)
        self.grandson_name = grandson_name
        print("GrandSon Class Constructor")
    def showGrandSon(self)-> None:
        print("GrandSon Name:", self.grandson_name)
father_name = "Jamshed"
son_name = "Junaid"
grandson_name = "Saifullah"

g : GrandSon = GrandSon(father_name, son_name, grandson_name)
g.showSon()
g.showGrandSon()
g.showFather()
```
```python
Father Class Constructor
Son Class Constructor
GrandSon Class Constructor
Son Name: Junaid
GrandSon Name: Saifullah
Father Name: Jamshed
```
## Hierarchical Inheritance

1. Example 1
```python
# Base class
class Animal:
    def __init__(self, name: str)-> None:
        self.name = name
# Derived class 1
class Dog(Animal):
    def speak(self)-> str:
        return f"{self.name} says Woof!"

# Derived class 2
class Cat(Animal)-> str:
    def speak(self):
        return f"{self.name} says Meow!"

# Derived class 3
class Cow(Animal):
    def speak(self)-> str:
        return f"{self.name} says Moo!"

# Create instances of the derived classes
dog : Dog = Dog("Buddy")
cat : Cat = Cat("Whiskers")
cow : Cow = Cow("Bessie")

# Call the speak method on instances of derived classes
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
print(cow.speak())  # Output: Bessie says Moo!
```
## Python Multiple inheritance
```python
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
```
2. Example 2
```python
class Animal:
    def __init__(self, name : str):
        self.name = name

    def speak(self):
        pass

# Base class 2
class Bird:
    def __init__(self, name: str):
        self.name = name

    def chirp(self):
        pass

# Derived class inheriting from both Animal and Bird
class Parrot(Animal, Bird):
    def speak(self)-> str:
        return f"{self.name} says Hello!"
    
    def chirp(self)-> str:
        return f"{self.name} chirps loudly!"

# Create an instance of the derived class Parrot
parrot: Parrot = Parrot("Polly")

# Call methods from both base classes
print(parrot.speak())  # Output: Polly says Hello!
print(parrot.chirp())  # Output: Polly chirps loudly!
```

### Example: Inheriting from a Base Class
```python
class Animal:
    def __init__(self, name : str, age : int)-> None:
        self.name = name
        self.age = age
    
    def speak(self)-> None:
        print("Some generic sound")

class Dog(Animal):
    def bark(self-> None:
        print("Woof!")
```

## Example: Employee, Designer, and Developer
Here, we define an `Employee` class and two subclasses `Designer` and `Developer`.

### Base Class: Employee
```python
class Employee:
    def __init__(self, name: str, age: int, department: str) -> None:
        self.name: str = name
        self.age: int = age
        self.department: str = department
    
    def display_info(self) -> None:
        print(f"Name: {self.name}, Age: {self.age}, Department: {self.department}")

```

### Subclass: Designer
```python
class Designer(Employee):
    def __init__(self, name: str, age: int, department: str, tool: str) -> None:
        super().__init__(name, age, department)
        self.tool: str = tool
    
    def display_info(self) -> None:
        super().display_info()
        print(f"Design Tool: {self.tool}")

```

### Subclass: Developer
```python
class Developer(Employee):
    def __init__(self, name: str, age: int, department: str, language: str) -> None:
        super().__init__(name, age, department)
        self.language: str = language
    
    def display_info(self) -> None:
        super().display_info()
        print(f"Programming Language: {self.language}")

```

### Usage Example
```python
designer : Designer = Designer("Alice", 30, "Design", "Photoshop")
developer : Developer = Developer("Bob", 25, "Development", "Python")

designer.display_info()
developer.display_info()
```

---

You can save this content to a `README.md` file in your project directory. It provides a comprehensive guide on the basics of OOP in Python, with examples and explanations for each concept.