class Vehicle:
	def __init__(self,color,maxspeed):
		self.color = color
		self.__maxspeed = maxspeed
	def get(self):
		return self.__maxspeed
	
	def setMaxSpeed(self,maxspeed):
		self.__maxspeed = maxspeed
	
	def display(self):
		print("Car MaxSpeed : ",self.get())
		print("Car Color : ",self.color)


class Car(Vehicle):
	"""docstring for Car"""
	def __init__(self,color,maxspeed,name,gearnumber):
		super().__init__(color,maxspeed)
		self.name = name
		self.gearnumber = gearnumber

	def display(self):
		super().display()
		print("Name of Car : ",self.name)
		print("Number of Gear : ",self.gearnumber)
	


obj = Car('red',324,'honda',5)
obj.display()

# obj1 = Vehicle("Blue",32)
# obj1.display()




