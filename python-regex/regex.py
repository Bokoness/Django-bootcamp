import re #importing regex
patterns = ['term1', 'term2']

text = 'This is  a string with term1, but not with the other'

#re.search take 2 params: 1. pattern of search, 2.the test to search in
match = re.search(patterns[0], text)
if match:
    print('Match!')
else:
    print('No match!')

print (type(match)) # the type is match
print (match.start()) # the index of the match in string

#findall() method
text = "Ness, im Ness, my name is Ness, and its a Ness"
    #params: 1. pattern, 2. text 
print(re.findall('Ness', text))