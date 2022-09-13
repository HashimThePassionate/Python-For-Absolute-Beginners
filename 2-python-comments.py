#Single-Line Comments
'''
This code is to show an example of a single-line comment  
'''
print( 'This statement does not have a hashtag before it' ) 
#Multi-Line Comments
'''
#use multi #tags
'''
# it is a  
# comment  
# extending to multiple lines  

#Using String Literals
'''
Because Python overlooks string expressions that aren't
allocated to a variable, we can utilize them as comments.
'''
'it is a comment extending to multiple lines'

#Python Docstring
'''
he strings enclosed in triple quotes that come immediately 
after the defined function are called Python docstring.
It's designed to link documentation developed for Python modules,
methods, classes, and functions together. It's placed just beneath
the function, module, or class to explain what they perform. 
The docstring is then readily accessible in Python
using the __doc__ attribute
'''
def add(x, y):  
    """This function adds the values of x and y"""  
    return x + y  
   
# Displaying the docstring of the add function  
print( add.__doc__ )  