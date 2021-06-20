class Mother:
    def __init__(self):
        self.name = "MohitSingh"

    def print(self):
        print("This print is Mother class")

class Father:
    def print(self):
        print('This print is Father Class')

class Childclass(Mother,Father):
    def __init__(self):
        super().__init__()
    
    def printChild(self):
        print("Name of Student :",self.name)

c = Childclass()
c.printChild()
c.print()