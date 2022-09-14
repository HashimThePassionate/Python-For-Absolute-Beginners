#Python control flows - Loops
'''
Python’s for statement iterates over the items of any sequence 
(a list or a string), in the order that they appear in the 
sequence.

The built-in Range function 'range()' comes in handy 
if you do need 
to iterate over a sequence of numbers. 
It generates arithmetic 
progressions:

range(start, stop, step)
start
The value of the start parameter (or 0 if the parameter was not supplied)
stop
The value of the stop parameter
step
The value of the step parameter (or 1 if the parameter was not supplied)

The following sorts of loops are available
 in the Python programming language.
Sr.No.	    Name of the loop	        Loop Type & Description
1	        While loop	                Repeats a statement or
                                         group of statements while a 
                                         given condition is TRUE. 
                                         It tests the condition 
                                         before executing the loop body.
2	        For loop	                This type of loop executes a
                                         code block multiple times and 
                                         abbreviates the code that 
                                         manages the loop variable.
3	        Nested loops	            We can iterate a loop inside
                                         another loop.

Loop Control Statements
Statements used to control loops and change the course of iteration are 
called control statements. All the objects produced within the local 
scope of the loop are deleted when execution is completed.          

Sr.No.	    Name of the control statement	    Description
1	        Break statement                 	This command terminates
                                                the loop's execution and
                                                transfers the program's
                                                control to the statement
                                                next to the loop.
2	        Continue statement	                This command skips the
                                                current iteration of the
                                                loop. The statements
                                                following the continue
                                                statement are not
                                                executed once the 
                                                Python interpreter
                                                 reaches the continue 
                                                statement.
3	        Pass statement	                    The pass statement is 
                                                used when a statement
                                                is syntactically 
                                                necessary, but no code
                                                is to be executed                            
''' 

#The range() Function
'''
With the help of the range() function, we may produce a series of numbers.
range(10) will produce values between 0 and 9. (10 numbers).
We can give specific start, stop, and step size values in the manner
range(start, stop, step size). If the step size is not specified, 
it defaults to 1.
Since it doesn't create every value it "contains" after we construct
it,the range object can be characterized as being "slow." 
It does provide
in, len, and __getitem__ actions, but it is not an iterator.
'''
#The example that follows will make this clear.
print(range(15))    
print(list(range(15)))    
print(list(range(4, 9)))    
print(list(range(5, 25, 4))) 
 