#Use of Continue, Break, Pass
'''
terminate the current "iteration" or even the "whole loop" without 
checking test expression.
'''
#Continue
#The continue statement is used to skip current iteration 
# Program to show the use of continue statement inside loops
#Example1
for val in "string":
    if val == "i":
        continue
    print(val)

'''
s
t
r
n
g
'''
#Example2
for i in range(1, 11):  
    if i == 5:  
        continue  
    print( i," ",end="" ) 
'''
1  2  3  4  6  7  8  9  10
'''
#Break
'''
The break statement terminates the loop containing it.
If the break statement is inside a nested loop,
the break statement will terminate the innermost loop.
'''
# Use of break statement inside the loop
#Example1
for val in "string":
    if val == "i":
        break
    print(val)
'''
s
t
r
'''

#Example2
n=2  
while 1:  
    i=1;  
    while i<=10:  
        print("%d X %d = %d\n"%(n,i,n*i))  
        i = i+1;  
    choice = int(input("Do you want to continue printing the table, press 0 for no?"))  
    if choice == 0:  
        break    
    n=n+1 
'''
2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
2 X 4 = 8
2 X 5 = 10
2 X 6 = 12
2 X 7 = 14
2 X 8 = 16
2 X 9 = 18
2 X 10 = 20
Do you want to continue printing the table, press 0 for no?
'''
#Pass Statement
'''
In Python programming, the pass statement is a null statement. 
The difference between a "comment" and a pass statement in 
Python is that while the interpreter ignores a comment entirely, 
"pass" is not ignored.

However, nothing happens when the pass is executed. 
It results in no operation
'''
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass
