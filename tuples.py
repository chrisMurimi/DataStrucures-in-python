# More on tuples datastructures By {Chris Murimi}.
"""
- Tuples are sequence type datastructures
- Tuples are are in built-in python
- Tuples are immutable # used for data that does not change
- Tuples can be sorted
- Tuples are faster then list
- Tuples are order datastructures
"""
value = [1, 2, 3, 4]  # this is a list
# To create a new empty tuple you can use any of the following:
My_Tuple = tuple(value)
# or
My_Tuple1 = (1, 2, 3, 4)

print('My_Tuple:', My_Tuple, '\n', 'My_Tuple1:', My_Tuple1)

# Tuple can hold elements of different datatype
My_Tuple2 = ("collins", "m", 345, True)
print(My_Tuple2)

# You can access each element in a tuple using it index. NB: indexing starts at 0
print(My_Tuple2[0])
print(My_Tuple2[3])

"""
Indexing of Tuple:
  index => 0 1 2 3 4 5
  tuple =>(1,2,3,4,5,6)
"""
# If you don't know the length of the tuple and you wish to get value of the last element,
# you can get it by using the index of [-1]
print(My_Tuple2[-1])  # Print the last element
print(My_Tuple2[-2])  # Print the second last element

# You can concatenate two tuples using '+' i.e combing two list
y = (1, 2, 3, 4)
z = (5, 6, 7)
print(y+z)  # combines the two tuples

# You can use * (asterisk) to duplicate a tuple number of times in a single tuple ie multiplying a tuple
print(z * 3)

# Checking membership
africaCountries = ('Kenya', 'Uganda', 'Congo', 'Egypt')
print('Kenya' in africaCountries)  # This checks if element is in the tuple and returns a boolean (True or False)
print('USA' not in africaCountries)  # Checks if element is not in the tuple

# You can get the size of the tuple (ie no of elements in the tuple) using the len function
print(len(africaCountries))

# You can get the maximum or minimum in a tuple using the max and min functions respectively
# Note that this will work for tuples with elements of same datatype
numbers = (2, 4, 5, 1, 6, 4, 9, 3)
print(max(numbers))
print(min(numbers))

letters = ('r', 'd', 'a', 'z')  # for max or min of characters or strings element will depend or alphabetic order
print(max(letters))
print(min(letters))

# You can get the sum of a list (i.e those with numeric elements only) using the sum function
costs = (300, 400, 120, 5600)
totalCost = sum(costs)
print(totalCost)

# sorting tuple
#  Using the  sorted function.NB => this returns a new tuple
num = (4, 2, 21, 7, 8, 89, 128, 4, 1, 6)
alpha = ('abu', 'dan', 'collo', 'bena')
print(sorted(num))
print(sorted(alpha))   # sorts on alphabetic order
# NB : tuples have no object sort
# sorting in reverse order
values = (23, 1, 4, 2, 5, 60, 77)
print(sorted(values, reverse=True))


# Counting how many times an element appears in a tuple
toCount = ('zii', 'we', 'end', 'zii', 'chem')
print(toCount.count('zii'))

# getting the index of an element in a tuple
fruits = ('mango', 'banana', 'apple', 'orange', 'pineapple')
print(fruits.index('apple'))

# unpacking a tuple
marks = (30, 28, 21, 6)
mike, kim, erick, edwin = marks  # NB: the number of items to unpack to must equal the number of elements in the tuple
print(mike, kim, erick, edwin)


# slicing a tuple
# slicing is cutting elements from a given index to another index in a tuple
# [start : end : step]
slicing = (3, 4, 5, 6, 6, 7, 8)
print(slicing[3: 6])  # slices from elements in index 3 to but not inclusive element in index 6
print(slicing[3:])  # slices from index 3 to the end
print(slicing[:6])  # slices from element in index zero to index 6 but not inclusive
print(slicing[3: 6: 2])  # slices from elements in index 3 to but not inclusive element in index 6 with two steps
print(slicing[:-2])  # slices from index zero to second last element but second last item not inclusive

