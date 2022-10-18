# FIRST IN -> FIRST OUT

# Initializing a queue
queue = []
  
# Adding elements to the queue
queue.append('g')
queue.append('f')
queue.append('g')
  
print("Initial queue")
print(queue)
  
# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
  
print("\nQueue after removing elements")
print(queue)
  
# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty

#_________________________________
'''
Initial queue
['g', 'f', 'g']

Elements dequeued from queue
g
f
g

Queue after removing elements
[]
'''
