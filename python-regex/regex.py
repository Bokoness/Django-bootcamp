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

print('\n')

def multi_re_find(patterns, phrase):
    
    for pat in patterns: 
        print('Searching for pattern {}'.format(pat))
        print(re.findall(pat, phrase))
        print('\n')
        

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

# *
test_patterns = ['sd*'] # * - find letter 'd' 0 or more 'd'
multi_re_find(test_patterns, test_phrase)

# +
test_patterns = ['sd+'] # + - find letter 'd' 1 or more
multi_re_find(test_patterns, test_phrase)

# ?
test_patterns = ['sd?'] # + - find letter 'd' 0 or 1 time
multi_re_find(test_patterns, test_phrase)

# {x} count - pattern with x number of items 
test_patterns = ['sd{3}'] # + - find letter 'd' 3 times
multi_re_find(test_patterns, test_phrase)

# {x, y} count - pattern with x or y number of items 
test_patterns = ['sd{1,3}'] # + - find letter 'd' 1 or 3 times
multi_re_find(test_patterns, test_phrase)

# [x,y] 
test_patterns = ['s[sd]+'] # + - find letter 's' followed with 1 or more number of s, OR followed by 1 or more number of d
multi_re_find(test_patterns, test_phrase)
