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
# Define a class
'''
To define a class, you use the class keyword followed by 
the class name. For example, the following defines a Person class:

Since the Person class is incomplete; you need to use the pass 
statement to indicate that you’ll add more code to it later.
'''




from datetime import date
from typing import Dict, Optional
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

# Define instance attributes
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
# Parameterized Constructor


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# The following creates a Person object named person:
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
p = Person("Hashim", 22)
'''
The p object now has the name and age attributes. 
To access an instance attribute, you use the dot notation. 
For example, the following returns the value of the name 
attribute of the person object
'''
p.name
p.age

# Non-parameterized Constructor
# it is clearly seen that self and obj is referring to the same object


class check:
    def __init__(self):
        print("This is non parametrized constructod id =  ", id(self))


obj = check()
print("Address of class object = ", id(obj))
'''
Output
This is non parametrized constructod id = =  2175972664240
Address of class object =  2175972664240
'''

# Define Class Attribute
'''
Unlike instance attributes, class attributes are shared by all 
instances of the class. They are helpful if you want to define 
class constants or variables that keep track of the number of 
instances of a class.

For example, the following defines the "counter" class attribute 
in the Person class:
'''


class Person:
    counter = 0  # Attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def great(self):
        return f"Hi, it's {self.name}."

# The following creates two instances of the Person class and
# shows the value of the counter:


p1 = Person('Hashim', 22)
p1.great()
p2 = Person('Hamza', 20)
p2.great()
print(Person.counter)
Person.counter = 10
print(Person.counter)
print("The First  object counter value is ", p1.counter)
print("The Second  object counter value is ", p2.counter)
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
# Let’s create the instance method update() method
# to modify the Person age and roll number


class Person:
    def __init__(self, roll_no, name, age):
        self.roll_no = roll_no
        self.name = name
        self.age = age
    # instance method access instance variable

    def show(self):
        print('Roll Number:', self.roll_no,
              'Name:', self.name, 'Age:', self.age,)
    # instance method to modify instance variable

    def update(self, roll_number, name, age):
        self.roll_no = roll_number
        self.name = name
        self.age = age


# create object
s = Person(2, "Hashim", 21)
print(Person.counter)
# call instance method
s.show()

# Modify instance variables
s.update(1, "Hamza", 20)
s.show()


# Type Checking in Constructor
from typing import Union
class Person(object):
    def __init__(self, name: str, age: int, salary: Union[int, float]) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(age, int):
            raise TypeError("Age must be an integer")
        if not isinstance(salary, (int, float)):
            raise TypeError("Salary must be either an int or a float")

        self.name = name
        self.age = age
        self.salary = salary
    def __str__(self) -> str:
        return f'''
        Person Name is {self.name}
        person Age is {self.age}
        Person Salary is {self.salary}
        '''

# Example usage:
try:
    person1 = Person("John", 25, 50000)
    print(person1)
    print('\n-----------------------------------------------')
except TypeError as e:
    print(e)

try:
    person2 = Person("Alice", "30", 60000)  # Raises TypeError
    print(person2)
    print('\n-----------------------------------------------')
except TypeError as e:
    print(e)
try:
    person3 = Person("Alice", 25, 60000.2345) # Raises TypeError
    print(person3)
    print('\n-----------------------------------------------')
except TypeError as e:
    print(e)

try:
    person4 = Person("Bob", 35, "70000")  # Raises TypeError
    print(person4)
    print('\n-----------------------------------------------')
except TypeError as e:
    print(e)

try:
    person5 = Person(1, "35", "70000")  # Raises TypeError
    print(person5)
    print('\n-----------------------------------------------')
except TypeError as e:
    print(e)

