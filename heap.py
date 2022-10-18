# importing "heapq" to implement heap queue
import heapq
  
# initializing list
li = [5, 7, 9, 1, 3]
  
# using heapify to convert list into heap
heapq.heapify(li)
  
# printing created heap
print ("The created heap is : ",end="")
print (list(li))
# print(li)
  
# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)
  
# printing modified heap
print ("\nThe modified heap after push is : ",end="")
print (list(li))
  
# using heappop() to pop smallest element
print ("\nThe popped and smallest element is : ",end="")
print (heapq.heappop(li))
print("And again : ",end="")
print (heapq.heappop(li))


#______________________________________________________
'''
The created heap is : [1, 3, 9, 7, 5]

The modified heap after push is : [1, 3, 4, 7, 5, 9]

The popped and smallest element is : 1
And again : 3
'''
