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

# slicing strings
print(my_str[1:3]) # prints 'li'
print(my_str[:3])   #prints 'Eli' its like [0:3]
print(my_str[3:]) #prints 'ezer' prints the string from index 3 to the end of the string


# Methods to work with strings
# len() to get length
print(len(my_str))  # Output: 5

print(my_str.replace('e','x')) # Elixzxr
print(my_str.split())

print(my_str)

#string formatting
# We can format using the .format() method
name = "Eliezer"
age = 25
formatted_str = "My name is {} and I am {} years old.".format(name, age)
print(formatted_str)  # Output: My name is Eliezer and I am 23 years old.

# Or using f-strings (Python 3.6+)
f_string = f"My name is {name} and I am {age} years old."
print(f_string)  # Output: My name is Eliezer and I am 23 years old.


