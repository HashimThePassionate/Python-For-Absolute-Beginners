# Python classes

# Everything in Python is an object. An object has a state and 
# behaviors. To create an object, you define a class first. 
# And then, from the class, you can create one or more 
# objects. The objects are instances of a class.

# Classes provide a means of bundling data and functionality together. 
# Creating a new class creates a new type of object, allowing new 
# instances of that type to be made.

# The simplest form of class definition looks like this:
# class ClassName:
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>

# Class definitions, like function definitions (def statements) 
# must be executed before they have any effect.


#Define a class
# 
# To define a class, you use the class keyword followed by 
# the class name. For example, the following defines a Person class:

# Since the Person class is incomplete; you need to use the pass 
# statement to indicate that you’ll add more code to it later.

class Person:
    pass
print(Person)
print(id(Person))
# 

# To create an object from the Person class, you use the class name 
# followed by parentheses (), like calling a function:

# An object is a container that contains data and functionality
# the data of an object is called the "state". 
# Python uses attributes to model the state of an object.
# 
p : Person = Person()

#Define instance attributes
# 
# Python is dynamic. It means that you can add an attribute to an 
# instance of a class dynamically at runtime.

# For example, the following adds the name attribute to the person
# object:
# 
p.name = 'Hashim'
# 
# To define and initialize an attribute for all instances of a class, 
# you use the __init__ method also known as constructor. The following 
# defines the Person class with two instance 
# attributes "name" and "age":
# 
#Parameterized Constructor
class Person:
    def __init__(self, name : str, age : int) -> None:
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
	def __init__(self)->None:
		print("This is non parametrized constructod id =  ",id(self))

obj : check = check()
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
    counter : int = 0 #Class Attribute
    def __init__(self, name : str, age : int):
        self.name = name
        self.age = age
        Person.counter+=1
    def great(self):
        return f"Hi, it's {self.name}."

# The following creates two instances of the Person class and 
# shows the value of the counter:

p1 : Person = Person('Hashim', 22)
p1.great()
p2 : Person = Person('Hamza', 20)
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
    def __init__(self, roll_no : int, name : str, age : int)-> None:
        self.roll_no = roll_no
        self.name = name
        self.age = age
    # instance method access instance variable
    def show(self)-> None:
        print('Roll Number:', self.roll_no, 'Name:', self.name, 'Age:', self.age,)
    # instance method to modify instance variable
    def update(self, roll_number: int ,name : str , age : int)-> None:
        self.roll_no = roll_number
        self.name = name
        self.age = age

# create object
s : Person = Person(2, "Hashim", 21)
print(Person.counter)
# call instance method
s.show()

# Modify instance variables
s.update(1,"Hamza", 20)
s.show()

# This is just Simple Example How we relate in real world Shopping Cart Ecommerce Website don't be confuse we can cover everything in very detail
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



#Define class method
'''
inside an instance method, we use the self keyword to access or modify the 
instance variables. Same inside the class method, we use the cls keyword as 
a first parameter to access class variables

The class method can only access the class attributes, not the instance attributes

'''
from datetime import date
class Person:
    def __init__(self, name : str, age :  int)-> None:
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name : str , birth_year : int) -> int:
        # calculate age an set it as a age
        # return new object
        return Person(name, date.today().year - birth_year)

    def show(self)-> None:
        print(self.name + "'s age is: " + str(self.age))

a : Person = Person('Hashim', 21)
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

#This is an Class Method Example 
class Car:
    num_wheels : int = 4  # Class variable shared among all instances

    def __init__(self, color : str , make : str , model : str) -> None:
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

#Static Method 
'''
A static method is bound to the class and not the 
object of the class. Therefore, we can call it 
using the class name.
'''
class Person:
    @staticmethod
    def sample(x: int):
        print('Inside static method', x)

# call static method
Person.sample(10)

#Another Example of static method
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c: float):
        return 9 * c / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f: float):
        return 5 * (f - 32) / 9
print(TemperatureConverter.celsius_to_fahrenheit(30))  # 86.0

# Example of Class, Instance and Static Level Methods and Attributes
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


#Single inheritance
'''
A class can reuse another class by inheriting it. When a child class 
inherits from a parent class, the child class can access the 
attributes and methods of the parent class.

Syntax
class derived-class(base class):  
    <class-suite>  
'''
class Father:
    pocketMoney: int = 1000

    def show(self) -> None:
        print("Parent Class Instance Method")

    @classmethod
    def showMoney(cls) -> None:
        print(cls.pocketMoney)


class Son(Father):
    def display(self) -> None:
        print("Child Class Instance Method")


child: Son = Son()
child.show()
child.showMoney()
child.display()

# --------------------------------------------------------------------------------
class Animal:  
    def speak(self)-> None:  
        print("Animal Speaking") 
class Dog(Animal):  
    def bark(self)-> None:  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak()  
