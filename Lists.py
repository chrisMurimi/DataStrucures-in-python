# More on list datastructures By {Chris Murimi}.
"""
 -Lists are the most used datastructures
 - List is a sequence type datastructures
 - List are are in built-in python
 - List are ordered
 - List can be sorted
 - List are mutable (can grow or shrink).
 - List have some similar characteristics borrowed from arrays and arrayLists for those who have used languages
   like Java.
"""

# To create a new empty list you can use any of the following:
My_List = list()
# or
My_List1 = []

print('My_List:', My_List, '\n', 'My_List1:', My_List1)

# List can hold elements of different datatype
My_List1 = ["collins", "m", 345, True]
print(My_List1)

# You can then use the List append function to add into a List.
My_List.append('Chris')
My_List.append('Brian')
My_List.append('Evans')
My_List.append('Derick')

print(My_List)

# You can access each element in a list using it index. NB: indexing starts at 0
print(My_List[0])
print(My_List[3])

"""
Indexing of Lists:
  index => 0 1 2 3 4 5
  list => [1,2,3,4,5,6]
"""
# If you don't know the length of the list and you wish to get value of the last element,
# you can get it by using the index of [-1]
print(My_List[-1])  # Print the last element
print(My_List[-2])  # Print the second last element

# You can concatenate two lists using '+' i.e combing two list
y = [1, 2, 3, 4]
z = [5, 6, 7]
print(y+z)  # combines the two lists

# You can use * (asterisk) to duplicate a list number of times in a single list ie multiplying a list
print(z * 3)

# Checking membership
africaCountries = ['Kenya', 'Uganda', 'Congo', 'Egypt']
print('Kenya' in africaCountries)  # This checks if element is in the list and returns a boolean (True or False)
print('USA' not in africaCountries)  # Checks if element is not in the list

# You can get the size of the list (ie no of elements in the list) using the len function.
print(len(africaCountries))

# You can get the maximum or minimum in a list using the max and min functions respectively
# Note that this will work for list with elements of same datatype
numbers = [2, 4, 5, 1, 6, 4, 9, 3]
print(max(numbers))
print(min(numbers))

letters = ['r', 'd', 'a', 'z']  # for max or min of characters or strings element will depend or alphabetic order
print(max(letters))
print(min(letters))

# You can get the sum of a list (i.e those with numeric elements) using the sum function
costs = [300, 400, 120, 5600]
totalCost = sum(costs)
print(totalCost)

# sorting list
# 1. Using the  sorted function.NB => this returns a new list
num = [4, 2, 21, 7, 8, 89, 128, 4, 1, 6]
alpha = ['abu', 'dan', 'collo', 'bena']
print(sorted(num))
print(sorted(alpha))   # sorts on alphabetic order

# 2. you can use the  sort function
numeric = [4, 2, 21, 7, 8, 89, 128, 4, 1, 6]
numeric.sort()  # sorts the list
print(numeric)

# sorting in reverse order
values = [23, 1, 4, 2, 5, 60, 77]
print(sorted(values, reverse=True))

# Counting how many times an element appears in a list
toCount = ['zii', 'we', 'end', 'zii', 'chem']
print(toCount.count('zii'))

# getting the index of an element in a list
fruits = ['mango', 'banana', 'apple', 'orange', 'pineapple']
print(fruits.index('apple'))

# unpacking a list
marks = [30, 28, 21, 6]
mike, kim, erick, edwin = marks  # NB: the number of items to unpack to must equal the number of elements in the list
print(mike, kim, erick, edwin)

# you can remove elements from the list using remove function
toRemoveFrom = ['chelsea', 'man_u', 'arsenal']
toRemoveFrom.remove('arsenal')
print(toRemoveFrom)

# You can delete the entire list using del function
nothing = [1, 3, 5, 6]
del nothing
# print(nothing)  #this will give an error because the list nothing no longer exist

# slicing a list
# slicing is cutting elements from a given index to another index in a list
# [start : end : step]
slicing = [3, 4, 5, 6, 6, 7, 8]
print(slicing[3: 6])  # slices from elements in index 3 to but not inclusive element in index 6
print(slicing[3:])  # slices from index 3 to the end
print(slicing[:6])  # slices from element in index zero to index 6 but not inclusive
print(slicing[3: 6: 2])  # slices from elements in index 3 to but not inclusive element in index 6 with two steps
print(slicing[:-2])  # slices from index zero to second last element but second last item not inclusive

# extend function : concatenate a list to another
m = [1, 2, 3, 4]
n = [4, 5, 6]
m.extend(n)
print(m)

# insert function : adds element to a list to a given index without replacing the previous element in that index
d = [1, 3, 4, 5]
d.insert(1, 2)  # 1 is the index while 2 is the value to be inserted
d[2] = 6  # this will replace the value at index 2 previously with 6
print(d)

# pop function: removes the last element in a list and returns it
print(d.pop(), d)

# reverse function : reverses a list
reversing = [1, 2, 3, 4, 5, 6, 6]
reversing.reverse()
print(reversing)


# List comprehension

myValues = [m for m in range(10)]
print(myValues)

myValues = [m for m in range(10) if m % 2 == 0]  # even numbers
print(myValues)


