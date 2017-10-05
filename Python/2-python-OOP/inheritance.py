###################
### INHERITANCE ###
###################

class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")
    
    def eat(self):
        print('EATING')

#to inherit from baseclass - just pass baseclass as param to derived class
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self) #like super in JS, call baseclass constructor
        print("DOG CREATED")

    def bark(self):
        print('Woof')


mydog = Dog()
mydog.whoAmI() #using the base class methods
mydog.eat() #using the base class methods
mydog.bark()