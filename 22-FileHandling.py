#Python File Handling
'''
The file handling plays an important role when the data needs 
to be stored permanently into the file. A file is a named location
on disk to store related information. We can access the stored 
information (non-volatile) after the program termination.

The file-handling implementation is slightly lengthy or complicated in 
the other programming language, but it is easier and shorter in Python.

Hence, a file operation can be done in the following order.

1. Open a file
2. Read or write - Performing operation
3. Close the file

'''
#Opening a file
'''
Python provides an open() function that accepts two arguments, 
"file name" and "access mode" in which the file is accessed. 
Syntax:

file object = open(<file-name>, <access-mode>)  
e.g
path = 'C:\\Users\\DELL\\Desktop\\python-course-for-beginner\\Newfile.txt'
file = open (path, "r")
file.close()

SN	    Access mode     	Description
1	      r	             It opens the file to read-only mode. The file 
                            pointer exists at the beginning. The file is by 
                            default open in this mode if no access mode is 
                            passed.
2       	rb	             It opens the file to read-only in binary format.
                            The file pointer exists at the beginning of the 
                            file.
3       	r+	             It opens the file to read and write both. The 
                            file pointer exists at the beginning of the file.
4       	rb+	             It opens the file to read and write both in
                            binary format. The file pointer exists at the 
                            beginning of the file.
5          w	             It opens the file to write only. It overwrites 
                            the file if previously exists or creates a new 
                            one if no file exists with the same name. The 
                            file pointer exists at the beginning of the file.
6       	wb	             It opens the file to write only in binary format. 
                            It overwrites the file if it exists previously 
                            or creates a new one if no file exists. The file
                            pointer exists at the beginning of the file.
7       	w+	             It opens the file to write and read both. It is 
                            different from r+ in the sense that it overwrites 
                            the previous file if one exists whereas r+ doesn't 
                            overwrite the previously written file. It creates 
                            a new file if no file exists. The file pointer 
                            exists at the beginning of the file.
8	     wb+               It opens the file to write and read both in binary 
                            format. The file pointer exists at the beginning 
                            of the file.
9       	 a	             It opens the file in the append mode. The file 
                            pointer exists at the end of the previously 
                            written file if exists any. It creates a new 
                            file if no file exists with the same name.
10	      ab	             It opens the file in the append mode in binary 
                            format. The pointer exists at the end of the 
                            previously written file. It creates a new file 
                            in binary format if no file exists with the 
                            same name.
11	      a+	             It opens a file to append and read both. The 
                            file pointer remains at the end of the file if 
                            a file exists. It creates a new file if no file 
                            exists with the same name.
12	      ab+	             It opens a file to append and read both in 
                            binary format. The file pointer remains at the 
                            end of the file.

'''
#Example1 to open file Successfully
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
file = open(path,"r")  
print(file)  
if file:    
    print("file is opened successfully") 

'''
Output
file is opened successfully
'''

#The close() method
'''
Once all the operations are done on the file, we must close it through 
our Python script using the close() method. Any unwritten information 
gets destroyed once the close() method is called on a file object

Syntax
file.close()  
'''
#Example using close method
#opens the file in read mode    

#We should use the following method to overcome such type of problem.
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
try:    
   file = open(path)  
   print(file) 
   print("File Opened Successfully")
   # perform file operations  
finally:  
   file.close() 

#The with statement
'''
The with statement was introduced in python 2.5. The with statement 
is useful in the case of manipulating the files. It is used in the 
scenario where a pair of statements is to be executed with a block 
of code in between

with open(<file name>, <access mode>) as <file-pointer>:    
    #statement suite  

e.g
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
with open(path, "r") as file:
     Statement1
     statement2
     statement3



     statements

It is always suggestible to use the with statement in the case of files 
because, if the break, return, or exception occurs in the nested block 
of code then it automatically closes the file, we don't need to write
the close() function. It doesn't let the file to corrupt. 

'''
#Example "with" Statement
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
with open(path,'r') as file:    
    content = file.read();    
    print(content)  

#Writing the file
'''
w: It will overwrite the file if any file exists. The file pointer is 
at the beginning of the file.

a: It will append the existing file. The file pointer is at the end of 
the file. It creates a new file if no file exists.

'''
#Using Write Example
# open the file.txt in append mode. Create a new file if no such file exists.  
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
with open(path, "w") as file:  
     file.write("""Python is the modern day language. It makes things so simple. 
It is the fastest-growing programing language""")  

#using Append Example 
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
with open(path, "a") as file:  
     file.write("""\nPython has an easy syntax and user-friendly interaction.""")
    
#Reading text from file using read() method
'''
The syntax of the read() method is given below.

Syntax:

content= file.read(10) #<count> read only first 10 characters
or
content1= file.read() #read complete text

'''
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
with open(path, "r") as file:
     content = file.read(10)
     print(type(content)) 
     print("print first 10 letters")
     print(content)    

with open(path, "r") as file:
     content = file.read()
     print("print everything to the end")
     print(content)

#Read file through for loop
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
print("\nPrint Through For Loop\n")
with open(path, "r") as file:
     for i in file:    
         print(i) 

#Read Line of the file
'''
Python facilitates to read the file line by line by using a function 
readline() method. The readline() method reads the lines of the file 
from the beginning, i.e., if we use the readline() method two times, 
then we can get the first two lines of the file.
'''
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
with open(path, "r") as file:
     content1 = file.readline() 
     content2 = file.readline()
     #it will print two lines bcz we use two times
     print(content1)
     print(content2)

# Reading Lines Using readlines() function that reads everyline
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
with open(path, "r") as file:
     content = file.readlines()
     print(content)
'''
Output
['Python is the modern day language. It makes things so simple. \n', 
'It is the fastest-growing programing language\n', 
'Python has an easy syntax and user-friendly interaction']

'''

#Creating a new file
'''
x: it creates a new file with the specified name. It causes an error a 
file exists with the same name.

a: It creates a new file with the specified name if no such file exists. 
It appends the content to the file if the file already exists with the 
specified name.

w: It creates a new file with the specified name if no such file exists. 
It overwrites the existing file

'''

#Using x
path = r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
with open(path, "x") as file:
     print(file)    
     if file:    
        print("File created successfully")  

'''
Output
File Already Exists thats why error show
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileExistsError: [Errno 17] File exists: r'C:\Users\DELL\Desktop\python-course-for-beginner\Newfile.txt'
'''