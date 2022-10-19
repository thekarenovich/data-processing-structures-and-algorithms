# log2(n)

def fun1(n):
    if(n == 1):
        return 0
    else:
        return 1 + fun1(n//2)

print(fun1(4))

#_____________
'''
2
'''
