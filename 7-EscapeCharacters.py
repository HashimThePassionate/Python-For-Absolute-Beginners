#Python Escape Characters
'''
You will get an error if you use double quotes inside a string 
that is surrounded by double quotes:
'''
txt = "We are the so-called "Vikings" from the north."

'''
The escape character allows you to use double quotes 
when you normally would not be allowed:
'''
txt = "We are the so-called \"Vikings\" from the north."

'''
ESCAPE SEQUENCE	MEANING
Code	        Result	
\'	            Single Quote	
\\	            Backslash	
\n             	New Line	
\"	            Double Quote	
\t	            Tab
'''
#Single Qoute
txt = 'It\'s alright.'
print(txt) 
#Double Quote
txt = 'It\"s alright.'
print(txt) 
#Backslash
txt = "This will insert one \\ (backslash)."
print(txt) 
#Newline
txt = "Hello\nWorld!"
print(txt) 
#Tab
txt = "Hello\tWorld!"
print(txt) 
