from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def startEngine(self):
        pass

    def stopEngine(self):
        pass

class Car(Vehicle):
    def startEngine(self):
        print("Engine Started")

car = Car()
car.startEngine()