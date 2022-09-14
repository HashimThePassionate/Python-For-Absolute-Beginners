#Python "for" Loops (Definite Iteration)

'''
for (int i=0;i<=10;i++)
{
    print(i)
}
0
1
2
3
4
5
6
7
8
9
10
11<=10 condition false
break
'''
'''
for item in sequence:
    execute expression

1.for starts a for loop.
2.item is an individual item during each iteration.
It is given a temporary arbitary variable name.
3.in separates each item from the other(s).
4.sequence is what we want to iterate over.
5.a colon : gives the instruction to execute the body of code 
that follows.
6.A level of indentation. 4 spaces before writing the body of 
the loop, otherwise we get an IndentationError.
'''
str = "Hashim"
for i in str:
    print(i)
'''
str = "Hashim"
 +---+---+---+---+---+---+
 | H | a | s | h | i | m |  
 +---+---+---+---+---+---+
   0   1   2   3   4   5   

i=0 => str[0]=H
H
i=1 => str[1]=a
a
'''
names = ['Hashim', 'Farooq', 'Hamza', 'Usman', 'Madiha']
for i in names:
    print(i)

for i in range(len(names)):
    print(i,names[i],len(names[i]))

#...remember range(start, stop, step)
range(10)
list(range(5, 10))
list(range(0, 10, 3))
list(range(-10, -100, -30))

for i in range(1,10):
    print(i)

#Even
for i in range(2,100,2):
    print(i)

for i in range(1,10):
    print("*",end=' ')

##Nested Loops
'''
*
* *
* * *
* * * *
* * * * *
'''
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1): 
        print("* ", end="")
    print("\n")

'''
rows = 5
step 1 for outer loop
i=0 i<=5
i=0 range(i+1)=> range(1) => range(0,1) 
  
Step 2 for outer loop
i=1 range(1+1) => range(2) => range(0,2)
step 1.1 
'''
'''
* 
**
***
****
****
'''





