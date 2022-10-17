# Creating a Tuple with
# the use of Strings
# Tuple_example1 = 'Geeks',
# Tuple_example2 = 'Geeks', 'For'
Tuple = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple)
      
# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
Tuple = tuple(list1)
  
# Accessing element using indexing
print("First element of tuple")
print(Tuple[0])
  
# Accessing element from last
# negative indexing
print("\nLast element of tuple")
print(Tuple[-1])
  
print("\nThird last element of tuple")
print(Tuple[-3])

#____________________________________
'''
Tuple with the use of String: 
('Geeks', 'For')

Tuple using List: 
First element of tuple
1

Last element of tuple
6

Third last element of tuple
4
'''
