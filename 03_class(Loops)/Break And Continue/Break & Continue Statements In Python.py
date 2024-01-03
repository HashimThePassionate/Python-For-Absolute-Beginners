########## Break & Continue Statements Tutorial ###############

# i = 0

# while(i<45):
#     print(i+1)
#     i = i+1

############### Break Statement ############
i = 0

while(True):
    # print(i+1, end =" ")
    if(i==11):
        break # Stop the loop if i become 44
    i = i+1

# After break while loop stops
# Program comes here 

# Output : 1 2 3 4 5 6 7 8 9 10 11

############### Continue Statement ############

# continue used to not execute codes below it in loop

# if we want to print numbers which are greater than 5
i = 0

while(True):
    if i+1<5:
        i = i+1
        continue
    # below code inside while will not execute till i+1<5
    print(i+1, end =" ")
    if(i==11):
        i = i+1
        break # Stop the loop
    i = i+1
    
# Output : 5 6 7 8 9 10 11 12 

###### Quiz ######

# Keep taking input from user
# till user enter number greater than 100


# Solution :
while(True): 
    num = input("Please enter a number") 
    if(int(num)<100): 
        continue 
    else: 
        print("congratulations, you entered number >= 100") 
        break


