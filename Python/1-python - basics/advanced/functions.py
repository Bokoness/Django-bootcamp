#################
### Functions ###
#################

# definning a function
# param1 = somthing - default parameter
def my_func(param1='default'):
    
    """
    this is the way to document the function
    """

    print('my first python function! ', param1)

#calling a function
my_func()
my_func('passing a param') #hover on my_func with mouse to see the docstring

# using return
def my_func2(name='ness'):
    """
    returnning your name
    """
    return name;
print(my_func2('Ness Bokobza'))

#type validation
def addNum(num1, num2):
    if(type(num1))==type(num2)==(type(10)): #if type of num1 and type of num2 is integer (the type of 10)
        return num1 + num2
    else:
        return "Sorry, insert only integers"


#Filter
my_list = [1,2,3,4,5,6,7,8]

def even_bool(num):

    """
    return true if number is even,
    and false if number is odd
    """
    return num % 2 == 0

#filter func:
    # 1st param: a function to filter
    # 2nd param: the object to filter
evens = filter(even_bool, my_list)
print('even numbers: ', list(evens)) #list - casting the generator to list

# Lambda Expression
    #same func with lambda expression
evens = filter(lambda num: num%2 == 0, my_list)
print ('lambda version: ', list(evens))
