######################
### Python classes ###
######################

class Circle():
    
    # CLASS OBJCT ATTRIBUTE
        # class constant variables - wont change withing different objects
    pi = 3.14
    
    #CLASS CONSTRUCTOR
        #def __init__ - is the syntax
        #self is essential - like 'this' in js
        #other params - are the paramters that the class accepted
    def __init__(self, radius=1):
        #deffine attributes 
        self.radius = radius
    
    # CLASS METHODS
        #the self param is essential - to define between a global function to class method
        #area() - return the area of the circle
    def area(self):
        return self.radius * self.radius * Circle.pi #pi is class object attr, that why we reffer to it with Circle 
    
    def set_radius(self, new_r):
        self.radius = new_r

    #SPECAIL METHODS
        #__str__ - build in special method, to invoke it just print(obj)
    def __str__(self):
        return "The radius of your circle is " + str(self.radius)

        #__len__ - build in special method - return the lengh of the class
    def __len__(self):
        return 365

    def __del__(self):
        print("the circle deleted")

myc = Circle(3)
myc.set_radius(99)
print (myc.area())
#invoking special method __str__:
print(myc)
#invoking special method __len__:
print(len(myc))
#invoking special method __del__: 
del(myc) # delete the circle
#print(myc) # will throw an error becuse myc has been deleted





