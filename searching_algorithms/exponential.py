# Экспоненциальный поиск — это еще один алгоритм поиска, который может быть достаточно легко реализован на Python, по сравнению с jump search и поиском Фибоначчи, которые немного сложны. 
# Экспоненциальный поиск зависит от бинарного поиска для выполнения окончательного сравнения значений.
# Экспоненциальный поиск выполняется за время O(log i), где i — индекс искомого элемента. В худшем случае временная сложность равна O(log n), когда искомый элемент — это последний элемент в массиве (n — это длина массива).
# Экспоненциальный поиск работает лучше, чем бинарный, когда искомый элемент находится ближе к началу массива. 
# На практике мы используем экспоненциальный поиск, поскольку это один из наиболее эффективных алгоритмов поиска в неограниченных или бесконечных массивах.

def exponentialSearch(lys, val):
    if lys[0] == val:
        return 0
    index = 1
    while index < len(lys) and lys[index] <= val:
        index = index * 2
    return binarySearch( lys[:min(index, len(lys))], val)

def binarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index

print(exponentialSearch([1,2,3,4,5,6,7,8],3))

#____________________________________________
'''
2
'''
