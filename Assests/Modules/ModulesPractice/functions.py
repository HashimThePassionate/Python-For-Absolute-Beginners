def length( string ):  
    "This prints the value of length of string"  
    return len(string)

def number_play(x):
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

