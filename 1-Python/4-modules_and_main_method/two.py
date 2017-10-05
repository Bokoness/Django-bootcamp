import one as one

print('TOP LEVEL two.py')
one.one_func() # calling one func

if __name__ == '__main__':
    print('Two.py is main method')
else:
    print("two isn't main but its imported")