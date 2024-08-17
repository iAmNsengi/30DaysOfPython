
# Complex types in Python refer to data structures that can store multiple values or more complex data, such as lists, 
# tuples, dictionaries, and sets. 

# 1. Lists
# Lists are ordered, mutable collections of items that can hold elements of different data types.

# Creating Lists
my_list = [1, 2, 3, 'Python', 4.5]
# Accessing List Elements
# You can access list elements using indexing:

print(my_list[0])  # Output: 1
print(my_list[-1]) # Output: 4.5
# Modifying Lists
# Since lists are mutable, you can modify them:


my_list[1] = 'changed'
print(my_list)  # Output: [1, 'changed', 3, 'Python', 4.5]
# List Methods
# append(): Add an element to the end of the list.

my_list.append('new')
# remove(): Remove the first occurrence of a value.

my_list.remove(3)

# pop(): Remove an element by index and return it.

item = my_list.pop(0)

# extend(): Extend the list by appending elements from another list.

my_list.extend([6, 7])



# 2. Tuples
# Tuples are ordered, immutable collections, meaning once they are created, they cannot be modified.

# Creating Tuples

my_tuple = (1, 2, 3, 'Python', 4.5)
# Accessing Tuple Elements
# You can access elements in the same way as lists:


print(my_tuple[0])  # Output: 1
print(my_tuple[-1]) # Output: 4.5

# Immutability
# Tuples cannot be modified after creation:


# my_tuple[1] = 'changed'  # This will raise a TypeError



# 3. Dictionaries
# Dictionaries are unordered, mutable collections of key-value pairs. Keys must be unique and immutable, 
# while values can be of any type.

# Creating Dictionaries

my_dict = {'name': 'Eliezer', 'age': 25, 'language': 'Python'}
# Accessing Dictionary Elements
# You can access elements by key:


print(my_dict['name'])  # Output: Eliezer
# Modifying Dictionaries
# You can add or modify elements:

my_dict['age'] = 26
my_dict['city'] = 'Berlin'

# Dictionary Methods
# keys(): Get all keys in the dictionary.

print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'language', 'city'])
# values(): Get all values in the dictionary.

print(my_dict.values())  # Output: dict_values(['Eliezer', 26, 'Python', 'Berlin'])

# items(): Get all key-value pairs.

print(my_dict.items())  # Output: dict_items([('name', 'Eliezer'), ('age', 26), ('language', 'Python'), ('city', 'Berlin')])
# get(): Safely access a key, providing a default value if the key doesn’t exist.

print(my_dict.get('country', 'Unknown'))  # Output: Unknown



# 4. Sets
# Sets are unordered collections of unique elements, making them useful for eliminating duplicates.

# Creating Sets

my_set = {1, 2, 3, 'Python', 4.5}
# Modifying Sets
# You can add or remove elements:

my_set.add(5)
my_set.remove('Python')
# Set Operations
# Union: Combine two sets.

another_set = {3, 4, 5, 6}
# union_set = my_set.union(another_set)
# Intersection: Find common elements.


intersection_set = my_set.intersection(another_set)
# Difference: Find elements in one set but not in another.

difference_set = my_set.difference(another_set)



# 5. Nested Data Structures
# Python allows nesting of complex types, meaning you can have lists of lists, dictionaries of dictionaries, etc.

# Example of Nested Structures

nested_list = [[1, 2, 3], ['a', 'b', 'c']]
nested_dict = {'key1': {'subkey1': 1, 'subkey2': 2}, 'key2': [1, 2, 3]}