# Tiger Class
class Tiger:
    # def __init(self) -> None:
    #     ...
    def __init__(self, tiger_age, tiger_gender, tiger_color, tiger_breed, tiger_mood) -> None:
        self.tiger_age = tiger_age
        self.tiger_gender = tiger_gender
        self.tiger_color = tiger_color
        self.tiger_breed = tiger_breed
        self.tiger_mood = tiger_mood

    # def tiger_attributes(self, tiger_age, tiger_gender, tiger_color, tiger_breed, tiger_mood):
    #     self.tiger_age = tiger_age
    #     self.tiger_gender = tiger_gender
    #     self.tiger_color  = tiger_color
    #     self.tiger_breed  = tiger_breed
    #     self.tiger_mood   = tiger_mood

    def our_tiger(self, tiger_name, tiger_diet_plan, tiger_env, tiger_outing):
        self.tiger_name = tiger_name
        self.tiger_diet_plan = tiger_diet_plan
        self.tiger_env = tiger_env
        self.tiger_outing = tiger_outing

    def tiger_memory_address(self):
        print(f'Tiger is located in {id(self)} address')

    def tiger_reports(self):
        print(f'''
Tiger Name is   {self.tiger_name}
Tiger Diet Plan  {self.tiger_diet_plan}
Tiger Gender  {self.tiger_gender}
''')

# jack : Tiger = Tiger()
# jack.tiger_attributes('2  Months','Male','Mustard','Chicken','Aggressive')
# jack.our_tiger('Jaguar','3/3','Garden','Commercial Market')
# jack.tiger_reports()
# print(f'Jack Address is {id(jack)}')
# jack.tiger_memory_address()
# rose : Tiger = Tiger()
# rosee : Tiger = Tiger()
# print(f'Rose Address is {id(rose)}')
# rose.tiger_memory_address()


david: Tiger = Tiger('2  Months', 'Male', 'Mustard', 'Chicken', 'Aggressive')
david.tiger_name = 'David'
david.tiger_diet_plan = '3 / 3'
david.tiger_reports()


# This is just Simple Example How we relate in real world Shopping Cart Ecommerce Website don't be confuse we can cover everything in very detail
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def remove_item(self, product):
        for item in self.items:
            if item["product"] == product:
                self.items.remove(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

    def __str__(self):
        cart_str = "Shopping Cart:\n"
        for item in self.items:
            cart_str += f"{item['product']} x{item['quantity']}\n"
        cart_str += f"Total: ${self.calculate_total():.2f}"
        return cart_str


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product, quantity=1):
        self.shopping_cart.add_item(product, quantity)

    def remove_from_cart(self, product):
        self.shopping_cart.remove_item(product)

    def checkout(self):
        total = self.shopping_cart.calculate_total()
        print(f"Thank you, {self.name}! Your total is ${total:.2f}.")
        self.shopping_cart = ShoppingCart()


# Sample usage
# Create some products
product1 = Product(1, "T-shirt", 15.99)
product2 = Product(2, "Jeans", 29.99)
product3 = Product(3, "Sneakers", 49.99)

# Create a customer
customer = Customer("Alice", "alice@example.com")

# Add products to the customer's cart
customer.add_to_cart(product1, 2)
customer.add_to_cart(product2)
customer.add_to_cart(product3)

# Display the cart contents and total
print(customer.shopping_cart)

# Checkout
customer.checkout()


class Account:
    def __init__(self, account_number: str, pin: str, balance: float = 0.0) -> None:
        self.account_number: str = account_number
        self.pin: str = pin
        self.balance: float = balance

    def deposit(self, amount: float) -> bool:
        self.balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        return self.balance


class Transaction:
    @staticmethod
    def check_pin(account: Account, pin: str) -> bool:
        return account.pin == pin


class ATM:
    def __init__(self, bank_name: str) -> None:
        self.bank_name: str = bank_name

    def authenticate_user(self, account_number: str, pin: str) -> Optional[Account]:
        # Assuming accounts are stored in a dictionary
        if account_number in accounts:
            account = accounts[account_number]
            if Transaction.check_pin(account, pin):
                return account
        return None

    def deposit(self, account: Account, amount: float) -> str:
        if account.deposit(amount):
            return f"Deposit successful. New balance is {account.get_balance()}"
        else:
            return "Deposit unsuccessful. Insufficient funds."

    def withdraw(self, account: Account, amount: float) -> str:
        if account.withdraw(amount):
            return f"Withdrawal successful. New balance is {account.get_balance()}"
        else:
            return "Withdrawal unsuccessful. Insufficient funds."

# Example usage:


