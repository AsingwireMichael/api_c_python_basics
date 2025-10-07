
class ElectricCar():
    def startEngine(self):
        print("Engine Started from Ev")

class Car():
    def startEngine(self):
        print("Engine Started")

def callAny(object):
    object.startEngine()

callAny(ElectricCar())
callAny(Car())