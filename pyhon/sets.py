#Sets
    #sets are just like dictionaris, but without index, and they dont have prticular order
    #sets have uniq items - which means the same value cannot assigend two times
x = set()

x.add(1)
x.add(2)
x.add(4)
x.add(0.1)
x.add('hey')
print(x)

#uniq elements
converted_set = set([1,1,1,1,2,2,2,2,2,3,3,3,3,3,]) #output 1,2,3
print('converted set: ', converted_set)