def one_func():
    print("one_func() in one.py")

print("TOP LEVEL one.py")
if __name__ == '__main__':
    print('one.py is main method')
else:
    print("one.py isn't main but is beind imported")