# fun() returns the maximum value in the input array a[] of size n.

def fun( a, n):
    if(n == 1):
        return a[0]
    else:
        x = fun(a, n - 1)
    if(x > a[n - 1]):
        return x
    else:
        return a[n - 1]
 
# Driver code
arr = [12, 10, 30, 50, 100]
print(fun(arr, 5))
 
#__________________________
'''
100
'''
