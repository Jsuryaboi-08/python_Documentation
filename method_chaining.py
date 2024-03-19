#method chaining:
# Method chaining is a technique used to simplify code. It involves calling multiple methods in a single line.

class Car:
    def turn_on(self):
        print("Car is starting")
        return self
    def drive(self):
        print("Car is moving")
        return self
    def brake(self):
        print("Car is stopping")
        return self
    def turn_off(self):
        print("Car is stopping")
        return self
car = Car()
#method chaining
car.turn_on().drive()
#explanation: The turn_on method is called first, followed by the drive method. This is an example of method chaining.
car.brake().turn_off()
#explanation: The brake method is called first, followed by the turn_off method. This is an example of method chaining.
car.turn_on().drive().brake().turn_off()
