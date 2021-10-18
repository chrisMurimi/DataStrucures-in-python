# More on sets datastructures By {Chris Murimi}.
"""
- Sets are unordered datastructures
- sets are sequence type datastructures
- sets are are in built-in python
- sets does not allow duplicates
- sets are faster than lists
- sets are mutable
- sets can do math set operations (union, intersection etc)
- sets can not be sorted
"""
# creating a new set
my_set = {1, 2, 4, 3, 4, 7, 5, 3}
print(my_set)   # since this is a set python will remove duplicate

# creating a set from a list or any other datastructures
myList = [1, 2, 3, 7, 6, 5, 3]
sets = set(myList)
print(sets)

# adding elements into a set
newSet = {'kim', 'enock', 'hellen'}
newSet.add('cliff')
print(newSet)

# removing elements from a set: can remove a element from a set using the .remove function
set1 = {'chris', 'kelvin', 'mark'}
set1.remove('mark')
print(set1)

# checking the number of items in a set
print(len(set1))

# using pop function : since sets are not ordered the pop function will remove random elements from the set
set2 = {'Arsenal', 'Chelsea', 'Madrid', 'Hot_spurs'}
print(set2.pop())
print(set2)

# to delete the entire set we use the clear function
set2.clear()
print(set2)

# checking membership in a set
countries = {'USA', 'India', 'China', 'Japan'}
print('China' in countries)  # checks if element is in the set and returns a boolean
print('Nairobi' in countries)  # checks if an element is not in


# Mathematical set operations
set1 = {1, 2, 3, 4}
set2 = {4, 5, 3, 6, 7}

# Intersection (AND):  checks the common element in both sets
# for intersection we use "&"
print(set1 & set2)

# Union (OR): combines the two sets together
# for union we use "|"
print(set1 | set2)

# Symmetric difference (XOR) : this gives elements in the two sets but not in both I.e only in one
# for XOR we use "^"
print(set1 ^ set2)

# Difference : this gives those in set1 but not in set2 i.e only in set1
# for difference we use "-"
print(set1 - set2)

# Subset : checking if set2 is a subset of set1. will return a boolean value
# to check subset we use "<="
print(set1 <= set2)

# Superset : checking if set1 is a superset of set2. will return a boolean value
# to check superset we use ">="
print(set1 >= set2)