#dicionaries - just like objects in javascript

my_stuff = {
    "key1": "value1", #string
    'key2': 'value2',
    'key3': 3, #int
    'key4': [1,2,3], #list
    'key5': {'key5.1': [1,2, 'grabMe']} #dictionaris with lists inside
}
print(my_stuff)
print(my_stuff['key2'])
#get grabme
print(my_stuff['key5']['key5.1'][2])

#reasign dics
my_stuff2 = {'lunch': 'pizza', 'bfast':'eggs'}
my_stuff2['lunch'] = 'burger'
print(my_stuff2['lunch'])