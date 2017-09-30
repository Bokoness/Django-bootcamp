###########
## Range ##
###########
# range iterates values without saving it in memory
    #first param - starting point
    #second param - ending point (not include)
    #thid param - progress value
print('###### Range ######')

print( list(range(0, 22)) ) 
print( list(range(0, 22, 2)) ) #from 0 to 20, progress 2 each iterate

###############
## For Loops ##
###############
print('###### For Loops ######')

#for in lists
print("for in lists")
my_list = [1,2,3,4,5]
for item in my_list:
    print(item * item)
    
#for in dicionaries
print("for in dicionaries")
dic = {"Sam":1, "Frank":2, "Dan":3}
for item in dic:
    print(item ,dic[item])

#for in tuples
print("for in tuples")
mypairs = [(1,2), (3,4), (5,6)] #list of tuples
for (tup1, tup2) in mypairs: # (tup1, tup2) unpacking the tuple () - not nesecery
    print(tup1, tup2)

#for with range
print("for with range")
for item in range(10):
    print(item)

#################
## While Loops ##
#################
print('###### While Loops ######')

i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i + 1

