from abc import ABC,abstractmethod

class Automobile(ABC):

    def __init__(self):
        print('Automobile Created')

    @abstractmethod
    def start(self):
        print('Abstrct class Start method activate')
    @abstractmethod    
    def stop(self):
        pass
    @abstractmethod
    def drive(self):
        pass

# c = Automobile()

class Car(Automobile):

    def __init__(self,name):
        # print("Car Class Created!!")
        self.name = name
    
    def start(self):
       print('Car class Start mehtod Activate')
       super().start()

    def stop(self):
        pass
    
    def drive(self):
        pass

c = Car("mohit")
c.start()


        
