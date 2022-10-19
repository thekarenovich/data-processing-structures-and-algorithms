# The function fun() calculates and returns ((1 + 2 … + x-1 + x) +y), which is x(x+1)/2 + y. 
# For example, if x is 5 and y is 2, then fun should return 15 + 2 = 17.

def fun1(x, y) :
 
    if (x == 0) :
        return y
    else :
        return fun1(x - 1, x + y)

print(fun1(5, 2))     

#________________
'''
17
'''
