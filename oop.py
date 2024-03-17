class Car:
    
    def __init__(self, make, model, year, color):
        self.make = make#instance variables
        self.model = model#instance variables
        self.year = year#instance variables
        self.color = color#instance variables
    def drive(self):
            print("This "+self.model+" is driving")    
    def stop(self):
            print("This "+self.model+" is stopping")

car_1=Car("Toyota", "Corolla", 2015, "Red")
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
car_1.drive()
car_1.stop()
car_2=Car("Honda", "Civic", 2018, "Blue")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
car_2.drive()
car_2.stop()


#class variables
class car:
    wheels = 4#class variables
    def __init__(self, make, model, year, color):
        self.make = make#instance variables
        self.model = model#instance variables
        self.year = year#instance variables
        self.color = color#instance variables
    def drive(self):
            print("This "+self.model+" is driving")    
    def stop(self):
            print("This "+self.model+" is stopping")



car_2=car("Honda", "Civic", 2018, "Blue")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
car_2.drive()
car_2.stop()
car_2.wheels = 2#changing the value of class variable
print(car_2.wheels)

