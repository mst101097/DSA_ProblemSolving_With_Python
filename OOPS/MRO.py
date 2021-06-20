class Point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    
    def __str__(self):
        return "This point at ("+str(self.__x)+","+str(self.__y)+")"
    
    def __add__(self,point_object):
        return Point(self.__x + point_object.__x,self.__y + point_object.__y)

p1 = Point(3,4)
p2 = Point(2,1)
p3 = p1+p2
print(p3)
