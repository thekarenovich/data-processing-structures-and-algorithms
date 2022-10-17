# Creating a Set with
# a mixed type of values
# (Having numbers and strings)
Set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(Set)
  
# Accessing element using
# for loop
print("\nElements of set: ")
for i in Set:
    print(i, end =" ")
print()
  
# Checking the element
# using in keyword
print()
print("Geeks" in Set)

#____________________
'''
Set with the use of Mixed Values
{1, 2, 4, 6, 'Geeks', 'For'}

Elements of set: 
1 2 4 6 Geeks For 

True
'''
