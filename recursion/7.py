# For a positive n, fun2(n) prints the values of n, 2n, 4n, 8n … while the value is smaller than LIMIT. After printing values in increasing order, it prints same numbers again in reverse order. For example fun2(100) prints 100, 200, 400, 800, 800, 400, 200, 100. 
# If n is negative, the function is returned immediately. 

LIMIT = 1000
def fun2(n):
    if (n <= 0):
        return
    if (n > LIMIT):
        return
    print(n, end=" ")
    fun2(2 * n)
    print(n, end=" ")
 
fun2(5)
#____________________
'''
> 
5 10 20 40 80 160 320 640 640 320 160 80 40 20 10 5
'''
