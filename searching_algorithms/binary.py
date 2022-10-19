# Бинарный поиск работает по принципу «разделяй и властвуй». 
# Он быстрее, чем линейный поиск, но требует, чтобы массив был отсортирован перед выполнением алгоритма.
# Алгоритм бинарного поиска можно написать как рекурсивно, так и итеративно. В Python рекурсия обычно медленнее, потому что она требует выделения новых кадров стека.
# Поскольку хороший алгоритм поиска должен быть максимально быстрым и точным, давайте рассмотрим итеративную реализацию бинарного поиска.
# В виде комментария запишем бинарный поиск с использованием рекурсии.
# Одним из недостатков бинарного поиска является то, что если в массиве имеется несколько вхождений элемента, он возвращает индекс не первого элемента, а ближайшего к середине

def binarySearch(lys, val):
    first = 0
    last = len(lys) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index
  
print(BinarySearch([10,20,30,40,50], 20))

#_____________________________________________________
'''
1
'''
#_____________________________________________________


# def binarySearch (arr, l, larr, x):
  
#     if larr >= l:

#         mid = l + (larr - l) // 2
  
#         if arr[mid] == x:
#             return mid
          
#         elif arr[mid] > x:
#             return binarySearch(arr, l, mid-1, x)

#         else:
#             return binarySearch(arr, mid+1, larr, x)
  
#     else:
#         return -1
  
# arr = [ 2, 3, 4, 10, 40 ]
# x = 10
  
# result = binarySearch(arr, 0, len(arr)-1, x)
  
# if result != -1:
#     print ("Element is present at index % d" % result)
# else:
#     print ("Element is not present in array")
