#Python Lambda Functions
'''
Lambda Functions in Python are anonymous functions, 
implying they don't have a name. The def keyword is needed to create 
a typical function in Python, as we already know. We can also use 
the "lambda" keyword in Python to define an unnamed function.

Syntax of Python Lambda Function
lambda arguments: expression 
'''
#Example1 
# Code to demonstrate how we can use a lambda function  
add = lambda num: num + 4  
print( add(6) )  
'''
Output
10
'''
#Example2
def reciprocal( num ):  
    return 1 / num  
lambda_reciprocal = lambda num: 1 / num  
print( "Lambda keyword: ", lambda_reciprocal(6) ) 
print( "Def keyword: ", reciprocal(6) )  
'''
Output
Def keyword:  0.16666666666666666
Lambda keyword:  0.16666666666666666
'''
#Example3 Lambda Function with filter()
# Code to filter odd numbers from a given list  
list_ = [34, 12, 64, 55, 75, 13, 63]  
odd_list = list(filter( lambda num: (num % 2 != 0) , list_ ))  
print(odd_list)  
'''
Output
[55, 75, 13, 63]
'''
#Example4 Lambda Function with map()
#Code to calculate the square of each number of a list using the map() 
# function    
numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]    
squared_list = list(map( lambda num: num ** 2 , numbers_list ))    
print( squared_list ) 
'''
Output
[4, 16, 25, 1, 9, 49, 64, 81, 100]
'''

#Example5 Lambda Function with List Comprehension and For Loop
#Code to calculate square of each number of list using list comprehension  
squares = [lambda num = num: num ** 2 for num in range(0, 11)]     
for square in squares:  
    print( square(), end = " ")  
'''
Output
0 1 4 9 16 25 36 49 64 81 100 
'''    

#Example6 Lambda Function with if-else
Minimum = lambda x, y : x if (x < y) else y     
print(Minimum( 35, 74 )) 
'''
Output
35
'''
