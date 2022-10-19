# It calculates a*b (a multiplied b)

def fun(a, b):
    if (b == 0):
        return 0
    if (b % 2 == 0):
        return fun(a + a, b//2)
     
    return fun(a + a, b//2) + a
 
# Driver code
 
print(fun(4, 3))
 
 #_____________________________
 '''
 12
 '''
