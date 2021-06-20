class Circle(object):
    def __init__(self,radius):
        self.__radius = radius
    
    def __str__(self):
        return "This is Circle Class which has radius as a argument"
    

c = Circle(3)
print(c)