# Creating some accounts
accounts: Dict[str, Account] = {
    '123456': Account('123456', '1234', 1000.0),
    '789012': Account('789012', '5678', 500.0),
}

# Creating an ATM
atm: ATM = ATM("Al Habib Bank")

# Authenticating a user
account = atm.authenticate_user('123456', '1234')
if account:
    print("Authentication successful")
    print(atm.deposit(account, 500.0))  # Depositing money
    print(atm.withdraw(account, 200.0))  # Withdrawing money
else:
    print("Authentication failed")

# Define class method
'''
inside an instance method, we use the self keyword to access or modify the 
instance variables. Same inside the class method, we use the cls keyword as 
a first parameter to access class variables

The class method can only access the class attributes, not the instance attributes

'''


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

# This is an Class Method Example


class Car:
    num_wheels = 4  # Class variable shared among all instances

    def __init__(self, color, make, model):
        self.color = color  # Instance variable
        self.make = make    # Instance variable
        self.model = model  # Instance variable


# Creating car instances
car1 = Car("Red", "Toyota", "Camry")
car2 = Car("Blue", "Honda", "Civic")

# Accessing class variable
print(car1.num_wheels)  # Outputs: 4
print(car2.num_wheels)  # Outputs: 4

# Changing class variable
Car.num_wheels = 3

# All instances reflect the change
print(car1.num_wheels)  # Outputs: 3
print(car2.num_wheels)  # Outputs: 3


# Quiz Exercise Answer
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity


class Receipt:
    def __init__(self, name, date, items):
        self.name = name
        self.date = date
        self.items = items

    def get_subtotal(self):
        return sum(item.get_total_price() for item in self.items)

    def get_total_with_tax(self, tax_rate):
        subtotal = self.get_subtotal()
        tax = subtotal * tax_rate
        return subtotal + tax


print('SHOP NO 1 2 ROYAL PLAZA')
print('QUETTA CHAMAN')
# Example usage
product1 = Product("Milk", 2.5, 1)
product2 = Product("Bread", 3.0, 2)

receipt = Receipt("My Local Store", "2024-02-29", [product1, product2])

print(f"Subtotal: ${receipt.get_subtotal():.2f}")
print(f"Total with 5% tax: ${receipt.get_total_with_tax(0.05):.2f}")

# Static Method
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

# Another Example of static method


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9 * c / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5 * (f - 32) / 9


print(TemperatureConverter.celsius_to_fahrenheit(30))  # 86.0

# Example of Class, Instance and Static Level Methods and Attributes


class IAJK:
    admin = "Administrator Tasks"
    university = "COMSTATS UNIVERSITY ISLAMABAD"
    library = "Books"
    Sports = ["Cricket", "Hockey", "Football"]

    def __init__(self, facultyMember, noOfStudents, departmentName, courseSubjects, noOfGrounds, admissions, courseDuration, courseName, courseTeacher) -> None:
        self.facultyMember = facultyMember
        self.noOfStudents = noOfStudents
        self.departName = departmentName
        self.courseSubjects = courseSubjects
        self.noOfGrounds = noOfGrounds
        self.admissions = admissions
        self.courseDuration = courseDuration
        self.courseName = courseName
        self.courseTeacher = courseTeacher

    @classmethod
    def uniInfo(cls):
        print(f'{cls.admin}')
        print(f'{cls.university}')
        print(f'{cls.library}')
        print(f'{cls.Sports}')

    def Show(self):
        print(f'Total Faculty Members are : {self.facultyMember}')
        print(f'Your Department Name is : {self.departName}')
        print(f'Number of Students are : {self.noOfStudents}')
        print(f'Total Courses offers are : {self.courseSubjects}')
        print(f'Sports Grounds are  : {self.noOfGrounds}')
        print(f'Total  Admissions : {self.admissions}')
        print(f'Course Durations : {self.courseDuration}')
        print(f'Teacher Name  : {self.courseTeacher}')

    @staticmethod
    def iajkboy():
        fileshandle = ["Document Print", "Files Racking"]
        refreshment = ["Water", "Quette Chai"]
        print(fileshandle)
        print(refreshment)


