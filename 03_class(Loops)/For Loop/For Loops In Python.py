################### For Loop Tutorial ###############

# A List
list1 = ['Vivek', 'Larry', 'Carry', 'Marie']

# To print all elements in list
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
# Output :
# Vivek
# Larry
# Carry
# Marie

# We can do same thing easily using for loop
# for loop runs len(list1) times
# each time item is equal to one elemrnt of list from starting
for item in list1: 
    print(item)
# Output :
# Vivek
# Larry
# Carry
# Marie

# We can iterate tuple, list of lists, dictionary, 
# and many more containers using for loop

# Examples : 

# Iterating tuple
list1 = ('Vivek', 'Larry', 'Carry', 'Marie')
for item in list1: 
    print(item)
# Output :
# Vivek
# Larry
# Carry
# Marie

# Iterating a list of lists 
list1 = [ ["Vivek", 1], ["Larry", 2],
          ["Carry", 6], ["Marie", 250]]
for item in list1: 
    print(item)
# Output :
# ['Vivek', 1]
# ['Larry', 2]
# ['Carry', 6]
# ['Marie', 250]

# Iterating a dictionary
dict1 = dict(list1)
print(dict1)
# Output : 
# {'Vivek': 1, 'Larry': 2, 'Carry': 6, 'Marie': 250}

for item in dict1:
    print(item) # It will print only keys
# Output :
# Vivek
# Larry
# Carry
# Marie

# to print both key and value while iterating dictionary
for item, lollypop in dict1.items():
    print(item, "and lolly is ", lollypop)
# Output :
# Vivek and lolly is  1
# Larry and lolly is  2
# Carry and lolly is  6
# Marie and lolly is  250

# Quiz time :
# Ques : Create a list if item in list is numerical
#  and number is greater than 6 


# Solution
items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)
# Remember str(item).isnumeric() is correct
# item.isnumeric() is wrong

# Output :
# 22
# 21
# 64
# 23
# 233
# 23
# 6
