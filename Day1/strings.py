# The string in python is a sequence of characters.
# Python supports Unicode characters.


a = "My first string"
b = 'My second string'

# We might use the , to concantenate two or several strings
print(a,b)
c = a,b # Creating a tuple
print(c)
print(type(c))

# Multiline string we use """ """  or ''' '''
str = ''' this is my multiline
string'''
print(str)

# Accessing strings we use indexing
my_str = 'Eliezer'
print(my_str[0]) #print 'E'
print(my_str[-1]) #starts from the end and logs 'r'
