# More on '{dictionaries}' datastructures By {Chris Murimi}.
"""
- dictionaries are sequence type datastructures
- dictionaries are in built-in python
- dictionaries are keys/ values pair datastructures
- dictionaries are unordered
- dictionaries can not be sorted
- dictionaries are mutable
- dictionaries are similar to hashMaps in java
"""
# ways of creating a new dictionary
dict1 = {'1': 'chris', '2': 'mark', '3': 'evans'}  # 1,2,3 are keys while chris, mark, evans are values
print(dict1)

dict2 = dict([('1', 'chris'), ('2', 'mark'), ('3', 'evans')])
print(dict2)

# adding new key / values into a dictionary
# your_dict['key] = value
dict1['4'] = 'josh'
print(dict1)

# deleting elements from a dictionary
# del your_dict['key]
del dict1['2']
print(dict1)

# deleting all elements of the dictionary
dict1.clear()
print(dict1)

# accessing keys and values in a dictionary
dict4 = {'1': 'chris', '2': 'mark', '3': 'evans', '4': 'josh'}
print(dict4.keys())  # gets all keys of pairs in the dictionary
print(dict4.values())  # gets all values of pairs in the dictionary
print(dict4.items())  # returns a list of tuples with key and value pairs

# iterating through a dictionary
for keys, values in dict4.items():
    print(keys, values)
































