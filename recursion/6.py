# Total numbers of stars printed is equal to 1 + 2 + …. (n-2) + (n-1) + n, which is n(n+1)/2. 

def  fun1(n):
    i = 0
    if (n > 1):
        fun1(n - 1)
    for i in range(n):
        print(" * ",end="")

fun1(5)
#___________________________
'''
*  *  *  *  *  *  *  *  *  *  *  *  *  *  *
'''
