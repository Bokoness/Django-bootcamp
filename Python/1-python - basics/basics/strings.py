#slicing
my_string = 'abcdefg'
a = 4
print(my_string[2:]) #will print from index 2 to the end
print(my_string[:5]) #will print from beginning to index 5 (not include)
print(my_string[::2]) #will print string with jumps of 2

#upperCase
print(my_string.upper()) # to uppercase
print(my_string.lower()) # to lowercase
print(my_string.capitalize()) # captilize the first letter
print(my_string.split()) # splits the string to an array args - the letter that splits the string, default is space

#print formatting
print("Insert another string here: {x}, and here {y}".format( x= "Insert me!",  y="i'm the second inserted string") ) # will insert second string to curly braces