# ------------------------------------------------------------------------------------
#Constructor in Single Inheritance
class Father:
    def __init__(self, money: int) -> None:
        self.money: int = money

    def show(self) -> None:
        print("Parent Class Instance Method")


class Son(Father):
    def display(self) -> None:
        print("Child Class Instance Method", self.money)


s: Son = Son(500)
print(s.money)
s.show()
s.display()


# ----------------------------------------------------------------------------------------
#Constructor Overriding
'''
    If we write constructor in both classes, parent class and child class then the parent
    class constructor will not available to the child class
    In this case only child class constructor only accessible which means child class 
    constructor is replacing parent class constructor.
    Constructor ovveriding is used when the programmer want to modify the existing behaviour
    of a constructor.

'''
class Father:
    def __init__(self) -> None:
        self.money: int = 1000
        print("Father Class Constructor")

    def show(self) -> None:
        print("Parent Class Instance Method")


class Son(Father):
    def __init__(self) -> None:
        super().__init__()  # Call the parent class constructor
        self.money: int = 5000
        self.car: str = "BMW"
        print("Son Class Constructor", self.money, self.car)

    def disp(self) -> None:
        print("Parent Class Instance Method")


S: Son = Son()

# -----------------------------------------------------------------------------
#Constructor With Supper() Method
'''
    If we write constructor in both classes, parent class and child class then the parent
    class constructor will not available to the child class
    In this case only child class constructor only accessible which means child class 
    constructor is replacing parent class constructor.
    Super() Method is used to call parent class constructor from the child class

'''
class Father:
    def __init__(self, money: int) -> None:
        self.money: int = money
        print("Father Class Constructor", self.money)

    def show(self) -> None:
        print("Parent Class Instance Method")


class Son(Father):
    def __init__(self, money: int, car: str) -> None:
        super().__init__(3000)  # Assuming the initial money for Father class is always 3000
        self.money: int = money
        self.car: str = car
        print("Son Class Constructor", self.money, self.car)

    def disp(self) -> None:
        print("Parent Class Instance Method")


S: Son = Son(700000, "Mercedes")


# ----------------------------------------------------------------------------------------
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
class Father:
    def __init__(self, name: str) -> None:
        self.name: str = name
        print("Father Class Constructor")

    def showFather(self) -> None:
        print("Father Name:", self.name)


class Son(Father):
    def __init__(self, father_name: str, son_name: str) -> None:
        super().__init__(father_name)
        self.son_name: str = son_name
        print("Son Class Constructor")

    def showSon(self) -> None:
        print("Son Name:", self.son_name)


class GrandSon(Son):
    def __init__(self, father_name: str, son_name: str, grandson_name: str) -> None:
        super().__init__(father_name, son_name)
        self.grandson_name: str = grandson_name
        print("GrandSon Class Constructor")

    def showGrandSon(self) -> None:
        print("GrandSon Name:", self.grandson_name)


father_name: str = "Jamshed"
son_name: str = "Junaid"
grandson_name: str = "Saifullah"

g: GrandSon = GrandSon(father_name, son_name, grandson_name)
g.showSon()
g.showGrandSon()
g.showFather()

# -----------------------------------------------------------------------
#Hierarchical Inheritance
# Base class
class Animal:
    def __init__(self, name: str) -> None:
        self.name: str = name

# Derived class 1
class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says Woof!"

# Derived class 2
class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says Meow!"

# Derived class 3
class Cow(Animal):
    def speak(self) -> str:
        return f"{self.name} says Moo!"

# Create instances of the derived classes
dog: Dog = Dog("Buddy")
cat: Cat = Cat("Whiskers")
cow: Cow = Cow("Bessie")

# Call the speak method on instances of derived classes
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
print(cow.speak())  # Output: Bessie says Moo!
# Output: Bessie says Moo!

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
# Base class 1
class Animal:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def speak(self) -> None:
        pass

# Base class 2
class Bird:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def chirp(self) -> None:
        pass

# Derived class inheriting from both Animal and Bird
class Parrot(Animal, Bird):
    def speak(self) -> str:
        return f"{self.name} says Hello!"
    
    def chirp(self) -> str:
        return f"{self.name} chirps loudly!"

# Create an instance of the derived class Parrot
parrot: Parrot = Parrot("Polly")

# Call methods from both base classes
print(parrot.speak())  # Output: Polly says Hello!
print(parrot.chirp())  # Output: Polly chirps loudly!

# --------------------------------------------------------------
class Calculation1:  
    def Summation(self, a: int, b: int) -> int:  
        return a + b

class Calculation2:  
    def Multiplication(self, a: int, b: int) -> int:  
        return a * b

class Derived(Calculation1, Calculation2):  
    def Divide(self, a: int, b: int) -> float:  
        return a / b

d: Derived = Derived()  
print(d.Summation(10, 20))  
print(d.Multiplication(10, 20))  
print(d.Divide(10, 20))