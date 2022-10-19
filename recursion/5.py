# The function fun2() prints the binary equivalent of n. For example, if n is 21 then fun2() prints 10101. 

def fun2(n):
    if(n == 0):
        return
     
    fun2(n // 2)
    print(n % 2, end="")

fun2(2)
print()

#______________________
'''
10
'''
