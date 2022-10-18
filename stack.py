# LAST IN -> FIRST OUT

stack = []
  
# append() function to push
# element in the stack
stack.append('g')
stack.append('f')
stack.append('g')
  
print('Initial stack')
print(stack)
  
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
  
print('\nStack after elements are popped:')
print(stack)
  
# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty

#________________________________

'''
Initial stack
['g', 'f', 'g']

Elements popped from stack:
g
f
g

Stack after elements are popped:
[]
'''
