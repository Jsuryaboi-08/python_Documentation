#abstract classes
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def go(self):
        pass

class Car(Vehicle):
    @abstractmethod
    def go(self):
        print("Car is moving")

class Boat(Vehicle):
    def go(self):
        print("Boat is moving")


vehicle = Vehicle()     
car = Car()
boat = Boat()

vehicle.go()
car.go()

# abstract classes are not meant to be instantiated
