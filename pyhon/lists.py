# lists - python forms of arrays
mylist1 = [1,2,3]
mylist2 = ['string', 1, 23.2, True, [1,2,3]]
print(mylist2)

#list length
print('list length: ', len(mylist2))
print(mylist1[1:])

#list reasignment
print('before reasignment: ', mylist2)
mylist2[0] = 'ness'
print('after reasignment', mylist2)

#append - adds a new list to the current list (array inside of array)
mylist1.append(['a', 'b', 'c'])
print('append: ', mylist1)

#extend - add values to the list
mylist1.extend(['e', 'f', 'g'])
print('extend: ', mylist1)

#pop - poped off the last item from the list
mylist3 = [1,2,3]
print('pop: ',mylist3, mylist3.pop(0))

#reverse
mylist4 = [1, 2, 3]
mylist4.reverse()
print('revrse: ', mylist4)

#sort
mylist5 = [1,7,5,23,1,2,6,77,5,24,5,98]
print('before sort: ', mylist5)
mylist5.sort()
print('after sort: ', mylist5)

#print a column in matrix
matrix = [ [1,2,3],
           [4,5,6],
           [7,8,9]
        ]
first_col = [row[0] for row in matrix]
print(first_col)