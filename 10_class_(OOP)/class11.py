

# class Product:
#     def __init__(self, product_id, name, price):
#         self.product_id = product_id
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"{self.name} - ${self.price:.2f}"


# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, product, quantity=1):
#         self.items.append({"product": product, "quantity": quantity})

#     def remove_item(self, product):
#         for item in self.items:
#             if item["product"] == product:
#                 self.items.remove(item)

#     def calculate_total(self):
#         total = 0
#         for item in self.items:
#             total += item["product"].price * item["quantity"]
#         return total

#     def __str__(self):
#         cart_str = "Shopping Cart:\n"
#         for item in self.items:
#             cart_str += f"{item['product']} x{item['quantity']}\n"
#         cart_str += f"Total: ${self.calculate_total():.2f}"
#         return cart_str


# class Customer:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.shopping_cart = ShoppingCart()

#     def add_to_cart(self, product, quantity=1):
#         self.shopping_cart.add_item(product, quantity)

#     def remove_from_cart(self, product):
#         self.shopping_cart.remove_item(product)

#     def checkout(self):
#         total = self.shopping_cart.calculate_total()
#         print(f"Thank you, {self.name}! Your total is ${total:.2f}.")
#         self.shopping_cart = ShoppingCart()

# # Sample usage
# # Create some products
# product1 = Product(1, "T-shirt", 15.99)
# product2 = Product(2, "Jeans", 29.99)
# product3 = Product(3, "Sneakers", 49.99)

# # Create a customer
# customer = Customer("Alice", "alice@example.com")

# # Add products to the customer's cart
# customer.add_to_cart(product1, 2)
# customer.add_to_cart(product2)
# customer.add_to_cart(product3)

# # Display the cart contents and total
# print(customer.shopping_cart)

# # Checkout
# customer.checkout()



# from datetime import date
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def calculate_age(cls, name, birth_year):
#         # calculate age an set it as a age
#         # return new object
#         return Person(name, date.today().year - birth_year)

#     def show(self):
#         print(self.name + "'s age is: " + str(self.age))

# a = Person('Hashim', 21)
# a.show()



# class Person:
#     @staticmethod
#     def sample(x):
#         print('Inside static method', x)

# # call static method
# Person.sample(10)

# #Another Example of static method
# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(c):
#         return 9 * c / 5 + 32

#     @staticmethod
#     def fahrenheit_to_celsius(f):
#         return 5 * (f - 32) / 9
# print(TemperatureConverter.celsius_to_fahrenheit(30))  # 86.0

# class IAJK:
#     admin = "Administrator Tasks"
#     university = "COMSTATS UNIVERSITY ISLAMABAD"
#     library = "Books"
#     Sports = ["Cricket","Hockey","Football"]

#     def __init__(self,facultyMember, noOfStudents, departmentName, courseSubjects, noOfGrounds, admissions, courseDuration,courseName , courseTeacher ) -> None:
#         self.facultyMember = facultyMember
#         self.noOfStudents = noOfStudents
#         self.departName = departmentName
#         self.courseSubjects = courseSubjects
#         self.noOfGrounds = noOfGrounds
#         self.admissions = admissions
#         self.courseDuration = courseDuration
#         self.courseName = courseName
#         self.courseTeacher = courseTeacher

#     @classmethod
#     def uniInfo(cls):
#         print(f'{cls.admin}')
#         print(f'{cls.university}')
#         print(f'{cls.library}')
#         print(f'{cls.Sports}')

#     def Show(self):
#         print(f'Total Faculty Members are : {self.facultyMember}')
#         print(f'Your Department Name is : {self.departName}')
#         print(f'Number of Students are : {self.noOfStudents}')
#         print(f'Total Courses offers are : {self.courseSubjects}')
#         print(f'Sports Grounds are  : {self.noOfGrounds}')
#         print(f'Total  Admissions : {self.admissions}')
#         print(f'Course Durations : {self.courseDuration}')
#         print(f'Teacher Name  : {self.courseTeacher}')

#     @staticmethod
#     def iajkboy():
#         fileshandle = ["Document Print", "Files Racking"]
#         refreshment = ["Water", "Quette Chai"]
#         print(fileshandle)
#         print(refreshment)



# fm = int(input("Please Enter Total Faculty member"))
# ns = int(input("Please Enter Number of Studentsr"))
# dp = input("Please your Department Name")
# UIIT = IAJK(fm,ns,dp,10,1,100,"6 Months","DevOPS","Ehtisham")
# IAJK.uniInfo()
# UIIT.Show()
# IAJK.iajkboy()


# class father:
#     pocketMoney = 1000
#     def show(self):
#         print("Parent Class Instance Method")
#     @classmethod
#     def showMoney(cls):
#         print(cls.pocketMoney)
# class Son(father):
#     def display(self):
#         print("Child Class Instance Method")

# child = Son()
# child.show()
# child.showMoney()
# child.display()


# class father:
#     def __init__(self,money):
#         self.money = money
#     def show(self):
#         print("Parent Class Instance Method")
# class Son(father):
#     def display(self):
#         print("Child Class Instance Method",self.money)
# s = Son(500)
# print(s.money)
# s.show()
# s.display()


# class Father:
#     def __init__(self):
#         self.money = 1000
#         print("Father Class Constructor")
#     def show(self):
#         print("Parent Class Instance Method")
# class Son(Father):
#     def __init__(self):
#         self.money = 5000
#         self.car = "BMW"
#         print("Son Class Constructor", self.money, self.car)
#     def disp(self):
#         print("Parent Class Instance Method")
# S = Son()


# class Father:
#     def __init__(self,money):
#         self.money = money
#         print("Father Class Constructor",self.money)
#     def show(self):
#         print("Parent Class Instance Method")
# class Son(Father):
#     def __init__(self,money,car):
#         super().__init__(3000)
#         self.money = money
#         self.car = car
#         print("Son Class Constructor", self.money, self.car)
#     def disp(self):
#         print("Parent Class Instance Method")
# S = Son(700000,"Mercendes")

# class Father:
#     def __init__(self, name):
#         self.name = name
#         print("Father Class Constructor")
#     def showFather(self):
#         print("Father Name:", self.name)
# class Son(Father):
#     def __init__(self, father_name, son_name):
#         super().__init__(father_name)
#         self.son_name = son_name
#         print("Son Class Constructor")
#     def showSon(self):
#         print("Son Name:", self.son_name)
# class GrandSon(Son):
#     def __init__(self, father_name, son_name, grandson_name):
#         super().__init__(father_name, son_name)
#         self.grandson_name = grandson_name
#         print("GrandSon Class Constructor")
#     def showGrandSon(self):
#         print("GrandSon Name:", self.grandson_name)
# father_name = "Jamshed"
# son_name = "Junaid"
# grandson_name = "Saifullah"

# g = GrandSon(father_name, son_name, grandson_name)
# g.showSon()
# g.showGrandSon()
# g.showFather()


# class Person:
#     def __init__(self, name : str, age :int):
#         self.name = name  
#         self.age = age



class Product:
    def __init__(self, product_id : int, name : str , price : int )-> None:
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self)-> str:
        return f"{self.name} - ${self.price:.2f}"


class ShoppingCart:
    def __init__(self)-> None:
        self.items = []

    def add_item(self, product, quantity=1)-> None:
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

