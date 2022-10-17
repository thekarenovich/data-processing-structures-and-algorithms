# Creating a Dictionary
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("Creating Dictionary: ")
print(Dict)
  
# accessing a element using key
print("\nAccessing a element using key:")
print(Dict['Name'])
  
# accessing a element using get()
# method
print("\nAccessing a element using get:")
print(Dict.get(1))
  
# creation using Dictionary comprehension
print()
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)

#________________________________________

'''
Creating Dictionary: 
{'Name': 'Geeks', 1: [1, 2, 3, 4]}

Accessing a element using key:
Geeks

Accessing a element using get:
[1, 2, 3, 4]

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''
