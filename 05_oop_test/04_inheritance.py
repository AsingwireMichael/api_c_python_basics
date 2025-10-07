
class Vehicle():
    def startEngine(self):
        print("Engine Started")
        
    def checkOil(self):
        print("Oil change")

class Car(Vehicle):
    pass

car = Car()
car.startEngine()