fm = int(input("Please Enter Total Faculty member"))
ns = int(input("Please Enter Number of Studentsr"))
dp = input("Please your Department Name")
UIIT = IAJK(fm, ns, dp, 10, 1, 100, "6 Months", "DevOPS", "Ehtisham")
IAJK.uniInfo()
UIIT.Show()
IAJK.iajkboy()

# Python Magic Methods and Dunder Methods "Double Underscore Methods"
# python 3 magic method
# __str__ Method


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def draw(self):
        print(f'Point({self.x},{self.y})')

    def __str__(self) -> str:
        return f'Point({self.x},{self.y})'

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __gt__(self, other) -> bool:
        return self.x > other.x and self.y > other.y

    def __add__(self, other) -> any:
        return Point(self.x + other.x, self.y + other.y)


p1: Point = Point(1, 2)
p2: Point = Point(1, 2)
p3: Point = Point(10, 20)
p4: Point = Point(1, 2)
combine = p1 + p2
print(p)
print(p1 == p2)
print(p3 > p4)
print(combine)

# Making Custom Containers


class TagCloud:
    def __init__(self) -> None:
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0)+1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


# cloud = TagCloud()
# cloud.add('python')
# cloud.add('python')
# cloud.add('python')
# cloud.add('python')
# print(cloud.tags)
tag_cloud = TagCloud()
tag_cloud.add("Python")
tag_cloud.add("python")
tag_cloud.add("Java")
tag_cloud.add("python")
tag_cloud.add("C++")
print(tag_cloud["python"])  # Output: 3
tag_cloud["java"] = 2
print(tag_cloud["java"])  # Output: 2
print(len(tag_cloud))  # Output: 3
for tag in tag_cloud:
    print(tag, tag_cloud[tag])
# Single inheritance
'''
A class can reuse another class by inheriting it. When a child class 
inherits from a parent class, the child class can access the 
attributes and methods of the parent class.

Syntax
class derived-class(base class):  
    <class-suite>  
'''


class father:
    pocketMoney = 1000

    def show(self):
        print("Parent Class Instance Method")

    @classmethod
    def showMoney(cls):
        print(cls.pocketMoney)


class Son(father):
    def display(self):
        print("Child Class Instance Method")


child = Son()
child.show()
child.showMoney()
child.display()
# --------------------------------------------------------------------------------


class Animal:
    def speak(self):
        print("Animal Speaking")


class Dog(Animal):
    def bark(self):
        print("dog barking")


d = Dog()
d.bark()
d.speak()
# ------------------------------------------------------------------------------------
# Constructor in Single Inheritance


class father:
    def __init__(self, money):
        self.money = money

    def show(self):
        print("Parent Class Instance Method")


class Son(father):
    def display(self):
        print("Child Class Instance Method", self.money)


s = Son(500)
print(s.money)
s.show()
s.display()

# ----------------------------------------------------------------------------------------
# Constructor Overriding
'''
    If we write constructor in both classes, parent class and child class then the parent
    class constructor will not available to the child class
    In this case only child class constructor only accessible which means child class 
    constructor is replacing parent class constructor.
    Constructor ovveriding is used when the programmer want to modify the existing behaviour
    of a constructor.

'''


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
# -----------------------------------------------------------------------------
# Constructor With Supper() Method
'''
    If we write constructor in both classes, parent class and child class then the parent
    class constructor will not available to the child class
    In this case only child class constructor only accessible which means child class 
    constructor is replacing parent class constructor.
    Super() Method is used to call parent class constructor from the child class

'''


class Father:
    def __init__(self, money):
        self.money = money
        print("Father Class Constructor", self.money)

    def show(self):
        print("Parent Class Instance Method")


class Son(Father):
    def __init__(self, money, car):
        super().__init__(3000)
        self.money = money
        self.car = car
        print("Son Class Constructor", self.money, self.car)

    def disp(self):
        print("Parent Class Instance Method")


S = Son(700000, "Mercendes")

# ----------------------------------------------------------------------------------------
# Python Multi-Level inheritance
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
    def __init__(self, name):
        self.name = name
        print("Father Class Constructor")

    def showFather(self):
        print("Father Name:", self.name)


