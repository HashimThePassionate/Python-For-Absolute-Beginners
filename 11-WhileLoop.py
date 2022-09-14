#Python While Loop
'''
i=1
while(i<15)
{
    statements
}
1,2,3,4,5
1+4+9+16+25=55
'''
#Example
n=5
s=1
summation=0
while s<=n:
    summation = summation + s**2
    s+=1
print("The sum of squares is", summation)  

#Multiplication Table using While Loop
num = 5        
counter = 1      
# we will use a while loop for iterating 10 times for the 
# multiplication table        
print("The Multiplication Table of: ", num)      
while counter <= 10: # specifying the condition  
    ans = num * counter      
    print (num, 'x', counter, '=', ans)      
    counter += 1 # expression to increment the counter

#Python While Loop Multiple Conditions
num1 = 17  
num2 = -12  
   
while num1 > 5 and num2 < -5 : # multiple conditions in a single while loop  
    num1 -= 2  
    num2 += 3  
    print( (num1, num2) ) 

#Multiple conditions with an OR operator
num1 = 17  
num2 = -12  
   
while num1 > 5 or num2 < -5 :  
    num1 -= 2  
    num2 += 3  
    print( (num1, num2) )  