class Son(Father):
    def __init__(self, father_name, son_name):
        super().__init__(father_name)
        self.son_name = son_name
        print("Son Class Constructor")

    def showSon(self):
        print("Son Name:", self.son_name)


class GrandSon(Son):
    def __init__(self, father_name, son_name, grandson_name):
        super().__init__(father_name, son_name)
        self.grandson_name = grandson_name
        print("GrandSon Class Constructor")

    def showGrandSon(self):
        print("GrandSon Name:", self.grandson_name)


father_name = "Jamshed"
son_name = "Junaid"
grandson_name = "Saifullah"

g = GrandSon(father_name, son_name, grandson_name)
g.showSon()
g.showGrandSon()
g.showFather()
# -----------------------------------------------------------------------
# Hierarchical Inheritance
# Base class


class Animal:
    def __init__(self, name):
        self.name = name
# Derived class 1


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Derived class 2


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Derived class 3


class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo!"


# Create instances of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

# Call the speak method on instances of derived classes
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
print(cow.speak())  # Output: Bessie says Moo!

# Python Multiple inheritance
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
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Base class 2


class Bird:
    def __init__(self, name):
        self.name = name

    def chirp(self):
        pass

# Derived class inheriting from both Animal and Bird


class Parrot(Animal, Bird):
    def speak(self):
        return f"{self.name} says Hello!"

    def chirp(self):
        return f"{self.name} chirps loudly!"


# Create an instance of the derived class Parrot
parrot = Parrot("Polly")

# Call methods from both base classes
print(parrot.speak())  # Output: Polly says Hello!
print(parrot.chirp())  # Output: Polly chirps loudly!

# --------------------------------------------------------------
# PolyMorphism
from typing import Union, overload

class Adder:
    @overload
    def add(self, x: int, y: int) -> int:
        ...
        
    @overload
    def add(self, x: float, y: float) -> float:
        ...
        
    @overload
    def add(self, x: str, y: str) -> str:
        ...
        
    
    def add(self, x: Union[int, float, str], y: Union[int, float, str]) -> Union[int, float, str]:
        if isinstance(x, int) and isinstance(y, int):
            return x + y
        elif isinstance(x, float) and isinstance(y, float):
            return x + y
        elif isinstance(x, str) and isinstance(y, str):
            return x + y
        else:
            raise TypeError("Invalid argument types!")

# Usage examples
adder = Adder()
result1 = adder.add(1, 2)  # Should return 3
result2 = adder.add(1.5, 2.5)  # Should return 4.0
result3 = adder.add("Hello, ", "world!")  # Should return "Hello, world!"
# res4 = adder.add(1,'mystring')
print(result1)
print(result2)
print(result3)
# print(res4)


class Calculation1:
    def Summation(self, a, b):
        return a+b


class Calculation2:
    def Multiplication(self, a, b):
        return a*b


class Derived(Calculation1, Calculation2):
    def Divide(self, a, b):
        return a/b


d = Derived()
print(d.Summation(10, 20))
print(d.Multiplication(10, 20))
print(d.Divide(10, 20))

# Unpacking something using classes
class DynamicArgsDemo:
    def __init__(self, **kwargs):
        self.data = kwargs

    def process_data(self):
        # Simulating a dictionary with different key-value pairs
        # In a real scenario, this could be user input, API response, etc.
        sample_data = {
            'name': 'John',
            'age': 30,
            'location': 'New York',
            'interests': ['Python', 'Data Science', 'AI']
        }

        # Updating self.data with sample_data
        self.data.update(sample_data)

        # Unpacking self.data dynamically
        # Here, we're interested in 'name', 'age', and 'location'
        # We'll use these to "process" the data (printing in this case)
        # 'interests' is omitted from this example
        try:
            name = self.data['name']
            age = self.data['age']
            location = self.data['location']

            # Processing the data (printing in this example)
            print(f"Name: {name}")
            print(f"Age: {age}")
            print(f"Location: {location}")
        except KeyError as e:
            print(f"KeyError: {e} not found in data")

# Creating an instance and demonstrating dynamic unpacking
demo = DynamicArgsDemo()
demo.process_data()
